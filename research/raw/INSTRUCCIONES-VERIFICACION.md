# Instrucciones de la 2.ª pasada (verificación con presupuesto de búsquedas ESTRICTO)

**Por qué existe esta pasada:** en la 1.ª pasada 16 agentes en paralelo agotaron el tope compartido de WebSearch (200 por turno) y casi todo quedó "SIN VERIFICACIÓN WEB". Ahora cada agente tiene un **presupuesto fijo de búsquedas**: usalo con criterio.

## Reglas de presupuesto
- Tu prompt indica **N = máximo de llamadas a WebSearch**. **No superes N.** Llevá la cuenta. Si una búsqueda devuelve "budget used up" (o similar), **dejá de buscar de inmediato** y terminá de escribir tus archivos con lo que tengas. No intentes rodear el límite.
- WebFetch NO funciona. Solo WebSearch (modo `standard`). Resultados sesgados a EE. UU.: buscá en el idioma/escritura nativa y con palabras de tienda ("PDF", "descargar", "comprar", "talles/tallas", "gratis").
- Priorizá por **valor comercial**: primero los idiomas/temas con más mercado; dejá para el final (o saltá) los de muy poca presencia web, y decí honestamente que no se pudo verificar.
- Una búsqueda bien elegida puede verificar varios términos a la vez (p. ej. el término de molde + "PDF" + "imprimir"). Mirá títulos y resúmenes de TODOS los resultados antes de concluir.

## Reglas de rigor
- Marcá `confianza=alta` solo con ≥2 usos reales (URLs distintas, ideal dominios distintos) vistos en resultados; `media` con 1 uso real o fuente indirecta clara; `baja` si seguís sin evidencia. **Nunca inventes URLs**; solo copiá URLs que aparecieron en tus resultados.
- Si un término de la 1.ª pasada resulta incorrecto o poco usado, corregilo y anotá el cambio en `ambiguedades_y_trampas`.
- Quitá la marca "SIN VERIFICACIÓN WEB" de una fila solo si la verificaste (aunque sea parcialmente: en ese caso escribí "VERIFICADO PARCIALMENTE: <qué sí/qué no>").
- No hagas `git`.

## Salidas por tipo de agente
**Terminología (grupo X):** leé `research/raw/terminologia/part-X.csv` (1.ª pasada) y escribí `research/raw/terminologia/part-X.v2.csv` con **todas** las filas y EXACTAMENTE las mismas 16 columnas (mismo orden), actualizando términos, `confianza` y `evidencia_urls`. Validá con el módulo `csv` de Python (mismo número de columnas, mismas filas). Además `research/raw/terminologia/verif-X.md` (breve): qué se verificó, qué cambió, qué sigue sin verificar y cuántas búsquedas usaste.
**Temático:** completá/corregí el informe indicado en un archivo nuevo `research/raw/V2-<tema>.md` (hechos con URL y fecha; etiquetas [HECHO]/[EVIDENCIA]/[OPINIÓN]/[NO VERIFICADO]); indicá qué pendientes del informe original quedaron resueltos.
**Respuesta final:** máximo 100 palabras: búsquedas usadas, qué quedó verificado, qué no.
