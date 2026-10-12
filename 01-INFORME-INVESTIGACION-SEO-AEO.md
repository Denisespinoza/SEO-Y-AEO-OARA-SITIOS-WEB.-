# 01 · Informe de investigación: SEO y AEO/GEO global para una tienda de moldes digitales (oct. 2026)

> Para: moldey.com (moldes digitales de costura: PDF A4/Letter/A0, archivos editables/CAD, plantillas de sublimación; vende al mundo).
> Cómo se hizo: 7 informes temáticos + 9 de terminología por idioma + una segunda pasada de verificación. Los informes completos, con las URL, están en `research/raw/` (`T1`…`T7`, `V2-*`). **Este documento es la síntesis.**

## 0. Cómo leer este informe (honestidad sobre la evidencia)

- **Etiquetas:** `[HECHO]` = lo dice la plataforma o una fuente primaria (visto vía resultados de búsqueda). `[EVIDENCIA]` = estudio de terceros con metodología (casi siempre de proveedores de herramientas, con interés comercial). `[OPINIÓN]` = consejo de la industria o criterio nuestro sin prueba. `[NO VERIFICADO]` = sin respaldo.
- **Límites del método (importante):** la investigación se hizo solo con búsqueda web (no se pudo abrir ninguna página, solo leer resúmenes de resultados) y con un tope de búsquedas por turno. Por eso: (1) **no se auditó moldey.com** (no hay acceso desde el entorno de investigación), (2) casi todas las cifras llegan vía medios secundarios, (3) la terminología de muchos idiomas está **inferida y marcada con su nivel de confianza** (ver `03`). Todo lo costoso o irreversible debe reconfirmarse en la fuente oficial antes de ejecutarse.
- **Fecha de los datos:** lo más reciente visto es de mediados de 2026. Entre junio y octubre de 2026 pudo cambiar algo.

## 1. Las 12 conclusiones que gobiernan el plan

1. **AEO/GEO "sigue siendo SEO" — según Google.** `[HECHO]` Su primera guía oficial para funciones de IA (15-may-2026) dice que optimizar para búsqueda generativa es optimizar para la experiencia de búsqueda; descarta `llms.txt`, "chunking", reescritura específica para IA y schema especial. Exige estar **indexado y ser elegible para snippet**, y pide contenido "no commodity": experiencia y datos propios. Esto vale para Google; ChatGPT, Perplexity, Copilot y Claude tienen sus propios índices y reglas.
2. **Ranking top-10 ya no garantiza ser citado.** `[EVIDENCIA]` Ahrefs (mar-2026): solo ~38 % de las citas de AI Overviews salen de páginas top-10 (en jul-2025 era 76 %; el cambio puede ser metodológico). Las IA no son un solo sistema: no extrapolar entre ellas.
3. **Las menciones de marca fuera de tu sitio son la señal más correlacionada** (0,664) con aparecer en AI Overviews `[EVIDENCIA, correlacional, marcas ya establecidas]`. Y las fuentes más citadas son Reddit, YouTube, Wikipedia, LinkedIn: plataformas ajenas.
4. **`llms.txt` no tiene efecto medible.** `[HECHO + EVIDENCIA]` Google lo desaconseja; estudios de logs muestran que casi nadie lo lee; SE Ranking (~300 mil dominios) no halló relación con citas. **El schema tampoco movió citas** en el experimento controlado más grande (Ahrefs, 1.885 páginas); sirve para rich results y claridad de entidad, no como "truco de IA".
5. **Estructura "respuesta primero" y páginas enfocadas** tienen respaldo moderado: ~44 % de las citas de ChatGPT salen del primer 30 % de la página (un estudio); una página enfocada rinde más que una "guía definitiva" enorme `[EVIDENCIA media-baja]`.
6. **robots.txt separa entrenamiento, búsqueda y acción del usuario** en OpenAI (GPTBot / OAI-SearchBot / ChatGPT-User), Perplexity y Anthropic. Se puede aparecer en la búsqueda de IA y bloquear el entrenamiento. **robots.txt no protege PDF de pago**: eso es control de acceso (URLs firmadas, marca de agua).
7. **Traducir con IA no está prohibido, pero el volumen sin valor se penaliza.** `[HECHO]` La política vigente es "scaled content abuse": generar muchas páginas para manipular rankings, con IA o sin ella. Google retiró en jun-2025 el consejo de bloquear con robots.txt las páginas autotraducidas (ahora apunta a `noindex` por página). El caso Reddit (traducción masiva con IA que subió en 2025 y habría caído en 2026) **no es extrapolable**.
8. **Arquitectura recomendada para 100 idiomas:** subdirectorios por idioma en un solo dominio (`moldey.com/es/`, `/pt-br/`…), hreflang **en sitemap**, cada URL autocanónica, HTML renderizado en servidor/estático. Search Console ya no tiene informe de segmentación internacional (retirado en 2022). `[HECHO]`
9. **Los rastreadores de IA, en su mayoría, no ejecutan JavaScript** (Vercel/MERJ; Gemini y Applebot son excepciones; el estudio es de fecha incierta, verificar en logs) `[EVIDENCIA]`. Lo que importa debe estar en el HTML inicial.
10. **El comercio dentro del chat está en retirada.** `[EVIDENCIA]` OpenAI recortó Instant Checkout en mar-2026; el checkout agéntico de Google (UCP) solo aplica a EE. UU./Canadá/Australia y comercios seleccionados. **No gastar en protocolos agénticos (ACP/UCP/AP2/MCP/NLWeb).** Lo útil: catálogo limpio, `Product`/`Offer` correctos, políticas de entrega y reembolso claras.
11. **"100 idiomas" no son 100 mercados.** Muchas entradas del ranking son variedades habladas que se escriben/buscan en otro idioma (árabe egipcio→árabe estándar; bhojpurí→hindi; wu→chino). Un análisis estima ~71 sitios propios y ~29 idiomas atendidos con otro (ver `02`). Y los idiomas de poca presencia web escrita (hausa, yoruba, igbo, zulú…) se compran en inglés/francés.
12. **Vender global exige resolver pagos e impuestos antes que traducir** (ver §8): sin un *Merchant of Record* hay obligaciones de IVA desde la primera venta en varias jurisdicciones; la comisión fija pesa mucho en tickets de USD 5–12.

