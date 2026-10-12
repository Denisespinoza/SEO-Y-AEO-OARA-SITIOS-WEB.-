#!/usr/bin/env python3
"""Asigna cada idioma de data/idiomas-master.csv a una oleada y genera data/oleadas.csv.

Las oleadas salen del modelo de priorización del informe T6 (hipótesis, NO datos medidos) y se ajustan con datos
reales (Search Console, Keyword Planner, Trends, Wordstat, Naver) antes de cada oleada.
Uso: python3 scripts/generar_oleadas.py
"""
import csv, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLEADAS = {
    "0": ("Base (ya avanzada)", ["en", "es"]),
    "1": ("Rentables", ["pt", "de", "id", "fr", "ru"]),
    "2": ("Grandes y viables", ["tr", "hi", "ar", "vi", "it", "pl", "nl", "ja", "fil"]),
    "3": ("Media prioridad", ["uk", "th", "ms", "bn", "ur", "ko", "fa", "ro", "cs", "hu", "el", "sv", "da", "nb", "fi", "he",
                                "ta", "te", "mr", "gu", "kn", "ml", "zh-Hans", "yue"]),
    "4": ("Largo plazo", ["ne", "si", "km", "my", "lo", "kk", "uz", "az", "sr", "hr", "bg", "sk", "sl", "lt", "lv", "et",
                          "ka", "hy", "mn", "sw", "af", "ca"]),
    "5": ("Hub mínimo (1 página + glosario)", ["ha", "yo", "ig", "om", "zu", "xh", "sn", "ny", "rw", "ln", "ak", "ff", "so", "mg",
                                                "ti", "am", "qu", "ht", "sd", "ps", "ku", "as", "or"]),
}
# Variedades: se atienden con su "padre" (sin sitio propio). bcp47 -> padre
VARIEDADES = {
    "arz": "ar", "apc": "ar", "apd": "ar", "ary": "ar", "acm": "ar", "ars": "ar", "arq": "ar", "aeb": "ar", "afb": "ar",
    "bho": "hi", "mai": "hi", "awa": "hi", "mag": "hi", "hne": "hi", "raj": "hi", "bgc": "hi",
    "dcc": "ur", "skr": "ur", "pnb": "ur",
    "nan": "yue", "wuu": "zh-Hans", "cjy": "zh-Hans", "hsn": "zh-Hans", "hak": "zh-Hans",
    "jv": "id", "su": "id", "ceb": "fil", "pcm": "en",
}

def main():
    master = list(csv.DictReader(open(os.path.join(RAIZ, "data", "idiomas-master.csv"), encoding="utf-8")))
    cods = {r["bcp47_web"]: r for r in master}
    asign = {}
    for ola, (_, langs) in OLEADAS.items():
        for l in langs:
            if l in asign:
                print("DUPLICADO en oleadas:", l); return 1
            asign[l] = ("ola " + ola, "")
    for v, padre in VARIEDADES.items():
        if v in asign:
            print("variedad también en oleada:", v); return 1
        asign[v] = ("variedad", padre)
    faltan = [c for c in cods if c not in asign]
    sobran = [c for c in asign if c not in cods]
    if faltan or sobran:
        print("SIN ASIGNAR:", faltan, "| NO EXISTEN en el master:", sobran); return 1
    out = os.path.join(RAIZ, "data", "oleadas.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["bcp47_web", "idioma_es", "tipo", "oleada", "atendido_con"])
        for r in master:
            o, padre = asign[r["bcp47_web"]]
            w.writerow([r["bcp47_web"], r["idioma_es"], r["tipo"], o, padre])
    from collections import Counter
    print(Counter(v[0] for v in asign.values()), "->", out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
