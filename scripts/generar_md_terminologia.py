#!/usr/bin/env python3
"""Genera 03-TERMINOLOGIA-MOLDERIA-100-IDIOMAS.md a partir de data/terminologia-100-idiomas.csv y data/oleadas.csv.
Uso: python3 scripts/consolidar_terminologia.py && python3 scripts/generar_oleadas.py && python3 scripts/generar_md_terminologia.py
"""
import csv, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDEN = ["ola 0", "ola 1", "ola 2", "ola 3", "ola 4", "ola 5", "variedad"]
TITULOS = {
    "ola 0": "Oleada 0 — Base", "ola 1": "Oleada 1 — Rentables", "ola 2": "Oleada 2 — Grandes y viables",
    "ola 3": "Oleada 3 — Media prioridad", "ola 4": "Oleada 4 — Largo plazo", "ola 5": "Oleada 5 — Hub mínimo",
    "variedad": "Variedades (sin sitio propio: se atienden con su idioma padre)",
}


def limpiar(s, n):
    s = re.sub(r"\s+", " ", (s or "").replace("|", "/")).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def main():
    term = {r["bcp47_web"]: r for r in csv.DictReader(open(os.path.join(RAIZ, "data", "terminologia-100-idiomas.csv"), encoding="utf-8"))}
    olas = list(csv.DictReader(open(os.path.join(RAIZ, "data", "oleadas.csv"), encoding="utf-8")))
    conf = {"alta": 0, "media": 0, "baja": 0}
    for t in term.values():
        conf[t["confianza"].lower()] = conf.get(t["confianza"].lower(), 0) + 1
    out = []
    w = out.append
    w("# 03 · Cómo se dice y se busca «molde de costura» en 113 idiomas (100 más hablados + 13 extras)\n")
    w("> **Generado automáticamente** desde `data/terminologia-100-idiomas.csv` (fuente de verdad, con 16 columnas por idioma, incluidas las URL de evidencia). "
      "No editar a mano este archivo: corregir el CSV y volver a ejecutar `scripts/generar_md_terminologia.py`.\n")
    w("## Cómo leer esta tabla (¡importante!)\n")
    w(f"- **Confianza:** `alta` = término visto en ≥2 usos reales (URL distintas) en resultados de búsqueda; `media` = 1 uso real o fuente indirecta clara; `baja` = **inferido por el modelo de IA sin verificación web**. Hoy: **{conf.get('alta',0)} alta · {conf.get('media',0)} media · {conf.get('baja',0)} baja** (de {len(term)}).")
    w("- **Ningún término de confianza `baja` ni `media` debe publicarse en producción sin revisión de un hablante nativo** que además confirme cómo busca la gente (Search Console, Keyword Planner, Trends, Wordstat, Naver, autosuggest local).")
    w("- La investigación usó solo búsqueda web (sin poder abrir páginas) y un presupuesto de búsquedas limitado: el resultado es un **punto de partida honesto**, no un diccionario cerrado. Cada fila del CSV indica en `ambiguedades_y_trampas` qué quedó sin verificar.")
    w("- En idiomas de poca presencia web escrita (hausa, yoruba, igbo, zulú, xhosa, quechua…) el comercio busca en inglés/francés/español/portugués: la columna lo dice. **No inventar términos nativos.**\n")
    w("## Hallazgos transversales\n")
    w("1. **La palabra del oficio no es la del producto.** En hindi/urdu la gente busca «cutting» («ब्लाउज कटिंग», «قمیض کی کٹنگ», Roman Urdu «kameez cutting»), no «pattern»; el producto físico en India es «paper cutting pattern / farma». El PDF aparece casi solo en inglés. En telugu, tamil y malayalam solo se vio uso latino/inglés («blouse cutting and stitching in Telugu»).")
    w("2. **«Pattern» puede ser estampado, no molde:** «ankara pattern» es el estampado de la tela; «shweshwe» es una tela (se cose con moldes occidentales buscados en inglés); en bengalí «নকশা» en prensa de moda significa diseño. Titular siempre «molde de costura / sewing pattern + prenda».")
    w("3. **Español:** conviven «patrones» (España; tallas EU 32–58, precios en €) y «moldes/moldería/talles» (Cono Sur: «Pack Talles S al XXL»); **el reparto por país no quedó verificado**. «Patronaje» no apareció. Ofrecer A4 + Carta + A0 juntos es el estándar.")
    w("4. **Portugués:** en Brasil el título dominante es «Molde em PDF» (≥10 listados en Hotmart; grade «PP ao G5» o «36 ao 54», «A4 + plotter»); «modelagem» **no** aparece en títulos de producto. Portugal sin evidencia.")
    w("5. **Francés:** el término real para proyector es «vidéoprojection»; los atributos recurrentes son «calques par taille», «marges de couture de 1 cm», formatos «A4 / A0 / US Letter». Québec y África sin verificar.")
    w("6. **Alemán:** «Schnittmuster» (+ «Sofort-Download», «Nahtzugabe», «Kontrollquadrat»); BERNINA (CH) usa «Schnittbogen» para el PDF impreso con cuadrado de control de 10×10 cm (no 5 cm). No se vio ninguna tienda indie alemana: no extrapolar.")
    w("7. **Japonés (confianza alta):** 型紙, 実物大型紙, 洋裁, 文化式原型; se vende en BOOTH, note y Yahoo!クリエイターズ.")
    w("8. **Chino:** simplificado «纸样 / 版型 / 服装样板»; Taiwán «紙型 / 紙樣 / 版型». wu, jin, xiang, hakka y min nan **se buscan en chino escrito**; el cantonés escrito de Hong Kong es mayormente chino tradicional (sin verificar «紙樣» de HK).")
    w("9. **Turco:** «kalıp», «PDF kalıp»; «patron» también se usa. **Indonesio:** «pola» (Tokopedia: «Pola dasar dan pecah pola»). **Malayo:** «pola baju kurung» confirmado, «corak jahitan» descartado.")
    w("10. **Nórdicos:** finés «kaava / ompelukaava» (Ottobre Design) y danés «mønster / symønster» con confianza alta; sueco y noruego «mønster/mönster» con evidencia débil.")
    w("11. **Sublimación:** casi no se pudo verificar en idiomas distintos del inglés. En inglés: «cut & sew patterns / sublimation patterns»; la plantilla es un *dieline* (PDF/AI/EPS/CDR). Sialkot (Pakistán) aparece como polo en inglés. Una app en español ofrece «archivos DXF/AI para sublimación». **Pendiente de verificar con nativos.**")
    w("12. **Árabe, persa, hebreo (alta en el término principal):** árabe «باترون» (préstamo «patron», visto en 4 dominios), persa «الگوی خیاطی» (3 dominios), hebreo «גזרה» domina en foros y revistas (y «תבנית תפירה» es secundario). Variedades egipcio, Golfo y marroquí con confianza media; levantino, sudanés, iraquí, najdí, argelino, tunecino, pastún y kurdo siguen en baja. **No se pudo medir** si en el Golfo/Egipto se busca en árabe o en inglés, ni si el Magreb busca en francés. Irán: Telegram bloqueado desde 2018 e Instagram desde 2022 (fuente: voidly.ai, feb-2026): pagos internacionales imposibles, prioridad C.")
    w("13. **Sin evidencia web:** italiano, neerlandés, catalán, afrikáans, pidgin nigeriano, criollo haitiano, armenio, amárico, igbo, oromo y somalí (los resultados vinieron en inglés o castellano).\n")
    w("## Tabla por oleada\n")
    w("Columnas: idioma · código · cómo se busca «molde de costura» · «PDF/digital» · «sublimación» · confianza. Para el detalle (romanización, sinónimos, imprimir en casa, oficio, plataformas, trampas, evidencia) ver el CSV.\n")
    for o in ORDEN:
        sel = [r for r in olas if r["oleada"] == o]
        if not sel:
            continue
        w(f"### {TITULOS[o]}\n")
        w("| Idioma | Código | «Molde de costura» | PDF / digital | Sublimación | Confianza |")
        w("|---|---|---|---|---|---|")
        for r in sel:
            t = term[r["bcp47_web"]]
            extra = f" → {r['atendido_con']}" if r["atendido_con"] else ""
            w(f"| {r['idioma_es']}{extra} | `{r['bcp47_web']}` | {limpiar(t['termino_molde_costura'], 130)} | {limpiar(t['termino_pdf_digital'], 70)} | {limpiar(t['termino_sublimacion'], 60)} | {t['confianza']} |")
        w("")
    w("## Trampas y ambigüedades (oleadas 0–2)\n")
    for o in ORDEN[:3]:
        for r in [x for x in olas if x["oleada"] == o]:
            t = term[r["bcp47_web"]]
            w(f"- **{r['idioma_es']} (`{r['bcp47_web']}`):** {limpiar(t['ambiguedades_y_trampas'], 420)}")
    w("")
    w("## Cómo usar esto en moldey.com\n")
    w("1. Cargar `data/terminologia-100-idiomas.csv` como **glosario inicial** de cada idioma (bloqueado en la herramienta de traducción) y como lista de **consultas objetivo** (20–30 por idioma).")
    w("2. Antes de abrir un idioma: revisión nativa del término principal, de los de «PDF/digital» y «imprimir en casa», y prueba de demanda (Search Console / Keyword Planner / Trends / Wordstat / Naver).")
    w("3. Registrar en el CSV los cambios y subir la confianza a `alta` solo con ≥2 usos reales verificados; mantener `evidencia_urls`.")
    w("4. Para filas de confianza `baja`, **no publicar páginas indexables**: usar el hub mínimo o esperar la revisión.")
    path = os.path.join(RAIZ, "03-TERMINOLOGIA-MOLDERIA-100-IDIOMAS.md")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("OK ->", path, f"({len(out)} líneas)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