## 2. SEO tradicional: lo que sigue siendo la base

| Área | Qué hacer | Etiqueta |
|---|---|---|
| Indexación | HTML servido (SSR/SSG), sitemap por idioma, Search Console (dominio + prefijo por idioma), Bing Webmaster Tools, IndexNow (Bing, Yandex, Naver, Seznam; **Google no lo soporta**, confirmado en la 2.ª pasada vía terceros) | `[HECHO]`/`[EVIDENCIA]` |
| Contenido | No-commodity: tablas de medidas, hojas por talla, rendimiento de tela, fotos de prendas cosidas, guías de impresión/armado. Páginas enfocadas | `[HECHO]` Google 2026 + `[EVIDENCIA]` |
| Autoridad | Menciones y enlaces reales (blogs, creadores, escuelas, prensa de manualidades); YouTube/Pinterest/Reddit con aporte genuino | `[EVIDENCIA]` correlacional |
| Rendimiento | LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1; móvil primero; sin cargar PDF en la ficha; fuentes CJK del sistema | `[HECHO*]` |
| Datos estructurados | `Product`/`Offer`, `Organization`+`sameAs`, `BreadcrumbList`, `WebPage.inLanguage`. **HowTo (2023) y FAQ (cambio de mayo de 2026 según el changelog) ya no dan rich results**; Product/Merchant listings/VideoObject siguen vigentes | `[EVIDENCIA media-alta]` ver `V2-G2` |
| Imágenes/vídeo | ALT por idioma, una URL de imagen compartida, `VideoObject`, sitemaps de vídeo | `[HECHO*]` |

## 3. AEO/GEO: qué hacer realmente (y qué no)

**Hacer**
1. Estar indexado y rastreable por Googlebot, Bingbot **y** OAI-SearchBot, PerplexityBot, Claude-SearchBot (si el WAF/CDN los bloquea por defecto, desaparecés de sus respuestas).
2. Escribir **respuesta primero** (definición o respuesta directa arriba), encabezados en forma de pregunta, afirmaciones con dato y fuente, fecha de actualización real.
3. Publicar **datos propios** que nadie más tiene (tablas de tallas por país, número de hojas A4/Letter/A0 por talla, rendimiento de tela, pruebas de ajuste, compatibilidad CAD probada).
4. Construir **presencia externa verificable**: canal de YouTube con tutoriales, Pinterest, comunidades (aportando valor y declarando la relación comercial), reseñas reales.
5. **Entidad consistente:** nombre, descripción, logo y perfiles iguales en todos lados; `Organization` con `sameAs`. Atención: **"moldey" se lee como "moldy" (mohoso) en inglés** `[OPINIÓN]`: reforzar la marca con contexto ("Moldey — moldes de costura digitales / digital sewing patterns").
6. **Medir** con un protocolo manual mensual (30–40 prompts por idioma, varias plataformas, 3 corridas) + canal "IA" en GA4 + logs de bots. Detalle en `05`.

