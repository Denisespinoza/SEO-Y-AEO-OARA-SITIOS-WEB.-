# T1 — AEO / GEO / LLMO en 2025–2026: cómo los motores de respuesta con IA encuentran, seleccionan y citan fuentes

**Fecha del informe:** 12 de octubre de 2026. **Destino práctico:** moldey.com (moldes digitales de costura, PDF A4/Letter/A0, DXF/vectoriales, plantillas para sublimar; venta global, multi-idioma por etapas).

## 0. Limitaciones de esta investigación (leer primero)

- **WebFetch no funcionó** (error DNS), así que no pude abrir páginas primarias. Todo lo que cito de Google, OpenAI, Perplexity, Anthropic y de los estudios lo vi **a través de resultados de WebSearch** (resúmenes + títulos/URLs). Por eso, cuando una cifra llegó por un medio secundario, lo marco.
- **El presupuesto de búsquedas del turno se agotó** (límite de 200 compartido entre todos los agentes) tras unas 20 búsquedas útiles, antes de cubrir bien los puntos 5 (herramientas), 6 (entidades), 8 (multilingüe) y 9 (riesgos), y el detalle de la lista de user-agents y de Cloudflare. En esas secciones **no tengo fuentes de esta sesión**: lo que escribo viene de conocimiento previo del modelo y lo marco como **[NO VERIFICADO]** (no inventé URLs ni cifras para cubrir el hueco). Al final hay una lista de "pendientes de verificar".
- No vi nada posterior a ~junio de 2026 (el dato más reciente es Similarweb, mayo de 2026). Entre junio y octubre de 2026 pudo cambiar algo.
- Muchas fuentes son blogs de proveedores de herramientas de visibilidad en IA (con interés comercial). Los resúmenes del buscador son generados automáticamente y a veces se contradicen entre sí en fechas y cifras; lo señalo donde pasó.

Etiquetas: **[HECHO]** = documentado por la plataforma/fuente primaria (visto vía resultados); **[EVIDENCIA]** = estudio de terceros con metodología; **[OPINIÓN]** = consejo de industria sin prueba; **[NO VERIFICADO]**.

---

## 1. Resumen ejecutivo (10 líneas)

1. **Google dice que AEO/GEO "sigue siendo SEO".** El 15 de mayo de 2026 publicó su primera guía oficial de optimización para funciones generativas y desaconseja explícitamente llms.txt, "chunking", reescritura para IA y schema especial. [HECHO, vía resúmenes]
2. **Para Google, el requisito técnico es: estar indexado y ser elegible para snippet.** No hay marcado ni archivo especial. [HECHO, vía resúmenes]
3. **Las IA no son un solo sistema.** ChatGPT, Perplexity, Copilot, Gemini, Claude y los AI Overviews/AI Mode usan índices, rastreadores y reglas distintas; los resultados de uno no se extrapolan a otro. [EVIDENCIA]
4. **Ranking top-10 ≠ citación.** Ahrefs midió (marzo 2026) que solo ~38 % de las citas de AI Overviews salen de páginas top-10 (era 76 % en julio 2025; cambio de metodología posible). [EVIDENCIA, vía secundarios]
5. **Las señales fuera de tu sitio pesan mucho:** menciones de marca web (correlación 0,664 con presencia en AI Overviews) y plataformas ajenas (Reddit, Wikipedia, YouTube, LinkedIn) acaparan citas. Es correlación. [EVIDENCIA]
6. **llms.txt: sin evidencia de efecto.** Ningún gran proveedor lo documenta; estudios de logs muestran que casi no lo leen; SE Ranking (~300 k dominios) no halló relación. [HECHO + EVIDENCIA]
7. **Schema no mueve las citas** en el mayor experimento controlado visto (Ahrefs, 1.885 páginas); sirve para SEO clásico/rich results. [EVIDENCIA]
8. **Estructura:** ~44 % de las citas de ChatGPT salen del primer 30 % de la página (un solo estudio, Kevin Indig); páginas enfocadas > "guía definitiva". [EVIDENCIA, solidez media-baja]
9. **Robots.txt:** separar entrenamiento / búsqueda / acción del usuario es posible en OpenAI, Anthropic y Perplexity. Se puede estar en búsqueda de IA y bloquear entrenamiento. Pero **robots.txt no protege archivos de pago**; eso lo hace el control de acceso. [HECHO + OPINIÓN]
10. **Para un sitio nuevo y chico, la palanca realista** es contenido original y específico (long-tail de costura), HTML rastreable, presencia real en YouTube/Reddit/Pinterest y medición manual barata; no herramientas caras ni trucos.

---

## 2. Qué dicen las propias plataformas

