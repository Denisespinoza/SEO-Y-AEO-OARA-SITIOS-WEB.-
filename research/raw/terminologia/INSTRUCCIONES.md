# Instrucciones para los agentes de terminología

**Negocio:** moldey.com vende moldes digitales de costura/indumentaria para todo el mundo, en formatos para **imprimir** (PDF A4/Letter/A0), **editar** (vectorial, DXF/AAMA, CAD) y **sublimar** (plantillas listas para impresión por sublimación). Es *moldería textil*.

**Objetivo:** documentar cómo se dice y cómo se BUSCA eso en cada idioma de tu archivo `asignacion-<GRUPO>.csv`.

## Herramientas y límites (importante)
- **WebFetch NO funciona** en este entorno (DNS). Usá **WebSearch** (resultados sesgados a EE. UU.: buscá en el idioma nativo y escritura nativa).
- Modo `standard` para verificar un término; `extended` solo cuando algo clave no aparece.
- Verificá buscando el término nativo junto a palabras de tienda/blog ("PDF", "descargar", "comprar", "gratis", "talla") y mirá si los resultados reales (tiendas, blogs de costura, Etsy local, marketplaces, YouTube, Pinterest) usan ese término. Mejor evidencia: tiendas y editoriales de patrones de ese idioma, no diccionarios.
- Fuentes útiles: tiendas/editoriales locales de patrones de costura, libros/revistas de patronaje, escuelas de moda, Wikipedia local del artículo "sewing pattern", Wiktionary, Etsy/Shopee/Tokopedia/Mercado Libre/Trendyol/Allegro/Rakuten/Taobao etc. según región.
- **No inventes.** Si no pudiste verificar un término, ponelo igual si es muy probable, pero con `confianza=baja` y decilo. Es preferible dejar un campo vacío antes que una invención. Nunca rellenes con traducción literal del inglés sin comprobar uso real.

## Qué producir
1. **`part-<GRUPO>.csv`** (UTF-8, comillas dobles para todos los campos que contengan comas; separador `;` dentro de un campo para varios valores), **una fila por idioma de tu asignación**, con EXACTAMENTE estas columnas:

| columna | contenido |
|---|---|
| `bcp47_web` | el código de tu asignación (no lo cambies) |
| `idioma_es` | nombre en español (de tu asignación) |
| `termino_molde_costura` | término(s) NATIVOS (en su escritura) más usados en tiendas/blogs para **molde/patrón de costura de prendas** (lo que se compra para coser una prenda) |
| `romanizacion` | transliteración latina si la escritura no es latina (si es latina, dejar vacío) |
| `sinonimos_y_variantes` | otras formas reales de buscarlo (variantes regionales, formas coloquiales, anglicismos usados) separadas con `;` |
| `termino_pdf_digital` | cómo se dice "molde/patrón en PDF / digital / descargable" |
| `termino_patronaje_oficio` | el oficio/técnica de trazar moldes ("patronaje", "pattern making/drafting"), y "patronista" si existe |
| `termino_imprimir_en_casa` | "imprimir en casa", "hoja A4/Carta", "armar/pegar hojas", "proyector", "imprimir en copistería/plotter" |
| `termino_sublimacion` | "sublimación", "plantilla para sublimar", "sublimación total", "ropa deportiva/camisetas sublimadas" |
| `termino_coser_confeccion` | "coser", "costura", "confección", "sastrería", "tallista" (palabras base que la gente busca) |
| `uso_de_anglicismos` | ¿la gente busca en inglés ("sewing pattern", "PDF pattern")? ¿se mezcla? (alto/medio/bajo + una línea) |
| `buscadores_y_plataformas` | buscadores, redes, marketplaces y asistentes de IA dominantes para este idioma/región (breve) |
| `ambiguedades_y_trampas` | falsas amistades y ambigüedades (p. ej. "molde" = recipiente; "pattern" = estampado), diferencias dialectales, escritura/ortografía múltiple |
| `nota_localizacion` | tamaño de papel habitual (A4/Letter), unidad de medidas (cm/in), tallas locales, métodos de pago o hábitos de compra relevantes si los encontraste |
| `confianza` | `alta` (verificado con ≥2 usos reales), `media` (1 uso real o fuente indirecta), `baja` (inferido, sin verificar) |
| `evidencia_urls` | 1–3 URLs reales vistas en resultados de búsqueda que muestren el uso (separadas por `;`) |

2. **`notas-<GRUPO>.md`** (breve, en español): hallazgos transversales de tu grupo (diferencias entre variedades, qué idiomas conviene servir con otro, riesgos de traducción, oportunidades de nicho, lo que NO pudiste verificar).

## Reglas de calidad
- Para variedades habladas que se escriben con otro idioma estándar (p. ej. árabe egipcio → árabe estándar; bhojpurí → hindi; wu → chino simplificado), indicá en `ambiguedades_y_trampas` cuál es la forma escrita de búsqueda real y poné en `termino_molde_costura` el término que realmente se busca; agregá solo diferencias léxicas locales si existen.
- Escritura: usá la escritura nativa correcta. Para chino distinguí simplificado/tradicional; para serbio, cirílico/latín; para árabe, términos con o sin tashkeel (sin).
- Idiomas de poca presencia web: decilo con honestidad (`uso_de_anglicismos` alto, `confianza` baja) en vez de inventar.
- Español: escribí tus notas en español. Los términos van en el idioma objetivo.
- Escribí los archivos en `/home/user/seo-y-aeo-oara-sitios-web.-/research/raw/terminologia/` y validá el CSV con Python (`csv` module: mismo número de columnas en todas las filas, todas las filas de tu asignación presentes).
- No hagas `git` de ningún tipo.
- Respuesta final al terminar: máximo 120 palabras (cuántos idiomas, cuántos con confianza alta/media/baja, qué quedó sin verificar).