**Confirmado en la 2.ª pasada (`V2-G1`):**
- **Anthropic documenta tres bots** en un artículo oficial: ClaudeBot (entrenamiento), Claude-User (pedido del usuario) y Claude-SearchBot (indexación para búsqueda). `[HECHO]`
- **Google-Extended es solo un token de robots.txt**: no afecta la inclusión en Search ni en AI Overviews/AI Mode (esos dependen de Googlebot y de los controles de snippet). `[HECHO vía secundarios concordantes]`
- **Cloudflare bloquea por defecto rastreadores de IA en dominios nuevos desde el 1-jul-2025** `[HECHO vía prensa]` → revisar el panel. Existe la sintaxis `Content-Signal: search=yes, ai-input=yes, ai-train=no` (declarativa y no vinculante).
- **Bing Webmaster Tools "AI Performance"** (vista previa desde feb-2026, según terceros): citas, páginas citadas y *grounding queries*, **sin clics**. Microsoft dijo (mar-2025) que usa schema para que sus LLM entiendan el contenido `[declaración, vía prensa]`.
- **Idioma de las fuentes citadas** `[EVIDENCIA, calidad baja a media: vendors y preprints]`: los AI Overviews tienden a citar fuentes **en el idioma de la consulta** (85 %–96 % según vendors; Grok cambia al inglés ~48 % de las veces); los preprints muestran **sesgo al inglés que se agrava en idiomas de pocos recursos** y menos fuentes en consultas no inglesas (p. ej. hindi). **Conclusión práctica: una página solo en inglés probablemente no sea la que se cite en una consulta en español; hace falta una página en el idioma.**
- **AI Mode ya no es solo inglés** (hindi, indonesio, japonés, coreano, portugués de Brasil; luego 7 idiomas de India y español); no hay lista oficial vigente verificada.
- Que Perplexity-User "ignore robots.txt" viene de terceros/disputa con Cloudflare, no de documentación oficial `[NO VERIFICADO]`.

**No hacer**: contratar "garantías de citas", pagar por llms.txt/schema "para IA", publicar `llms-full.txt` con tu catálogo, bloquear todos los bots de IA, ni confiar en una sola captura de un prompt.

**Rastreadores (robots.txt):** permitir búsqueda y acción del usuario (OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, Claude-SearchBot, Claude-User, Googlebot, Bingbot); decidir aparte el entrenamiento (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot, Meta-ExternalAgent). Postura sugerida: permitir páginas públicas de marketing/guías, bloquear áreas de pago. Plantilla en `plantillas/robots.txt`. Los nombres de bots no confirmados por documentación oficial están marcados en `05`.

## 4. SEO internacional técnico (resumen operativo)

- **URLs:** `moldey.com/` (inglés + `x-default`), `/es/`, `/pt-br/`, … Parámetros `?lang=` prohibidos para indexables; ccTLD y subdominios descartados. Slugs traducidos y sin diacríticos en idiomas latinos; **slug ASCII + ID estable** en idiomas no latinos (el título nativo va en `<title>`/H1).
- **Canónicos:** cada URL de idioma es autocanónica; nunca canonicalizar una traducción al original.
- **hreflang:** en sitemap (con 100 idiomas cada entrada pesa ~11,7 KB → ~4.000 URLs por archivo, no 50.000; generar por script). Códigos ISO 639-1 + región; `es-419` no es válido; escritura: `zh-Hans`/`zh-Hant` **probablemente** aceptados (un resumen de la doc de Google y un tercero; sin texto literal), `sr-Latn` sin evidencia directa → usar `zh-CN`/`zh-TW` (sintaxis documentada con certeza) y publicar serbio con una sola escritura por URL. **Baidu y Naver no usan hreflang** (solo terceros): usar `Content-Language` y contenido claro en su idioma. Añadir `<html lang>` y `Content-Language` (Bing pesa poco el hreflang).
- **Sin redirecciones automáticas por IP/idioma;** banner no bloqueante; selector `/languages/` con enlaces `<a>` reales y endónimos.
- **Escrituras:** `dir="rtl"` y propiedades lógicas de CSS para árabe/hebreo/persa/urdu; `lang` correcto en CJK (unificación Han); birmano solo Unicode; normalizar NFC; una escritura por URL (serbio, uzbeko, kazajo).
- **Mercados con buscador propio:** Yandex (Rusia ≈71 %), Naver (Corea ≈64–68 %), Baidu (China; ICP para alojar), Seznam (Chequia 13,5 %). Prioridad baja para la etapa 1; ver `02`.

