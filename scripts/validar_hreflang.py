#!/usr/bin/env python3
"""Valida anotaciones hreflang en los sitemaps XML generados (o de tu sitio).

Comprueba: reciprocidad (si A apunta a B, B debe apuntar a A), auto-referencia, códigos con sintaxis válida,
un solo href por (página, idioma), x-default presente y URLs duplicadas en distintos idiomas.
Uso:  python3 scripts/validar_hreflang.py salida/sitemap-*.xml
Código de salida 1 si hay errores. Solo biblioteca estándar.
"""
import re, sys
import xml.etree.ElementTree as ET
from collections import defaultdict

NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "x": "http://www.w3.org/1999/xhtml"}
BCP47 = re.compile(r"^(x-default|[a-z]{2,3}(-[A-Z][a-z]{3})?(-([A-Z]{2}|\d{3}))?)$")


def main(paths):
    anot = {}  # url -> {hreflang: href}
    errores = []
    for p in paths:
        for u in ET.parse(p).getroot().findall("s:url", NS):
            loc = u.findtext("s:loc", namespaces=NS).strip()
            d = {}
            for l in u.findall("x:link", NS):
                h, href = l.get("hreflang"), l.get("href")
                if not BCP47.match(h or ""):
                    errores.append(f"{loc}: hreflang con sintaxis inválida '{h}'")
                if h in d and d[h] != href:
                    errores.append(f"{loc}: dos destinos distintos para hreflang '{h}'")
                d[h] = href
            anot[loc] = d
    for loc, d in anot.items():
        if loc not in d.values():
            errores.append(f"{loc}: falta la auto-referencia")
        if "x-default" not in d and d:
            errores.append(f"{loc}: no tiene x-default (recomendado)")
        for h, href in d.items():
            if href == loc:
                continue
            if href not in anot:
                errores.append(f"{loc}: apunta a {href} ({h}), que no está en los sitemaps analizados")
            elif loc not in anot[href].values():
                errores.append(f"{loc} -> {href} ({h}): falta el enlace de vuelta (reciprocidad)")
    vistos = defaultdict(list)
    for loc, d in anot.items():
        for h, href in d.items():
            if href == loc and h != "x-default":
                vistos[loc].append(h)
    for loc, hs in vistos.items():
        if len(hs) > 1:
            errores.append(f"{loc}: la misma URL declarada para varios idiomas {hs}")
    for e in errores:
        print("ERROR:", e)
    print(f"{len(anot)} URLs revisadas, {len(errores)} problemas")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) if len(sys.argv) > 1 else print(__doc__) or 2)