| Plataforma | Qué dice (fuente) | Qué exige/recomienda | Etiqueta |
|---|---|---|---|
| **Google (AI Overviews y AI Mode)** | Página "AI features and your website": ambos muestran enlaces; usan **query fan-out** (varias búsquedas relacionadas por subtemas); pueden usar modelos distintos, por lo que los enlaces varían entre AI Overviews y AI Mode; los AI Overviews solo aparecen cuando Google los considera aditivos. https://developers.google.com/search/docs/appearance/ai-features | Estar indexado y ser elegible para snippet (según resumen de terceros de la misma página). | [HECHO] vía resumen del buscador |
| **Google, guía de mayo 2026** | "Optimizing your website for generative AI features on Google Search", publicada el **15-may-2026**, sección "Generative AI fundamentals". https://developers.google.com/search/docs/fundamentals/ai-optimization-guide. Cobertura: https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/ , https://www.semrush.com/blog/google-publishes-generative-ai-search-guide/ , https://searchengineland.com/google-publishes-guide-on-optimizing-for-generative-ai-features-477671 | Dice que AEO y GEO son términos usados para visibilidad en IA, pero "optimizar para búsqueda generativa es optimizar para la experiencia de búsqueda, y por lo tanto sigue siendo SEO". Las funciones de IA están "arraigadas en los sistemas centrales de ranking y calidad" y usan RAG + fan-out sobre el índice de Search. Sección "mitos": **no hacen falta llms.txt, chunking, reescritura específica para IA ni schema especial**; menciona las menciones de marca "inauténticas" como táctica inútil. Prioriza contenido **"no commodity"**: conocimiento y experiencia propios, no rehacer lo que ya está online o lo que un modelo produciría fácil. Recomienda evaluar servicios AEO/GEO de terceros con sus pautas sobre asesoría SEO de terceros. | [HECHO] vía varios resúmenes concordantes; no pude leer el texto original |
| **Google, declaraciones previas** | Gary Illyes (Search Central Live Deep Dive Asia-Pacific; una fuente lo fecha en **julio 2025**): Google no soporta llms.txt ni planea hacerlo; para AI Overviews basta SEO normal. https://searchengineland.com/google-says-normal-seo-works-for-ranking-in-ai-overviews-and-llms-txt-wont-be-used-459422 . John Mueller (Reddit): llms.txt "puramente especulativo", comparable a la meta keywords. | — | [HECHO] declaraciones públicas, vía prensa |
| **OpenAI** | Documento "Overview of OpenAI Crawlers": **OAI-SearchBot** (aparecer en la búsqueda de ChatGPT), **GPTBot** (entrenamiento), **ChatGPT-User** (acciones iniciadas por usuario; las reglas de robots.txt "pueden no aplicar"; no se usa para decidir aparición en Search). Se controlan por separado; los cambios tardan ~24 h en reflejarse en búsqueda. Sitios que bloquean OAI-SearchBot no se muestran en respuestas de ChatGPT search, aunque pueden aparecer como enlaces de navegación. https://developers.openai.com/api/docs/bots | Para aparecer en ChatGPT search: permitir OAI-SearchBot. | [HECHO] vía resultado del buscador |
| **Perplexity** | Docs de crawlers: **PerplexityBot** (índice; recomiendan permitirlo para aparecer en resultados; publican UA e IPs en perplexity.com/perplexitybot.json) y **Perplexity-User** (lectura puntual cuando el usuario pregunta; no se usa para crawling ni entrenamiento). Cada ajuste es independiente; ~24 h de demora. https://docs.perplexity.ai/docs/resources/perplexity-crawlers.md | Permitir PerplexityBot. Varias guías de terceros dicen que Perplexity-User "generalmente ignora robots.txt" por ser acción del usuario; el extracto oficial que vi no lo confirma. | [HECHO] (roles) / [NO VERIFICADO] (que ignore robots.txt) |
| **Anthropic** | Artículo de soporte oficial: **ClaudeBot** respeta robots.txt (y Crawl-delay); para excluirse se pone `User-agent: ClaudeBot / Disallow: /` en cada subdominio; **Anthropic no publica rangos IP**, bloquear por IP no es fiable. https://support.claude.com/en/articles/8896518-what-is-claude-bot . **Claude-SearchBot** (indexa para mejorar relevancia de la búsqueda de Claude) y **Claude-User** (fetch a pedido del usuario) aparecen en directorios de terceros, p. ej. https://siteline.ai/ai-agent-directory/claude-searchbot/ ; su documentación oficial no apareció en mis resultados. | Permitir Claude-SearchBot/Claude-User si querés citas en Claude con web search; bloquear ClaudeBot no afectaría la citación (según una fuente secundaria). | [HECHO] (ClaudeBot) / [NO VERIFICADO] (los otros dos, solo terceros) |
| **Microsoft (Copilot/Bing)** | No obtuve fuente en esta sesión. | — | [NO VERIFICADO] |
| **Meta AI, Grok, DeepSeek, Apple/Siri, Gemini app** | No obtuve fuente en esta sesión. | — | [NO VERIFICADO] |