## 5. Traducción y calidad (el punto de mayor riesgo)

- **Flujo seguro:** traducción automática con glosario → post-edición nativa → control de calidad por muestreo → publicar. Mientras no esté aprobada: `noindex, follow`, fuera del sitemap y del clúster hreflang, **sin bloquear con robots.txt** (Google no vería el `noindex`).
- **Niveles:** A (≈5 %: home, categorías, top-50, tallas, políticas) 100 % revisado; B (≈85 %: fichas) con glosario + muestreo 10–20 %; C (blog/guías) 100 % revisado.
- **Idiomas "nivel C" de alto riesgo para MT** (nepalí, birmano, amárico, tigriña, oromo, jemer): revisión humana obligatoria; las métricas automáticas fallan en ellos.
- **Keywords:** no se traducen; se investigan en cada idioma (Search Console, Trends, Wordstat, Naver, Keyword Planner, autosuggest local). Ver `03` y `02`.
- **Evitar plantillas repetidas:** cada ficha debe tener datos reales localizados.

## 6. El nicho: moldes digitales (qué piden los compradores)

- **Demanda inglesa** `[EVIDENCIA débil]`: "sewing pattern" ~74.000/mes vs "pdf sewing patterns" ~3.600/mes; "sewing pattern pdf" −21 % (abr-2025→mar-2026) según una herramienta de Etsy (estimaciones débiles). La oportunidad está en la **cola larga multilingüe y en nichos** (formatos, tallas, prendas tradicionales), no en pelear el término genérico en inglés.
- **Quejas reales verificadas:** escala de impresión incorrecta, falta de A0, sin margen de costura, falta de archivos Letter, geobloqueos, pocas explicaciones. **Una ficha que responda todo arriba es un diferenciador.**
- **Qué declarar en cada ficha:** hojas A4/Letter/A0/proyector, páginas por talla, capas, margen de costura (cuánto), cuadrado de prueba (medida), tallas y sistema (cm y pulgadas), dificultad, tela, idioma de instrucciones, **licencia** (personal / venta pequeña / fabricación; hay vendedores que cobran US$ 125 por patrón para fabricación).
- **DXF no es un formato de moldería en sí:** hay convenciones (AAMA, ASTM D6673) y los importadores suelen requerir correcciones. **Probar en Optitex, Gerber, Clo3D, Lectra antes de declarar compatibilidad.**
- **Sublimación:** la plantilla es un *dieline* vectorial (PDF/AI/EPS/CDR) a escala real, 300 dpi, sangrado (varía 3–5 mm o 0,25–0,5 in según proveedor), zona segura; color RGB vs CMYK depende del RIP del taller (fuentes en conflicto: preguntar).
- **Palabras trampa:** "pattern" (estampado vs molde) y "molde" (recipiente/molde industrial). Titular siempre "molde de costura / sewing pattern + prenda".
- **Estacionalidad invertida** entre hemisferios (clave para vender desde Argentina): programar contenido por hemisferio.
- **IA:** "foto→molde" no está probado para prendas ajustadas; lo real es personalización por medidas/paramétrica. No prometer "moldes con IA desde una foto".
- **Piratería:** sin cifras fiables; protección principalmente **contractual** + marca de agua con ID de pedido + vigilancia/DMCA; el formato editable es el de mayor riesgo.

## 7. Plataformas y comercio con IA

