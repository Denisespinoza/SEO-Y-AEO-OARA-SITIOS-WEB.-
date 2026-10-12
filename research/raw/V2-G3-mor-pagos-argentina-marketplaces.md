# V2-G3 — Verificación: MoR, pagos y marketplaces para un vendedor con sede en Argentina

Fecha de la verificación: 12 de octubre de 2026. Informes de origen: `T7-pagos-impuestos-legal-entrega-global.md` (secciones 3 y 11) y `T2-comercio-agentico-feeds.md`. Búsquedas WebSearch usadas: **12 de 12** (registro en la sección 6).

> **Aviso: esto NO es asesoramiento fiscal ni legal.** Son hechos documentados con su fuente y la antigüedad que tenía cada fuente. Cualquier decisión sobre inscripción, facturación, régimen cambiario o sociedad la valida un contador.

## 0. Límites de esta pasada (leer primero)

- **No pude abrir ninguna página oficial.** Volví a probar WebFetch y falla (`getaddrinfo ENOTFOUND polar.sh` y `help.etsy.com`). Todo lo que sigue sale de los **resúmenes que devuelve el buscador** sobre cada página, no de la lectura directa. Por eso uso **[HECHO·vía buscador]** cuando el resumen atribuye el dato a una página oficial, y **[EVIDENCIA]** cuando viene de terceros.
- "Versión actual de cada doc" **no se pudo confirmar**. Cuando el buscador informó la antigüedad de una página la anoto, convertida a fecha aproximada contando desde hoy (12-oct-2026). Esas fechas son orientativas.
- Las búsquedas con `allowed_domains` a sitios oficiales dieron buenos resultados para Polar, Lemon Squeezy, Paddle, Creem, Gumroad y Etsy. No dieron nada de Payhip, de la elegibilidad de OpenAI ni de Mercado Pago oficial.

## 1. Resumen: qué quedó resuelto

| # | Pregunta | Estado | Respuesta corta |
|---|---|---|---|
| 1a | Polar: ¿Argentina como país de payout? | **Confirmado** (otra vez) | Sí, está en la lista oficial de países. Requiere cuenta bancaria argentina en moneda local. |
| 1b | Creem | **Resuelto (antes "no confirmada")** | Sí, Argentina está en la tabla oficial de transferencia bancaria local (87 países). |
| 1c | Lemon Squeezy | **Confirmado, pero con fuente vieja** | Argentina figura en la lista de payouts bancarios, página de ≈2021. Cobra en ARS posible; paga en USD. |
| 1d | Paddle | **Parcial** | Argentina no está en la lista de países donde Paddle no puede tener vendedores. No hay tabla explícita de payout por país. Pago por transferencia en USD/EUR/GBP/AUD/CAD. |
| 1e | FastSpring | **No resuelto** | Solo vi que acepta ARS como moneda de venta. Sin lista de países de payout. |
| 2a | Gumroad | **Parcial y contradictorio** | Artículo más nuevo lista a Argentina para pago a banco local (en moneda local); el artículo viejo no. Si no hay banco, paga por PayPal en USD. |
| 2b | Payhip | **No resuelto** | La búsqueda no devolvió ningún resultado de Payhip. |
| 3a | Stripe para comerciante argentino | **Confirmado: no hay cuenta directa** según todas las fuentes de 2026 salvo una poco fiable. | La vía es entidad en EE. UU. (o Reino Unido). Stripe Atlas: sin información. |
| 3b | PayPal | **Cifras todavía inconsistentes** | Spread 3%–4,5% (una fuente); comisión de retiro varía por fuente; ninguna fuente oficial vista. |
| 4 | Etsy desde Argentina | **Resuelto en lo esencial** | Disponible con **Payoneer** (cobro en USD). Comisiones de listado/transacción vistas solo en terceros. |
| 5 | ChatGPT Shopping / feeds: ¿Argentina elegible? | **No resuelto** | No hay lista oficial de países vista. Las expansiones recientes de ChatGPT Ads que aparecen no incluyen LatAm. |
| 6a | Mercado Pago para cobrar al exterior en USD | **No hay evidencia de que exista** | Opera en pesos; los pocos indicios de cobro internacional son de tarjetas y de un usuario. |
| 6b | Pix para vender a Brasil desde Argentina | **No resuelto directamente** | Solo hay indicios de que los proveedores con Pix suelen pedir CNPJ. |
| 7 | Hotmart/Kiwify siendo extranjero | **No resuelto** | Hotmart acepta Pix; nada sobre productores extranjeros ni sobre Kiwify. |