**Lectura crítica:** que Google diga "es solo SEO" es literalmente cierto para *Google*. Comentaristas señalan que la guía es incompleta para ChatGPT, Perplexity, Copilot y Claude, que no comparten su índice (https://www.paz.ai/blog/google-ai-search-optimization-guide-still-seo-incomplete) [OPINIÓN]. Además, Google tiene incentivo en desalentar la industria de "GEO". Aun así, los estudios de la sección 3 son coherentes con la idea de que lo que hace bien a un sitio en búsqueda clásica correlaciona con ser citado.

---

## 3. Estudios 2025–2026 sobre qué se cita

### 3.1 Cuadro resumen con solidez

| Hallazgo | Cifra | Fuente (URL, fecha) | Solidez |
|---|---|---|---|
| Citas de AI Overviews provenientes de páginas top-10 | ~38 % (marzo 2026) vs 76 % (julio 2025). 863 k SERPs, ~4 M URLs. Rango 11–100: 26,2 %; fuera del top-100: 36,7 %. Con solo listados orgánicos estrictos: 37,1 %. | Ahrefs, 2-mar-2026, vía https://news.designrush.com/ai-overview-citations-drop-ahrefs y https://almcorp.com/blog/google-ai-overview-citations-drop-top-ranking-pages-2026/ (el post original: https://ahrefs.com/blog/search-rankings-ai-citations , solo vi el título) | Media. Muestra grande, pero la caída puede deberse a cambios en Google, cobertura o **parseo** (los secundarios lo advierten). |
| Solape top-10 en otras plataformas | BrightEdge ~17 % (estable); Ahrefs ago-2025, asistentes conversacionales ~12 %, Perplexity ~28,6 % | Citados en los mismos secundarios | Baja-media (secundarios; metodologías distintas) |
| Menciones de marca web vs presencia en AI Overviews | Correlación **0,664** (menciones web de marca), 0,527 (anchors de marca), 0,392 (volumen de búsqueda de marca); 75 k marcas con DR>40; ~26 % tenían cero menciones | Ahrefs https://ahrefs.com/blog/ai-overview-brand-correlation/ (fecha no visible en el resultado) | Media. Correlacional, filtro DR>40 (marcas ya establecidas). |
| Factores en citas de ChatGPT | 129 k dominios, 216.524 páginas, 20 nichos. **Dominios de referencia** = predictor más fuerte (pocos <2.500 dominios: 1,6–1,8 citas de media; >350 k: 8,4; salto cerca de 32 k). La confianza a nivel dominio pesa más que a nivel página. Dominios .gov/.edu no superaron a los comerciales (3,2 vs 4,0). Peso del largo del contenido ~0,06 y de frescura ~0,018 (tabla de SE Ranking, según resumen). | SE Ranking vía https://www.searchenginejournal.com/new-data-top-factors-influencing-chatgpt-citations/561954/ (fecha no visible) | Media. Correlacional; vendor. |
| AI Mode | "Tráfico global del dominio pesa ~3x más que el contenido" | SE Ranking, https://seranking.com/blog/how-to-optimize-for-ai-mode/ (solo título visto) | Baja (solo título/resumen) |
| Posición dentro de la página (ChatGPT) | **44,2 %** de citas del primer 30 % del contenido; 31,1 % del medio; 24,7 % del último tercio. Dentro del párrafo: 53 % del medio, 24,5 % primera oración, 22,5 % última. 1,2 M respuestas / 18.012 citas verificadas. | Kevin Indig, https://searchengineland.com/chatgpt-citations-content-study-469483 | Media-baja: un analista, solo ChatGPT; un post social menciona otra muestra (3 M respuestas/30 M citas), hay discrepancia de tamaños. |
| Foco vs "guía definitiva" | 815 k pares consulta-página: la "ultimate guide" rinde peor que una página enfocada más corta | https://www.growth-memo.com/p/shorter-focused-content-wins-in-chatgpt | Media-baja (parcialmente de pago; solo resumen) |
| Frescura | 17 M de citas. ChatGPT cita contenido más reciente (edad media ~958 días); Perplexity ~1.166; **Google AI Overviews ~1.432 días** (cerca del orgánico) | Ahrefs, 28-jul-2025, https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/ | Media-alta para "varía por plataforma". Cifras como "3,2x más citas si se actualizó en 30 días" o "76,4 % actualizado en 30 días" vienen de blogs secundarios y **no coinciden** con el estudio: tratar como no verificadas. |
| Schema/JSON-LD | 1.885 páginas que agregaron JSON-LD (ago-2025 a mar-2026) vs 4.000 de control: **sin aumento significativo** en AI Overviews (−4,6 %, significativo), AI Mode (+2,4 %), ChatGPT (+2,2 %). Páginas citadas tenían ~3x más JSON-LD, pero no es causal. | Ahrefs, mayo 2026, https://ahrefs.com/blog/schema-ai-citations/ | Media-alta (con grupo de control; los propios autores advierten tendencias previas). Contradicción parcial: Otterly (dic-2025 a mar-2026) vio aumentos solo en AI Mode y AI Overviews, y lo atribuye a elegibilidad de funciones SERP: https://otterly.ai/blog/schema-markup-real-impact-ai-search/ . Afirmaciones tipo "FAQ schema +200 %" son de proveedores **sin diseño controlado**. |
| Estadísticas, citas y fuentes en el texto | Hasta **+40 %** de visibilidad en respuestas generativas (Princeton/Georgia Tech/AI2/IIT Delhi, KDD 2024, arXiv 2311.09735; GEO-bench ~10.000 consultas) | https://collaborate.princeton.edu/en/publications/geo-generative-engine-optimization/ ; resumen: https://everything-pr.com/we-found-the-paper-that-launched-geo-heres-whats-actually-in-it/ ; crítica metodológica: https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique (no la leí) | Media-baja para hoy: es **2023–2024**, con motores generativos de laboratorio, y otras cifras que circulan (22–41 %, +115 % en posición 5) **no las pude confirmar**. |
| Efecto en clics (Google) | Seer: caída de CTR orgánico de ~61 % en consultas con AI Overview. En consultas informativas: CTR 2,07 % si tu marca está citada vs 0,94 % si no vs 3,35 % sin AIO. Seer advierte que **no se puede probar causalidad** (marcas fuertes se citan más y ya tenían más CTR). | https://seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update ; https://ppc.land/google-ai-overviews-reduce-organic-ctr-61-paid-traffic-68/ | Media (cifras vía secundarios; períodos distintos entre fuentes). Un resumen dice que la caída fuerte de 2025 no continuó al mismo ritmo a inicios de 2026. |

### 3.2 Qué tipo de sitios se cita (Reddit, YouTube, Wikipedia, marcas)

Los números **no coinciden** entre estudios, porque miden cosas distintas (porcentaje de todas las citas vs participación dentro del top-10 de fuentes, plataformas y fechas diferentes):

- **Profound** (agosto 2024 a fines de octubre 2025): Reddit es el dominio más citado en conjunto (3,11 % de citas), Wikipedia 1,35 %. En ChatGPT, Wikipedia es la más citada (7,8 % de las citas en un análisis anterior; 47,9 % del top-10 de fuentes), Reddit 11,3 % del top-10. En Perplexity Reddit 6,6 % (46,7 % del top-10); en AI Overviews Reddit 2,2 % (21 % del top-10). https://www.tryprofound.com/blog/ai-platform-citation-patterns , https://www.tryprofound.com/blog/the-data-on-reddit-and-ai-search [EVIDENCIA, vendor, cifras vía resumen]
- **Similarweb** (ene–feb 2026): en ChatGPT Wikipedia 13,15 % y Reddit 11,97 % (reportado en resultados secundarios; no verifiqué el original). [EVIDENCIA, vía secundario]
- **Peec AI** (30 M de fuentes): Reddit primero; luego YouTube, LinkedIn, Wikipedia, Forbes. https://almcorp.com/blog/top-domains-cited-by-ai-search/ [EVIDENCIA, vendor]
- **Semrush** (325 k prompts, ene–feb 2026): LinkedIn citada en 14,3 % de respuestas de ChatGPT Search, 13,5 % de AI Mode, 5,3 % de Perplexity, solo detrás de Reddit; no cubre AI Overviews. https://almcorp.com/blog/linkedin-ai-search-citations-2026/ . Estudio previo de 3 meses (jul–oct 2025, 100 M+ citas): en ChatGPT crecieron YouTube, Reddit y Facebook; cayeron Medium, Quora y LinkedIn (que luego subió en 2026). https://www.semrush.com/blog/most-cited-domains-ai/ [EVIDENCIA, vendor]
- **Mención ≠ cita:** en el estudio de manufactura de Semrush (ene–jul 2026, ChatGPT, Gemini, AI Mode, AI Overviews), de los 15 dominios principales por cada métrica **solo dos** aparecen en ambas listas (más mencionados vs más citados). https://www.semrush.com/blog/manufacturing-seo-ai-search/ [EVIDENCIA]
- Un agregador afirma que Reddit superó a Wikipedia en ChatGPT hacia julio de 2026: **[NO VERIFICADO]**.

**Conclusiones defendibles:** (a) la citación está **concentrada** en un conjunto pequeño de dominios de alta autoridad y UGC (ChatGPT cita "un pequeño grupo de dominios": https://searchengineland.com/chatgpt-citations-domains-study-472349 ); (b) la mezcla cambia por plataforma y por mes; (c) **las marcas/tiendas chicas aparecen poco**, así que la vía para un sitio como moldey.com suele ser la **cola larga** y la **presencia en las plataformas que sí se citan**. No encontré en esta sesión un desglose específico para e-commerce ni para "productos digitales / costura": **[NO VERIFICADO]**; hay que medirlo (protocolo en sección 6).

### 3.3 Cuota de tráfico real de la IA

- Similarweb: la IA generativa promedió **9,5 mil millones de visitas web mensuales** en el año a mayo de 2026 (+57 % en visitantes únicos vs +2 % de búsqueda), pero sigue en **~1/5 del tamaño de la búsqueda**. La cuota de ChatGPT entre plataformas generativas bajó de ~76 % (jun-2025) a ~53 % (may-2026) y Gemini subió de <9 % a ~27–28 %. https://aisearch.similarweb.com/blog/gen-ai-stats/ , https://salience.co.uk/insight/similarweb-2026-generative-ai-landscape , https://searchenginejournal.com/ai-search-isnt-replacing-google-its-layering-on-top-similarweb-data/583378/ [EVIDENCIA, solidez media; las fuentes miden cosas distintas y una de ellas notó que no coinciden entre datasets: visitas a las plataformas vs sesiones referidas a sitios].
- Un cambio de ChatGPT hacia el 7-may-2026 habría movido la proporción de referidos de IA que aterrizan en la **home** de ~25 % a casi 60 % en tres semanas (Salience, citando Similarweb). Implica que el tráfico referido de ChatGPT puede aterrizar en tu portada y no en la página citada. [EVIDENCIA, un solo resumen]
- Para el tamaño de mercado de moldey.com: la IA es una **fuente adicional, no un reemplazo** de Google ("capa encima", según Similarweb). SEO clásico sigue siendo la base. [EVIDENCIA]

---

## 4. llms.txt, llms-full.txt, markdown para agentes, ai.txt — veredicto

**Veredicto: no hay evidencia de que mejore citaciones en ninguna plataforma relevante. Es un archivo opcional de coste casi nulo, pero no hay que invertir tiempo en él.**

| Aspecto | Evidencia |
|---|---|
| **Google** | Declara que no lo usa ni planea (Illyes, vía prensa, julio 2025). La guía oficial de **15-may-2026** lo lista entre las cosas innecesarias; un resumen dice que Google "puede descubrirlo pero no le da trato especial". Mueller: "puramente especulativo", comparable a meta keywords; también cuestionó páginas Markdown separadas para bots. [HECHO, vía prensa] https://www.techwyse.com/news/ai-search/google-john-mueller-llms-txt-speculative-webmcp-ai-agents |
| **Matiz/contradicción dentro de Google** | En dic-2025 apareció un llms.txt en los docs de Search Central (Mueller respondió "hmmn :-/"; interpretado como actualización de un CMS interno). Y según una fuente, **Lighthouse 13.3** agregó una categoría "Agentic Browsing" que **audita** llms.txt (separada de las auditorías SEO; lo trata como ayuda a agentes de navegador, no como factor de ranking). https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit , https://www.searchenginejournal.com/googles-llms-txt-guidance-depends-on-which-product-you-ask . No pude verificar el detalle de Lighthouse (se agotó la búsqueda). [NO VERIFICADO] |
| **OpenAI / Anthropic / Perplexity** | Documentan sus rastreadores y directivas de robots.txt; **ninguno documenta soporte de llms.txt** (afirmación de un resumen; coincide con lo que vi en sus docs). Una fuente secundaria dice que Anthropic "reconoció internamente" considerarlo: **[NO VERIFICADO]**. |
| **Logs de servidor** | Ahrefs (137 k sitios): "97 % de los llms.txt nunca se leen"; 77 % de los bots que lo leen no son de herramientas de IA (https://ahrefs.com/blog/llmstxt-study/ , solo vi el título/resumen). Estudios chicos de logs: 48 días/12.099 peticiones de bots, **cero** a llms.txt (https://www.wislr.com/articles/ai-bot-behavior-log-analysis/); 68.759 peticiones en 2 sitios: GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot y Applebot sin acceso (https://weekerp.com/en/blog/llms-txt-effect); un sitio propio: robots.txt 120 veces, sitemap 43, llms.txt 0 (https://saaslinks.net/blog/llms-txt-server-log-study); 83 sitios/12 semanas: OpenAI lo leyó 7 veces y Anthropic 9, vs miles de robots.txt (https://www.ezy.ai/research/do-ai-bots-read-llms-txt); Prosopo: "ningún crawler de IA lo leyó" (https://prosopo.io/blog/llms-txt/). [EVIDENCIA, baja-media: muestras chicas, muchos autores son vendors, no revisadas por pares; los user-agents se pueden falsificar] |
| **Efecto en citas** | SE Ranking, ~300 k dominios, 10,13 % con llms.txt: **sin relación medible**; sacar la variable del modelo lo mejoró levemente. Fecha ambigua en los resúmenes (nov-2025 o mayo-2026). https://www.searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/561542/ . Otro análisis (ALLMO, ~94.600 URLs citadas, 5 plataformas): solo 1 URL era una página llms.txt — **[NO VERIFICADO]**, solo lo vi citado de segunda mano. [EVIDENCIA] |
| **Quién sí lo usa** | Sitios de documentación para desarrolladores (Mueller admite que podría servir ahí); las herramientas de coding con agentes lo leen. No aplica a una tienda de patrones. [OPINIÓN/NO VERIFICADO] |
| **llms-full.txt, ai.txt, markdown para agentes** | Sin documentación de uso por plataformas en lo que vi. **Riesgo específico para moldey.com:** un `llms-full.txt` con el catálogo completo expone texto/estructura que querés vender. No lo publiques. [OPINIÓN] |

---

## 5. Gestión de rastreadores de IA: robots.txt, cabeceras, Cloudflare

### 5.1 Tabla de user-agents

Verificado en esta sesión (fuente oficial vía buscador): OpenAI, Perplexity y ClaudeBot. El resto es **conocimiento previo del modelo [NO VERIFICADO en esta sesión]**: confirmá cada uno en la documentación del proveedor antes de actuar, y verificá por rangos IP publicados cuando existan (los UA se falsifican).

| User-agent / token | Operador | Función | Estado de verificación |
|---|---|---|---|
| **OAI-SearchBot** | OpenAI | Búsqueda en ChatGPT (aparecer/citar) | [HECHO] |
| **GPTBot** | OpenAI | Entrenamiento de modelos de base | [HECHO] |
| **ChatGPT-User** | OpenAI | Visita iniciada por usuario; robots.txt "puede no aplicar"; no afecta a Search | [HECHO] |
| **PerplexityBot** | Perplexity | Índice de búsqueda | [HECHO] |
| **Perplexity-User** | Perplexity | Fetch por pregunta del usuario; no entrena | [HECHO] roles; ¿ignora robots.txt? [NO VERIFICADO] |
| **ClaudeBot** | Anthropic | Entrenamiento (respeta robots.txt y Crawl-delay; IPs no publicadas) | [HECHO] |
| **Claude-SearchBot**, **Claude-User** | Anthropic | Búsqueda y fetch a pedido | Solo directorios de terceros |
| **anthropic-ai** | Anthropic | Token antiguo/legado | [NO VERIFICADO] |
| **Googlebot** | Google | Rastreo de Search; también alimenta AI Overviews/AI Mode (no hay otro bot separado para Search) | [NO VERIFICADO esta sesión], coherente con el requisito "indexado + elegible para snippet" |
| **Google-Extended** | Google | Token de robots.txt para exclusión de entrenamiento/uso en Gemini; según la documentación de Google **no afecta la inclusión en Search ni AI Overviews** | [NO VERIFICADO esta sesión] |
| **Bingbot** | Microsoft | Búsqueda Bing; alimenta Copilot y, según múltiples reportes, parte del grounding de otros asistentes | [NO VERIFICADO] |
| **Applebot / Applebot-Extended** | Apple | Applebot rastrea para Siri/Spotlight/Safari; Applebot-Extended es token de exclusión de entrenamiento de IA (no rastrea) | [NO VERIFICADO] |
| **Meta-ExternalAgent / Meta-ExternalFetcher** | Meta | Rastreo para entrenamiento/indexación / fetch por usuario | [NO VERIFICADO] |
| **Bytespider** | ByteDance | Entrenamiento; reputación de no respetar robots.txt | [NO VERIFICADO] |
| **CCBot** | Common Crawl | Corpus abierto usado para entrenar muchos modelos | [NO VERIFICADO] |
| **Amazonbot** | Amazon | Alexa/IA de Amazon | [NO VERIFICADO] |
| **DuckAssistBot**, **YouBot**, **cohere-ai**, **Diffbot** y otros | DuckDuckGo, You.com, Cohere, Diffbot | Respuestas con IA / entrenamiento / datos | [NO VERIFICADO] |
| Grok (xAI), DeepSeek | — | No tengo un user-agent documentado confirmado | [NO VERIFICADO] |

Dato de logs: un análisis de 2026 reportó que **OAI-SearchBot ya genera más eventos de log que GPTBot** y que el rastreo automático de OpenAI se triplicó tras GPT-5 (https://www.techwyse.com/news/ai-search/openai-crawlers-tripled-gpt5-log-file-analysis) [EVIDENCIA, baja-media: blog de agencia].

### 5.2 Recomendación para moldey.com (quiere visibilidad y proteger PDF de pago)

Principio: **separar tres cosas.** (1) Búsqueda/citación (permitir), (2) acciones del usuario (permitir), (3) entrenamiento (decisión de negocio) y (4) **archivos de pago (proteger con acceso, no con robots.txt)**.

Esquema propuesto de `robots.txt` (ejemplo orientativo; adaptá las rutas reales y verificá nombres de tokens):

```
# Búsqueda / respuestas con IA: PERMITIR
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: Googlebot
User-agent: Bingbot
Allow: /
Disallow: /descargas/
Disallow: /mi-cuenta/
Disallow: /checkout/
Disallow: /cart/

# Entrenamiento: permitir solo marketing/catálogo público (decisión; ver abajo)
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: Meta-ExternalAgent
User-agent: CCBot
User-agent: Bytespider
Disallow: /descargas/
Disallow: /mi-cuenta/
Disallow: /checkout/
Disallow: /*.pdf$
Disallow: /*.dxf$

Sitemap: https://moldey.com/sitemap.xml
```

- **¿Bloquear entrenamiento (GPTBot, ClaudeBot, Google-Extended)?** [OPINIÓN]. No hay evidencia que mida si permitir entrenamiento mejora la mención de tu marca en el conocimiento "interno" del modelo; sí es plausible que contenido público masivo ayude al reconocimiento, pero no está probado. Una postura equilibrada: **permitir entrenamiento sobre páginas públicas de marketing/guías, bloquear en archivos y áreas de pago**. Si priorizás no ceder nada, bloqueá los bots de entrenamiento enteros: según los docs de OpenAI y Anthropic, eso **no** te saca de la búsqueda de ChatGPT/Claude.
- **Wildcards** `*` y `$` los soportan Google/Bing; otros bots pueden no interpretarlos. Y **robots.txt es voluntario**: bots mal portados (Bytespider por reputación, scrapers anónimos) lo ignoran. [HECHO general / NO VERIFICADO por bot]
- **Protección real de PDF/DXF de pago** [OPINIÓN de ingeniería, no investigada]: guardarlos fuera de la raíz pública; entrega por URL firmada con expiración y atada al pedido; sin enlaces directos ni listado en sitemap; cabecera `X-Robots-Tag: noindex, noarchive, nosnippet` en la ruta de descargas; vistas previas de baja resolución y con marca de agua; marca de agua o huella por comprador en el PDF; licencia clara de uso (personal/comercial) en términos. Ninguna IA "compra" y descarga un PDF protegido, pero sí puede aprender de copias filtradas en terceros: eso solo se mitiga con vigilancia/DMCA.
- **JavaScript:** que el contenido clave esté en HTML servido (SSR/estático). Es práctica extendida que varios rastreadores de IA no ejecutan JavaScript — [NO VERIFICADO esta sesión].
- **Cuidado con el WAF/CDN:** si tu hosting o Cloudflare tiene activado el bloqueo "por defecto" de bots de IA o "Bot Fight Mode", podés estar bloqueando OAI-SearchBot o PerplexityBot sin saberlo. Revisá los logs. [NO VERIFICADO; riesgo práctico plausible]

### 5.3 Cloudflare AI Crawl Control, pay-per-crawl, Content Signals — todo [NO VERIFICADO esta sesión; conocimiento previo]

- **AI Crawl Control** (antes AI Audit): panel para ver qué bots de IA te rastrean y permitir/bloquear por bot. Útil si usás Cloudflare.
- **Bloqueo por defecto** de crawlers de IA en dominios nuevos (desde julio 2025, según recuerdo) y **pay-per-crawl** (cobrar por rastreo; HTTP 402): beta privada, orientada a grandes editores. **Para moldey.com no conviene** apostar por pay-per-crawl (nadie va a pagar por una tienda nueva; además el bloqueo reduce visibilidad).
- **Content Signals Policy** (septiembre 2025, recuerdo): líneas en robots.txt tipo `Content-Signal: search=yes, ai-input=yes, ai-train=no`. Es declarativo y no vinculante; costo cero. Razonable agregarlo (`search=yes, ai-input=yes, ai-train=no`), sabiendo que su efecto depende de que el bot lo respete.
- Pendiente: confirmar nombres vigentes y fechas.

---

## 6. Medición de la visibilidad en IA

### 6.1 Herramientas — [NO VERIFICADO], solo nombres vistos en resultados

Aparecieron en mis resultados como proveedores activos de seguimiento/estudios: **Profound, Peec AI, Otterly.ai, Semrush (AI visibility), Ahrefs (Brand Radar), SE Ranking, Similarweb (AI search), Passionfruit Labs, Trakkr**. Otros que mencionaste (Scrunch, Bing Webmaster Tools "AI Performance", GSC con AI Mode) no los pude verificar en esta sesión. No verifiqué precios ni cobertura de idiomas. [OPINIÓN]: para una tienda chica, **empezar con herramientas gratuitas** (Google Search Console, Bing Webmaster Tools, GA4, logs de servidor) más el protocolo manual; una herramienta de pago solo cuando haya baseline y presupuesto. Pedir en cualquier herramienta: cobertura de **idiomas y países** (muchas trabajan sobre todo en inglés/EE. UU.).

### 6.2 Métricas

- **Mention rate**: % de prompts del set donde la marca es nombrada.
- **Citation rate / citation share**: % de prompts donde se cita una URL tuya; cuota sobre el total de citas.
- **Share of voice**: tus menciones / menciones de todos los competidores en el set.
- **Sentimiento y exactitud**: ¿lo que dice la IA sobre tus precios, formatos, licencias es correcto?
- **Idioma de la fuente citada** vs idioma de la consulta (clave para tu caso).
- Advertencia [OPINIÓN]: las respuestas de IA son **no deterministas**, cambian con ubicación, historial y modo; hacer **varias corridas** por prompt y no interpretar una sola captura.

### 6.3 Protocolo manual barato (≈2–3 h por ronda; mensual)

1. **Set de 30–40 prompts** por idioma de la etapa actual (ES, EN, PT al inicio). Tipos:
   - Informativos "cómo": "cómo hacer el molde de una falda circular", "how to print a sewing pattern on A4 and assemble", "como imprimir molde PDF A0 em copiadora".
   - Comerciales: "dónde comprar moldes de costura en PDF para imprimir", "best sites to buy PDF sewing patterns", "plantillas para sublimar camisetas descargables".
   - Comparativos: "mejores webs de patrones de costura PDF", "Etsy vs tienda propia para patrones PDF".
   - De marca: "¿qué es moldey.com?", "¿moldey.com es confiable?", "moldey precios".
   - Específicos de producto: "archivos DXF para corte CAD de patrones", "tamaño de patrón A0 proyector".
2. **Plataformas:** ChatGPT (búsqueda activada; sesión sin cuenta si es posible), Google (AI Overviews y pestaña AI Mode, ventana privada, país/idioma fijados), Perplexity, Copilot, Gemini, Claude con búsqueda web.
3. **Registrar en una hoja:** fecha, plataforma, idioma, prompt, ¿mencionó moldey?, ¿citó URL de moldey?, URLs/dominios citados (top 5), competidores nombrados, idioma de las fuentes, exactitud (sí/no + nota), corrida 1/2/3.
4. **Calcular** mention rate, citation rate y share of voice por idioma y plataforma; comparar mes a mes.
5. **Línea base probable:** cercana a cero en consultas genéricas; el objetivo inicial es aparecer en consultas de marca (que sea correcta) y en cola larga.

### 6.4 Tráfico referido de IA en GA4

- Fuentes/referrers típicos: `chatgpt.com` (además de `chat.openai.com` antiguo), `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`, `claude.ai`, y otros (`deepseek.com`, `grok.com`, `meta.ai`, `you.com`). ChatGPT suele añadir `utm_source=chatgpt.com` a sus enlaces. [NO VERIFICADO esta sesión; práctica conocida.]
- Crear un **grupo de canales personalizado "IA"** en GA4 con regla de fuente que coincida con regex tipo `chatgpt\.com|chat\.openai\.com|perplexity|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|deepseek|grok|meta\.ai|you\.com`. Un ejemplo de clasificación de tráfico de IA en otra herramienta (Adobe) está en https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/derived-fields/ai-traffic [no lo leí].
- **Límites:** (a) clics desde AI Overviews/AI Mode se contabilizan dentro de Google orgánico, no como "IA"; en Search Console se mezclan con el resto [NO VERIFICADO esta sesión]; (b) parte del tráfico de apps llega como "directo" sin referrer; (c) la caída de clics por AI Overviews es real (Seer) y el tráfico referido de IA sigue siendo pequeño (Similarweb: del orden de 0,2–0,3 % en abril–mayo 2026 según un resumen, sin que pude confirmar el denominador) https://seranking.com/blog/chatgpt-referral-traffic-may-2026/ ; (d) la landing de ChatGPT cambió de patrón en mayo de 2026 (más a home).
- **Complemento:** mirar logs del servidor para ver qué páginas visitan OAI-SearchBot, PerplexityBot, etc. (sin ellos no hay citación posible).

---

## 7. Entidades y señales fuera del sitio — [NO VERIFICADO] salvo lo indicado

Lo que sí tengo con evidencia de esta sesión:
- Las **menciones de marca en la web** son el factor con mayor correlación (0,664) con la presencia de marca en AI Overviews, por encima de anchors de marca (0,527) y búsquedas de marca (0,392) [EVIDENCIA, correlacional, marcas DR>40]. https://ahrefs.com/blog/ai-overview-brand-correlation/
- Las plataformas más citadas (Reddit, YouTube, LinkedIn, Wikipedia) son todas **fuera de tu control** (sección 3.2). El estudio de Semrush muestra además que ser **mencionado** y ser **citado** son cosas distintas.
- Google (guía mayo 2026) dice que las menciones "inauténticas" no sirven y que prioriza contenido no-commodity [HECHO vía resúmenes].

Lo que sigue es práctica generalizada sin respaldo experimental de esta sesión [OPINIÓN]:
- **Consistencia de entidad:** mismo nombre ("Moldey"), descripción, logo y datos en todos los perfiles (web, YouTube, Pinterest, Instagram, Facebook, LinkedIn, Etsy si aplica, Google Business Profile si corresponde).
- **Schema.org** `Organization` con `sameAs` apuntando a esos perfiles, `logo`, `url`, `contactPoint`; `Product`/`Offer` en fichas. Dado el experimento de Ahrefs, no esperes que mejore citas de IA; sí desambigua la entidad y habilita rich results en búsqueda clásica.
- **Wikipedia/Wikidata:** requieren notabilidad; una tienda nueva probablemente no califique y autopromocionarse viola políticas. **No crear páginas propias.** Lo realista es ser mencionado en fuentes independientes (blogs de costura, prensa de moda/manualidades, directorios sectoriales).
- **Comunidades:** Reddit (r/sewing y similares), grupos de Facebook, foros de costura en cada idioma, Pinterest, YouTube (tutoriales de impresión/montaje A4 y A0, proyector). Participar de forma genuina, divulgando la relación comercial, con valor real; el spam daña y los moderadores lo detectan.
- **Reseñas:** pedir reseñas verificables de compradores; no fabricarlas.

---

## 8. Contenido "citable" y comercial/e-commerce

**Con respaldo (según sección 3):** respuesta/definición directa en el primer tercio de la página (44 % de citas de ChatGPT salen del primer 30 %); lenguaje definitorio ("X es…", "X se refiere a…"); encabezados formulados como la pregunta (78,4 % de las citas ligadas a preguntas venían de encabezados, según un resumen del estudio de Indig); página enfocada en un tema; estadísticas, citas atribuidas y fuentes (Princeton, con las salvedades de arriba); fechas reales de actualización (importan sobre todo para ChatGPT); datos propios y experiencia directa (la guía de Google las prioriza).

**Sin respaldo sólido de esta sesión:** "tablas comparativas", "listas numeradas", "FAQ", "autoría con credenciales" y "respuesta de 40–60 palabras": aparecen como consejos de industria. En particular, la "cápsula de 40–60 palabras" es un playbook de proveedor, **no** parte del estudio de Indig; y no encontré datos de que tablas o listas aumenten citas [OPINIÓN]. Google dice que no hace falta dividir el contenido en trozos para IA.

**Intención comercial ("dónde comprar", "mejor X"):** no obtuve datos específicos de e-commerce ni de productos digitales. Hipótesis a contrastar con el protocolo [OPINIÓN]: en "mejor X / dónde comprar" suelen dominar Reddit, YouTube, listados de terceros (marketplaces como Etsy), medios y comparadores; las tiendas propias pocas veces ganan sin reseñas y menciones externas. Para moldey.com, esto sugiere (a) nombrar el producto con precisión (tipo de prenda, talles, formato A4/Letter/A0, DXF, proyector, sublimación), (b) páginas de categoría y producto con datos únicos (tabla de medidas, lista de piezas, número de hojas A4, consumo de tela, nivel de dificultad, instrucciones de montaje, licencia), (c) reseñas y fotos de prendas reales cosidas con el molde, (d) presencia en los canales citados.

**Particularidades de productos digitales** [OPINIÓN]: el texto de la ficha es el único "contenido" indexable (el PDF no se puede ni debe publicarse); conviene una guía gratuita/mini-molde de muestra como pieza de captación y citación, separada del producto de pago.

---

## 9. AEO multilingüe — **no pude obtener evidencia en esta sesión** [NO VERIFICADO]

Pregunta pendiente: ¿citan los motores fuentes en el idioma de la consulta o traducen? ¿Qué rinden los idiomas de pocos recursos? ¿Hay sesgo hacia el inglés? No tengo ningún estudio de 2025–2026 de mis búsquedas. Lo que puedo ofrecer con honestidad:

- **Conocimiento previo [NO VERIFICADO]:** los modelos de lenguaje funcionan mejor en inglés y en idiomas de muchos recursos; la calidad cae en idiomas con poco texto; Google expandió AI Overviews/AI Mode a decenas de idiomas durante 2025. Los AI Overviews/AI Mode se apoyan en el índice de Search, así que las reglas de calidad de Search (incluida la política de spam sobre contenido traducido automáticamente sin revisión humana, que en su momento calificaba como contenido autogenerado/"scaled content abuse") aplican. Verificar contra la documentación de Google.
- **Implicaciones lógicas [OPINIÓN]:** (1) la citación depende de que exista contenido relevante en el idioma de la consulta o, si no, la IA cita fuentes en inglés y las traduce al responder; (2) por eso publicar en un idioma de pocos recursos puede ser **ventaja** (menos competencia) o **inútil** (si la IA ni encuentra ni valora esas páginas): hay que testearlo; (3) la traducción automática sin revisión de miles de páginas es el patrón de más riesgo de calidad/spam; traducción asistida + revisión nativa en las páginas de mayor valor es la ruta segura; (4) `hreflang` y URLs por idioma son prácticas de búsqueda clásica; su efecto sobre IA no está verificado.
- **Cómo cerrar el hueco con bajo costo:** repetir los 8–10 prompts clave de la sección 6.3 en 8–10 idiomas (ES, EN, PT, FR, DE, IT, ID, HI, AR, TR), con ubicaciones coherentes, y registrar el idioma de las fuentes citadas, si la IA responde en el idioma de la consulta, y si aparece alguna página de moldey.com. Con 2–3 rondas se ve el patrón real.

---

## 10. Riesgos — [OPINIÓN / NO VERIFICADO], salvo lo indicado

- **Alucinaciones sobre tu marca/precios/licencias:** los motores pueden inventar o desactualizar precios, formatos o políticas. Mitigación: página "Acerca de/Precios/Licencia/Políticas" clara en HTML, datos consistentes en todos los perfiles, y auditoría periódica de prompts de marca (sección 6.3). Exactitud y sentimiento son métricas a vigilar.
- **Scraping y copias:** contenido público puede ser raspado; los PDF pagos filtrados en terceros pueden entrenar modelos aunque bloquees. Mitigación: control de acceso, marca de agua, DMCA.
- **Cambios frecuentes:** la propia dinámica de los datos lo muestra (top-10 76 % → 38 % en 8 meses; cuotas de ChatGPT vs Gemini; cambio de aterrizaje de referidos en mayo 2026). No hay "hack" estable; priorizar fundamentos.
- **"AI SEO snake oil":** Google recomienda evaluar a los proveedores AEO/GEO como cualquier asesor SEO de terceros. Señales de alerta que vi: "FAQ schema +200 % de citas" sin grupo de control; cifras de frescura o de Princeton que no coinciden con el original; "garantizamos citas en ChatGPT"; vender llms.txt como solución. Aun herramientas de medición tienen conflicto de interés al publicar estudios que "descubren" que su método funciona.

---

## 11. Qué hacer en moldey.com (priorizado)

Escala: Impacto A/M/B × Esfuerzo A/M/B.

| # | Acción | Impacto | Esfuerzo | Base |
|---|---|---|---|---|
| 1 | **Asegurar indexabilidad y rastreo:** HTML servido (SSR/estático) para fichas, categorías y guías; sitemap; Search Console y **Bing Webmaster Tools** verificados; revisar que WAF/CDN no bloquee OAI-SearchBot, PerplexityBot, Claude-SearchBot, Googlebot, Bingbot. | A | B | Google: indexado + elegible para snippet; OpenAI/Perplexity: hay que permitir su bot |
| 2 | **robots.txt separado por función** (sección 5.2): permitir búsqueda/usuario; decidir entrenamiento; cerrar `/descargas`, `/mi-cuenta`, `/checkout`. | A | B | Docs OpenAI/Anthropic/Perplexity |
| 3 | **Proteger archivos de pago por acceso:** URLs firmadas con expiración, `X-Robots-Tag` en descargas, marca de agua por comprador, previews de baja resolución. | A | M | Ingeniería; robots.txt es voluntario |
| 4 | **Contenido no-commodity y específico de costura:** tablas de medidas por talle, número de hojas A4/Letter/A0, consumo de tela, fotos de prendas cosidas, tutoriales de impresión y montaje, comparativas propias de formatos (PDF vs A0 vs DXF vs sublimación). Páginas **enfocadas**, no "guías definitivas" gigantes. | A | M–A | Google 2026; Indig (páginas enfocadas) |
| 5 | **Estructura "respuesta primero":** definición o respuesta directa en las primeras líneas; H2/H3 en formato de pregunta; lenguaje afirmativo; datos y fuente citada; fecha de actualización real. | A | B–M | Indig (44 % del primer 30 %); Princeton (con reservas) |
| 6 | **Presencia externa real en los sitios que se citan:** canal de YouTube (tutoriales), Pinterest, Reddit y grupos de Facebook de costura (aportando valor), reseñas verificadas, menciones en blogs y prensa de manualidades. | A | A | Ahrefs 0,664; datos de Reddit/YouTube/LinkedIn |
| 7 | **Línea base de medición:** protocolo manual (6.3) + grupo de canales "IA" en GA4 + revisar logs. Repetir mensualmente. | M | B | — |
| 8 | **Entidad:** nombre/descripción/logo consistentes; `Organization` + `sameAs`; `Product`/`Offer` en fichas (para búsqueda clásica y claridad). | M | B | Ahrefs: schema no mueve citas; sí ayuda a SEO clásico |
| 9 | **Multilingüe por etapas:** traducir primero las páginas de mayor valor con revisión nativa; testear con el protocolo de idiomas antes de expandir a más idiomas. | M | M–A | Sección 9 (sin evidencia dura) |
| 10 | **Cola larga de intención comercial** ("molde PDF falda circular talle X", "plantilla sublimación camiseta A0"): menos competencia frente a Reddit/Wikipedia. | M | M | Concentración de citas en pocos dominios |
| 11 | **Contenido de marca verificable** (precios, licencia, formatos, políticas) para reducir alucinaciones. | M | B | — |
| 12 | `llms.txt` opcional (si querés, 30 minutos, sin llms-full.txt). Sin expectativas. | B | B | Sección 4 |
| 13 | Content Signals en robots.txt (`ai-train=no`, `search=yes`, `ai-input=yes`) si usás Cloudflare. | B | B | [NO VERIFICADO] |

## 12. Qué NO hacer

- No contratar servicios que **garanticen** citas en ChatGPT/Google ni pagar por "llms.txt/llms-full.txt/schema para IA" como solución (Google lo desmiente y los estudios controlados no muestran efecto).
- No publicar `llms-full.txt` con el contenido de tus productos de pago.
- No confiar en robots.txt para proteger PDF/DXF de pago; no dejarlos en URLs adivinables.
- No bloquear **todos** los bots de IA por miedo si querés visibilidad: bloqueás OAI-SearchBot/PerplexityBot y desaparecés de sus respuestas. Tampoco dejar el WAF bloqueándolos "por defecto".
- No traducir automáticamente cientos de páginas sin revisión (riesgo de calidad/spam y de alucinaciones sobre tus productos).
- No hacer spam en Reddit/Quora/grupos, ni reseñas falsas, ni "menciones" compradas (Google lo menciona como inútil; los moderadores lo detectan).
- No crear tu propia página de Wikipedia/Wikidata sin notabilidad.
- No trocear el contenido artificialmente ("chunking") ni inflar páginas "ultimate guide" (Google dice que no hace falta; los datos de Indig favorecen páginas enfocadas).
- No mostrar a los bots contenido distinto del que ven los usuarios (cloaking), ni versiones Markdown "para bots" divergentes (Mueller las considera mala idea).
- No decidir con una sola captura de un prompt; no confundir correlación con causa (menciones, schema, longitud).
- No abandonar SEO clásico: es la base de lo que Google/Bing citan, y la IA sigue siendo ~1/5 del tamaño de la búsqueda.

---

## 13. Pendientes de verificar (por falta de presupuesto de búsqueda y de acceso a páginas primarias)

1. Texto original de la guía de Google (15-may-2026): confirmar exactamente qué dice de llms.txt, schema, traducciones/idiomas y la frase sobre "Search generative AI features en Search Console".
2. Documentación oficial de Anthropic para Claude-SearchBot y Claude-User; de Microsoft (Copilot, Bing, "AI Performance" en Bing Webmaster Tools), Apple (Applebot-Extended), Meta, xAI, DeepSeek.
3. Estudios 2025–2026 sobre **idioma/multilingüe** y sesgo al inglés; comportamiento en idiomas de pocos recursos.
4. Datos de citación en **e-commerce y productos digitales**; "dónde comprar".
5. Cloudflare AI Crawl Control / pay-per-crawl / Content Signals: fechas y detalles actuales.
6. Herramientas de medición: precios, idiomas soportados.
7. Si Perplexity-User y ChatGPT-User respetan robots.txt en la práctica.
8. Fechas exactas de los estudios de SE Ranking (llms.txt y factores de ChatGPT) y del post de Ahrefs sobre marcas.
9. Cualquier cambio entre junio y octubre de 2026.

## 14. Fuentes consultadas (todas aparecieron en resultados de búsqueda)

Google/Plataformas: https://developers.google.com/search/docs/appearance/ai-features · https://developers.google.com/search/docs/fundamentals/ai-optimization-guide · https://developers.openai.com/api/docs/bots · https://support.claude.com/en/articles/8896518-what-is-claude-bot · https://docs.perplexity.ai/docs/resources/perplexity-crawlers.md · https://siteline.ai/ai-agent-directory/claude-searchbot/
Cobertura de la guía de Google y llms.txt: https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/ · https://www.semrush.com/blog/google-publishes-generative-ai-search-guide/ · https://searchengineland.com/google-publishes-guide-on-optimizing-for-generative-ai-features-477671 · https://previsible.com/seo-ai-news/google-published-its-first-guide-to-ai-search-optimization/ · https://www.paz.ai/blog/google-ai-search-optimization-guide-still-seo-incomplete · https://searchengineland.com/google-says-normal-seo-works-for-ranking-in-ai-overviews-and-llms-txt-wont-be-used-459422 · https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit · https://www.techwyse.com/news/ai-search/google-john-mueller-llms-txt-speculative-webmcp-ai-agents · https://www.searchenginejournal.com/googles-llms-txt-guidance-depends-on-which-product-you-ask
Estudios: https://ahrefs.com/blog/search-rankings-ai-citations · https://news.designrush.com/ai-overview-citations-drop-ahrefs · https://almcorp.com/blog/google-ai-overview-citations-drop-top-ranking-pages-2026/ · https://ahrefs.com/blog/ai-overview-brand-correlation/ · https://ahrefs.com/blog/schema-ai-citations/ · https://otterly.ai/blog/schema-markup-real-impact-ai-search/ · https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/ · https://ahrefs.com/blog/llmstxt-study/ · https://www.searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/561542/ · https://www.searchenginejournal.com/new-data-top-factors-influencing-chatgpt-citations/561954/ · https://seranking.com/blog/how-to-optimize-for-ai-mode/ · https://searchengineland.com/chatgpt-citations-content-study-469483 · https://searchengineland.com/chatgpt-citations-domains-study-472349 · https://www.growth-memo.com/p/shorter-focused-content-wins-in-chatgpt · https://www.tryprofound.com/blog/ai-platform-citation-patterns · https://www.tryprofound.com/blog/the-data-on-reddit-and-ai-search · https://www.semrush.com/blog/most-cited-domains-ai/ · https://almcorp.com/blog/linkedin-ai-search-citations-2026/ · https://www.semrush.com/blog/manufacturing-seo-ai-search/ · https://almcorp.com/blog/top-domains-cited-by-ai-search/ · https://seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update · https://ppc.land/google-ai-overviews-reduce-organic-ctr-61-paid-traffic-68/ · https://aisearch.similarweb.com/blog/gen-ai-stats/ · https://salience.co.uk/insight/similarweb-2026-generative-ai-landscape · https://seranking.com/blog/chatgpt-referral-traffic-may-2026/ · https://searchenginejournal.com/ai-search-isnt-replacing-google-its-layering-on-top-similarweb-data/583378/ · https://collaborate.princeton.edu/en/publications/geo-generative-engine-optimization/ · https://everything-pr.com/we-found-the-paper-that-launched-geo-heres-whats-actually-in-it/ · https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique
Logs/llms.txt: https://www.wislr.com/articles/ai-bot-behavior-log-analysis/ · https://weekerp.com/en/blog/llms-txt-effect · https://saaslinks.net/blog/llms-txt-server-log-study · https://www.ezy.ai/research/do-ai-bots-read-llms-txt · https://prosopo.io/blog/llms-txt/ · https://www.techwyse.com/news/ai-search/openai-crawlers-tripled-gpt5-log-file-analysis
Medición: https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/derived-fields/ai-traffic
