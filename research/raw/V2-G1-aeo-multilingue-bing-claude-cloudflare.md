# V2-G1 — Verificación temática: AEO multilingüe, Microsoft/Bing, Anthropic, Google-Extended, Cloudflare, Perplexity/ChatGPT-User

**Verificador:** G1 (2.ª pasada). **Fecha:** 12-oct-2026. **Base:** `research/raw/T1-aeo-geo-llmo.md` (sección 13, "Pendientes de verificar").
**Presupuesto:** 12 de 12 búsquedas WebSearch usadas (1: multilingüe general; 2: Temso; 3: AI Mode idiomas; 4: AI Mode/idiomas de pocos recursos; 5: Bing AI Performance; 6: Bing + schema; 7: Anthropic; 8: Google-Extended; 9: Cloudflare bloqueo por defecto; 10: Content Signals; 11: guía Google 15-may-2026; 12: Perplexity-User/ChatGPT-User). Además intenté 1 WebFetch a la guía de Google: falló con `ENOTFOUND` (confirmado que WebFetch no funciona).

**Limitación central:** todo lo de abajo lo vi como **resúmenes de resultados de búsqueda** (títulos, URLs y un resumen generado). No pude leer ninguna página primaria. Donde la fuente es oficial pero el texto me llegó por un resumen o por terceros, lo digo. No hay URLs inventadas: todas aparecieron en mis resultados. Cuando una fecha no era visible, lo marco así.

Etiquetas: **[HECHO]** documentado por la plataforma/fuente primaria; **[EVIDENCIA]** estudio de terceros con metodología; **[OPINIÓN]**; **[NO VERIFICADO]**.

---

## 0. Resumen ejecutivo

1. **Idioma de las fuentes citadas (hueco 1, parcialmente cerrado):** la evidencia 2026 disponible es en su mayor parte de **vendors** y preprints, no de e-commerce. Dice, con cautela, que los AI Overviews citan mayormente fuentes **en el idioma de la consulta** (Temso: 85,4 % local; Weglot: 96 % para México) mientras que otros asistentes, como Grok, cambian al inglés (51,7 % local). Los preprints académicos muestran **sesgo al inglés** que **se agrava en idiomas de pocos recursos** y **menos fuentes en consultas no inglesas** (p. ej. AI Overviews sin fuentes en 30 % de respuestas en hindi, tema salud mental). [EVIDENCIA, calidad baja a media]
2. **AI Mode ya no es solo inglés:** se expandió en 2025 a hindi, indonesio, japonés, coreano y portugués de Brasil, luego a 7 idiomas de India y a español (una fuente fecha el español el 26-ene-2026). No encontré una lista oficial vigente a octubre de 2026. [HECHO vía prensa]
3. **Bing Webmaster Tools "AI Performance" existe** (vista previa pública desde feb-2026, según blogs de terceros): da citas totales, páginas citadas y *grounding queries*; **no da clics ni tráfico**; datos de muestra; exportación solo CSV. No vi la documentación oficial de Microsoft. Microsoft (Fabrice Canel, SMX Munich, mar-2025) dijo que usa **schema** para que sus LLM entiendan el contenido. [HECHO por declaración, vía prensa]
4. **Anthropic documenta los tres bots** en un artículo oficial: ClaudeBot (entrenamiento), Claude-User (pedido del usuario) y Claude-SearchBot (indexación para búsqueda). Cierra el pendiente de T1. [HECHO]
5. **Google-Extended es un token de robots.txt, no un rastreador**; no afecta la inclusión en Search ni (según los secundarios concordantes) en AI Overviews/AI Mode; estos dependen de Googlebot y de los controles de snippet. [HECHO vía secundarios concordantes]
6. **Cloudflare:** bloqueo por defecto de rastreadores de IA en dominios nuevos desde el **1-jul-2025** [HECHO vía prensa]; **Content Signals** con sintaxis `Content-Signal: search=yes, ai-train=no` (tres señales: `search`, `ai-input`, `ai-train`) [HECHO vía resúmenes del blog/docs de Cloudflare]. Aparece además una **novedad no verificada** de **15-sep-2026** (nuevo bloqueo por defecto para rastreadores multifunción en páginas con anuncios).
7. **Guía de Google del 15-may-2026:** la fecha y el título quedan **confirmados** por el anuncio oficial en el blog de Search Central; **no hallé** que trate idiomas, traducción o hreflang. [Ausencia de evidencia, no evidencia de ausencia]
8. **Perplexity-User:** que "generalmente ignora robots.txt" sigue viniendo de **guías de terceros** y de la postura de Perplexity en la disputa con Cloudflare (ago-2025); no vi texto oficial que lo diga. En esa disputa, Cloudflare dijo que ChatGPT-User **sí** respetó el bloqueo. [EVIDENCIA mixta / disputado]

---

## 1. Estudios 2025–2026 sobre AEO fuera del inglés (hueco 1)

### 1.1 Tabla de estudios

