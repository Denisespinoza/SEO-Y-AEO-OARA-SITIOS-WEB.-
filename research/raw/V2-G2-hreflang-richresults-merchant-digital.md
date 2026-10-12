# V2-G2 — Verificación temática: hreflang con escritura, rich results 2026, Product/Offer y Merchant Center para digitales, Baidu/Naver, IndexNow, Pinterest, sitemaps

Verificador: G2. Fecha de consulta: 12 de octubre de 2026. Presupuesto: **12 de 12 búsquedas WebSearch usadas** (agotado; no se hizo ninguna más).
Informes que se completan: `T3-seo-internacional-tecnico.md` (sección 14) y `T2-comercio-agentico-feeds.md` (sección 11).

## 0. Limitaciones que condicionan TODO lo de abajo

1. **No pude abrir ninguna página primaria.** `WebFetch` falló (`getaddrinfo ENOTFOUND developers.google.com`) y un `curl` de prueba por el proxy devolvió 403 (`CONNECT tunnel failed`). No intenté rodearlo.
2. **Los resultados de WebSearch son resúmenes redactados por la herramienta, no citas literales.** Cuando abajo digo "la doc de Google dice", significa "el resumen de la herramienta sobre la URL de Google que apareció en los resultados". Es evidencia indirecta aunque la URL sea oficial. Por eso uso `[EVIDENCIA]` y no `[HECHO]` salvo donde dos búsquedas independientes coinciden y la URL es oficial.
3. Los resultados no traen fecha de publicación; las fechas que cito son las que mencionan los propios resúmenes (entradas de changelog) y quedan marcadas como tales.

Etiquetas: [HECHO] = fuente primaria vista en resultados y resumen coherente en ≥2 búsquedas; [EVIDENCIA] = resumen de fuente oficial no confirmado literalmente, o terceros coincidentes; [OPINIÓN] = inferencia mía o consejo de industria; [NO VERIFICADO].

## 1. Resumen: qué pendientes quedaron resueltos

| # | Pendiente original | Estado | Veredicto corto | Confianza |
|---|---|---|---|---|
| 1 | `zh-Hans`/`zh-Hant`/`sr-Latn` en hreflang (T3 §14, §11) | **Parcial** | Un resumen de la doc de Google dice que acepta escrituras ISO 15924; un tercero (http.dev) también. No vi el texto literal. `sr-Latn` solo tiene apoyo genérico. | media (zh) / baja (sr-Latn) |
| 2 | Rich results vigentes 2026 (T3 §14, T2 §11.5) | **Casi resuelto** | HowTo: eliminado. FAQ: eliminado en mayo de 2026 (según changelog, con una contradicción menor). Product/Merchant listings/VideoObject: vigentes y con cambios de doc en 2026. Breadcrumb/Organization: sin señales de retiro, sin confirmación explícita. | media-alta |
| 3 | Product/Offer para digitales descargables (T3 §14, T2 §11.5) | **Parcial** | Google no tiene una guía específica para digitales; `shippingDetails` y la política de devoluciones son opcionales/recomendadas; existe `MerchantReturnNotPermitted`. | media |
| 4 | Merchant Center / digitales (T2 §11.3) | **Parcial** | Confirmado: eBooks/libros digitales no se admiten en anuncios de Shopping y hay suspensión crítica a nivel de cuenta (`prohibited_content_ebooks`). Plantillas/PDF de patrones: ni listados como prohibidos ni como admitidos en lo que vi. | alta (eBooks) / baja (plantillas) |
| 5 | hreflang en Baidu y Naver (T3 §14) | **Parcial** | Solo terceros: ninguno de los dos usa hreflang; usan meta de idioma. Sin doc oficial. | media-baja |
| 6 | IndexNow y Google (T3 §14) | **Resuelto (terceros)** | Google no lo soporta; Bing, Yandex, Naver, Seznam, (Yep) sí. Sin página oficial vista. | alta (Google no) |
| 7 | Pinterest y digitales (T2 §11.4) | **No resuelto** | No hay texto de política sobre bienes digitales en lo que apareció. | baja |
| 8 | Límites de sitemap de Google (T3 §14) | **Resuelto** | 50 MB sin comprimir o 50.000 URLs por sitemap; un índice admite hasta 50.000 sitemaps. CrUX por país: **no verificado** (no alcanzó el presupuesto). | alta (sitemap) |

