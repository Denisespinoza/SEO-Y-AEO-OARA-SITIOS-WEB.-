#!/usr/bin/env python3
"""Une research/raw/terminologia/part-*.csv con data/idiomas-master.csv y valida la cobertura.

Salida:
  data/terminologia-100-idiomas.csv   (una fila por idioma: master + terminología)
  data/terminologia-100-idiomas.json
Uso:  python3 scripts/consolidar_terminologia.py
Solo biblioteca estándar.
"""
import csv, glob, json, os, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(RAIZ, "data", "idiomas-master.csv")
def _partes():
    """Por grupo usa la 2.ª pasada (part-X.v2.csv, verificada con búsquedas) si existe; si no, la 1.ª (part-X.csv)."""
    d = os.path.join(RAIZ, "research", "raw", "terminologia")
    elegidas = []
    for p1 in sorted(glob.glob(os.path.join(d, "part-A?.csv"))):
        p2 = p1[:-4] + ".v2.csv"
        elegidas.append(p2 if os.path.exists(p2) else p1)
    return elegidas


PARTES = _partes()
COLS_TERM = [
    "termino_molde_costura", "romanizacion", "sinonimos_y_variantes", "termino_pdf_digital",
    "termino_patronaje_oficio", "termino_imprimir_en_casa", "termino_sublimacion",
    "termino_coser_confeccion", "uso_de_anglicismos", "buscadores_y_plataformas",
    "ambiguedades_y_trampas", "nota_localizacion", "confianza", "evidencia_urls",
]


def _norm(k):
    """Normaliza nombres de columna (sin tildes, minúsculas): algunos agentes escribieron 'confección'."""
    return "".join(c for c in unicodedata.normalize("NFD", (k or "").strip()) if unicodedata.category(c) != "Mn").lower()


def leer(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [{_norm(k): v for k, v in fila.items()} for fila in csv.DictReader(f)]


def main():
    master = leer(MASTER)
    por_codigo = {r["bcp47_web"]: r for r in master}
    term, problemas = {}, []
    for p in PARTES:
        for i, fila in enumerate(leer(p), start=2):
            cod = (fila.get("bcp47_web") or "").strip()
            if cod not in por_codigo:
                problemas.append(f"{os.path.basename(p)} fila {i}: código desconocido '{cod}'")
                continue
            if cod in term:
                problemas.append(f"{os.path.basename(p)} fila {i}: código duplicado '{cod}'")
            faltan = [c for c in COLS_TERM if c not in fila]
            if faltan:
                problemas.append(f"{os.path.basename(p)} fila {i} ({cod}): faltan columnas {faltan}")
            term[cod] = {c: (fila.get(c) or "").strip() for c in COLS_TERM}
    sin = [c for c in por_codigo if c not in term]
    for c in sin:
        problemas.append(f"sin terminología: {c} ({por_codigo[c]['idioma_es']})")
    filas = []
    for m in master:
        t = term.get(m["bcp47_web"], {c: "" for c in COLS_TERM})
        filas.append({**m, **t})
    out_csv = os.path.join(RAIZ, "data", "terminologia-100-idiomas.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(filas)
    with open(os.path.join(RAIZ, "data", "terminologia-100-idiomas.json"), "w", encoding="utf-8") as f:
        json.dump(filas, f, ensure_ascii=False, indent=2)
    conf = {"alta": 0, "media": 0, "baja": 0, "(vacía/otra)": 0}
    for f_ in filas:
        k = f_["confianza"].lower()
        conf[k if k in conf else "(vacía/otra)"] += 1
    print(f"Idiomas: {len(filas)} | con terminología: {len(term)} | confianza: {conf}")
    for p in problemas:
        print("AVISO:", p)
    return 1 if any(not x.startswith("sin terminología") for x in problemas) else 0


if __name__ == "__main__":
    sys.exit(main())