| Estudio | Qué midió | Hallazgo (según resumen visto) | Fecha | Fuente | Calidad |
|---|---|---|---|---|---|
| **Temso, "Lost in Translation"** | ~7 M de citas de IA, 4 modelos, 6 idiomas no ingleses, 47 verticales | Google AI Overview: **85,4 %** de citas en el idioma local; Grok: **51,7 %** (brecha de 34 pp). En Grok con prompts en neerlandés, **53,5 %** de las fuentes eran en inglés vs 38,3 % en neerlandés. Idiomas germánicos (neerlandés, sueco) sufren más; los románicos (español, francés) mejor. No pude ver qué otros dos modelos incluye ni las cifras de ChatGPT/Perplexity/Gemini. | abril 2026 (según el resumen) | https://www.temso.ai/data/-Lost-in-Translation-How-AI-Models-Handle-Local-Language-Sources | Baja a media. Vendor (Temso vende herramientas de visibilidad en IA); metodología no clara en el resumen. Muestra grande. |
| **Weglot, "AI search and language"** | Consultas localizadas, mercado México | **96 %** de las citas de AI Overviews venían de fuentes en español en consultas localizadas para México | no visible | https://www.weglot.com/blog/ai-search-and-language | Baja. **Conflicto de interés**: Weglot vende traducción de sitios. |
| **"Sources of Truth" (auditoría multiplataforma y multilingüe de citas en consultas de salud mental)** | 7 idiomas, varias plataformas | **AI Overviews no devolvió fuentes en 30 % de las respuestas en hindi**; las consultas no inglesas mostraron **menos fuentes** que las inglesas | ID arXiv 2609 → sept-2026 (inferencia por el ID) | https://arxiv.org/pdf/2609.00319 | Media (preprint, sin revisión de pares visible). **Tema salud mental**, no e-commerce: extrapolar con cuidado. |
| **"Evaluating Commercial AI Chatbots as News Intermediaries"** | Chatbots comerciales y noticias, 6 regiones | **Wikipedia en inglés** es la fuente más citada globalmente aunque 5 de las 6 regiones eran de contenido no inglés | ID arXiv 2605 → mayo-2026 (inferencia) | https://arxiv.org/pdf/2605.22785 | Media (preprint). Contexto de noticias. |
| **Estudio controlado de RAG multilingüe (arXiv 2509.13930)** | Preferencia de idioma de fuente en generación con recuperación | Los modelos prefieren citar fuentes en inglés cuando la consulta está en inglés; el **sesgo se amplifica en idiomas de pocos recursos**; a veces sacrifican relevancia del documento por la preferencia de idioma | "Submitted 02 Oct 2025" (v2) | https://www.alphaxiv.org/abs/2509.13930v2 | Media (laboratorio, no motores de producción). |

**Piezas que aparecieron pero no pude leer (no las uso como evidencia):** Johns Hopkins, "multilingual artificial intelligence often reinforces bias" (2-sep-2025), https://hub.jhu.edu/2025/09/02/multilingual-artificial-intelligence-often-reinforces-bias/ (solo vi el título); un estudio sobre sesgo de Google Scholar contra papers no ingleses, https://www.labmanager.com/google-scholar-shows-bias-against-non-english-papers-25165 (otro dominio, poco relevante para citación en IA).

### 1.2 Calidad en idiomas de pocos recursos

- Evidencia más directa de esta pasada: el preprint de RAG (sesgo hacia el inglés más fuerte en idiomas de pocos recursos) y la auditoría de salud mental (AI Overviews sin fuentes en 30 % de respuestas en hindi). Ninguno mide e-commerce ni patrones de costura. [EVIDENCIA, preprints]
- Un resumen de TechCrunch (dic-2024, anterior a la expansión) recoge que un director de ingeniería de Gemini admitió que los AI Overviews en idiomas nativos como el hindi tendían a tener **imprecisiones**: https://techcrunch.com/2024/12/20/google-is-expanding-geminis-in-depth-research-mode-to-40-languages . Es **viejo**: no refleja el estado de 2026. [HECHO de 2024, vía resumen]
- Google afirma que su modelo para AI Mode "no es solo pasar el texto por un traductor" sino que entiende información local y contexto cultural (Gemini 2.5 personalizado): https://www.maginative.com/article/google-expands-ai-mode-in-search-to-five-new-languages/ . Es la propia afirmación de Google, sin medición independiente. [HECHO de Google / afirmación de marketing]

### 1.3 Expansión de AI Mode a otros idiomas

| Hito | Detalle | Fuente | Fecha |
|---|---|---|---|
| Solo inglés | Más de seis meses solo en inglés | https://techcrunch.com/2025/10/08/googles-search-live-comes-to-india-ai-mode-gets-more-languages | mención en nota de oct-2025 |
| 5 idiomas | Hindi, indonesio, japonés, coreano, portugués de Brasil | https://searchengineland.com/google-expands-ai-mode-beyond-english-461680 ; https://www.maginative.com/article/google-expands-ai-mode-in-search-to-five-new-languages/ ; https://www.neowin.net/news/googles-ai-mode-finally-available-for-non-english-users-starting-with-these-languages/ | 2025 (fecha exacta no visible; el resumen dice "fines de 2025") |
| 7 idiomas de India | Bengalí, canarés, malayalam, maratí, tamil, telugu, urdu; parte de una expansión de **más de 35 idiomas y 40 países/territorios** | https://techcrunch.com/2025/10/08/googles-search-live-comes-to-india-ai-mode-gets-more-languages | 8-oct-2025 |
| Español global | AI Mode para hispanohablantes en todo el mundo | https://www.folio3.ai/ai-pulse/google-ai-mode-expands-spanish-speakers-globally | el resultado trae "26-ene-2026"; no es seguro que sea la fecha del lanzamiento (puede ser la del post) |
| "Escala más rápido entre idiomas" | Titular de Search Engine Journal; **solo vi el título**, no el contenido | https://www.searchenginejournal.com/google-says-ai-mode-can-now-scale-faster-across-languages/575791/ | no visible (el ID 575791 está cerca del 575026 de la cobertura de la guía del 15-may-2026, lo que sugiere ~mayo-2026; **inferencia**) |

