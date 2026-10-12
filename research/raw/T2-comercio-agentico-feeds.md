# T2 — Comercio con IA ("agentic commerce"), feeds de producto y compras en buscadores (2025–2026), aplicado a moldey.com

Fecha del informe: 12 de octubre de 2026. Tienda objetivo: productos digitales descargables (moldes de costura en PDF/DXF), multi-idioma, vendedor en Argentina.

## 0. Aviso de cobertura y de método (leer primero)

- **El presupuesto de búsquedas web de la sesión se agotó** tras unas 17 consultas útiles (límite compartido entre agentes). WebFetch tampoco funciona (DNS). Por eso:
  - Los puntos **1 (OpenAI)** y **2 (Google: Merchant Center, UCP, política de contenido digital)** tienen evidencia de esta sesión.
  - Los puntos **3 (Copilot, Perplexity, Amazon, Meta, Pinterest, TikTok), 4 (protocolos, solo en parte), 5 (feeds multi-país, GTIN, categorías), 6 (marketplaces) y los datos estructurados (Product/Offer/MerchantReturnPolicy, rich results vivos)** **no pudieron buscarse**. Esas secciones se redactaron con conocimiento previo del modelo y están marcadas **[NO VERIFICADO]**. No llevan URL porque no las vi en resultados. Deben tratarse como hipótesis de trabajo hasta una segunda pasada.
- **Leyenda de fiabilidad.** [HECHO] = documentado por la plataforma. [EVIDENCIA] = datos o prensa de terceros con fuente identificable. [OPINIÓN] = consejo de la industria. [NO VERIFICADO] = sin respaldo suficiente en esta sesión.
  - Nota de método: los resultados del buscador son **resúmenes automáticos** de las páginas. Cuando marco [HECHO] una afirmación sobre una página oficial (Google, OpenAI), significa que el resumen la atribuye a esa página, pero **no pude abrir la página original**. Verificar el texto vigente antes de decidir.

---

## 1. Resumen ejecutivo

1. **El checkout dentro del chat está en retirada, no en auge.** OpenAI lanzó Instant Checkout en septiembre de 2025 (primero vendedores de Etsy en EE. UU.; Shopify "en camino"). En marzo de 2026 reportes de The Information, CNBC y otros dijeron que lo recortó tras muy poca adopción (cifras de "unas pocas decenas" de comercios, no confirmadas por OpenAI) y que pasa a descubrimiento de producto + compra en el sitio o app del comerciante. [EVIDENCIA]
2. **Lo que sí está vivo y es útil para una tienda chica es el feed de producto para descubrimiento.** OpenAI dice que "la mayoría de los comercios empiezan con feeds" y que la compra se completa en el sitio del comerciante. [HECHO, según resumen de chatgpt.com/merchants] En junio de 2026 la gestión de feeds pasó al ChatGPT Ads Manager. [EVIDENCIA, fuentes secundarias]
3. **Los productos digitales son una zona gris o restringida en casi todos los canales de compras.** Google excluye los eBooks de los anuncios de Shopping desde 2021 [HECHO]; las cuentas de Merchant Center con descargas digitales sufren rechazos frecuentes según foros [EVIDENCIA débil]. El feed de OpenAI "acepta pero ignora" `is_digital` [HECHO] y su política comercial restringe ciertos bienes digitales, con redacción contradictoria entre versiones [NO VERIFICADO, ver 2.4].
4. **Google UCP existe (enero 2026) pero su checkout en AI Mode/Gemini solo aplica a EE. UU., Canadá y Australia y a comercios seleccionados**, con atributo `native_commerce` en el feed de Merchant Center. [HECHO, según resumen de la ayuda de Google]. No es accionable para moldey.com hoy.
5. **La preparación realista es barata y sirve a todo:** un catálogo limpio y estructurado (un solo origen de verdad), schema `Product`/`Offer` correcto, precios por moneda, políticas de entrega y reembolso visibles, y la capacidad de exportar un feed. Todo lo demás (ACP, UCP, AP2, MCP, NLWeb) es **opcional o prematuro** para una tienda de este tamaño. [OPINIÓN fundamentada en lo anterior]

---

## 2. OpenAI: ChatGPT Shopping, Instant Checkout y Agentic Commerce Protocol

