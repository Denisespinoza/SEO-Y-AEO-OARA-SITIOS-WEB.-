# Verificación A6 (2.ª pasada) - 2026-10-12

**Búsquedas usadas: 14 de 14** (WebSearch, modo standard). Nunca apareció "budget used up". Salida: `part-A6.v2.csv` (14 filas + cabecera, 16 columnas, validado con `csv`).

Convención de `confianza` en v2: `media` = el término central (molde) tiene ≥1 uso real visto y quedan columnas sin verificar; `baja` = el término central sigue sin evidencia. **Ninguna fila llega a `alta`** (ningún idioma tiene ≥2 usos comerciales visibles en dominios distintos para todo el conjunto de columnas). Los resúmenes del buscador son generados por el propio motor: cuando un dato solo salió de ahí (no de un título/URL) está marcado "vía resumen".

## Registro de búsquedas
| # | Idioma | Consulta (resumen) | Resultado útil |
|---|---|---|---|
| 1-2 | id | pola baju PDF download / beli pola jahit PDF A4 | Tokopedia "pola dress anak"; libro "Pola dasar dan pecah pola"; el resto spam o Etsy/Fiverr extranjeros |
| 3 | id | pola jersey sublimasi template CDR | artículo UPI (konveksi Padang), 2 plantillas CDR en Gumroad |
| 4-6 | tr | kalıp PDF indir / ücretsiz kalıp / forma kalıbı sublimasyon | **nada útil** (spam en inglés, hojas para colorear) |
| 7-8 | th | แพทเทิร์น PDF / เสื้อซับลิเมชั่น | solo 1 directorio (yellowpages.co.th); resto en inglés |
| 9 | ms | pattern baju kurung PDF corak jahitan | guía PDF de pago en mykreasi.com |
| 10 | fil | sewing pattern PDF Philippines short bond | solo fichas Payhip de punto de cruz |
| 11 | my | birmano | 0 resultados en birmano |
| 12 | km | jemer | 0 resultados en jemer |
| 13 | uz/kk/az | выкройки PDF лекала + lekala andoza kroy | solo ruso general (Rusia), sin resultado regional |
| 14 | tr | PDF dikiş kalıbı con `allowed_domains` (Etsy, Trendyol, Hepsiburada, YouTube, Pinterest) | **7 usos reales turcos** (Pinterest y YouTube) |

Lección: con consultas en escritura nativa el buscador devuelve inglés o spam salvo que se restrinja con `allowed_domains` a Pinterest/YouTube/tiendas. Para turco funcionó; para th/my/km no se probó (sin presupuesto).

## Verificado
- **id**: `pola` = patrón de costura (Tokopedia `/find/pola-dress-anak`, libro "Pola dasar dan pecah pola busana", Kanisius 2001); anglicismos `pattern making tools` (Tokopedia) y `pattern cutting` (tesis Telkom). Sublimación (vía resumen): `sublimasi`, `kertas sublimasi`, `konveksi`, `pola jersey`; plantillas jersey `.CDR` existen en Gumroad (no probado que sea mercado id). Precio de referencia: pola dress anak ~Rp15.000-99.000 (vía resumen).
- **tr**: `kalıp` = patrón; `PDF kalıp`, `ücretsiz PDF kalıp`, `elbise kalıpları PDF indir`, `dikiş kalıpları`, `A4 çıktısını birleştirme` (6 URLs, Pinterest + YouTube). Pinterest y YouTube confirmados como plataformas.
- **ms**: `pola baju kurung` / `melakar pola` en guía PDF de pago (mykreasi.com, RM49.90). 1 solo dominio.
- **th**: `งานซับลิเมชั่น` (yellowpages.co.th). Solo eso.
- **fil**: `short bond paper` (8.5 x 11) y `PDF Pattern / Downloadable File` en inglés (3 fichas Payhip, punto de cruz).
- **uz/kk/az**: el vocabulario ruso `выкройки PDF` / `лекала` existe y se vende para A4, pero todo es Rusia (rublos, bancos rusos).

## Cambios respecto a la 1.ª pasada
1. **tr: corrección importante.** `patron` NO es solo "jefe": aparece como patrón de costura en el título de pin "Dikiş Kalıpları ve Patronları" (el resumen cita además el dominio dikiskalipvepatronlari.com; no vino como enlace). Es menos frecuente que `kalıp`. Añadido a sinónimos y reescrita la trampa.
2. **ms:** `pola baju kurung` pasa a primer término; **`corak jahitan` desaconsejado** (no apareció en ningún resultado; `corak` = motivo/estampado). Se retira la afirmación "pattern domina sobre pola": el único producto malayo visto usa `pola`. `uso_de_anglicismos` degradado a "medio-por verificar". Añadido `melakar pola`.
3. **id:** añadidas 3 trampas nuevas: `Generator Pola AI` (pola = patrón gráfico), SERP de "pola baju anak" contaminado por PDFs-spam en dominios ajenos, y `pola jahit/template` en servicios de archivo de impresión de jerseys = plantilla vectorial, no molde de costura.
4. **fil:** trampa nueva: "PDF pattern" en contexto filipino suele ser punto de cruz.
5. `confianza`: id, tr, ms de baja a media. Resto sigue baja. Filas sin verificación llevan "SIN VERIFICACIÓN WEB" (my, km, jv, su, ceb, lo); filas con verificación parcial llevan "VERIFICADO PARCIALMENTE: sí/no" al inicio de `ambiguedades_y_trampas`.

## Sigue sin verificar
- **id:** `pola baju/jahit PDF`, `unduh/download pola`, `pola siap cetak`, kemeja/gamis/kebaya, `jersey printing/full print`, `sablon` vs sublimasi, Shopee/Lazada/TikTok Shop. No apareció ninguna tienda indonesia de patrones PDF (puede ser sesgo del buscador).
- **tr:** `gömlek/pantolon kalıbı`, `hazır kalıp`, `kalıp çıkarma/serileme`, **toda la sublimación** (`forma kalıbı`, `sublimasyon`, `halı saha forması`), Trendyol/Hepsiburada/Etsy/N11. Ninguna tienda o blog turco visto (solo Pinterest/YouTube).
- **th:** todo lo de patrones (`แพทเทิร์น`, `แบบตัดเสื้อ`, PDF, A4) y `เสื้อกีฬาพิมพ์ลาย`.
- **ms:** `pattern baju` (anglicismo), `muat turun`, `jersi sublimasi`, `tempahan baju`.
- **fil:** todo término tagalo de ropa y sublimación.
- **my y km:** nada (1 búsqueda cada una, 0 resultados en su escritura; el hueco es del buscador, no prueba de ausencia). `ပုံစံဖော်`, `គំរូកាត់ដេរ` siguen sin verificar.
- **uz/kk/az:** `andoza`, `kroy`, `lekala` (latín), `үлгі`, `qəlib`; ningún dominio .uz/.kz/.az. La hipótesis "el ruso es lengua puente" es plausible, no demostrada.
- **jv, su, ceb, lo:** 0 búsquedas por instrucción (poca presencia web). jv/su heredan parcialmente id; ceb hereda parcialmente fil; lo sin nada.

## Recomendación si hay otra pasada
Repetir con `allowed_domains`: tr (etsy.com, trendyol.com, hepsiburada.com) para sublimación y tiendas; id (tokopedia.com, shopee.co.id) para `pola ... PDF`; th (shopee.co.th, pantip.com, facebook.com); uz/kk (olx.kz, olx.uz, kaspi.kz).