[NO VERIFICADO]: la **lista oficial vigente a octubre de 2026** de idiomas/países de AI Mode y AI Overviews. No apareció una página oficial de Google; habría que consultar la ayuda de Búsqueda de Google. Una nota de Taiwán decía que la función no estaba activa pese a figurar en la lista (resumen del buscador): la disponibilidad real varía por país.

### 1.4 Lectura crítica (qué se puede y qué no se puede concluir)

- **Sí es defendible** [EVIDENCIA, calidad baja a media]: en idiomas grandes (español, francés, y presumiblemente portugués) los AI Overviews tienden a citar fuentes en el idioma de la consulta. Para moldey.com esto implica que **una página solo en inglés probablemente no sea la que se cite en una consulta en español**; hace falta una página en el idioma. Es coherente con cómo funciona la búsqueda clásica.
- **Contradicción/controversia:** los números de vendors (85 %, 96 %) contrastan con los preprints (menos fuentes y sesgo al inglés en idiomas de pocos recursos). No son incompatibles: miden cosas distintas (idioma de la fuente cuando hay fuentes vs cantidad de fuentes; idioma alto vs bajo de recursos; plataforma). Hay que esperar que el patrón dependa de la plataforma (Grok vs AI Overviews) y del idioma.
- **No hay estudio visto de e-commerce ni de productos digitales en otros idiomas.** Sigue [NO VERIFICADO] y T1 §13 punto 4 queda abierto.
- **Vendor bias:** Temso y Weglot venden productos que se benefician de la narrativa "necesitás contenido local". Usarlos como indicio, no como base de decisión.

---

## 2. Microsoft: Bing Webmaster Tools "AI Performance" y datos estructurados (hueco 2)

### 2.1 AI Performance (Bing Webmaster Tools)

| Punto | Lo que vi | Fuente | Etiqueta |
|---|---|---|---|
| Existencia y fecha | Vista previa pública desde **feb-2026**; accesible a quien tenga un sitio verificado en BWT | https://www.searchinfluence.com/blog/bing-ai-performance-report-copilot-citations/ ; https://previsible.io/seo-ai-news/bing-ai-performance-report/ | [HECHO vía terceros]; no vi doc oficial de Microsoft |
| Cobertura | Copilot, resúmenes de IA dentro de Bing y "integraciones de socios de IA seleccionados"; no hay filtro por canal ni se identifica a los socios | https://momenticmarketing.com/blog/bing-wmt-ai-performance-report | [EVIDENCIA, reseña de agencia] |
| Métricas | Citas totales, promedio de páginas citadas, *grounding queries* (consultas cortas y temáticas que la IA genera por detrás para recuperar información de la web; **no** son lo que escribe la gente), detalle por URL (frecuencia, no importancia ni posición) | https://www.searchinfluence.com/blog/bing-ai-performance-report-copilot-citations/ ; https://contra.com/p/OWb3MX3B-26-grounding-queries-what-pulls-a-site-into-copilot-answers | [EVIDENCIA, reseñas] |
| Límites | **Sin clics ni tráfico**; sin vínculo entre *grounding query* y cita; datos de muestra ("piso muestreado, no censo"); exportación **solo CSV**; API "en el backlog" según Fabrice Canel (Microsoft) en X, sin plazo | https://momenticmarketing.com/blog/bing-wmt-ai-performance-report ; https://pasqualepillitteri.it/en/news/5220/bing-webmaster-tools-ai-citation-share-geo | [EVIDENCIA]; la frase de Canel llega de segunda mano |
| Novedades de mediados de 2026 | Clasificación por **intención** (Informativa, Comercial, Navegacional, "Learn and Solve", Investigación, Creación y Local); todo sigue en vista previa | un resumen del buscador (no identifiqué el sitio exacto) | [NO VERIFICADO] |

**Calidad:** casi todo viene de blogs de agencias y vendors con datos de uno o pocos sitios (p. ej. "20.000 citas de Copilot" en Search Influence). Anecdótico. El informe es útil como **medición gratuita**, no como prueba de qué funciona.

### 2.2 Qué dice Bing/Microsoft sobre IA y datos estructurados