### 2.1 Cronología
| Fecha | Hecho | Fiabilidad | Fuente |
|---|---|---|---|
| Sep 2025 | Lanzamiento de Instant Checkout y ACP (OpenAI + Stripe). Compras de un solo artículo, EE. UU., Etsy primero, Shopify después. | [EVIDENCIA] | https://alternativeto.net/news/2025/9/chatgpt-launches-instant-checkout-with-in-chat-purchases-and-merchant-integration ; https://www.searchengineworld.com/openai-introduces-instant-checkout-in-chatgpt-to-buy-in-chat |
| 3 Oct 2025 | Agregadores de feeds (Channable) ya ofrecen feed "ChatGPT Commerce". | [EVIDENCIA] | https://helpcenter.channable.com/changelog/october-2025/october-3-2025-new-feed-open-ais-chatgpt-commerce |
| 5 Mar 2026 | The Information: OpenAI recorta el checkout en el chat. Las compras irían a apps de minoristas (Instacart, Target, Expedia). | [EVIDENCIA] | https://www.theinformation.com/articles/openai-scales-back-shopping-plans-chatgpt ; https://www.storyboard18.com/digital/openai-reduces-chatgpt-shopping-focus-shifts-to-product-discovery-93192.html |
| 20 y 24 Mar 2026 | CNBC: el primer intento "tropezó"; OpenAI rediseña la experiencia de compras. | [EVIDENCIA] | https://www.cnbc.com/2026/03/20/open-ai-agentic-shopping-etsy-shopify-walmart-amazon.html ; https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html |
| Mar 2026 | Análisis: "qué salió mal", "el líder del comercio agéntico retrocede". | [OPINIÓN/EVIDENCIA] | https://www.modernretail.co/technology/what-went-wrong-with-chatgpts-instant-checkout/ ; https://www.forrester.com/blogs/what-it-means-that-the-leader-in-agentic-commerce-just-pulled-back |
| Jun 2026 | La gestión de feeds de producto migra al ChatGPT Ads Manager (anuncios autogenerados desde catálogo). Base: un solo hallazgo en LinkedIn replicado por blogs. | [NO VERIFICADO] (fuentes secundarias coinciden entre sí) | https://ppc.land/chatgpt-ads-manager-now-supports-product-feeds-after-checkout-is-killed/ ; https://stellagent.ai/insights/chatgpt-ads-product-feeds-checkout ; https://novadata.io/resources/news/chatgpt-ads-manager-product-feeds-june-2026 |
| 6 Jun 2026 | Anuncios de ChatGPT llegan al Reino Unido (según un blog). | [NO VERIFICADO] | Blog de terceros cuya URL exacta no pude identificar en los resultados (fuente única); no usar como dato firme |
| Ago–Sep 2026 | Expansión de ChatGPT Ads a Europa, India, MENA. **Las fechas se contradicen:** 24 ago (Lengow, 31 mercados europeos), 31 ago (Dataïads, auto-servicio), 4 sep (Common Thread Co., +30 países). | [NO VERIFICADO] | https://www.lengow.com/es/integrations/chatgpt ; https://www.dataiads.io/en/blog/chatgpt-ads-manager-europe-flux-produit ; https://commonthreadco.com/blogs/coachs-corner/chatgpt-ads-september-2026-product-feeds-now-required-platform-expands-globally-and-the-new-tools-ecommerce-brands-need-right-now |

**Estado actual (oct 2026):** Instant Checkout como producto independiente está desprioritizado. OpenAI dijo que "no ofrecía la flexibilidad" necesaria. Quedan: (a) feeds para descubrimiento, (b) apps de comercios grandes, (c) ACP como protocolo abierto. Algunas fuentes afirman que el checkout "sigue para algunos comercios" y otras que "está muerto"; **es controvertido** y no hay página oficial leída que lo zanje. https://www.digitalsilk.com/digital-trends/digital-trends-chatgpt-ecommerce/ ; https://stellagent.ai/insights/openai-shopping-agent-strategy-pivot