## 2. Detalle por tema

### 2.1 Merchant of Record: ¿pagan a vendedores con sede en Argentina?

| Plataforma | Qué dice la fuente | Antigüedad / etiqueta | URL |
|---|---|---|---|
| **Polar** | La página oficial de países soportados incluye **Argentina** en la lista de payouts. La lista sale de Stripe Connect Express (payouts a residentes o empresas de los países listados). Los pagos de los clientes llegan a Polar como MoR, así que el país de payout **no necesita** Stripe Payments disponible. Restricción práctica: Stripe Connect exige **cuenta bancaria en el mismo país que el negocio y en moneda local**; cuentas multimoneda o "borderless" pueden no pasar la verificación. Polar dice que no puede pagar a un país que no esté en la lista. Conversión entre divisas de payout: **0,25% (UE) a 1% (otros países)**. | Fecha de la página no visible. [HECHO·vía buscador]. La parte de la cuenta bancaria viene de la página de cuentas de payout de Polar, resumida por el buscador. | https://polar.sh/docs/merchant-of-record/supported-countries ; https://polar.sh/docs/features/finance/accounts ; https://polar.sh/resources/pricing |
| **Lemon Squeezy** | La página oficial de países soportados lista **Argentina** entre los países con payout bancario. El changelog habla de 79 países con banco y 200+ con PayPal. El pago siempre se liquida en USD; si elegís otra moneda de payout, el procesador convierte a **tipo de cambio mid-market** del día del pago. **ARS** está entre las monedas en las que se puede vender (cliente argentino paga en pesos). | La página de países tiene ≈5 años según el buscador (≈2021); la cifra de 79 viene de un changelog de la época del lanzamiento. **Vigencia actual no confirmada.** [HECHO·vía buscador, fuente vieja]. | https://docs.lemonsqueezy.com/help/getting-started/supported-countries ; https://docs.lemonsqueezy.com/help/payments/currencies ; https://www.lemonsqueezy.com/changelog?ef124dd3_page=15 ; https://www.lemonsqueezy.com/blog/new-bank-payouts |
| **Paddle** | **No encontré una tabla de países de payout.** Lo que sí hay: (a) la página de países de Paddle muestra a Argentina como mercado (ARS, impuesto incluido) y Argentina **no** está en la lista de países donde Paddle no puede dar soporte a vendedores (Afganistán, Antártida, Bielorrusia, Birmania, República Centroafricana, Cuba, etc.); (b) monedas de payout: la página de desarrolladores dice USD, EUR, GBP, AUD, CAD; el Help Center lista más (CHF, CNY, CZK, DKK, HUF, PLN, SEK, ZAR) y **no incluye ARS**; (c) pagos mensuales con mínimo por defecto de **USD 100**; margen de conversión de hasta **1,5%** si la moneda de payout difiere; transferencias en moneda distinta de la del banco receptor van por SWIFT con **cargo de USD 15**. | Las páginas de desarrolladores tienen ≈887 días según el buscador (≈mayo de 2024); el Help Center podría ser más reciente. Fuentes se contradicen en monedas. [EVIDENCIA·parcial]. **Inferencia mía [OPINIÓN]:** el camino probable es transferencia internacional en USD a un banco argentino; confirmar con soporte. | https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle ; https://developer.paddle.com/concepts/sell/supported-countries-locales/ ; https://developer.paddle.com/concepts/sell/supported-currencies/ ; https://www.paddle.com/help/manage/get-paid/can-i-be-paid-in-my-local-currency ; https://www.paddle.com/help/manage/get-paid/is-there-a-fee-taken-for-payouts |
| **Creem** | La página oficial de países soportados incluye **Argentina** en la tabla de **transferencia bancaria local**, que cubre **87 países** (T7 había contado 86). Comisión de payout: **7 EUR/USD o 1% del monto, lo que sea mayor**. Aclara que algunos países tienen restricciones en las transferencias vía Wise; el resumen no mostró si Argentina es uno. Otras páginas de Creem hablan de 190+ países, pero eso se refiere a cobertura de venta e impuestos, no de payout. | Fecha no visible. [HECHO·vía buscador]. | https://docs.creem.io/merchant-of-record/supported-countries |
| **FastSpring** | Solo vi que acepta **ARS como moneda de transacción** y que "convierte ese precio de vuelta a la moneda de tu tienda antes de hacer el payout". **No apareció lista de países de payout** ni documentación para vendedores argentinos. La cifra "200+ regiones" es de dónde vende, no de dónde paga. | [NO VERIFICADO] para vendedor argentino. | https://developer.fastspring.com/docs/currencies-and-conversions ; https://fastspring.com/merchant-of-record/ |