## 2. hreflang con escritura: `zh-Hans`, `zh-Hant`, `sr-Latn` (2 búsquedas: #1 y #2)

**Lo que apareció**
- La página de Google "Localized Versions of your Pages / Tell Google about localized versions of your page" apareció como resultado: https://developers.google.com/search/docs/specialty/international/localized-versions (también la versión antigua https://support.google.com/webmasters/answer/189077). El resumen indica: código de idioma ISO 639-1 + región opcional ISO 3166-1 Alpha 2; `es-419` no se admite; valor insensible a mayúsculas; `x-default` para sin idioma específico. [EVIDENCIA]
- El mismo resumen añadió que "la escritura se deriva automáticamente del país en códigos como `zh-TW`, y también se puede fijar explícitamente con códigos ISO 15924, como `zh-Hant` o `zh-Hans`". **No pude confirmar esta frase en el texto literal**, y no coincide con la descripción que T3 tenía de la doc ("solo ISO 639-1 + 3166-1"). La trato como [EVIDENCIA] de confianza media, no como [HECHO].
- Un tercero independiente (http.dev, https://http.dev/hreflang) afirma que Google acepta pares idioma-escritura y idioma-escritura-región, que `zh-Hans`/`zh-Hant` son alternativas válidas a `zh-CN`/`zh-TW` y que `sr-Latn` es serbio en escritura latina. [EVIDENCIA, tercero]
- Las referencias JATS del NLM (https://jats.nlm.nih.gov/archiving/tag-library/1.4/attribute/hreflang.html) solo documentan que `zh-Hant`, `zh-Hans`, `sr-Latn-RS` son formas válidas del estándar IETF BCP 47. Eso prueba que son códigos válidos en el estándar, **no que Google los interprete**.
- **No encontré ninguna declaración de Google (Mueller u otros) específica sobre `sr-Latn`.** Para `sr-Latn` la confianza es baja.

**Conclusión para T3**
- Cambio: la fila "Chino simplificado/tradicional" de T3 §2 (`zh-Hans/Hant [NO VERIFICADO]`) pasa a: **`zh-Hans`/`zh-Hant` probablemente se aceptan (media); `zh-CN`/`zh-TW` siguen siendo la opción de menor riesgo por estar en la sintaxis documentada con certeza.** [OPINIÓN]
- Para serbio: `sr-Latn` sin evidencia directa de Google. Ofrecer **una sola escritura por URL** (T3 ya lo recomienda) y, si se publica serbio en latino, declarar `sr-Latn` y, a la vez, no depender de que Google lo interprete (la página debe estar claramente en latín). [OPINIÓN]
- Nota: Search Console ya no tiene informe de segmentación internacional (T3 lo documenta), así que no hay validador oficial para probar si Google entiende la escritura. [HECHO según T3]

## 3. Rich results de Google vigentes en 2026 (2 búsquedas: #3 y #4)

| Tipo | Estado a oct-2026 | Evidencia | Etiqueta |
|---|---|---|---|
| **HowTo** | **Eliminado**: dejó de mostrarse en móvil en 2023 (restricción) y en escritorio desde el 13 sep 2023; la doc de datos estructurados se retiró después. | https://developers.google.com/search/blog/2023/08/howto-faq-changes ; https://www.searchenginejournal.com/google-completely-removes-how-to-rich-results/496479/ ; https://www.schemaapp.com/schema-app-news/how-to-rich-results-removed-on-google-search/ | [HECHO] |
| **FAQ** | Desde ago-2023 solo sitios gubernamentales/de salud. Según el changelog de Google (vía resumen), **"ya no aparecerá en Google Search desde el 7 de mayo de 2026"**; soporte en Rich Results Test retirado en jun-2026 y en la API de Search Console en ago-2026. | https://developers.google.com/search/updates ; https://www.seerinteractive.com/insights/google-faq-updates-and-howto-rich-results ; https://www.elementera.com/blog/google-has-removed-faq-rich-results ; https://www.truinc.com/blogs/google-deprecated-faq-rich-results | [EVIDENCIA]. **Contradicción:** otra búsqueda devolvió un tercero que dice que el 7 de mayo de 2026 el rich result "dejó de aparecer en la mayoría de sitios y quedó para gobierno/salud", y no pude confirmarlo en la doc de Google. Un resumen añade que Google seguiría usando `FAQPage` para entender la página (no verificado literalmente). |
| **Product snippets** (reseñas/precio en páginas de producto) | Sin señales de retiro en ninguna lista vista. No vi la página específica en esta pasada. | — | [NO VERIFICADO directamente] |
| **Merchant listings** | **Vigente y mantenido**: el changelog registra el 7 jul 2026 una ampliación de la doc (`Product.category` acepta texto o un valor `CategoryCode`). | https://developers.google.com/search/updates ; https://developers.google.com/search/docs/appearance/structured-data/merchant-listing | [EVIDENCIA] |
| **VideoObject** | **Vigente**: el 24 sep 2026 se añadió la propiedad `creator` y se aclararon los tipos de `interactionStatistic`. | https://developers.google.com/search/updates | [EVIDENCIA] |
| **Breadcrumb** | No apareció en ninguna lista de retiro; no hay cambio 2025–2026 en los resultados. | — | [NO VERIFICADO explícitamente]; ausencia de evidencia de retiro |
| **Organization** | Ídem. | — | [NO VERIFICADO explícitamente] |
| Retiros de la simplificación (anunciada jun-2025): Book Actions, Course Info, Estimated Salary, ClaimReview, Learning Video, Special Announcement, Vehicle Listing | Los 7 están en retirada; en nov-2025 Google dijo que desde enero de 2026 se quitaría su soporte de Search Console y de la API. Ninguno afecta a moldey. | https://developers.google.com/search/blog/2025/11/update-on-our-efforts ; https://www.relevantaudience.com/seo/google-removes-structured-data-2025-guide-for-websites/ ; https://www.engagecoders.com/google-retires-7-structured-data-features-to-streamline-search-results/ | [EVIDENCIA] (la fecha exacta "12 jun 2025" viene de un tercero) |

Otra señal: el título de Search Engine Journal "Google Is Not Diminishing The Use Of Structured Data In 2026" (https://www.searchenginejournal.com/google-is-not-diminishing-the-use-of-structured-data-in-2026/560516/). **Solo vi el título**, no el contenido: [NO VERIFICADO] lo que dice.

**Lectura para moldey.com [OPINIÓN]:** los tipos útiles siguen siendo `Product`/`Offer` (Merchant listings + Product snippets), `Organization`, `BreadcrumbList` y `VideoObject` (si hay tutoriales en vídeo). **No invertir esfuerzo en `FAQPage` ni `HowTo` para obtener rich results.** El contenido de FAQ y pasos conviene mantenerlo visible en la página (sirve a lectores y a respuestas de IA), pero el marcado dejó de ser un objetivo.

## 4. Product/Offer para productos digitales descargables (2 búsquedas: #5 y #6)

**Lo que se pudo establecer**
- No hay, en lo que apareció, **ninguna guía de Google específica para productos digitales** en datos estructurados. [NO VERIFICADO que exista]
- Doc de Merchant listing (https://developers.google.com/search/docs/appearance/structured-data/merchant-listing): según el resumen, `OfferShippingDetails` **no es obligatorio**; solo es necesario completar sus propiedades si se quiere ser elegible para la mejora de "detalles de envío". [EVIDENCIA]
- Doc de política de devoluciones (https://developers.google.com/search/docs/appearance/structured-data/return-policy): `MerchantReturnPolicy` se puede anidar en `Organization` vía `hasMerchantReturnPolicy` para una política general, o en la `Offer`; `returnPolicyCategory` incluye `MerchantReturnNotPermitted` ("no se admiten devoluciones"). [EVIDENCIA]
- ppc.land (https://ppc.land/google-expands-shipping-policy-options-for-online-merchants/) lista que `returnPolicyCountry` pasó a ser obligatorio en `MerchantReturnPolicy` en marzo de 2025; **no verificado** contra el changelog de Google. [NO VERIFICADO]
- Foros de Shopify: la advertencia "Missing field shippingDetails / hasMerchantReturnPolicy" en `offers` es frecuente; un vendedor recomienda definir envíos/devoluciones en Merchant Center y no repetirlas en el marcado; otro hilo dice que son atributos para comercios sin cuenta de Merchant Center. https://community.shopify.com/t/google-tells-me-missing-field-shippingdetails-in-offers/311805 ; https://community.shopify.com/t/google-merchant-return-policy-shipping-details-errors/226126 . [EVIDENCIA débil, anecdótica]
- Un PR de una tienda de software (https://github.com/NhinhoD/LuminaShop/pull/50) usó tarifa de envío 0, tránsito 0 y `MerchantReturnNotPermitted`. Es un ejemplo de implementación, no una referencia. [EVIDENCIA débil]
- Schema.org: el ejemplo de tarifa gratis es `MonetaryAmount` con `value: 0` (https://schema.org/OfferShippingDetails). Un resumen indicó además que `Product.category` se puede enviar como texto o `CategoryCode`.
- Un tercero (Telegram SchemaWire) afirma que la falta de política de devolución se está volviendo "puerta suave" de elegibilidad. **Sin confirmación.** [NO VERIFICADO]

**Qué pide Google como mínimo para merchant listings** (solo lo que los resultados respaldan): `name`, `image`, `offers` con `price`, `priceCurrency` y `availability`; lo demás es recomendado. Dado que el resumen no listó el conjunto exacto de campos obligatorios, **usar el Rich Results Test para confirmar** (que no pude correr).

**Qué hacer en el marcado de moldey.com [OPINIÓN, coherente con la evidencia]**
1. `Product` + `Offer` con `price`, `priceCurrency`, `availability: InStock`, `url`, `image`; el precio y la moneda deben coincidir con lo visible.
2. Devoluciones: declarar `hasMerchantReturnPolicy` **solo si coincide con la política real y visible** (`MerchantReturnNotPermitted` si no hay reembolsos; otra categoría si los hay). No inventar una política para quitar una advertencia. Anidarla una sola vez en `Organization` evita repetirla en cada producto.
3. `shippingDetails`: aceptar la advertencia "recomendado" o declarar tarifa 0 y plazo 0 (como hace el ejemplo del PR). Ninguna opción está respaldada como "la correcta" por Google en lo visto.
4. Describir en la página que es un **producto digital** (formatos A4/Letter/A0/DXF, entrega inmediata por descarga).

## 5. Google Merchant Center / Shopping para productos digitales (2 búsquedas: #7 y #8)

**Confirmado (fuente oficial vista, 2 búsquedas coinciden)**
- "Unsupported Shopping content" (https://support.google.com/merchants/answer/6150006): **eBooks y libros digitales (PDF, ePub, MOBI; sin audiolibros) no se admiten en anuncios de Shopping.** Página de arreglo: https://support.google.com/merchants/answer/14183113 ("Digital books can't be featured in ads": quitar la oferta del feed si infringe). [HECHO]
- A nivel de cuenta existe el problema crítico **"EBooks"/`prohibited_content_ebooks`** dentro de contenido prohibido (listado en https://developers.google.com/shopping-content/guides/account-issues). Es decir, no solo se rechaza el producto: puede haber **suspensión crítica de la cuenta**. [EVIDENCIA, resumen de la guía de problemas de cuenta]
- Contenido digital vendido con suscripciones recurrentes: no admitido; suscripciones de software prepagadas con renovación solo anual: admitidas. [EVIDENCIA, resumen de 6150006]
- Para el checkout vía UCP, los bienes que requieren instalar software antes de comprar no son elegibles (https://developers.google.com/merchant/ucp/guides/merchant-center). [EVIDENCIA]
- Otras páginas de política que aparecieron (no leídas en detalle): "Unsupported free listings content" https://support.google.com/merchants/answer/12077589 ; "Shopping ads and listings policies" https://support.google.com/merchants/answer/6149970 ; "Misrepresentation" https://support.google.com/merchants/answer/6150127 ; "Copyrighted content" https://support.google.com/merchants/answer/6150163. **No sé si "eBooks" también está excluido de los listados gratuitos**; el resumen no lo dijo. [NO VERIFICADO]

**Lo que NO apareció**
- Ninguna página oficial vista nombra **plantillas, printables, PDFs o patrones de costura** como prohibidos ni como admitidos. [NO VERIFICADO]
- No se reconfirmó en esta pasada que Google pida envío "0" para intangibles (T2 §3.2 lo tenía de 3 páginas, https://support.google.com/merchants/answer/7169130 entre ellas). El resumen de la búsqueda #8 dijo que no cubrió ese punto. El hallazgo de T2 queda tal cual: [HECHO, según resumen de T2].
- Atributo oficial "digital": sigue sin aparecer. **Trampa de nombre:** el atributo `pattern` de Merchant Center (https://support.google.com/merchants/answer/6324483) es el *estampado* de la prenda (rayas, lunares), **no** "patrón de costura". No usarlo para marcar moldes.

**Terceros y foros (contradictorios) [EVIDENCIA débil]**
- gmcunbanned.com (https://gmcunbanned.com/blog/google-merchant-center-digital-products/) lista eBooks/PDF y arte/printables como permitidos si la imagen muestra claramente el producto. **Contradice la política oficial sobre eBooks**; descontar.
- Foros: "en general todos los productos digitales serán rechazados" (https://community.shopify.com/t/digital-products-on-google-shopping/415596) ; vendedor de plantillas Canva aprobado y luego suspendido por *Misrepresentation* tras una impresión (https://community.shopify.com/t/merchant-products-were-approved-until-first-impression-on-google-ads-then-got-misrepresentation/419106) ; BlackHatWorld (https://www.blackhatworld.com/seo/anyone-getting-digital-products-approved-in-google-merchant-center.1770804/). Convergen en que es una zona de alto riesgo, pero son anécdotas.
- Cómo configurar descargas digitales en Merchant: https://community.shopify.com/t/how-to-setup-digital-downloads-for-google-merchant/311099 (no leído).

**Lectura para moldey.com [OPINIÓN]:** un PDF de patrón de costura no es literalmente un "libro digital", pero la política de eBooks incluye PDF y un revisor puede equipararlo, y la suspensión crítica de cuenta es un riesgo asimétrico. T2 §10 ya recomendaba no conectar una cuenta de Google Ads valiosa; **esta pasada lo refuerza**. Si se prueba, hacerlo con una cuenta separada, pocos productos y sin gasto publicitario, y leer el motivo exacto de cada rechazo.

## 6. hreflang en Baidu y Naver (1 búsqueda: #9)

- **Ninguna fuente oficial de Baidu ni de Naver apareció.** Todo es de terceros. [EVIDENCIA, tercero]
- **Baidu no usa hreflang**; usa señales propias, sobre todo la meta de idioma (`Content-Language`), ubicación del alojamiento, dominio y licencia ICP. Fuentes: https://martinkura.com/baidu-international-websites-hreflang-geographic-target-meta-language-tag/ ; https://www.chinafy.com/blog/how-to-create-a-multilingual-website-that-ranks-on-baidu ; https://www.dragonmetrics.com/technical-on-page-seo-guide-baidu/ ; https://www.baiduadvertising.com/how-to-optimize-your-multilingual-website-for-baidu-success/ (esta última no se resumió: no sé qué dice de hreflang). Esto **corrobora** el comentario de T3 §2 (tabla de motores; "Baidu y Bing se apoyan en `Content-Language`").
- **Naver:** una tabla comparativa lista "No; usar la meta de idioma HTML", y otra guía dice que Naver, Yahoo!, Bing y Baidu "siguen usando sus propias señales". Naver Search Advisor no apareció. [EVIDENCIA débil]. Controversia: T3 citaba a Linguise recomendando hreflang para Naver; sin doc oficial no se puede resolver.
- Conclusión: mantener hreflang (sirve para Google/Yandex) pero **añadir `<html lang>` correcto y `Content-Language`** en cada versión; no esperar efecto de hreflang en Baidu/Naver. La decisión de T3 de aplazar China/Corea queda intacta. [OPINIÓN]

## 7. IndexNow (1 búsqueda: #10)

| Pregunta | Respuesta | Confianza |
|---|---|---|
| ¿Google lo soporta? | **No**, a 2026. Google no lo adoptó para indexación web; para Google, usar sitemaps con `lastmod` fiable, enlaces internos y la herramienta de inspección de URL. (Un tercero dice que Google "lo probó" tras el lanzamiento de 2021 y no lo adoptó; la fecha del test difiere entre fuentes.) | alta; **todas las fuentes son terceros**, ninguna oficial |
| ¿Quién sí? | Bing, Yandex, Naver, Seznam.cz y Yep, según una guía. Otras añaden Amazon (búsqueda de productos) e Internet Archive; una fuente omite a Yep. **Discrepancia de listas.** | media |

Fuentes: https://pressonify.ai/blog/indexnow-instant-indexing-press-releases-2026 ; https://www.indexernow.com/google-indexnow ; https://www.indexbolt.com/glossary/indexnow ; https://upgrowth.in/indexnow-from-push-to-pull-say-bing-and-yandex/ ; https://en.wikipedia.org/wiki/IndexNow . No se vio `indexnow.org`. Los límites de IndexNow y de la API de envío de Bing **no se verificaron** (queda pendiente de T3 §14).

**Lectura [OPINIÓN]:** IndexNow cuesta poco (un plugin o un POST al publicar) y cubre Bing (que alimenta a varios motores y asistentes) más Yandex, Naver y Seznam. No sustituye el trabajo de Google.

## 8. Pinterest: catálogos y Product Pins para digitales (1 búsqueda: #11) — **NO RESUELTO**

- Guía oficial de catálogos: https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs ; directrices para comerciantes: https://policy.pinterest.com/en/merchant-guidelines . El resumen de las directrices decía que los productos deben cumplir las normas de la comunidad y términos, y que Pinterest "no participa en la compra, venta o entrega". Llegó truncado; **no se vio ninguna mención a bienes digitales/descargables**. [NO VERIFICADO]
- Los terceros (https://84pins.com/sell-digital-products-on-pinterest/ , https://www.bloggerteck.com/selling-digital-products-on-pinterest-a-beginners-guide/ , https://www.digital.dashleigh.com/selling-digital-goods-articles-blog/pinterest-marketing-for-digital-products-in-2023) describen la práctica de crear pines con enlace a Etsy, Gumroad, Shopify o el propio sitio, **no** el uso de catálogos. [EVIDENCIA débil]
- Requisitos de catálogo según terceros: cuenta de empresa, sitio web reclamado y el sitio debe vender realmente lo del catálogo, con datos que coincidan. [EVIDENCIA débil]
- **Para moldey.com [OPINIÓN]:** la vía de menor riesgo es **pines normales con enlace a la página del producto** (sin catálogo) y sitio web reclamado; catálogo solo tras leer el texto completo de las directrices.

## 9. Límites de sitemap de Google y Core Web Vitals por país (1 búsqueda: #12)

**Sitemaps [HECHO, 2 páginas oficiales vistas más la ayuda de Search Console]**
- Un sitemap: **máx. 50 MB sin comprimir o 50.000 URLs**; si se supera, partir en varios. Un índice de sitemaps puede tener hasta **50.000** entradas `<loc>`; más de 50.000 sitemaps en un índice es error en Search Console. Fuentes: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap ; https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps ; https://support.google.com/webmasters/answer/7451001 . La guía antigua de 2014 hablaba de 10 MB (superado): https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom .
- **Consecuencia para 100 idiomas [cálculo propio, OPINIÓN]:** si se declara hreflang en el sitemap, cada `<url>` lleva una línea `xhtml:link` por idioma (incluida ella misma). A ~110–120 bytes por línea, 100 idiomas son ~11–12 KB por URL, así que el límite de **50 MB se alcanza hacia las 3.000–5.000 URLs por archivo**, mucho antes que el de 50.000. Planificar sitemaps por sección/idioma o por lotes y un índice. Con pocos idiomas por etapa (T3 §12 plantea oleadas) no es problema hasta más adelante.

**Core Web Vitals por país / CrUX [NO VERIFICADO]**
- La búsqueda #12 no alcanzó la parte de CrUX ("no miré el esquema de BigQuery de CrUX"). **Sin evidencia de esta sesión.** Conocimiento previo del agente, no comprobado hoy: el conjunto de datos CrUX en BigQuery tiene desglose por país, la API pública consulta por origen/URL y tipo de dispositivo y no por país, y el informe de CWV de Search Console no se desglosa por país. Hasta confirmarlo con la documentación de CrUX, tratar esto como hipótesis.

## 10. Qué hacer en moldey.com (priorizado)

| # | Acción | Impacto | Esfuerzo | Base |
|---|---|---|---|---|
| 1 | Marcado `Product`/`Offer` completo + `Organization` + `BreadcrumbList`; devoluciones coherentes con la política visible. Validar con Rich Results Test. | Alto | Bajo | §3, §4 |
| 2 | Mantener `zh-CN`/`zh-TW` como valores por defecto; `zh-Hans`/`zh-Hant` solo como segunda opción tras ver más evidencia. Una sola escritura por URL. | Medio | Bajo | §2 |
| 3 | No conectar una cuenta de Google Ads/Merchant valiosa a productos digitales; si se prueba, cuenta separada y sin gasto. | Alto (evita riesgo) | Bajo | §5 |
| 4 | `<html lang>` + `Content-Language` correctos en todas las versiones (para Bing, Baidu, Naver). | Medio | Bajo | §6 |
| 5 | IndexNow al publicar (Bing, Yandex, Naver, Seznam); Google por sitemap con `lastmod` fiable. | Medio | Bajo | §7 |
| 6 | Pines con enlace directo y sitio reclamado en Pinterest antes que catálogo. | Medio | Bajo | §8 |
| 7 | Sitemaps partidos por lotes/idioma + índice; calcular el peso con hreflang. | Medio (al escalar) | Medio | §9 |
| 8 | Dejar `FAQPage`/`HowTo` como contenido visible; no priorizar su marcado. | Bajo | Bajo | §3 |

## 11. Qué NO hacer

1. No afirmar internamente que Google acepta `sr-Latn` ni que "Google no soporta escritura en hreflang": ninguna de las dos cosas está comprobada en el texto literal.
2. No planificar rich results de FAQ/HowTo.
3. No usar el atributo `pattern` de Merchant Center para "patrón de costura".
4. No fiarse de blogs (gmcunbanned) que dicen que "PDF/printables están permitidos" cuando la política oficial excluye eBooks/PDF de libros.
5. No invertir en hreflang para Baidu/Naver; no cambiar la decisión de aplazar China/Corea.
6. No declarar una política de devoluciones en el JSON-LD distinta de la visible.

## 12. Siguen sin verificar tras esta pasada

- Texto literal de la doc de Google sobre escrituras (ISO 15924) en hreflang y cualquier mención a `sr-Latn`.
- Estado explícito de Breadcrumb, Organization y Product snippets en 2026 (solo ausencia de señales de retiro); confirmación literal de la fecha del 7 de mayo de 2026 para FAQ.
- Si "plantillas/printables/PDF de patrones" están admitidos en Shopping ads o en listados gratuitos; si "eBooks" también se excluye en listados gratuitos.
- Política de Pinterest para bienes digitales en catálogos.
- Documentación oficial de Baidu y Naver sobre hreflang; páginas oficiales de IndexNow (`indexnow.org`) y sus límites; límites de la API de envío de Bing.
- CrUX/Core Web Vitals por país.

## 13. Registro de búsquedas (12/12)

| # | Tema | Modo |
|---|---|---|
| 1 | hreflang `zh-Hans`/`zh-Hant`/`sr-Latn` | standard |
| 2 | Doc de Google de hreflang (dominios Google/SEJ/SER) | standard |
| 3 | Rich results retirados 2025–2026 | extended |
| 4 | Changelog de datos estructurados 2026 | extended |
| 5 | Merchant listing y digitales (envío/devoluciones) | standard |
| 6 | Offer digital, `MerchantReturnNotPermitted` | extended |
| 7 | Merchant Center, digitales/printables/patrones | extended |
| 8 | "Unsupported Shopping content" (dominios Google) | standard |
| 9 | Baidu/Naver hreflang (con términos en chino y coreano) | extended |
| 10 | IndexNow y Google | extended |
| 11 | Pinterest catálogos y digitales | extended |
| 12 | Límites de sitemap (+ CrUX; solo respondió sitemaps) | standard |