### 2.2 Cómo se envía el feed y qué exige
- **Alta:** los comercios se postulan en https://chatgpt.com/merchants ("Power product discovery in ChatGPT"). Una fuente dice que OpenAI revisa solicitudes de forma continua y otra (Lengow, ES) que **OpenAI no publicó criterios de elegibilidad ni calendario por mercado**. [NO VERIFICADO / contradictorio]
- **Especificación:** hay una referencia oficial "Feed Reference / Product Feed Spec": https://developers.openai.com/commerce/specs/file-upload/products ; https://developers.openai.com/commerce/product-feeds/spec ; https://developers.openai.com/commerce/specs/spec . Versión estable citada por un tercero: 2026-01-30 (no verificado contra el changelog oficial).
- **Campos mínimos** (según guías de terceros): ID, título, descripción, precio, disponibilidad, URL, imagen; más datos del vendedor (`seller_name`, `seller_url`). IDs de producto/variante deben ser estables. [EVIDENCIA, fuentes secundarias: https://www.paz.ai/glossary/chatgpt-product-feed-format ; https://www.anglera.com/glossary/openai-product-feed]
- **Banderas de elegibilidad:** `is_eligible_search` y `is_eligible_checkout` (Forrester las nombra `enable_search`/`enable_checkout`; probable cambio de nombre entre versiones). Controlan si el producto es descubrible/comprable en ChatGPT sin alterar la web propia. [HECHO parcial: https://developers.openai.com/commerce/specs/file-upload/products ; https://www.forrester.com/blogs/a-holiday-season-gift-wrapped-in-agentic-commerce]
- **Formatos:** **las fuentes discrepan** (JSONL/CSV/TSV/Parquet según Alhena y Paz; CSV/TSV/XML/JSON según Lengow y Forrester). Verificar en la spec. Frecuencia: hasta cada 15 minutos (Lengow). Entrega: SFTP según Alhena/Vercel (modelo previo) vs. Ads Manager desde junio de 2026. https://alhena.ai/blog/chatgpt-shopping-product-feed-guide/
- **Compatibilidad con Google:** OpenAI "acepta el formato de feed de Google Shopping" (Paz.ai) y la spec tiene una tabla de campos "compatibles con Google". Las columnas desconocidas se descartan. [EVIDENCIA] https://www.paz.ai/blog/chatgpt-ads-manager-one-feed-two-jobs
- **Límites en Ads Manager:** hasta 1 millón de SKU por anunciante; muestra de 100 productos antes de conectar el catálogo completo (Nova Data). [NO VERIFICADO]
- **Plataformas:** Shopify Catalog envía productos elegibles a ChatGPT para compradores de EE. UU. (Vercel, secundaria). Existen conectores de Lengow, Channable, Feedoptimise, commercetools, PrestaShop (Webkul/PrestaShow) y guías para WooCommerce. https://www.feedoptimise.com/blog/list-your-products-in-openai-chatgpt-using-product-feed ; https://docs.commercetools.com/agentic-commerce/ai-hub/openai/overview ; https://webkul.com/blog/prestashop-agentic-commerce-with-chatgpt/amp/ . No encontré evidencia de un conector oficial para Etsy digital ni WooCommerce nativo.
- **Cuidado con una afirmación de marketing:** un analista dijo el 4 sep 2026 que "solo las marcas que envían feed a OpenAI aparecen en ubicaciones de compras de ChatGPT". SERoundtable solo lo sospecha. **No confirmado.** https://www.seroundtable.com/openai-chatgpt-ads-updates-42017.html

### 2.3 Países
- Registro de comercios: originalmente solo EE. UU.; compradores solo en EE. UU. (guías de 2025). Estado 2026 incierto y con fuentes contradictorias (ver cronología). **No hay prueba de que un comercio argentino pueda registrarse hoy.** [NO VERIFICADO]
- Contraste: los anuncios sí se expandieron a Europa/India/MENA en ago–sep 2026 (fechas discrepantes), lo que sugiere que el canal de pago crece más rápido que el orgánico.

### 2.4 ¿Admite productos digitales? (el punto crítico)
| Evidencia | Qué dice | Fiabilidad |
|---|---|---|
| Spec oficial de feed (tabla de campos "Google-compatible") | `is_digital` figura como "Accepted, but not used". | [HECHO parcial] https://developers.openai.com/commerce/specs/file-upload/products |
| Guía Alhena (tercero) | Vendedores de ebooks/cursos/plantillas/software deben marcar soporte digital en el onboarding; campo en blanco no cuenta como digital. | [OPINIÓN] — **contradice** a la spec |
| Política comercial de OpenAI | Prohíbe piratería; lista como "no soportados" los **derechos digitales de alto riesgo** (moneda de juego, recursos de cuenta, boosts, top-ups) con excepción de **software convencional, licencias y videojuegos completos**. | [HECHO, según resumen de https://openai.com/policies/commerce-policies/] |
| Una consulta devolvió dos versiones con fechas distintas: **17 jun 2026** (lista como no soportados: membresías, suscripciones, **archivos descargables, plantillas, gráficos, kits promocionales, ebooks independientes**) y **24 jun 2026** (recortada a derechos digitales de alto riesgo, sin nombrar plantillas/ebooks). Otra consulta posterior **no pudo reproducir** el texto de "ebooks". | **[NO VERIFICADO — contradictorio]**; no sé qué versión rige ni en qué región. |
| Apps SDK: "las apps solo pueden hacer comercio de bienes físicos" | Excluye bienes digitales, suscripciones, contenido digital, tokens o créditos. Aplica a **apps**, no a feeds. Fuentes de ~300 días de antigüedad. | [HECHO/antiguo] https://developers.openai.com/apps-sdk/app-submission-guidelines ; https://community.openai.com/t/was-anybody-working-on-a-services-app/1370150 |
| Términos de feed | El comerciante responde por cumplir las políticas de productos prohibidos; OpenAI puede retirar contenido a su discreción. | [HECHO] https://openai.com/policies/merchant-feed-terms-of-service/ |

**Conclusión práctica:** archivos descargables y plantillas son **riesgo alto de exclusión** en el canal de feeds de ChatGPT. Mejor leer la política vigente directamente antes de invertir tiempo. Ningún resultado afirmó que patrones de costura digitales estén soportados.

### 2.5 Costos y ACP
- ACP es de código abierto (Apache 2.0), gobernado por OpenAI y Stripe. Los "cinco endpoints" vs "cuatro endpoints" de la Checkout API discrepan entre guías. Un snapshot estable del 17 abr 2026 habría añadido carrito/feed/pedido/autenticación (fuente sin identificar claramente: [NO VERIFICADO]). https://developers.openai.com/commerce/guides/key-concepts ; https://opascope.com/insights/ai-shopping-assistant-guide-2026-agentic-commerce-protocols/
- "4 % de comisión por compra en Instant Checkout": solo fuentes secundarias. [NO VERIFICADO]. Irrelevante hoy salvo que el checkout vuelva.
- Implementar ACP exige API de checkout propia + tokens de pago delegados (las guías hablan de "delegated payment tokens"; el nombre de producto de Stripe es [NO VERIFICADO]). Para una tienda chica en Shopify/Etsy lo haría la plataforma, no el comerciante.

---

## 3. Google: Merchant Center, listados gratuitos, AI Mode, UCP y bienes digitales

### 3.1 Universal Commerce Protocol (UCP) — sí existe
- Estándar abierto anunciado en **enero de 2026**, compatible con A2A, AP2 y MCP. [HECHO, según resumen de https://support.google.com/merchants/answer/16837055 ; https://developers.google.com/merchant/ucp ; https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/]
- **Checkout agéntico en AI Mode y Gemini:** botón "Comprar" en fichas elegibles cuando el comerciante integró UCP y añadió el atributo **`native_commerce`** al feed de Merchant Center; paga con Google Pay (datos de Google Wallet). El comerciante sigue siendo **Merchant of Record** y gestiona cumplimiento y cliente. PayPal está "planeado". [HECHO]
- **Países:** productos con elegibilidad en **EE. UU., Canadá y Australia**, solo comercios participantes. [HECHO, según resumen de la ayuda]
- Co-desarrolladores citados: Shopify, Etsy, Wayfair, Target, Walmart. [EVIDENCIA] https://www.fonearena.com/blog/473307/google-agentic-commerce-ucp-ai-agents-native-checkout.html ; https://www.channelengine.com/en/blog/google-universal-commerce-protocol-merchant-center-ai-shopping
- Las fechas de funciones adicionales (carrito, YouTube) varían entre guías y no pude confirmarlas. https://www.bigcommerce.com/articles/ecommerce/google-agentic-checkout/ ; https://launchcodex.com/blog/web-digital-infrastructure/universal-commerce-protocol-merchant-guide/
- **Lectura para moldey.com:** inaccesible hoy (Argentina fuera de los tres países de checkout; sin evidencia de que se admitan bienes digitales).

### 3.2 Política de Google para productos digitales
| Punto | Qué dice | Fiabilidad |
|---|---|---|
| eBooks y libros digitales (PDF, ePub, MOBI; sin audiolibros) | **No admitidos en anuncios de Shopping ni anuncios de inventario local.** Se aplicó globalmente desde el **18 may 2021**. | [HECHO] https://support.google.com/merchants/answer/6150006 ; fix: https://support.google.com/merchants/answer/14183113 ; resumen: https://feedarmy.com/kb/digital-books-ebooks-for-shopping-ads-disapproved-in-google-merchant-center/ |
| Alcance de la limitación | La política dice que es específica de Shopping ads; los listados gratuitos orgánicos "no se vieron afectados" según cobertura de terceros | [EVIDENCIA, de segunda mano] |
| Productos intangibles (software, contenido digital, suscripciones) | Google indica enviar **costo de envío "0"** cuando el país exige costo de envío. Sin costo de envío, el producto no se muestra. | [HECHO, según resumen] https://support.google.com/merchants/answer/7169130 ; https://support.google.com/merchants/answer/6324484 ; https://support.google.com/merchants/answer/12157544 |
| Existencia de atributo `digital` | **No encontré ningún atributo oficial "digital"** en lo revisado. Una web de terceros habla de una regla de "digital delivery" que no está en la documentación de Google. | [NO VERIFICADO] https://gmcunbanned.com/blog/google-merchant-center-digital-products/ |
| Descargas digitales en general (moldes PDF, plantillas, printables) | **Ninguna página oficial encontrada** que las permita o las prohíba por nombre. Foros (Shopify Community, BlackHatWorld) reportan rechazos y suspensiones por "Misrepresentation"; aprobaciones raras (p. ej. software de Microsoft). Un blog de terceros especializado en Merchant Center (gmcunbanned.com) afirma que "descargas y printables están permitidos", **contradiciendo** foros y política de eBooks. | [EVIDENCIA débil/anecdótica] https://community.shopify.com/t/digital-products-on-google-shopping/415596 ; https://community.shopify.com/t/google-shopping-for-digital-products/396226 ; https://community.shopify.com/t/google-merchant-center-misrepresentation/388992 |
| Riesgo de cuenta | Foros advierten que una suspensión de Merchant Center puede arrastrar a la cuenta de Google Ads. | [EVIDENCIA anecdótica] |
| Suscripciones | Google habría actualizado en oct 2025 qué categorías pueden anunciar suscripciones (fuente: podcast de un tercero). | [NO VERIFICADO] https://alanawu.podbean.com/e/does-google-shopping-allow-subscriptions-policy-updated-october-2025 |
| Políticas de listados gratuitos | Cuatro áreas: contenido prohibido, prácticas prohibidas, contenido restringido, requisitos del sitio. | [HECHO] https://support.google.com/merchants/answer/12073010 |

**Zona gris relevante:** un molde PDF de costura no es "un libro", pero comparte formato (PDF) y es un archivo descargable. Google podría tratarlo como eBook o como producto "no entregable físicamente". **No hay respaldo para afirmar que sea aceptado ni rechazado.** [NO VERIFICADO]

### 3.3 Datos estructurados y rich results (sin búsquedas; conocimiento previo)
Todo lo de esta subsección es **[NO VERIFICADO en esta sesión]**; verificar en la documentación de Google Search Central.
- `Product` + `Offer` (con `price`, `priceCurrency`, `availability`, `url`) es el patrón estándar. Para bienes digitales no existe una propiedad "es digital" en la guía de merchant listings; conviene usar `Offer.availability = InStock`, `itemCondition` omitido o `NewCondition`, y describir "descarga instantánea" en la descripción. `OfferShippingDetails` es opcional; si se incluye, se suele expresar envío gratis con valor 0. `MerchantReturnPolicy` con `returnPolicyCategory` "MerchantReturnNotPermitted" (si no hay devolución por ser digital) o la política real de reembolso, **siempre coherente con la página visible**.
- Depuraciones: de memoria, Google restringió FAQ (ago 2023) y retiró HowTo (sept 2023), y en 2025 anunció la retirada gradual de varios tipos de resultados enriquecidos poco usados. **No verifiqué la lista vigente en oct 2026.** `Product`, `Organization`, `Breadcrumb`, `Review snippet`, `Video` y `Article` siguen siendo los tipos centrales. FAQ/HowTo ya no dan rich result visible pero el marcado puede seguir sirviendo a otros consumidores (IA, Bing) [OPINIÓN].

---

## 4. Otros canales: Copilot, Perplexity, Amazon, Meta, Pinterest, TikTok

**No se pudo buscar en esta sesión.** Lo siguiente es conocimiento previo [NO VERIFICADO] y debe revisarse en una segunda pasada:
| Canal | Hipótesis a verificar |
|---|---|
| Microsoft (Merchant Program / Copilot Checkout / Bing Shopping) | Usa un feed tipo Merchant Center; el Merchant Center de Microsoft acepta importar desde Google. Política de bienes digitales y regiones sin verificar. |
| Perplexity Shopping / PayPal | Programa de comerciantes con feeds y PayPal para checkout, orientado a EE. UU. y bienes físicos. Sin verificar. |
| Amazon | Venta de patrones digitales vía Amazon es limitada (KDP/“Merch” no son para PDFs de molde); sin verificar. |
| Meta (Shops/Catálogos) | Históricamente, las tiendas de Facebook/Instagram son para bienes físicos; bienes digitales restringidos. Sin verificar. |
| Pinterest | Catálogos y Product Pins: tradicionalmente aceptan enlace al producto; política de digitales sin verificar. Pinterest es un canal fuerte de descubrimiento para costura/DIY **sin necesidad de feed** (pines con enlace). [OPINIÓN] |
| TikTok Shop | Mayoritariamente bienes físicos y por región; digitales no soportados en la mayoría de regiones (hipótesis). |

---

## 5. Protocolos para agentes: qué es real y qué es hype

Salvo lo marcado, [NO VERIFICADO en esta sesión] (conocimiento previo).
| Protocolo | Estado probable | Veredicto para una tienda chica |
|---|---|---|
| **ACP** (OpenAI + Stripe) | Real, abierto; su producto estrella (Instant Checkout) fue recortado en 2026 [EVIDENCIA]. | Esperar; lo implementa la plataforma. |
| **UCP** (Google) | Real, lanzado en ene 2026, solo US/CA/AU y comercios seleccionados [HECHO]. | Seguir; no accionable desde Argentina. |
| **MCP** (Anthropic, nov 2024) | Real y muy adoptado como estándar de herramientas para agentes. Google dice que UCP es compatible con MCP, A2A y AP2 [HECHO]. | Útil si querés exponer catálogo/búsqueda a agentes; prioridad baja. |
| **A2A** (Google, 2025) | Real pero de uso nicho entre agentes empresariales. | Hype para este caso. |
| **AP2** (Google, 2025) | Especificación de pagos de agentes; adopción real incierta. | Hype por ahora. |
| **NLWeb** (Microsoft, 2025) | Real y abierto, hace de un sitio un endpoint consultable en lenguaje natural vía MCP. Adopción baja. | Opcional; solo si hay equipo técnico. |
| **Visa / Mastercard agent payments** | Programas piloto de credenciales tokenizadas para agentes. | Fuera del alcance de una tienda chica. |

**Qué debería preparar una tienda chica** [OPINIÓN]: (1) catálogo estructurado de una sola fuente (SKU estables, título, descripción, imágenes, precio, moneda, disponibilidad); (2) schema `Product`/`Offer` válido y coherente con lo visible; (3) políticas de entrega y reembolso legibles; (4) un export de feed (CSV/XML) regenerable; (5) sitemap y robots que permitan a bots de IA (ver otros informes); (6) pasarela que acepte varias monedas (Stripe/PayPal/Mercado Pago). Con esto, cualquier protocolo ganador será trivial de adoptar, porque **todos parten del mismo feed**.

---

## 6. Feeds multi-idioma y multi-país (conocimiento previo, [NO VERIFICADO] salvo lo indicado)

- **Estructura típica de Merchant Center:** un feed (o fuente) por combinación país + idioma, con etiqueta de feed (`feed label`) y `language` correctos; cada país exige `link` a la página en ese idioma, `price` en la moneda del país, y reglas fiscales (EE. UU. sin impuestos; UE con IVA incluido). Verificarlo en la ayuda de Merchant Center antes de implementar.
- **Envío:** para países que exigen costo de envío, se envía "0" en productos intangibles [HECHO parcial, ver 3.2]; omitirlo oculta el producto.
- **Identificadores:** GTIN/MPN/marca normalmente no aplican a moldes propios; se declara que el producto no tiene identificador y se usa la marca propia ("moldey"). Verificar si `identifier_exists` sigue vigente.
- **`product_type`** libre: p. ej. "Moldes de costura > Mujer > Vestidos > PDF". **`google_product_category`**: elegir de la taxonomía oficial la categoría de patrones/moldes de manualidades (Arts & Crafts) en lugar de "Software" o "Media > Libros", para no activar la política de eBooks. Consultar el archivo de taxonomía oficial para el ID exacto.
- **OpenAI:** admite campos "compatibles con Google" y descarta los desconocidos [HECHO parcial]; un feed de Google bien armado se reutiliza. Los precios por moneda y la localización por mercado son una carga de mantenimiento: empezar con 1–3 mercados.

---

## 7. Marketplaces como canal de descubrimiento (conocimiento previo, [NO VERIFICADO] salvo lo indicado)

| Marketplace | Notas a verificar |
|---|---|
| **Etsy** | Acepta descargas digitales; uno de los socios de Instant Checkout de OpenAI [EVIDENCIA] y co-desarrollador de UCP [EVIDENCIA]. SEO propio (título, 13 etiquetas, atributos). Etsy traduce listados automáticamente (verificar alcance). Etsy Ads: gasto adicional. Comisiones y tasas por listado: verificar. |
| **Creative Market, Makerist, Payhip, Gumroad** | Plataformas de bienes digitales; Makerist es fuerte en DACH para patrones. Cobran comisión o suscripción; algunas actúan como Merchant of Record para IVA (verificar caso por caso). |
| **Shopify / WooCommerce** | Plugins de descargas digitales (p. ej. Easy Digital Downloads ya tiene exportador de feed para Merchant Center, que menciona un bloque de envío de costo cero para ítems digitales). https://www.pixelyoursite.com/docs/google-merchant-center-feed [EVIDENCIA] |

**¿Vender en ambos (sitio propio + marketplace)?** [OPINIÓN]
- A favor: los marketplaces concentran demanda con intención de compra y son un canal de descubrimiento para marcas desconocidas; Etsy parece tener prioridad en integraciones de IA.
- En contra: canibalización de precio y de marca, y contenido duplicado entre listados y el sitio. Mitigación: redactar descripciones distintas en el marketplace, usar el marketplace como puerta de entrada (primera compra) y ofrecer en el sitio extras (paquetes, archivos editables, soporte, suscripción), sin ofrecer la misma oferta idéntica a menor precio en otro lado. Enlazar al sitio desde el contenido está limitado por las reglas de cada plataforma (verificar).

---

## 8. Contradicciones y controversias detectadas
1. Feed de OpenAI: formatos (JSONL/CSV/Parquet vs CSV/TSV/XML/JSON), entrega (SFTP vs Ads Manager), campos de elegibilidad (`enable_*` vs `is_eligible_*`).
2. Digital en OpenAI: spec dice `is_digital` ignorado; guía Alhena dice marcar digital; política comercial con dos versiones de junio de 2026 con alcance distinto.
3. Estado de Instant Checkout: "eliminado" vs "sigue para algunos".
4. Google y digitales: política oficial excluye eBooks de Shopping ads; foros reportan rechazos generalizados; un blog afirma que descargas y printables están permitidos.
5. Fechas de expansión de ChatGPT Ads en Europa (24 ago / 31 ago / 4 sep 2026).
6. Número de endpoints de la API de checkout de ACP (4 vs 5) y comisión del 4 %.

---

## 9. Qué hacer en moldey.com (priorizado)

| # | Acción | Impacto | Esfuerzo | Fiabilidad |
|---|---|---|---|---|
| 1 | **Catálogo limpio de una sola fuente de verdad**: SKU estables, títulos/descripciones por idioma, imágenes, precio por moneda, disponibilidad "descarga inmediata"; exportable a CSV/XML. Es la base de todo canal presente y futuro. | Alto | Medio | [OPINIÓN, coherente con los requisitos de feed de OpenAI y Google] |
| 2 | **Schema `Product` + `Offer`** en cada ficha, coherente con lo visible (precio, moneda, disponibilidad). Verificar en Rich Results Test. | Alto | Bajo | [NO VERIFICADO en esta sesión, práctica estándar] |
| 3 | **Página clara de entrega y reembolso para digitales** (descarga inmediata, formatos A4/Letter/A0/DXF, política de reembolso, contacto, datos del negocio). Reduce el riesgo de "Misrepresentation" en Merchant Center y mejora la conversión. | Alto | Bajo | [EVIDENCIA anecdótica + política de Google sobre sitio] |
| 4 | **Leer las políticas vigentes antes de invertir en feeds**: política comercial de OpenAI, "Unsupported Shopping content" de Google y reglas de Meta/Pinterest. Documentar qué categoría encaja un "molde PDF". | Alto | Bajo | [HECHO: política cambia, ver 2.4] |
| 5 | **Probar Merchant Center solo para listados gratuitos** (sin Google Ads vinculado ni anuncios) con 5–10 productos, `google_product_category` de manualidades, envío 0, y observar si se aprueban. Si hay rechazo, no insistir ni abrir cuentas nuevas. | Medio | Medio | [NO VERIFICADO: depende de política no explícita] |
| 6 | **Postular a chatgpt.com/merchants y revisar si hay país elegible**, pero sin esperar aprobación; la política puede excluir descargables. | Medio | Bajo | [NO VERIFICADO] |
| 7 | **Pinterest y SEO de contenido** (pines con enlace a fichas, imágenes por idioma) como canal de descubrimiento que no depende de feeds de compras. | Medio | Medio | [OPINIÓN] |
| 8 | **Etsy (u otro marketplace de digitales) como canal complementario** con listados diferenciados; medir canibalización 60–90 días. | Medio | Medio-alto | [OPINIÓN] |
| 9 | **Empezar feeds por 1–3 mercados/idiomas** (p. ej. EE. UU./inglés, España/español, Brasil/portugués) en vez de los 100 idiomas. | Medio | Medio | [OPINIÓN] |
| 10 | **Pasarela multi-moneda** (Stripe/PayPal) y política fiscal definida (IVA/ventas a distancia en servicios digitales). | Medio | Medio | [NO VERIFICADO] |
| 11 | **Seguimiento semestral de UCP/ACP/NLWeb**; implementar solo cuando lo ofrezca la plataforma de la tienda. | Bajo ahora | Bajo | [OPINIÓN] |

## 10. Qué NO hacer
- **No gastar en implementar ACP, UCP, AP2, A2A o checkout agéntico propio.** Checkout en chat: recortado por OpenAI en mar 2026; UCP: solo US/CA/AU y comercios seleccionados.
- **No presentar los moldes como "libros" ni "eBooks"** en feeds ni categorías (política de Google contra eBooks en Shopping ads).
- **No conectar una cuenta de Google Ads nueva o valiosa a un Merchant Center de productos digitales** hasta ver cómo se comporta: foros reportan suspensiones que se propagan.
- **No marcar `is_digital` esperando un beneficio** en OpenAI: la spec dice que se ignora.
- **No ocultar que el producto es digital** ni inventar GTINs o datos de envío falsos para pasar validaciones.
- **No dar por hecho que vender en un marketplace "da visibilidad en IA"**: es una hipótesis (Etsy es socio de OpenAI/Google, pero no hay prueba de que los listados digitales estén incluidos).
- **No duplicar textos idénticos** entre tienda y marketplace.
- **No creer afirmaciones de agencias** del tipo "solo salen en ChatGPT quienes envían feed" (no confirmado por OpenAI).

## 11. Pendientes de verificar (segunda pasada recomendada)
1. Texto vigente de https://openai.com/policies/commerce-policies/ y si cubre "archivos descargables/plantillas".
2. Países de registro de comercios de ChatGPT y si Argentina es elegible.
3. Página de Google "Unsupported Shopping content" completa; ¿hay mención a plantillas/printables?
4. Estado de Copilot Checkout, Perplexity, Meta, Pinterest, TikTok, Amazon y su postura sobre bienes digitales.
5. Lista vigente de rich results y atributos de `MerchantReturnPolicy`/`OfferShippingDetails` para bienes digitales.
6. Taxonomía de `google_product_category` para patrones de costura; requisitos de GTIN/identificadores.
7. Reglas de Etsy sobre traducción, etiquetas por idioma y publicidad.

## 12. Fuentes vistas en los resultados (no todas abiertas)
Oficiales: https://developers.openai.com/commerce/guides/key-concepts ; https://developers.openai.com/commerce/guides/get-started ; https://developers.openai.com/commerce/specs/file-upload/products ; https://openai.com/policies/commerce-policies/ ; https://openai.com/policies/merchant-feed-terms-of-service/ ; https://openai.com/policies/ad-policies/ ; https://chatgpt.com/merchants/ ; https://support.google.com/merchants/answer/16837055 ; https://developers.google.com/merchant/ucp ; https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/ ; https://support.google.com/merchants/answer/6150006 ; https://support.google.com/merchants/answer/14183113 ; https://support.google.com/merchants/answer/7169130 ; https://support.google.com/merchants/answer/6324484 ; https://support.google.com/merchants/answer/12157544 ; https://support.google.com/merchants/answer/12073010.
Prensa/terceros: las URL citadas en el cuerpo (CNBC, The Information, Modern Retail, Forrester, ppc.land, SERoundtable, Lengow, Channable, Alhena, Paz.ai, feedarmy, comunidad Shopify, etc.).