**Qué cambia respecto a T7:** Creem pasa de "no confirmada" a "listada". Paddle pasa de "inaccesible" a "no excluida, sin tabla de payout" (sigue sin confirmación explícita). Polar queda confirmada otra vez. Lemon Squeezy sigue apoyada en una página vieja. No se resolvió: tarifa vigente de Polar (4% + 0,40 vs. 5% + 0,50), ni si cada MoR acepta moldes de costura (no lo busqué: queda para verificar en la política de contenido de cada uno).

### 2.2 Gumroad y Payhip

- **Gumroad, payout:** el artículo "Getting paid by Gumroad" **lista a Argentina bajo pago a cuenta bancaria**, y aclara que solo paga a cuenta bancaria local y **en moneda local**. Antigüedad ≈800 días (≈agosto de 2024). [HECHO·vía buscador]. https://help.gumroad.com/article/13-getting-paid
- **Contradicción:** el artículo "Can I Use Gumroad in My Country?" (≈1.600 días, ≈mayo de 2022) **no lista a Argentina** entre los países con depósito directo; en ese caso Gumroad paga por **PayPal**, siempre en **USD**, normalmente en 1 a 3 días hábiles. El artículo más nuevo es la mejor guía, pero hay que confirmarlo en la sección Payments de la cuenta. https://help.gumroad.com/article/152-can-i-use-gumroad-in-my-country
- **PayPal en el checkout de Gumroad:** disponible salvo para Argelia, Brasil, Egipto, India, Israel, Japón, Micronesia, Marruecos y Turquía. Argentina no está en la lista de exclusión. https://help.gumroad.com/article/275-paypal-connect
- **Pregunta abierta para el contador:** si Gumroad paga "en moneda local" a una cuenta argentina, eso implica pesos. No vi a qué tipo de cambio ni cuándo. [NO VERIFICADO]
- **Impuestos para el vendedor argentino:** no cubierto. Gumroad es MoR desde el 1-ene-2025 según T7 (https://gumroad.com/pricing).
- **Hay además** artículos de Gumroad sobre Payoneer/Transferwise (https://help.gumroad.com/article/223-payoneer-and-gumroad) y un post sobre cuentas bancarias locales en más países (https://gumroad.gumroad.com/p/local-bank-account-support-in-more-countries); aparecieron en resultados pero no vi su contenido.
- **Payhip:** **sin resultados.** Las preguntas de T7 (remisión de IVA UE, payouts a Argentina, dependencia de Stripe/PayPal propios) siguen abiertas. [NO VERIFICADO]

### 2.3 Stripe y PayPal para un comerciante argentino

**Stripe**

| Dato | Fuente | Etiqueta |
|---|---|---|
| Stripe **no opera como país estándar** para Argentina; la vía práctica es formar un negocio en EE. UU. y activar Stripe desde esa entidad. | Zenind, 5-mar-2026: https://www.zenind.com/help/post/how-to-open-a-stripe-account-in-argentina-with-a-u-s-llc | [EVIDENCIA]. Proveedor que vende el servicio de LLC: interés comercial. |
| Argentina no figura entre los países admitidos; las empresas argentinas no pueden registrar cuenta directa. | Global66: https://www.global66.com/blog/?p=18565 | [EVIDENCIA] |
| Alternativa: empresa en Reino Unido. | Osome: https://osome.com/uk/blog/stripe-argentina-verified-account | [EVIDENCIA]. Interés comercial. |
| Guía de comisiones 2026: Argentina "no opera directamente; vía dLocal o partners". | (ya citada en T7) https://dodopayments.com/blogs/stripe-supported-countries-alternatives | [EVIDENCIA]. Competidor. |
| **Fuente discordante:** un artículo dice que Stripe está activo en Argentina "desde 2022" con cobros en ARS. Contradice a las demás y no está respaldado. | https://experience.thinkvermont.com/exp/stripe-funciona-en-latinoamrica-gua-completa | [NO VERIFICADO], poco fiable |
| Existe una sociedad "Stripe Payments Argentina S.A." publicada en el Boletín Oficial (constitución fechada en 2020 según prensa). **Existir una sociedad no prueba que haya servicio de cobro para comercios.** | https://www.boletinoficial.gob.ar/pdf/linkQR/VVBkSXRhQ0hJQWgreFpJZ1U0d1UwZz09 ; https://www.iprofesional.com/economia/318241-alerta-para-mercado-pago-como-es-la-empresa-que-llega-al-pais | [HECHO] sobre la sociedad; la inferencia sobre servicio queda [NO VERIFICADO] |
| **Stripe Atlas:** ningún resultado específico sobre Atlas para fundadores argentinos (requisitos, aceptación del país, costo). | — | [NO VERIFICADO]. T7 solo tenía un agregador no fiable con un precio. |

Nunca vi la página oficial de Stripe de disponibilidad por país: **todo es de terceros**.

**PayPal (retiro a Argentina)**

| Dato | Fuente | Etiqueta |
|---|---|---|
| PayPal aplica su propio tipo de cambio con **recargo de 3%–4,5%** sobre la referencia. Sugiere configurar la cuenta para **retener saldo en USD** y evitar la conversión automática. | https://www.jonatanalmeira.com/?p=70809 (2026) | [EVIDENCIA], blog comercial |
| Comisión de retiro: **ARS 75 por extracción** desde cuenta local; desde cuentas de EE. UU., 2,5% en dólares. La cuenta bancaria vinculada debe estar en pesos. | iProfesional, 19-jun-2026: https://www.iprofesional.com/finanzas/403093-pay-pal-argentina-como-cobrar-en-dolares | [EVIDENCIA], prensa |
| Vía Nubi: **USD 10** para retiros entre USD 20 y 1.999, **0,5%** entre USD 2.000 y 10.000, más **21% de IVA sobre la comisión**. Afirma que no se pueden vincular cuentas en dólares locales. | Global66, actualizado abril 2026: https://www.global66.com/blog/?p=19400 | [EVIDENCIA], con interés comercial |
| Costo total estimado: **8%–10%** de un cobro internacional de USD 100 retirado en pesos (una fuente). Alternativa mencionada: Airtm, ≈5% total. | Una de las fuentes de la búsqueda 7; el buscador no indicó cuál. Mismos resultados que arriba. | [EVIDENCIA débil, fuente no identificada] |

**Contradicciones que persisten:** (a) la cuenta bancaria vinculada, ¿solo en pesos o también en USD?; (b) la comisión de retiro cambia según la fuente; (c) ninguna fuente oficial de PayPal. T7 ya marcaba la inconsistencia: sigue igual. Cambió la fecha: ahora hay dos fuentes de 2026 (junio y abril).

### 2.4 Etsy desde Argentina

| Dato | Fuente | Etiqueta |
|---|---|---|
| La lista oficial de países elegibles para Etsy Payments **incluye a Argentina con asterisco**: los vendedores de esos países usan una **cuenta de pago de Payoneer**. | https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments | [HECHO·vía buscador] |
| La política de pagos de Etsy dice que los vendedores residentes en Argentina deben registrarse **directamente con Payoneer** para entrar a Etsy Payments. | https://www.etsy.com/legal/etsy-payments/ | [HECHO·vía buscador] |
| Etsy deposita **solo en USD** en la cuenta Payoneer; luego se retira al banco local en pesos. | https://help.etsy.com/hc/en-us/articles/16999319005207-How-Do-I-Use-a-Payoneer-Account-With-Etsy-Payments | [HECHO·vía buscador] |
| La tabla de tarifas de la política muestra **6,5% + USD 0,30 por pedido** para Argentina. No pude ver qué concepto representa (probablemente procesamiento de pagos). **Verificar.** | https://www.etsy.com/legal/etsy-payments/ | [NO VERIFICADO·ambiguo] |
| **Contradicción:** la lista "actualmente disponible" de la política **omite** a Argentina; la lista del Help Center la incluye. Un anuncio de fines de 2023 decía que Argentina estaba lanzada por completo. Existe una versión previa de la política "vigente hasta el 9-oct-2025". | https://community.etsy.com/t5/Announcements/Updated-12-12-Etsy-Payments-is-expanding-to-sellers-in-more/td-p/143664021?nobounce ; https://www.etsy.com/seller-handbook/article/1183344188826 ; https://www.etsy.com/legal/policy/etsy-payments-policy-effective-until/1403344077683 | [EVIDENCIA·contradictoria] |
| Comisiones generales (tarifas de EE. UU. según guías de 2026): **listado USD 0,20**, **transacción 6,5%** sobre el total pagado (incluye envío), **procesamiento 3% + USD 0,25** (EE. UU.), **conversión de moneda 2,5%** si el listado está en otra moneda que la cuenta, **Offsite Ads 12%–15%** (tope USD 100 por pedido, opcional). | https://checkoutpage.com/blog/etsy-fees ; https://crosslist.com/blog/etsy-review ; https://www.gelato.com/blog/etsy-fees | [EVIDENCIA], blogs de terceros; **no vi la página oficial de tarifas** |
| **No verifiqué** reglas específicas de listados digitales (renovación del listado cada 4 meses vs. al vender, ni IVA sobre descargas). | — | [NO VERIFICADO] |

### 2.5 ChatGPT Shopping / feeds de OpenAI: ¿Argentina elegible?

- **Ninguna fuente lista países elegibles para el feed de producto orgánico** y no llegué a la documentación oficial de OpenAI. Un proveedor (Lengow) dice que la disponibilidad "varía según la región y la elegibilidad del comercio"; T2 ya había anotado que OpenAI no publicó criterios de elegibilidad ni calendario por mercado. https://www.lengow.com/integrations/chatgpt [EVIDENCIA débil]
- **Dato nuevo (ads, no feed orgánico):** un proveedor dice que ChatGPT Ads salió en los 27 Estados miembro de la UE más Islandia, Liechtenstein, Noruega y Suiza el **24-ago-2026**; otro habla de una expansión el **4-sep** a países seleccionados de Europa, India, Medio Oriente y Norte de África. **Ninguno menciona Latinoamérica.** Las dos fechas no coinciden del todo. https://commonthreadco.com/blogs/coachs-corner/chatgpt-ads-september-2026-product-feeds-now-required-platform-expands-globally-and-the-new-tools-ecommerce-brands-need-right-now [EVIDENCIA débil, tienda comercial]
- El título de esa misma fuente dice que los feeds de producto serían **"requeridos"** para anunciar. No pude confirmarlo en OpenAI. [NO VERIFICADO]
- **Shopify:** la app "ChatGPT Ads Feed Sync" crea **un feed por país** con precios del mercado de Shopify correspondiente. Shopify Catalog cubre comercios con productos elegibles que venden a compradores de EE. UU. (según un proveedor). https://apps.shopify.com/chatgpt-ads-product-feed-sync [EVIDENCIA]
- Channable agregó un feed "ChatGPT Commerce" el 3-oct-2025. https://helpcenter.channable.com/changelog/october-2025/october-3-2025-new-feed-open-ais-chatgpt-commerce [EVIDENCIA]
- **Conclusión:** la elegibilidad de Argentina **no se pudo verificar**. Lo único documentado es que la expansión de ads reciente no incluye LatAm. Sigue pendiente de T2.

### 2.6 Mercado Pago y Pix

**Mercado Pago para cobrar al exterior en USD:** no encontré evidencia de que un vendedor argentino pueda cobrar a clientes del exterior con liquidación en una cuenta en USD.
- Una guía de Global66 (actualizada en abril de 2026) dice que PayPal y Mercado Pago **no tienen integración oficial** y que Mercado Pago opera en pesos argentinos. El buscador no indicó cuál de las páginas de Global66 devueltas es la fuente exacta (aparecieron `?p=16557`, `?p=18060`, `?p=19400` y `?p=20902` en https://www.global66.com/blog/). [EVIDENCIA, interés comercial; URL exacta no identificada]
- Hilo de la comunidad de Shopify: un usuario dice que Mercado Pago funciona para ventas internacionales desde Argentina "solo con tarjetas"; sin respuesta confirmada sobre si el cliente ve USD o ARS. https://community.shopify.com/t/mercado-pago-arg-moneda-en-checkout/582046 [testimonio, no oficial]
- Comisión de 2,99% + IVA es para **ventas locales** (T7, `guiadesoftware`). Los agregadores dLocal, Kushki y Astropay aparecen como camino para cobrar al exterior con liquidación en USD/EUR; **no verifiqué** requisitos para vendedores argentinos. https://www.guiadesoftware.com/blog/mejor-pasarela-pago-argentina [NO VERIFICADO]
- iProfesional del 28-jul-2026 trata comisiones, plazos y montos de Mercado Pago: https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos (no vi su contenido).
- **Qué no hay:** documentación oficial de Mercado Pago sobre cobros internacionales ni confirmación de cuentas en USD en 2026.

**Pix para vender a Brasil desde Argentina:** no tuve una búsqueda dedicada y los resultados de la búsqueda combinada **no responden la pregunta**. Lo visto:
- Un estudio de caso de Adyen dice que **Hotmart acepta Pix desde 2021** (vía Adyen). https://www.adyen.com/pt_BR/centro-de-conhecimento/hotmart-comeca-a-aceitar-pagamentos-pix-com-adyen
- EBANX informa que Pix Automático está activo en Hotmart (el resumen dice "desde el 16 de junio"; el año no apareció). https://business.ebanx.com/en/press-room/press-releases/hotmart-sees-a-32-percentage-point-boost-in-retention-after-launching-recurring-payments-with-pix-via-ebanx
- Un foro de Shopify (usuario) y una contabilidad brasileña dicen que, en la práctica, **los proveedores con Pix suelen pedir CNPJ**. La contabilidad vende servicios de CNPJ: leer con cautela. https://community.shopify.com/t/venda-sem-cnpj/138050 ; https://www.contabilidadezen.com.br/blog/vender-gringa-produtor-impostos-2026/ [EVIDENCIA débil, con interés comercial]
- **No verifiqué** si algún MoR de la sección 2.1 ofrece Pix al comprador brasileño cuando el vendedor es argentino. Es la verificación más importante que falta para PT-BR (Pix = 42% del e-commerce brasileño según T7 [S36]).

### 2.7 Hotmart y Kiwify siendo extranjero

- Hotmart: comisión citada de **9,9% + R$ 1,00** por venta aprobada (blog Bit4learn, puede estar desactualizado). https://bit4learn.com/pt/?p=183 [EVIDENCIA débil]
- Hotmart procesa el pago, retiene su comisión y deposita el resto; **el recaudo de impuestos es obligación de quien vende**. Esto describe al productor brasileño, no al extranjero. https://www.contabilidadezen.com.br/blog/hotmart-impostos-produtor-2026/ [EVIDENCIA débil]
- **Sin resultados** sobre Kiwify, sobre productores residentes en Argentina, sobre pagos en dólares ni sobre retención de impuestos para un extranjero que vende a compradores brasileños. [NO VERIFICADO]

## 3. Pendientes de T7 y T2: qué quedó resuelto

| Pendiente original | Resultado |
|---|---|
| T7 §11: Argentina como payout en **Creem** | **Resuelto: sí** (87 países, Argentina en tabla local). |
| T7 §11: Argentina como payout en **Paddle** | **Parcial:** no excluida; sin tabla de payout; pago por transferencia en monedas fuertes. |
| T7 §11: lista completa de **Lemon Squeezy** | **Sin cambio de fondo:** sigue siendo una página de ≈2021; Argentina sí figura. |
| T7 §11: **Polar** (BR/MX no vistos; tarifa vigente) | Argentina reconfirmada. BR/MX y tarifa: **sin resolver**. |
| T7 §11: IVA UE en **Payhip** | **Sin resolver** (cero resultados). |
| T7 §11: ¿cada MoR **acepta moldes digitales**? | **Sin resolver** (no se buscó la política de contenido). |
| T7 §11: **Etsy** como canal complementario | **Resuelto en lo esencial** (Payoneer, USD); tarifas oficiales y reglas digitales sin ver. |
| T7 §3 / §2.3: **Gumroad** payouts a Argentina | **Parcial/contradictorio** (banco local en moneda local según el artículo nuevo; PayPal según el viejo). |
| T7 §2.3: **Stripe** directo / Atlas | Consistente con T7: sin cuenta directa. Atlas **sin resolver**. |
| T7 §2.3: **PayPal** spread | Dos fuentes de 2026 más; cifras todavía inconsistentes; sin fuente oficial. |
| T7 §2.3: **Mercado Pago** cobrador global | Sin evidencia de cobro en USD; opera en pesos. |
| T7 §2.2 / §11: **Pix** para vender a Brasil | **Sin resolver.** |
| T7 §3.1: **FastSpring**, **Hotmart**, **Kiwify** | FastSpring sin lista de payout; Hotmart/Kiwify sin dato sobre extranjeros. |
| T2: ¿Argentina elegible para **comercios de ChatGPT**? | **Sin resolver**; las expansiones recientes de ads no incluyen LatAm. |

## 4. Qué hacer en moldey.com

| Prioridad | Acción | Impacto | Esfuerzo | Base |
|---|---|---|---|---|
| 1 | Hacer el **onboarding de prueba** (sin publicar) en **Creem y Polar**, que listan a Argentina, y mirar en la pantalla de alta: país, moneda de payout, requisitos de cuenta bancaria, y política de contenido para patrones de costura. | Alto | Bajo | §2.1 |
| 2 | Escribir a soporte de **Paddle y Lemon Squeezy** pidiendo por escrito: payout a un vendedor argentino (moneda, vía, costos) y aceptación de moldes PDF. Guardar la respuesta con fecha. | Alto | Bajo | §2.1 |
| 3 | Llevar al contador las preguntas concretas: cobro en **USD vs. ARS** (Gumroad "moneda local"; Lemon Squeezy convierte a mid-market si elegís otra moneda; Polar exige cuenta en moneda local), tipo de cambio aplicable y facturación al MoR. | Alto | Bajo | §2.1, §2.2 |
| 4 | Abrir cuenta **Payoneer** (también es requisito de Etsy). Usar Etsy como canal de **descubrimiento** si el margen lo justifica, verificando tarifas en la página oficial. | Medio | Medio | §2.4 |
| 5 | Dejar **Gumroad** como canal secundario solo después de confirmar en el panel de la cuenta si paga a banco local o por PayPal. | Bajo-Medio | Bajo | §2.2 |
| 6 | Para PT-BR: **verificar con cada MoR** si el checkout muestra Pix cuando el vendedor es argentino antes de invertir en contenido en portugués orientado a conversión. | Alto | Medio | §2.6 |
| 7 | Postular igual en `chatgpt.com/merchants` solo si es gratis y rápido, **sin esperar aprobación**. | Bajo | Bajo | §2.5 |

## 5. Qué NO hacer

- No pagar una LLC ni Stripe Atlas "para tener Stripe" **sin contador**: las únicas fuentes que lo recomiendan venden ese servicio.
- No tomar como prueba el artículo que dice que Stripe funciona en Argentina desde 2022.
- No asumir que Mercado Pago sirve para cobrar en USD al exterior: no hay evidencia.
- No asumir Pix ni CNPJ resuelto: no hay datos para un vendedor argentino.
- No dar por vigente la lista de Lemon Squeezy (página de ≈2021) sin confirmar con soporte.
- No decidir con las tarifas de PayPal ni de Etsy de este informe: son de terceros y se contradicen.

## 6. Registro de búsquedas (12 de 12)

| # | Consulta (resumida) | Resultado útil |
|---|---|---|
| 1 | Polar + Creem, países y payout (dominios oficiales) | Polar, Creem |
| 2 | Lemon Squeezy países payout (dominios oficiales) | Lemon Squeezy |
| 3 | Paddle países, monedas, payout (dominios oficiales) | Paddle |
| 4 | Creem + FastSpring (dominios oficiales) | Creem sí; FastSpring parcial |
| 5 | Gumroad + Payhip payout Argentina (dominios oficiales) | Gumroad; Payhip nada |
| 6 | Stripe Argentina / Atlas (en español) | Stripe |
| 7 | PayPal Argentina, comisión, spread 2026 | PayPal |
| 8 | Etsy tarifas 2026 (general) | Tarifas; Argentina no respondida |
| 9 | ChatGPT merchants feed, países elegibles | Elegibilidad no resuelta |
| 10 | Etsy Payments, países elegibles (dominios Etsy) | Etsy Argentina resuelto |
| 11 | Mercado Pago cobrar al exterior en USD | Sin evidencia |
| 12 | Brasil sin CNPJ, Pix, Hotmart, Kiwify (portugués) | Parcial |

La búsqueda 8 se gastó sin resolver Argentina en Etsy y obligó a la 10; la búsqueda dedicada a Pix no se hizo para poder cubrir Etsy.

## 7. Fuentes (todas aparecieron en resultados de esta pasada; fecha entre paréntesis cuando se vio)

- https://polar.sh/docs/merchant-of-record/supported-countries
- https://polar.sh/docs/features/finance/accounts
- https://polar.sh/resources/pricing
- https://docs.lemonsqueezy.com/help/getting-started/supported-countries (≈2021)
- https://docs.lemonsqueezy.com/help/payments/currencies
- https://docs.lemonsqueezy.com/help/checkout/payment-methods (no leída)
- https://www.lemonsqueezy.com/changelog?ef124dd3_page=15
- https://www.lemonsqueezy.com/blog/new-bank-payouts
- https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle
- https://developer.paddle.com/concepts/sell/supported-countries-locales/ (≈mayo 2024)
- https://developer.paddle.com/concepts/sell/supported-currencies/ (≈mayo 2024)
- https://www.paddle.com/help/manage/get-paid/can-i-be-paid-in-my-local-currency
- https://www.paddle.com/help/manage/get-paid/is-there-a-fee-taken-for-payouts
- https://docs.creem.io/merchant-of-record/supported-countries
- https://developer.fastspring.com/docs/currencies-and-conversions
- https://fastspring.com/merchant-of-record/
- https://help.gumroad.com/article/13-getting-paid (≈ago 2024)
- https://help.gumroad.com/article/152-can-i-use-gumroad-in-my-country (≈may 2022)
- https://help.gumroad.com/article/275-paypal-connect
- https://help.gumroad.com/article/223-payoneer-and-gumroad
- https://gumroad.gumroad.com/p/local-bank-account-support-in-more-countries
- https://www.zenind.com/help/post/how-to-open-a-stripe-account-in-argentina-with-a-u-s-llc (5-mar-2026)
- https://www.global66.com/blog/?p=18565
- https://osome.com/uk/blog/stripe-argentina-verified-account
- https://experience.thinkvermont.com/exp/stripe-funciona-en-latinoamrica-gua-completa
- https://www.boletinoficial.gob.ar/pdf/linkQR/VVBkSXRhQ0hJQWgreFpJZ1U0d1UwZz09
- https://www.iprofesional.com/economia/318241-alerta-para-mercado-pago-como-es-la-empresa-que-llega-al-pais
- https://www.iprofesional.com/finanzas/403093-pay-pal-argentina-como-cobrar-en-dolares (19-jun-2026)
- https://www.global66.com/blog/?p=19400 (actualizado abril 2026)
- https://www.jonatanalmeira.com/?p=70809 (2026)
- https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments
- https://www.etsy.com/legal/etsy-payments/
- https://www.etsy.com/legal/policy/etsy-payments-policy-effective-until/1403344077683
- https://help.etsy.com/hc/en-us/articles/16999319005207-How-Do-I-Use-a-Payoneer-Account-With-Etsy-Payments
- https://www.etsy.com/seller-handbook/article/1183344188826
- https://community.etsy.com/t5/Announcements/Updated-12-12-Etsy-Payments-is-expanding-to-sellers-in-more/td-p/143664021?nobounce
- https://checkoutpage.com/blog/etsy-fees ; https://crosslist.com/blog/etsy-review ; https://www.gelato.com/blog/etsy-fees
- https://www.lengow.com/integrations/chatgpt
- https://commonthreadco.com/blogs/coachs-corner/chatgpt-ads-september-2026-product-feeds-now-required-platform-expands-globally-and-the-new-tools-ecommerce-brands-need-right-now
- https://apps.shopify.com/chatgpt-ads-product-feed-sync
- https://helpcenter.channable.com/changelog/october-2025/october-3-2025-new-feed-open-ais-chatgpt-commerce
- https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos (28-jul-2026)
- https://www.global66.com/blog/?p=18060
- https://community.shopify.com/t/mercado-pago-arg-moneda-en-checkout/582046
- https://www.guiadesoftware.com/blog/mejor-pasarela-pago-argentina
- https://www.adyen.com/pt_BR/centro-de-conhecimento/hotmart-comeca-a-aceitar-pagamentos-pix-com-adyen
- https://business.ebanx.com/en/press-room/press-releases/hotmart-sees-a-32-percentage-point-boost-in-retention-after-launching-recurring-payments-with-pix-via-ebanx
- https://community.shopify.com/t/venda-sem-cnpj/138050
- https://www.contabilidadezen.com.br/blog/vender-gringa-produtor-impostos-2026/
- https://www.contabilidadezen.com.br/blog/hotmart-impostos-produtor-2026/
- https://bit4learn.com/pt/?p=183