- **Declaración:** Fabrice Canel (Microsoft) confirmó en SMX Munich (mar-2025) y en un comentario de LinkedIn que **Microsoft usa schema markup para ayudar a sus LLM a entender el contenido**; dijo además que la IA generativa valora el **contenido fresco** y recomendó **IndexNow** (indexnow.org) para avisar de cambios. Fuente: https://searchengineland.com/microsoft-bing-copilot-use-schema-for-its-llms-453455 (fecha de la nota no visible; evento mar-2025). [HECHO por declaración pública, vía prensa]
- **Qué NO dice:** no afirma que el schema aumente las **citas** ni da cifras. Search Engine Land aclara que **no está claro** si Gemini, OpenAI o Perplexity usan schema. [HECHO]
- **Contradicción con T1:** Ahrefs (mayo-2026, citado en T1) no halló aumento causal de citas por agregar JSON-LD; un hilo de WebmasterWorld comenta dos pruebas sin relación schema-citas (https://www.webmasterworld.com/gpt/5133290.htm; foro, no estudio). La lectura coherente es: **Microsoft lo usa para entender, pero eso no está medido como palanca de citación** [OPINIÓN]. Las cifras de blogs ("hasta 30 % más visibilidad") no tienen fuente primaria [NO VERIFICADO].
- **No hallé** documentación oficial de Microsoft sobre Copilot y rastreo (más allá de Bingbot) ni una guía oficial de Bing de AEO/GEO. Pendiente.

---

## 3. Anthropic: Claude-SearchBot y Claude-User (hueco 3)

**Resuelto.** Artículo oficial de ayuda: https://support.claude.com/en/articles/8896518 (también servido en https://support.anthropic.com/en/articles/8896518; el mismo ID aparece en T1 como `...8896518-what-is-claude-bot`). Fecha de publicación/actualización: **no visible**. [HECHO]

| Bot | Función según el artículo | Efecto de bloquearlo (palabras del resumen del buscador, que cita la página) |
|---|---|---|
| **ClaudeBot** | Recopila datos de la web pública para **desarrollo de modelos** (entrenamiento) | Señala que el contenido futuro del sitio se excluya de los conjuntos de entrenamiento |
| **Claude-User** | Recupera contenido **a pedido del usuario** | "Impide que el sistema recupere tu contenido en respuesta a una consulta de usuario", lo que "puede reducir la visibilidad" en búsqueda dirigida por el usuario |
| **Claude-SearchBot** | Analiza contenido en línea para **mejorar la relevancia y exactitud de las respuestas de búsqueda** | Detiene la indexación para búsqueda; "puede reducir la visibilidad en respuestas de búsqueda" |

- Cómo excluirse: regla en `robots.txt` en el directorio raíz, **por subdominio**; el ejemplo oficial bloquea ClaudeBot en todo el sitio. [HECHO]
- La versión alemana del artículo (https://support.claude.com/de/articles/8896518-crawlt-anthropic-daten-aus-dem-web-und-wie-konnen-website-betreiber-den-crawler-blockieren) dice que los bots respetan las señales de "no rastrear" de robots.txt y que admiten `Crawl-delay`. No lo vi en el extracto en inglés. Lo de **no publicar rangos de IP** viene de T1 (sesión anterior) y no lo re-verifiqué aquí.
- Un glosario de terceros (https://geotoolbox.ai/glossary/claudebot) resume lo mismo: bloquear ClaudeBot solo excluye del entrenamiento; las citas dependen de los otros dos. Es lectura secundaria. [OPINIÓN/secundario]
- **Qué queda sin verificar:** si Claude-User respeta robots.txt en la práctica (el artículo dice que los bots respetan robots.txt; no hay auditoría independiente vista) y el token `anthropic-ai` (legado).
- **Implicancia para T1:** la tabla de user-agents (T1 §5.1) y el robots.txt propuesto (§5.2) con Claude-SearchBot y Claude-User en el grupo "permitir" y ClaudeBot en el grupo "entrenamiento" **quedan respaldados**.

---

## 4. Google: Googlebot vs Google-Extended (hueco 4)

Todo llega por **secundarios concordantes** que citan o parafrasean la documentación de rastreadores de Google; no pude abrir la página oficial. [HECHO vía secundarios]

- **Google-Extended es un *token* de producto de robots.txt, no un rastreador**: no llega ninguna petición con ese nombre y no aparece en los logs. Controla si el contenido que **Googlebot ya rastreó** puede usarse para **entrenar modelos de Gemini** y para **grounding** en Gemini Apps y Vertex AI. Fuentes: https://ppc.land/google-extended/ ; https://www.mariehaynes.com/should-you-use-google-extended-in-robots-txt/ ; https://geotoolbox.ai/glossary/google-extended ; https://www.temso.ai/bots/google/google-extended .
- **Cita atribuida a la doc de Google:** el token "no afecta la inclusión de un sitio en Google Search ni se usa como señal de ranking en Google Search". [HECHO, texto citado por un secundario]
- **AI Overviews y AI Mode** forman parte de Search y dependen de **Googlebot**; su elegibilidad se gobierna con el acceso de Googlebot y los controles de snippet (`nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`). [HECHO vía secundarios; coherente con la página "AI features and your website" de T1]
- Regla de oro para robots.txt: `User-agent: Google-Extended` + `Disallow: /` (o por rutas). [HECHO]

**Implicancia para moldey.com:** poner `Google-Extended` en el grupo "entrenamiento" de T1 §5.2 es correcto y **no te saca de AI Overviews**. A la inversa, **permitir** Google-Extended no te mete en AI Overviews. Para ellos solo importan Googlebot y snippet. Y la única forma de "optar por salir" de AI Overviews es limitar snippets, que también degrada tu resultado orgánico: no recomendable. [OPINIÓN]

---

## 5. Cloudflare (hueco 5)

### 5.1 Bloqueo por defecto, Pay Per Crawl, AI Crawl Control

| Hecho | Detalle | Fuente | Etiqueta |
|---|---|---|---|
| Bloqueo por defecto | Desde el **1-jul-2025**, Cloudflare bloquea por defecto los rastreadores de IA conocidos en **todo dominio nuevo**; al dar de alta un sitio se pregunta si se permite el acceso. Más de 1 M de sitios ya lo habían activado por opción desde el otoño anterior | https://alternativeto.net/news/2025/7/cloudflare-blocks-ai-crawlers-by-default-and-launches-pay-per-crawl-for-publishers ; https://www.eweek.com/de/news/cloudflare-blocks-ai-crawlers/ ; https://about.getcoai.com/news/cloudflare-now-blocks-ai-crawlers-by-default-and-launches-pay-per-scrape-program | [HECHO vía prensa] |
| Pay Per Crawl | **Beta privada**; tres opciones por rastreador: permitir, bloquear o cobrar | los mismos | [HECHO vía prensa]. Que use HTTP 402 (T1) **no lo vi** → [NO VERIFICADO] |
| Estado | Las grandes empresas de IA aún no se habían comprometido; sigue en beta (según un resumen) | los mismos | [EVIDENCIA, prensa] |
| Renombre "AI Audit" → "AI Crawl Control" | **No pude confirmarlo** en estos resultados | — | [NO VERIFICADO] |
| **Novedad 15-sep-2026** | Un artículo (título coincidente: "From Pay Per Crawl to Pay Per Use", https://pasqualepillitteri.it/en/news/7205/cloudflare-ai-crawlers-pay-per-use , probable fuente; el resumen no dijo cuál resultado) afirma que, **desde el 15-sep-2026**, la configuración por defecto bloquearía rastreadores que **combinan búsqueda, entrenamiento y agente** en páginas **con anuncios**, salvo que el sitio decida otra cosa; anunciado entre el 1 y 2-jul-2026 | ídem | **[NO VERIFICADO]**: una sola fuente, no vi el anuncio de Cloudflare. Alcance exacto (¿afecta a Googlebot?) desconocido. Para moldey.com solo importaría si usa Cloudflare **y** muestra anuncios. |

### 5.2 Content Signals Policy (sintaxis)

Fuentes: blog oficial de Cloudflare https://blog.cloudflare.com/content-signals-policy/?tab=suite (misma página que otras variantes de URL con parámetros en los resultados); docs oficiales https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/index.md ; cobertura https://www.searchengineworld.com/cloudflare-enters-the-robots-txt-fray-with-a-content-signals-policy-for-ai-bots , https://citationcult.beehiiv.com/p/cloudflare-s-new-content-signals-an-ai-era-glow-up-for-robots-txt . **Fecha de lanzamiento: no visible** en los resultados (T1 recordaba septiembre 2025: **[NO VERIFICADO]**, sin contradicción).

**Sintaxis [HECHO vía resumen de docs/blog de Cloudflare]:**
- Una sola línea `Content-Signal:` con pares `clave=valor` separados por coma, dentro de un grupo `User-agent`. Ejemplo de Cloudflare:
  ```
  User-agent: *
  Content-Signal: search=yes, ai-train=no
  Allow: /
  ```
- **Tres señales:**
  - `search`: construir un índice de búsqueda y mostrar resultados de búsqueda; **no incluye** resúmenes generados por IA.
  - `ai-input`: usar el contenido como entrada de modelos de IA (RAG, grounding, recuperación en tiempo real).
  - `ai-train`: entrenar o ajustar modelos de IA.
- **Omitir una señal no significa "no":** solo que no se expresó preferencia.
- **robots.txt administrado de Cloudflare:** para clientes que lo usan, Cloudflare actualiza el robots.txt para incluir `search=yes, ai-train=no` y **no emite `ai-input`** (no quiere adivinar la preferencia). Más de **3,8 M de dominios** en ese servicio.
- **Límites:** es **declarativo**, sin fuerza legal; los rastreadores ignoran el bloque de comentarios; según el comentarista, empresas influyentes como Google no se habrían comprometido a respetarlo (resumen, no verificado en fuente primaria).

**Compatibilidad con T1:** la línea sugerida en T1 (`Content-Signal: search=yes, ai-input=yes, ai-train=no`) es **sintácticamente válida**. Nota nueva: como `search` excluye los resúmenes de IA y `ai-input` cubre grounding/RAG, un `ai-input=no` podría leerse como oposición al uso en respuestas de IA; conviene `ai-input=yes` si querés citaciones. [OPINIÓN, interpretación de las definiciones]

---

## 6. Guía de Google del 15-may-2026 y el tema idiomas/traducción (hueco 6)

- **Confirmado [HECHO]:** Google publicó el 15-may-2026 "Optimizing your website for generative AI features on Google Search"; anuncio oficial en el blog de Search Central: https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing (visto como resultado, sin poder abrirlo). Según el resumen del anuncio, las secciones son: contenido valioso "no commodity"; consejos para contenido **local, de compras, de imágenes y de video**; desmitificación de afirmaciones sobre AEO/GEO; **orientación inicial sobre agentes de IA**; y por qué las buenas prácticas de SEO siguen valiendo.
- **Idiomas/traducción: no apareció.** Ningún resultado describe orientación sobre páginas traducidas, localización, traducción automática ni hreflang. Lo "local" del anuncio podría referirse a búsqueda local, no a idioma (no verificado). Coberturas de la guía vistas: https://ppc.land/googles-new-guide-for-ai-search-what-seo-really-needs-now/ ; https://www.seo-day.de/news/article/google-publishes-guide-to-optimizing-for-generative-ai?lang=en ; https://gigazine.net/gsc_news/en/20260518-google-guide-optimizing-generative-ai ; https://elevarus.com/google-generative-ai-features-guide-may-2026/ ; https://www.seoteric.com/optimizing-websites-for-googles-generative-ai-search-features/ .
- **Corroborado por secundario:** la guía desaconseja llms.txt, marcado especial y "chunking" (seoteric.com).
- **Conclusión:** **no puedo afirmar que la guía diga algo sobre idiomas.** Las reglas sobre traducción automática sin revisión humana (contenido a escala sin valor) son de las **políticas de spam de Google**, no de esta guía, y siguen [NO VERIFICADO en esta pasada]. T1 §9 ya lo marcaba así.
- Resultados no relacionados vistos: localización automática de campañas en Google Ads; no aplican.

---

## 7. Perplexity-User / ChatGPT-User y robots.txt (hueco 7)

| Bot | Qué se sabe | Fuente | Etiqueta |
|---|---|---|---|
| **Perplexity-User** | Guías de terceros dicen que, según la documentación de Perplexity, es un *fetcher* pedido por el usuario que **generalmente ignora robots.txt** porque la petición es "iniciada por el usuario". No vi la página oficial en estos resultados | https://www.trakkr.ai/bots/perplexity-user ; https://siteline.ai/ai-agent-directory/perplexity-user | [NO VERIFICADO] como cita oficial; plausible |
| **Postura de Perplexity (ago-2025)** | Perplexity sostuvo que los asistentes iniciados por el usuario no deberían estar sujetos a las mismas restricciones que los rastreadores | https://rightstech.com/2025/08/perplexity-says-cloudflare-is-blocking-legitimate-ai-assistants/ | [HECHO] como postura de la empresa, vía prensa |
| **Acusación de Cloudflare (ago-2025)** | Al ser bloqueado, Perplexity usaría además un agente **genérico que imita a Chrome en macOS**, con IPs y ASN rotativos y no declarados; Cloudflare lo quitó de su lista de bots verificados | https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ ; https://the-decoder.com/cloudflare-accuses-perplexity-of-secretly-crawling-sites-despite-explicit-blocks/ ; https://tech.co/news/cloudflare-perplexity-bots-ignore-no-crawl-directives | [HECHO] que Cloudflare lo afirmó; **disputado** |
| **Respuesta de Perplexity** | Lo llamó "publicity stunt"; sugirió que el tráfico era de un servicio de navegador en la nube de terceros (BrowserBase, por una fuente alemana: https://www.computerwoche.de/article/4035827/umgeht-perplexity-gezielt-web-sperren.html ; no confirmado en inglés) | tech.co, computerwoche | [HECHO] como respuesta; contenido [NO VERIFICADO] |
| **ChatGPT-User** | En la prueba de Cloudflare, **sí leyó robots.txt y dejó de rastrear** cuando se lo bloqueó. La frase de OpenAI de que las reglas "pueden no aplicar" viene de T1 (sesión anterior); **no la re-confirmé** | https://the-decoder.com/cloudflare-accuses-perplexity-of-secretly-crawling-sites-despite-explicit-blocks/ | [EVIDENCIA, test de Cloudflare] |

**Lectura:** hay una **contradicción abierta** (docs de OpenAI que advierten que robots.txt puede no aplicar a ChatGPT-User vs la prueba de Cloudflare en que sí obedeció). Lo robusto para decidir: **no confiar en robots.txt para los fetchers iniciados por usuario**; proteger contenido de pago con acceso. [OPINIÓN]

---

## 8. Estado de los pendientes de T1 §13 (mi alcance)

| # T1 | Pendiente | Estado | Nota |
|---|---|---|---|
| 1 | Texto original guía Google 15-may-2026 (llms.txt, schema, idiomas) | **Parcial** | Fecha, título y secciones confirmadas por el blog oficial (vía resultado). Idiomas/traducción: no apareció. Texto original sigue sin leerse. |
| 2 | Docs oficiales Anthropic (Claude-SearchBot/Claude-User) | **Resuelto** | §3 |
| 2 | Microsoft (Copilot, Bing, AI Performance) | **Parcial** | AI Performance existe (vía terceros); declaración de Canel sobre schema; **sin doc oficial de Microsoft**. |
| 2 | Apple, Meta, xAI, DeepSeek | **Sin tocar** | Fuera de mi alcance |
| 3 | Estudios multilingües / sesgo al inglés / idiomas de pocos recursos | **Parcial** | §1; vendors y preprints; nada de e-commerce. |
| 4 | Datos de citación en e-commerce/productos digitales | **Sin tocar** | No era de mi alcance |
| 5 | Cloudflare (fechas y detalles) | **Parcial** | Bloqueo por defecto 1-jul-2025 y sintaxis de Content Signals OK; fecha de Content Signals y renombre "AI Crawl Control" sin confirmar; novedad 15-sep-2026 sin verificar. |
| 6 | Herramientas de medición | **Sin tocar** | Salvo Bing AI Performance |
| 7 | Perplexity-User / ChatGPT-User | **Parcial** | §7; contradicción abierta. |
| 9 | Cambios entre junio y octubre de 2026 | **Parcial** | Aparecieron cosas de mediados de 2026 (Intents en BWT; 15-sep-2026 de Cloudflare; SEJ sobre idiomas de AI Mode) todas sin confirmar a nivel primario. |

**Cambios concretos a T1 (para quien fusione):**
- §2, fila Anthropic: Claude-SearchBot y Claude-User pasan a **[HECHO]** con URL oficial (https://support.claude.com/en/articles/8896518).
- §5.1: fila "Claude-SearchBot, Claude-User" a **[HECHO]**; fila "Google-Extended" a **[HECHO vía secundarios concordantes]**, con la aclaración de que es un token y no un rastreador, y que AI Overviews/AI Mode dependen de Googlebot y snippet.
- §5.3: Cloudflare, bloqueo por defecto **1-jul-2025** [HECHO vía prensa]; sintaxis y tres señales de Content Signals [HECHO vía resumen de docs]; quitar o marcar como no verificado "AI Crawl Control (antes AI Audit)" y el "HTTP 402"; agregar la advertencia sobre el 15-sep-2026.
- §6.1: Bing Webmaster Tools "AI Performance" existe (vista previa, feb-2026); medición gratuita sin clics.
- §9 (multilingüe): reemplazar "no pude obtener evidencia" por la tabla de §1 de este informe, con las salvedades de calidad.
- §2, fila Microsoft: agregar declaración de Canel (schema, frescura, IndexNow).

---

## 9. Qué hacer en moldey.com

Escala: Impacto A/M/B × Esfuerzo A/M/B.

| # | Acción | Impacto | Esfuerzo | Base |
|---|---|---|---|---|
| 1 | **Mantener separados en robots.txt los tres grupos** (búsqueda/usuario permitidos; entrenamiento a decisión): Claude-SearchBot y Claude-User en "permitir", ClaudeBot/GPTBot/Google-Extended en "entrenamiento". Ya está en el esquema de T1 §5.2. | A | B | Anthropic (oficial), Google-Extended (secundarios concordantes) |
| 2 | **Si usás Cloudflare:** revisar el panel de bots de IA y el robots.txt administrado; confirmar que **OAI-SearchBot, PerplexityBot, Claude-SearchBot, Bingbot y Googlebot no están bloqueados** (dominios nuevos desde el 1-jul-2025 pueden venir bloqueados por defecto). Verificar en el blog de Cloudflare el cambio del 15-sep-2026 solo si mostrás anuncios. | A | B | Cloudflare (prensa) |
| 3 | **Publicar páginas en el idioma de cada mercado** (no depender de páginas en inglés para consultas en español/portugués): los AI Overviews tienden a citar fuentes en el idioma local en idiomas grandes. Empezar por ES y PT-BR, que están en AI Mode. | A | M-A | Temso/Weglot (vendors) + lógica de búsqueda clásica |
| 4 | **Ordenar la expansión de idiomas con la cobertura de AI Mode** como criterio secundario: ES, PT-BR, HI, ID, JA, KO y los 7 idiomas de India ya están en AI Mode; los demás no tienen confirmación. Antes de un idioma de pocos recursos, correr el protocolo de prompts de T1 §6.3 y anotar si el AI Overview aparece y cita. | M | M | TechCrunch/SEL; preprints sobre idiomas de pocos recursos |
| 5 | **Revisión nativa de las páginas de mayor valor** antes de publicarlas; evitar traducción automática masiva sin revisión. | A | M | T1 §9; políticas de spam de Google [NO VERIFICADO en esta pasada] |
| 6 | **Verificar el sitio en Bing Webmaster Tools** (se puede importar desde Search Console) y mirar **AI Performance** mensualmente: citas y *grounding queries* (ideas de long-tail). Recordar que no hay clics ni tráfico. | M | B | Reseñas de terceros; Canel |
| 7 | **IndexNow** para notificar altas y cambios de fichas. | M | B | Canel (declaración) |
| 8 | **Content Signals** en robots.txt: `Content-Signal: search=yes, ai-input=yes, ai-train=no` (válido; efecto voluntario). | B | B | Cloudflare (docs vía resumen) |
| 9 | **Proteger PDF/DXF de pago por acceso**, no por robots.txt, porque los fetchers iniciados por usuario (Perplexity-User, posiblemente ChatGPT-User) pueden no respetar robots.txt. | A | M | Perplexity (postura) / Cloudflare (disputado) / T1 §5.2 |
| 10 | **Mantener schema `Product`/`Offer`/`Organization`** por SEO clásico y claridad de entidad (Microsoft dice que lo usa para entender; Ahrefs no ve efecto en citas). | M | B | Canel; Ahrefs (T1) |
| 11 | **Agregar al protocolo de medición** (T1 §6.3) las columnas "idioma de la consulta" e "idioma de la fuente citada", y si el AI Overview/AI Mode apareció en ese idioma y país. | M | B | Hallazgos de §1 |

## 10. Qué NO hacer

- No creer que bloquear `Google-Extended` te saca de AI Overviews (ni que permitirlo te mete): dependen de Googlebot y snippet.
- No usar `nosnippet`/bloquear Googlebot para "salir" de las respuestas de IA: degrada tu resultado orgánico.
- No planificar con las cifras de Temso (85,4 %) o Weglot (96 %) como si fueran hechos: son de vendors y de metodología poco clara.
- No asumir que una página en inglés sirve para consultas en otros idiomas, ni que los idiomas de pocos recursos "funcionan igual" en IA: la evidencia (preprints) indica menos fuentes y más sesgo al inglés.
- No activar a ciegas el bloqueo de bots de IA de Cloudflare ni dejar el valor por defecto sin revisar.
- No interpretar AI Performance de Bing como tráfico: es una muestra de citas, sin clics.
- No confiar en robots.txt para fetchers iniciados por usuario ni para proteger archivos de pago.
- No tratar el titular "AI Mode escala más rápido entre idiomas" como evidencia hasta leer el contenido.

---

## 11. Fuentes vistas en esta pasada (todas aparecieron en resultados)

**Multilingüe:** https://www.temso.ai/data/-Lost-in-Translation-How-AI-Models-Handle-Local-Language-Sources · https://www.weglot.com/blog/ai-search-and-language · https://arxiv.org/pdf/2609.00319 · https://arxiv.org/pdf/2605.22785 · https://www.alphaxiv.org/abs/2509.13930v2 · https://hub.jhu.edu/2025/09/02/multilingual-artificial-intelligence-often-reinforces-bias/ · https://www.labmanager.com/google-scholar-shows-bias-against-non-english-papers-25165 · https://techcrunch.com/2024/12/20/google-is-expanding-geminis-in-depth-research-mode-to-40-languages
**AI Mode idiomas:** https://searchengineland.com/google-expands-ai-mode-beyond-english-461680 · https://techcrunch.com/2025/10/08/googles-search-live-comes-to-india-ai-mode-gets-more-languages · https://www.maginative.com/article/google-expands-ai-mode-in-search-to-five-new-languages/ · https://www.neowin.net/news/googles-ai-mode-finally-available-for-non-english-users-starting-with-these-languages/ · https://www.folio3.ai/ai-pulse/google-ai-mode-expands-spanish-speakers-globally · https://www.searchenginejournal.com/google-says-ai-mode-can-now-scale-faster-across-languages/575791/
**Microsoft:** https://www.searchinfluence.com/blog/bing-ai-performance-report-copilot-citations/ · https://momenticmarketing.com/blog/bing-wmt-ai-performance-report · https://previsible.io/seo-ai-news/bing-ai-performance-report/ · https://pasqualepillitteri.it/en/news/5220/bing-webmaster-tools-ai-citation-share-geo · https://contra.com/p/OWb3MX3B-26-grounding-queries-what-pulls-a-site-into-copilot-answers · https://searchengineland.com/microsoft-bing-copilot-use-schema-for-its-llms-453455 · https://www.webmasterworld.com/gpt/5133290.htm
**Anthropic:** https://support.claude.com/en/articles/8896518 · https://support.anthropic.com/en/articles/8896518 · https://support.claude.com/de/articles/8896518-crawlt-anthropic-daten-aus-dem-web-und-wie-konnen-website-betreiber-den-crawler-blockieren · https://geotoolbox.ai/glossary/claudebot
**Google-Extended:** https://ppc.land/google-extended/ · https://www.mariehaynes.com/should-you-use-google-extended-in-robots-txt/ · https://geotoolbox.ai/glossary/google-extended · https://www.temso.ai/bots/google/google-extended
**Cloudflare:** https://alternativeto.net/news/2025/7/cloudflare-blocks-ai-crawlers-by-default-and-launches-pay-per-crawl-for-publishers · https://www.eweek.com/de/news/cloudflare-blocks-ai-crawlers/ · https://about.getcoai.com/news/cloudflare-now-blocks-ai-crawlers-by-default-and-launches-pay-per-scrape-program · https://pasqualepillitteri.it/en/news/7205/cloudflare-ai-crawlers-pay-per-use · https://blog.cloudflare.com/content-signals-policy/?tab=suite · https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/index.md · https://www.searchengineworld.com/cloudflare-enters-the-robots-txt-fray-with-a-content-signals-policy-for-ai-bots · https://citationcult.beehiiv.com/p/cloudflare-s-new-content-signals-an-ai-era-glow-up-for-robots-txt
**Guía Google 15-may-2026:** https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing · https://ppc.land/googles-new-guide-for-ai-search-what-seo-really-needs-now/ · https://www.seo-day.de/news/article/google-publishes-guide-to-optimizing-for-generative-ai?lang=en · https://gigazine.net/gsc_news/en/20260518-google-guide-optimizing-generative-ai · https://elevarus.com/google-generative-ai-features-guide-may-2026/ · https://www.seoteric.com/optimizing-websites-for-googles-generative-ai-search-features/
**Perplexity / ChatGPT-User:** https://www.trakkr.ai/bots/perplexity-user · https://siteline.ai/ai-agent-directory/perplexity-user · https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ · https://the-decoder.com/cloudflare-accuses-perplexity-of-secretly-crawling-sites-despite-explicit-blocks/ · https://tech.co/news/cloudflare-perplexity-bots-ignore-no-crawl-directives · https://rightstech.com/2025/08/perplexity-says-cloudflare-is-blocking-legitimate-ai-assistants/ · https://www.computerwoche.de/article/4035827/umgeht-perplexity-gezielt-web-sperren.html