- **Cuota de buscadores:** Google ≈89–91 % global (StatCounter jul-2026); excepciones: Yandex en Rusia (~71 %), Naver en Corea (~64–68 %), Seznam en Chequia, Baidu en China (cifras poco fiables), Bing fuerte en escritorio (Japón ~45 %). `[EVIDENCIA]`
- **Asistentes:** ChatGPT ~900 M usuarios semanales (India ~100 M); Gemini ~950 M MAU; Meta AI entre 640 M y 1.200 M según definición (fuerte en India, Brasil, Indonesia, México vía WhatsApp); Doubao ~382 M en China. Los datos cambian rápido.
- **Descubrimiento:** Pinterest (≈640 M MAU; Brasil ≈40 M, México ≈27 M, Alemania ≈23 M) y YouTube son los canales de mejor relación alcance/relevancia para moldes. Reddit/YouTube figuran entre lo más citado por IA (los estudios no coinciden en cifras).
- **Marketplaces (`V2-G4`):** **Mercado Libre México prohíbe publicar artículos descargables** (excepción: el titular de los derechos que lo declare; Argentina sin verificar); Shopee no concluyente (guías contradictorias); Trendyol, Allegro, Rakuten y Taobao sin dato. **Sí aceptan moldes PDF** (con fichas reales A4/A0/plotter): **Hotmart** (Brasil; no probado que un vendedor argentino pueda abrir cuenta), **Payhip** (tiene páginas propias para vender patrones de costura; cobro a PayPal/Stripe del vendedor), **Gumroad** y **BOOTH** (descargas; tarifa 5,6 % + 45 JPY desde oct-2025). Existe al menos un canal de Telegram de moldes PDF (competencia/piratería).
- **Google Shopping y digitales (`V2-G2`):** los eBooks/libros digitales **no se admiten** en Shopping y pueden causar **suspensión crítica de la cuenta de Merchant Center** (`prohibited_content_ebooks`); no se vio que las plantillas/PDF de patrones estén listados ni como prohibidos ni como admitidos. **No presentar los moldes como libros ni eBooks.** Probar solo listados gratuitos con 5–10 productos, sin vincular una cuenta de Ads valiosa, y no insistir si hay rechazo. Para `Product`/`Offer` de digitales Google no tiene guía específica: `shippingDetails` y política de devoluciones son opcionales/recomendadas (`MerchantReturnNotPermitted` existe).

## 8. Pagos, impuestos, legal y entrega (condicionan la conversión)

- **Merchant of Record casi obligatorio** para B2C global desde Argentina. Estado tras la 2.ª pasada (`V2-G3`, todo vía resúmenes de buscador; **verificar en la página oficial antes de abrir cuenta**): **Polar** (Argentina en la lista oficial de payouts; exige cuenta bancaria argentina en moneda local); **Creem** (Argentina en la tabla oficial de transferencia local, 87 países; payout 7 EUR/USD o 1 %); **Lemon Squeezy** (Argentina listada, pero en una página de ≈2021; paga siempre en USD); **Gumroad** (artículo reciente la lista para banco local; uno viejo no; si no, PayPal en USD); **Paddle** (Argentina no figura entre los países excluidos, pero sin tabla de payout; mínimo de pago USD 100); **FastSpring y Payhip: sin resolver.** Etsy funciona desde Argentina vía **Payoneer** (cobro en USD). **Mercado Pago no parece cobrar al exterior en USD** (sin evidencia).
- **Stripe no tiene cuenta directa para comerciantes argentinos** (vía: sociedad en EE. UU./UK, con implicancias fiscales; Stripe Atlas sin información). PayPal: spread de ~3–4,5 % según una fuente, sin fuente oficial. **Elegibilidad de Argentina en los feeds de ChatGPT: sin dato** (las expansiones de ChatGPT Ads vistas no incluyen LatAm).
- **Costo fijo:** "5 % + US$ 0,50" cuesta ~13 % en un molde de US$ 6; diseñar packs y precio mínimo.
- **Métodos locales mueven conversión** (Pix 42 % del e-commerce brasileño en 2025; UPI en India; Alipay/WeChat 89 % en China) pero se heredan del MoR/PSP: no integrar uno por uno.
- **No vender a Rusia ni países sancionados** (Cuba, Irán, Corea del Norte, Siria; Polar y Paddle los bloquean).
- **Legal:** términos, privacidad, reembolsos y licencias en ES/EN (revisión de abogado); derecho de desistimiento en contenido digital (UE/UK); GDPR/LGPD/CPRA; accesibilidad (EAA 2025, WCAG 2.2). **No es asesoramiento legal ni fiscal:** lo debe validar un contador y un abogado (lista en `T7`).
- **Entrega:** enlaces firmados con caducidad, límite de descargas, marca de agua con ID del comprador; hoja de prueba; instrucciones en varios idiomas; sin geobloqueo.

## 9. Lo que quedó sin verificar (y cómo cerrarlo)

1. Auditoría real de moldey.com (Fase 0 del plan, `06`).
2. Demanda real por idioma (Search Console, Keyword Planner, Trends, Wordstat, Naver): el puntaje de idiomas en `02` es un modelo con hipótesis.
3. Terminología de idiomas con confianza baja en `03` (revisión nativa).
4. Políticas vigentes de Google Merchant/OpenAI para digitales, hreflang con escritura, Argentina en cada MoR (ver `V2-*`).
5. Medición de AEO multilingüe: no hay estudios sólidos; se mide con el protocolo de `05`.

## 10. Índice de fuentes
Cada informe de `research/raw/` termina con su lista de URL (todas vistas en resultados de búsqueda; algunas solo por resumen). Antes de citar una cifra en público, abrir la fuente original.
