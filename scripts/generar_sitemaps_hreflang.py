#!/usr/bin/env python3
"""Genera sitemaps XML por idioma con anotaciones hreflang (xhtml:link) + un sitemap index.

Entrada: CSV con columnas  grupo,bcp47,url,indexable
  grupo     identificador de la misma página en todos los idiomas (p. ej. "vestido-camisero-001")
  bcp47     código hreflang de esa versión (es, pt-BR, zh-Hans, sr-Latn, ...)
  url       URL absoluta de esa versión
  indexable "1"/"0" (las "0" NO entran: páginas aún sin revisar por un hablante nativo)
Opciones:  --x-default-lang en   (idioma de la versión x-default; por defecto "en")
Uso:  python3 scripts/generar_sitemaps_hreflang.py urls.csv salida/ --base https://moldey.com
Solo biblioteca estándar. Respeta el límite de 50.000 URLs por sitemap.
"""
import argparse, csv, os, sys
from collections import defaultdict
from xml.sax.saxutils import escape

MAX_URLS = 50000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("salida")
    ap.add_argument("--base", required=True, help="origen del sitio, p. ej. https://moldey.com")
    ap.add_argument("--x-default-lang", default="en")
    a = ap.parse_args()
    grupos = defaultdict(dict)
    with open(a.entrada, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            if fila["indexable"].strip() not in ("1", "true", "True", "si", "sí"):
                continue
            grupos[fila["grupo"]][fila["bcp47"].strip()] = fila["url"].strip()
    por_idioma = defaultdict(list)
    for g, vers in grupos.items():
        alt = []
        for lang, url in sorted(vers.items()):
            alt.append(f'    <xhtml:link rel="alternate" hreflang="{escape(lang)}" href="{escape(url)}"/>')
        xd = vers.get(a.x_default_lang)
        if xd:
            alt.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{escape(xd)}"/>')
        for lang, url in vers.items():
            por_idioma[lang].append((url, alt))
    os.makedirs(a.salida, exist_ok=True)
    indice = []
    for lang, items in sorted(por_idioma.items()):
        for n in range(0, len(items), MAX_URLS):
            parte = items[n:n + MAX_URLS]
            nombre = f"sitemap-{lang}.xml" if len(items) <= MAX_URLS else f"sitemap-{lang}-{n // MAX_URLS + 1}.xml"
            with open(os.path.join(a.salida, nombre), "w", encoding="utf-8") as f:
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n')
                for url, alt in parte:
                    f.write("  <url>\n    <loc>" + escape(url) + "</loc>\n" + "\n".join(alt) + "\n  </url>\n")
                f.write("</urlset>\n")
            indice.append(nombre)
    with open(os.path.join(a.salida, "sitemap-index.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for n in indice:
            f.write(f"  <sitemap><loc>{escape(a.base.rstrip('/') + '/' + n)}</loc></sitemap>\n")
        f.write("</sitemapindex>\n")
    print(f"{len(grupos)} grupos, {len(por_idioma)} idiomas, {len(indice)} sitemaps -> {a.salida}")


if __name__ == "__main__":
    sys.exit(main())
