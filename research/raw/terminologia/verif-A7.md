# Verificación A7 (2.ª pasada) — 14 de 14 búsquedas WebSearch usadas

Fecha: 2026-10-12. Ninguna búsqueda fue rechazada por presupuesto. WebFetch no se usó. Salida: `part-A7.v2.csv` (15 filas + cabecera, 16 columnas, validado con `csv`).

## Resumen honesto
Las 14 búsquedas en idioma nativo devolvieron sobre todo tiendas en inglés (Etsy, Payhip, Gumroad, Pixie Faire, Winslet's, Truro, Sew Over It, Fiverr). Solo aparecieron unos diez dominios nativos útiles, ninguno con un marketplace o tienda grande. **La ausencia de tiendas locales en estos resultados no prueba que no existan**: el buscador está sesgado a EE. UU. Por eso sube poco la confianza: **0 alta, 6 media (ru, pl, el, cs, sl, lt), 9 baja**. Ninguna fila llega a "alta" porque ningún término tiene ≥2 usos de dominios distintos *en contexto de patrón de costura en PDF*.

## Búsquedas y resultado
| # | Idioma | Consulta (resumida) | Qué apareció |
|---|---|---|---|
| 1 | hu | szabásminta PDF letölthető ruha … | 1 vendedora húngara en Gumroad (falda base, A4, pago Gumroad/PayPal, HUF→USD); el resto en inglés. "szabásminta" no apareció literal |
| 2 | el | πατρόν ραπτικής PDF φόρεμα … | **market.sxediomodas.gr** (tienda griega propia, PDF A4 + A0, 9-12 EUR, margen 1 cm) con títulos griegos "Πατρόν …" y URLs/títulos en inglés |
| 3 | cs | střih na šaty PDF ke stažení … | Directorio Šikulíci (Google Sites: střihy zdarma, "databáze střihů v PDF"), libro "Střihněte si na šaty – konstrukce oděvních střihů" (Grada 2016). Ninguna tienda |
| 4 | sr/hr | krojna lista šnit kroj za haljinu … | Solo academia de sastrería (akademijaoxford.com) y resultados en inglés. Ni "krojna lista" ni "šnit" |
| 5 | bg | изкройка рокля PDF … кройка | Nada búlgaro de patrones (Trendyol BG de ropa hecha, tiendas en inglés) |
| 6 | sk | strih na šaty PDF na stiahnutie … | Devolvió el directorio checo Šikulíci + Primark SK (ropa). Nada eslovaco de patrones |
| 7 | sl | krojni list obleka PDF … | **mladinska-knjiga.si** (PDF de patrón "Šivamo džersi 038 Krilo z naborki", 2026), cpi.si (catálogo "Krojaštvo"), dlib.si/COBISS (libro "Krojni vzorci za otroška oblačila") |
| 8 | lt | siuvimo iškarpos suknelė PDF … lekalai | **paslaugos.lt**: "lekalai", "Lekalai drabužiams" (servicios de trazado y gradación). "iškarpos" no apareció |
| 9 | lv+et | piegriezumi … \| lõiked … | Nada relevante (consulta combinada con "\|" fue mala idea: devolvió patrones de tejido y PDFs ajenos) |
| 10 | pl | sublimacja wykroje … | **useme.com/pl** ("sublimacja + wizka 3D", "full-zadruku") y grawerton.pl (blanks para sublimación). "wykroje do sublimacji" no apareció |
| 11 | ro | sublimare tipare … | Nada rumano (solo páginas en inglés / spam multilingüe de Xinflying) |
| 12 | cs | sublimace střihy dresy … | Nada checo (mismo spam Xinflying con título en inglés) |
| 13 | hu | női szabásminta PDF webshop … | Misma vendedora Gumroad HU + vendedores internacionales. Ningún webshop húngaro |
| 14 | hr/sr | krojevi za šivanje haljina kroj PDF … | Nada croata/serbio (Zara HR/BA, Payhip, Gumroad, Named Clothing) |

Las páginas de Xinflying (`xinflyinggroup.com/<lang>/sportswear-sublimation-trends-2026`) salen en muchos idiomas pero son traducción automática de un artículo en inglés (títulos en inglés): **no se usan como evidencia**.

## Qué cambió en el CSV
- **el → media.** "πατρόν" visto en títulos de producto de una tienda griega real; formato PDF A4 + A0 para copy shop; la tienda usa también "pattern" en inglés en URLs y títulos; marca "Sxedio Modas" (Greeklish de σχέδιο).
- **cs → media.** "střih/střihy" y "konstrukce oděvních střihů" confirmados en 2 dominios, pero en contexto de directorio gratuito y libro, no de tienda PDF.
- **sl → media.** Familia kroj-: añadidos "krojni vzorci", "krojni deli", "dodatki za šiv", "krojaštvo", "kontrolni kvadrat"; **"krojni list" y "krojna pola" siguen sin confirmar**; marcado "(sin confirmar en página real)". Parte del detalle (krojni deli, kontrolni kvadrat) viene del resumen parafraseado del buscador, no de texto literal visto.
- **lt → media y orden corregido:** "lekalai" pasa al primer lugar (único término visto); "iškarpos" queda "(sin verificar)". Ojo: la evidencia es de servicios de producción en un solo dominio, no de tienda de PDF para consumidor.
- **pl (media, sin cambio de nivel):** "sublimacja" confirmada en uso comercial real; añadidos "full zadruk/projekty full-zadruku" y "wizka 3D". "wykroje do sublimacji" **no se encontró**: en polaco el trabajo se describe como diseño de estampado total, no como "wykroje".
- **hu (baja):** solo "minta / szoknyaalap-minta" visto; **"szabásminta" no apareció literal**.
- **ru/uk:** sin búsquedas nuevas. Dato indirecto (1 fuente, resumen del buscador) de `en.cuturie.com.ua`: tienda ucraniana de PDF, ~2 USD, slug con tallas 42-62 (la 1.ª pasada decía 40-60), y declara que **no acepta tarjetas bancarias rusas**. No sustituye la verificación de sanciones/pagos de `notas-A7.md` §4.
- Marcas "TODO: conocimiento de fondo, no verificado" reemplazadas en `buscadores_y_plataformas` por "VERIFICADO PARCIALMENTE: …" (el, cs, sk, sl, lt, hu, sr, ru, uk) o "SIN VERIFICACIÓN WEB (2.ª pasada: …)" (ro, hr, bg, lv, et).

## Respuestas a las preguntas puntuales
- **sr/hr: ¿krojna lista o šnit?** No se pudo determinar; ninguno apareció en 2 búsquedas. Solo se vio la familia "krojač / kurs za krojača". Se deja el orden de la 1.ª pasada.
- **bg: изкройка vs кройка:** no resuelto con evidencia. Se mantiene "изкройка" primero por criterio lingüístico, marcado como tal.
- **sk:** la consulta eslovaca devolvió contenido checo. Es un apoyo débil (1 búsqueda, buscador sesgado) a la hipótesis de consumo cruzado cs/sk.
- **Sublimación:** confirmada solo en polaco. **Sin confirmar en rumano y checo** (sin resultados nativos).
- **lv, et:** sin ninguna evidencia (1 búsqueda combinada). La búsqueda con "|" no sirve; para otra ronda, una búsqueda por idioma.

## Sigue sin verificar
- ro, hr, bg, lv, et, sk: ningún término nativo visto. uk: sin búsqueda propia.
- Plataformas, buscadores (Yandex, Seznam, Allegro, eMAG, Skroutz, Kupindo, Njuškalo, etc.), pagos locales, tallas, monedas, sanciones/pagos RU/BY: conocimiento de fondo o dato indirecto, no verificado.
- "szabásminta" (hu), "krojna lista"/"šnit" (sr/hr), "krojni list" (sl), "iškarpos" (lt), "tipar" y sublimare (ro), sublimace (cs).
- Sugerencia para otra ronda: consultas con nombres de tiendas conocidas (p. ej. Vikisews, Lekala, Fler.cz, Allegro) o con `allowed_domains` de TLD nativos, porque las consultas genéricas con "PDF" atraen vendedores en inglés.
