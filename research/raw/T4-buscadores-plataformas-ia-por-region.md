# T4 — Buscadores, plataformas, marketplaces y asistentes de IA por región (2025–2026), aplicado a moldey.com

Fecha del informe: 12-oct-2026. Autor: agente de investigación T4.

---

## 0. Alcance, método y LÍMITES (leer primero)

- Se hicieron **31 búsquedas con resultado** (StatCounter, Ahrefs, Similarweb, SEC, QuestMobile, estudios de citas de IA, etc.). `WebFetch` no funciona, así que **no se abrió ninguna página primaria**: las cifras son las que devolvió el resumen de cada búsqueda. Donde el snippet de StatCounter omitía el nombre del líder (Google), lo marco como "inferido".
- **El presupuesto de WebSearch (límite compartido por turno) se agotó** antes de cubrir todo. **No pude investigar con fuentes**: Xiaohongshu/Douyin/WeChat/Bilibili/Zhihu/Weibo, VK/OK/Dzen/Telegram, LINE/Kakao/Zalo, políticas de productos digitales de los marketplaces, hábitos de búsqueda por macro-región (voz/imagen/Android/conexión lenta), ni Sarvam/Krutrim/BharatGPT, Jais/Falcon, Le Chat, GigaChat, HyperCLOVA X, Ernie, Kimi.
- Todo lo marcado con **†** viene de **conocimiento previo del agente, sin verificación en esta sesión**: es hipótesis de trabajo, no hallazgo. No hay cifras inventadas: donde no hay dato lo digo.
- Etiquetas: **[HECHO]** documentado por la plataforma/fuente primaria; **[EVIDENCIA]** dato de terceros con metodología; **[OPINIÓN]** consejo de industria o inferencia mía; **[NO VERIFICADO]** sin respaldo suficiente. Las referencias `[S#]` apuntan a la sección 9 (URLs vistas en los resultados).

---

## 1. Resumen ejecutivo

1. **Google sigue siendo el buscador por defecto casi en todo el mundo (~89–91 % global según StatCounter), pero hay cuatro "jardines cerrados" donde Google no basta**: China (Baidu + ecosistema WeChat/Xiaohongshu/Douyin), Rusia (Yandex ~71 %), Corea (Naver ~64–68 %) y, parcialmente, Japón (Bing fuerte en escritorio) y Chequia (Seznam ~13,5 %). [EVIDENCIA, S1, S3–S11]
2. **Bing importa más por lo que alimenta que por su cuota** (4–5 % global): Copilot, y según múltiples fuentes de industria también ChatGPT Search, DuckDuckGo, etc. (no hay documentación de OpenAI vista aquí). Bing Webmaster Tools + IndexNow es la acción de mayor retorno/menor esfuerzo para AEO. [EVIDENCIA/OPINIÓN, S19–S21]
3. **Los asistentes de IA ya son una capa de descubrimiento masiva**: ChatGPT ~900 M usuarios semanales (feb-2026; India 100 M), Gemini ~950 M MAU (T2-2026), Meta AI entre ~640 M (conteo estricto) y 1.200 M (conteo amplio), Doubao ~382 M MAU en China. Las cifras de blogs agregadores contradicen a las oficiales; usar solo las oficiales como ancla. [S27–S34]
4. **Para un nicho visual como los moldes de costura, Pinterest (640 M MAU, creciendo solo fuera de EE. UU./Canadá) y YouTube (India ~518 M de alcance publicitario) son los dos canales de descubrimiento con mejor relación alcance/relevancia**, y YouTube/Reddit aparecen entre los dominios más citados por IA (con desacuerdo entre estudios). [S42, S44, S50–S53]
5. **Meta AI/WhatsApp, TikTok y Facebook concentran el uso móvil en India, Brasil, Indonesia y México** (Meta AI: India ≈21 %, Brasil ≈9 %, Indonesia ≈7 % de los MAU estimados; TikTok ad reach: Indonesia 180 M, Brasil 131 M, México 99 M). [S31, S55]
6. **Los marketplaces generalistas de bienes físicos (Shopee, Lazada, Mercado Libre, Trendyol, Ozon, Wildberries, Flipkart, Jumia, Noon…) en general NO son el lugar para vender archivos descargables**†; los que sí aceptan digitales son Etsy, Gumroad, Payhip, Creative Market, Hotmart/Eduzz/Kiwify, BOOTH, note†. Hay que verificar la política de cada uno antes de listar.
7. **China y Rusia no son objetivo de etapa 1**: ICP (entidad china, 20–60 días hábiles y USD 3.000–15.000 según proveedores) y bloqueo de pagos internacionales hacen el costo/beneficio desfavorable para un vendedor argentino. [S22, S23; pagos Rusia †]
7b. **Corea y Japón son mercados de alto valor pero exigen localización nativa y presencia en plataformas propias** (Naver Search Advisor/Blog/Cafe; BOOTH/note/LINE†), no solo traducción.

---

## 2. Buscadores por país/región

### 2.1 Cuota de mercado (con fuente y fecha)

| Mercado | Líder y cuota | Alternativas relevantes | Fuente / fecha | Etiqueta y notas |
|---|---|---|---|---|
| **Mundo** | Google ≈ 91,3 % (inferido; jul-2026) | Bing 4,47 %; Yahoo! 1,24 %; Yandex 1,00 %; DuckDuckGo 0,65 %; Baidu 0,50 % | StatCounter jul-2026 [S1]. Jun-2026: Google 91,27 / Bing 4,68 / Yahoo 1,28 / Yandex 0,79 / DDG 0,67 / Baidu 0,43 | [EVIDENCIA]. StatCounter mide **referidos desde buscadores**, no incluye asistentes de IA. Una compilación de terceros con datos de ene-2026 da Google 89,33 / Bing 4,06 / Yandex 2,48 / Baidu 0,99 [S2]: **Yandex y Baidu varían mucho entre meses** (ruido de muestra). |
| **Europa** | Google ≈ 91 % (móvil ≈95 %, escritorio ≈80 %) | Bing ≈12 % en escritorio; DDG ≈0,6 %; Ecosia ≈0,4 %; Brave ≈0,08 % | Ahrefs, actualizado 8-oct-2026 [S14] | [EVIDENCIA]. Qwant y Startpage no aparecen a nivel Europa. |
| **Francia** | Google (dominante) | Ecosia ≈1,4 %; Qwant ≈0,83 %; DDG ≈0,79 % | StatCounter ago-2026 [S15] | [EVIDENCIA]. Las "alternativas éticas" pesan algo en Francia/Alemania, pero <3 % en conjunto. |
| **Rusia** | **Yandex 71,03 %** (jun-2026); 2.º 26,53 % (presumiblemente Google) | — | StatCounter [S5]; Yandex afirma ~7 de cada 10 consultas (abr-2026) [S4] | [EVIDENCIA]+[afirmación de la empresa]. Métricas distintas (tráfico vs. consultas). |
| **Kazajistán** | Google 68,41 % | Yandex (yandex.kz/.ru/ya.ru) ≈28 % | StatCounter jun-2026 [S6] | [EVIDENCIA]. Mercado dividido: hay que cubrir ambos. |
| **Turquía / Bielorrusia** | **Sin dato actual** | — | — | [NO VERIFICADO]. Solo hallé cifras viejas (Yandex ~5–6 % en Turquía en 2013). Google dominante en Turquía †. |
| **China** | Baidu 47–51 % (jun/jul-2026) | Bing 22,8–23,2 %; Haosou/360 9–14 %; Sogou 2,1–2,6 %; "Yandex" 10–13 % (anómalo) | StatCounter [S3] | [EVIDENCIA, **baja fiabilidad**]. En escritorio+tablet el mismo StatCounter pone a Bing primero (≈38 %) y Baidu 30,8 %. Yandex 10–13 % en China parece artefacto de medición [OPINIÓN]. Un artículo de analista (sin fuente, replicado en dominios espejo) dice Baidu ≈72 % del mercado doméstico: **[NO VERIFICADO]**. Shenma no apareció. |
| **Corea del Sur** | **Naver 66,69 %** vs Google 26,10 % (InternetTrend, jul-2026) | Daum/Kakao: sin dato | [S7]; StatCounter jul-2026 móvil: Naver 68,18 % / Google 27,33 %; **escritorio: Google 66,52 % / Naver 19,99 %** | [EVIDENCIA]. Medición contradictoria según firma (H1-2026: Naver 64,28 %/Google 28,37 %). La app de Google ya supera en MAU a la de Naver (47,0 M vs 46,9 M, jul-2026) [S8]: mide usuarios, no búsquedas. |
| **Japón** | Google ≈59–63 % (inferido; jun/ago-2026) | **Bing 28–33 %** (escritorio 44,9 %); Yahoo! Japón 6–7 % | StatCounter [S9]; resumen [S10] | [EVIDENCIA]. Ojo: la cuota "Yahoo" de StatCounter parece baja; Yahoo! Japón usa tecnología de Google† [NO VERIFICADO en esta sesión]. |
| **Chequia** | Google 80,8 % | **Seznam 13,5 %** (estable; móvil 13 %, tablet ≈27 %); Bing ≈4 % | StatCounter jun-2026 [S11]; Seznam Reporter instalado en ≈13 % de sitios checos [S12] | [EVIDENCIA]. |
| **Vietnam** | Google ≈95,6 % (inferido) | **Coc Coc 3,62 %**; Bing 0,44 % | StatCounter jun-2026 [S13] | [EVIDENCIA]. Una página con rótulo dic-2025 mostraba Coc Coc 5,96 %, pero la fecha era incoherente: tendencia a la baja **no confirmada**. |
| **Ucrania** | Google | Bing ≈1–2 % | Proveedor SEO [S59] | [OPINIÓN/débil]. |
| India, LatAm, MENA, África, SE Asiático (excepto Vietnam) | Sin consulta específica | — | — | [NO VERIFICADO]. Hipótesis†: Google >90 % en casi todos. |

**Lectura práctica:** el dato más útil no es el ranking sino el **cambio por dispositivo**: en Corea el móvil es de Naver y el escritorio de Google; en Japón y Europa **Bing pesa en escritorio (12–45 %)** y casi nada en móvil. Como los moldes en PDF suelen descargarse/imprimirse desde un PC, esa franja de escritorio no es despreciable [OPINIÓN].

### 2.2 Requisitos prácticos de indexación por buscador

| Buscador | Qué hacer para ser indexado | Estado de la evidencia |
|---|---|---|
| **Google** | Search Console, sitemap, hreflang, HTTPS, Core Web Vitals. | Estándar; no re-verificado aquí. |
| **Bing (+ Copilot, DDG, Ecosia, Qwant, y la fuente que se atribuye a ChatGPT Search)** | **Bing Webmaster Tools** (verificar dominio, sitemap, inspección de URL) + **IndexNow** (protocolo push; Shopify tiene app "IndexNow: for Bing and Yandex"). | [EVIDENCIA vendors, S19–S21]. "ChatGPT usa el índice de Bing" es afirmación repetida por blogs de industria, **sin documentación de OpenAI vista** → [OPINIÓN]. Un blog coreano atribuye a Bing que el 22 % de sus clics de dic-2025 vino de URLs entrantes por IndexNow: **no confirmado**. |
| **Baidu** | Cuenta en Baidu Webmaster (requiere identidad/teléfono chino†), sitemap, contenido en chino simplificado, hosting rápido en China continental. **Sitio alojado en China exige ICP**; para sitios fuera de China no es obligatorio, pero hay latencia y bloqueos. El ICP exige, en general, **entidad jurídica china**; plazo 20–60 días hábiles y USD 3.000–15.000 (cifras de proveedores); además registro PSB en 30 días y licencia aparte si hay cobro (valor agregado de telecom). | [S22, S23] guías de proveedores; sin fuente oficial MIIT. Fuentes discrepan sobre elegibilidad de extranjeros. Baiduspider y Baidu Webmaster: †. |
| **Yandex** | Yandex Webmaster (verificación de dominio, sitemap, región/geo, `robots.txt`), compatible con **IndexNow**. Contenido en ruso, hosting rápido en la región, enlaces locales. Turbo pages: estado 2026 **no verificado**. | IndexNow-Yandex [S20]; resto †. |
| **Naver** | **Naver Search Advisor**: verificar propiedad (archivo HTML, meta tag o DNS), enviar sitemap, solicitar recolección de páginas; Naver **no descubre bien sitios extranjeros sin registro**; robots.txt en raíz (crawler **Yeti**, fuente única). Contenido coreano nativo (la traducción automática "suele quedar corta"). 3–6 meses para tracción en marcas nuevas (estimación de blog). Blog/Cafe/지식iN son las superficies que ranquean. | [S24, S25, S58] vendors, **no hay fuente oficial de Naver en los resultados**. |
| **Seznam** | Seznam Webmaster/Reporter, sitemap, IndexNow †. Solo importa si se publica en checo. | Parcial [S12]. |
| **Coc Coc** | No requiere nada propio: Google SEO en vietnamita cubre ~96 %. | [S13]. |
| **Yahoo! Japón / Sogou / Shenma / 360** | Sin acción separada: Yahoo! Japón sigue a Google† (no verificado); Sogou (parte de Tencent/WeChat Search†), Shenma (Alibaba/UC†) y 360 exigen ICP/hosting chino para rendir bien†. | †. |
| **Brave Search / DuckDuckGo / Ecosia / Qwant / Startpage** | Brave tiene **índice propio** (>40.000 M páginas según Brave); Ecosia/Qwant/DDG complementan con Bing†. No hay consola de webmaster comparable: se entra por rastreo abierto + Bing. | Brave [S16]; resto †. |
| **Mail.ru / VK** | Marginal en búsqueda; la visibilidad pasa por contenidos dentro de VK/Dzen†. | †. |

**Rastreadores de IA que conviene no bloquear** (nombres según documentación de cada vendor, no re-verificados aquí †): Googlebot, Bingbot, OAI-SearchBot / ChatGPT-User (OpenAI), Claude-SearchBot / Claude-User (Anthropic), PerplexityBot / Perplexity-User, YandexBot, Baiduspider, Yeti (Naver). Bloquear solo los de **entrenamiento** (GPTBot, Google-Extended, ClaudeBot) es una decisión de negocio aparte †.

---

## 3. Asistentes y buscadores de IA por región

### 3.1 Escala y alcance (datos disponibles)

| Asistente | Escala (fuente, fecha) | Regiones fuertes | Búsqueda web / índice | Etiqueta |
|---|---|---|---|---|
| **ChatGPT** | **900 M usuarios semanales** (feb-2026, citada por varios agregadores que remiten a OpenAI) [S28]; **India 100 M semanales** (Altman en el AI Impact Summit, feb-2026), 2.º mercado tras EE. UU. [S27]. Una fuente aislada dice **1.200 M semanales** (29-sep-2026): **[NO VERIFICADO]** [S29]. Brasil: sin cifra oficial; estimaciones 45,8–69,6 M semanales (agregadores) | EE. UU., India, Brasil (por tráfico Similarweb ago-2025: India 9,3 %, Brasil 5,3 %) | Sí (ChatGPT Search). Índice: se repite que usa Bing [OPINIÓN]. | [HECHO] India/900 M; resto [EVIDENCIA débil] |
| **Gemini / AI Mode / AI Overviews** | Gemini app **>950 M MAU en T2-2026** (de 750 M el trimestre anterior; 900 M en I/O mayo-2026) [S30]; AI Mode >1.000 M MAU (reporte secundario). "230+ países, 70+ idiomas" (una fuente). Similarweb: 25,0 % del tráfico web de IA gen. en sep-2026 [S36][S38] | Global; Google no publica cifras por país. Tráfico: EE. UU. ≈15 %, luego India, Japón, Corea, Brasil (estimación Quantumrun) | Sí, **índice de Google** | [EVIDENCIA] vía terceros que citan a Alphabet; no leí la fuente primaria. |
| **Meta AI** (WhatsApp/Instagram/Facebook/Messenger) | **Conteo amplio: 1.200 M MAU (T1-2026)** [S32]; **conteo estricto ≈640 M MAU** (Presenc AI) [S31]. País (Presenc): **India ≈21 %, Brasil 9 %, Indonesia 7 %**; India+Brasil+Indonesia+México = 42 % | India, Brasil, Indonesia, México, LatAm | Responde dentro de las apps; índice no verificado † | [EVIDENCIA débil]: definiciones incompatibles. |
| **WhatsApp** (canal de distribución, no IA) | 3.300–3.500 M MAU [S33]. India: 535,8 M (DataReportal 2025) vs 853,8 M (otra fuente, **implausible**); Brasil ≈139–150 M; Indonesia ≈87–120 M | Sur de Asia, LatAm, África, MENA, Europa del Sur | — | [EVIDENCIA] con rango. |
| **Copilot (Microsoft)** | **Sin cifra hallada** | Escritorio Windows/Edge (Japón y Europa) | Sí, **índice de Bing** † | [NO VERIFICADO] |
| **Perplexity** | MAU estimados entre **34 M y >100 M** según fuente [S40]; **780 M consultas/mes en may-2025** (CEO) [S39]; 1.000–1.500 M/mes en 2026 (blogs, sin respaldo). Comet 3–18 M MAU (rango amplio) | EE. UU., India† | Sí; PerplexityBot propio † | [HECHO] 780 M; resto [NO VERIFICADO] |
| **Claude** | Similarweb: **8,9 % del tráfico web de IA gen.** (mediados de 2026; 1,6 % un año antes) [S37] | EE. UU./Europa† | Sí. **Muy probablemente índice de Brave** (Brave figura entre los subprocesadores de Anthropic; el API tiene un parámetro `BraveSearchParams`; Cowork ofrece opción Brave, jun-2026), **no confirmado por Anthropic** [S16–S18] | [EVIDENCIA indirecta] |
| **DeepSeek** | **130 M MAU en China** (QuestMobile H1-2026) [S34]; en Rusia, **29 % de los usuarios de IA** (Beeline Analytics T1-2026) [S41] | China, Rusia | Sí (búsqueda propia/de terceros †) | [EVIDENCIA] |
| **Doubao (ByteDance)** | **≈382 M MAU** (QuestMobile H1-2026); T1-2026 345 M (otra base: 260 M+). **Apps IA nativas de China: 499 M MAU** (may-2026) [S34] | China | Integrado a ecosistema Douyin/Toutiao † | [EVIDENCIA] |
| **Qwen / Tongyi (Alibaba)** | **≈167 M MAU** (H1-2026) [S34] | China | Ecosistema Alibaba/Quark † | [EVIDENCIA] |
| **Yuanbao (Tencent)** | **≈49,8 M MAU** (ranking que cita QuestMobile) [S35] | China | Conectado a WeChat † | [EVIDENCIA débil] |
| **Kimi, Ernie/Wenxin (Baidu)** | **Sin cifras halladas** | China | Ernie → índice Baidu † | [NO VERIFICADO] |
| **Alice AI / YandexGPT (Yandex)** | **67 % de los usuarios rusos de IA** (Beeline Analytics T1-2026) vs DeepSeek 29 % y ChatGPT 7 % (multiuso, suma >100 %) [S41]; 2 M suscriptores de "Alisa Pro" (dic-2024) | Rusia | Sí, índice Yandex † | [EVIDENCIA] |
| **GigaChat (Sber)** | **Sin cifras halladas** | Rusia | — | [NO VERIFICADO] |
| **Naver (AI Briefing / AI Tab / Cue: / HyperCLOVA X)** | **AI Briefing cubre >20 % de las búsquedas** (dic-2025, Korea Times) [S26]; meta de ≈40 % a fines de 2026 (blog SEO, sin verificar); "AI Tab" conversacional lanzado abr-2026 (fuente secundaria). Discrepancia sobre fecha de lanzamiento (mar-2025 vs jun-2025) | Corea | Índice Naver (Blog/Cafe/지식iN) † | [HECHO] 20 % (prensa); resto [NO VERIFICADO] |
| **Le Chat (Mistral), Jais/Falcon (EAU), Sarvam/Krutrim/BharatGPT (India), LINE/Kakao AI** | **Sin datos en esta sesión** | Francia; Árabe; India; Japón/Corea | — | [NO VERIFICADO]; no priorizar sin evidencia. |

### 3.2 Cómo ser citado (lo que sí se puede decir con respaldo)

- **Estar en el índice que cada asistente consulta** es la condición previa: Google (Gemini/AI Mode), Bing (Copilot; ChatGPT según industria), Brave (Claude, probable), Yandex (Alice), Baidu (Ernie†), Naver (AI Briefing†). Ningún asistente se ve "en frío" sin eso. [OPINIÓN fundada en S16–S21]
- **Las fuentes que más citan los asistentes no son sitios de tiendas sino plataformas de comunidad y vídeo** (sección 4.3). Aparecer allí aumenta la probabilidad de mención de marca. [EVIDENCIA, con desacuerdo]
- Citas de Reddit: **Peec AI (30 M de fuentes, 31-mar-2026)** pone a Reddit primero y YouTube y LinkedIn después [S50]; **LLM Pulse (may-2026)** pone YouTube 26,47 % y Reddit 17,39 % (URL primaria no vista; aparece resumido en agregadores [S52]); **Ahrefs (AI Mode, sep-2025)**: Wikipedia 1.º, Reddit 4.º; un análisis (Machine Relations Index) dice que **ChatGPT y Claude casi no citan Reddit** [S51]. **Controversia: el peso de Reddit depende del asistente y de la metodología.**
- No hay evidencia en este informe sobre `llms.txt` ni schema; **no asumir efecto**.

---

## 4. Plataformas de descubrimiento del nicho (costura / moldes / DIY)

### 4.1 Tabla por plataforma

| Plataforma | Alcance (dato) | Rol para moldes | SEO / acción | Etiqueta |
|---|---|---|---|---|
| **Pinterest** | **640 M MAU en T2-2026 (+11 % interanual)** [S42]; T1-2026: 631 M = EE. UU./Canadá 106 M, Europa 159 M, Resto del mundo 367 M [S43]. Segun un análisis secundario, en T2 Europa perdió ~2 M y UCAN quedó plano: **todo el crecimiento viene de Resto del Mundo** [S44]. Por país (DataReportal ene-2025): EE. UU. ≈96 M, **Brasil ≈40 M**, **México ≈27 M**, **Alemania ≈23 M** [S45]; Statista (oct-2025) EE. UU. 96,9 M / Brasil 42,2 M. India y Japón: sin dato | **Muy alto**: es el buscador visual de "ideas de costura"; los pines enlazan a la ficha del molde | Pinterest funciona como buscador: pesan palabras en títulos, descripciones, nombre del tablero, texto alternativo y nombre de archivo; los hashtags poco; formato vertical 2:3 (1000×1500) [S48, S49] (blogs de herramientas, no documentación de Pinterest). Idiomas: **41 en 2022** [S46]; incorporó árabe [S47]. **Rich Pins en 2026: sin dato**; ¿admite Pinterest Shopping productos digitales? †, verificar | [EVIDENCIA]+[OPINIÓN] |
| **YouTube** | Alcance publicitario India **≈518 M**, EE. UU. ≈259 M, Indonesia 3.º (DataReportal abr-2026, vía Statista) [S53]; global ≈2.530 M (inicios 2025) [S54] | Muy alto: tutoriales de "cómo usar el molde", "cómo imprimir y armar PDF A4/Letter/A0" | Títulos/descripciones/subtítulos en cada idioma (YouTube permite títulos y descripciones multilingües †). **YouTube está entre los 2 dominios más citados por IA** (S50, S52) | [EVIDENCIA] |
| **TikTok / Douyin** | Audiencia publicitaria 18+ (oct-2025, sin Douyin): **Indonesia 180,1 M, EE. UU. 153,1 M, Brasil 130,8 M, México 99,0 M** [S55]. Otra tabla de 2026 da cifras distintas (Indonesia 140 M, Brasil 120 M, México 90 M) con valores de penetración dudosos [S57]. Sudeste Asiático ≈510 M, LatAm y Norteamérica ≈230 M cada una (agregador, sin verificar) [S56]. TikTok Shop por país: **sin dato** | Alto en LatAm/SE Asiático para tutoriales cortos y "antes/después" | Búsqueda en TikTok creciente †; texto en pantalla y subtítulos en idioma local | [EVIDENCIA]+† |
| **Instagram / Facebook (grupos)** | Sin cifras de esta sesión. Meta AI + WhatsApp indican que el ecosistema Meta es el principal en India, Brasil, Indonesia, México [S31] | Alto: comunidades de costura en grupos de Facebook (LatAm, SE Asiático, África, MENA†) | Presencia con perfil de marca + participación útil, no spam † | [OPINIÓN] |
| **WhatsApp Channels / Telegram** | WhatsApp 3.300–3.500 M MAU [S33]. Telegram: sin datos | Alto como canal de retención en India, MENA, África, LatAm† (modistas comparten moldes por grupos) | Canal con novedades de moldes + enlace a la ficha; indexación en buscadores limitada† | [OPINIÓN]† |
| **Reddit** (r/sewing, r/sewingpatterns) | Estudios de citas arriba (sección 3.2) | Medio: reputación, reseñas, preguntas de "qué molde elegir" | Participación genuina, divulgar afiliación; evitar autopromoción (riesgo de baneo) † | [EVIDENCIA mixta] |
| **Xiaohongshu (RED), Douyin, WeChat (cuentas oficiales/mini-programas), Weibo, Bilibili, Zhihu** | **No investigado.** Solo sé por QuestMobile que Doubao (ByteDance) y Yuanbao (Tencent) compiten en IA [S34] | Se usan como buscador de tendencias de moda/DIY en chino† | Requieren cuenta empresa china, contenido en chino simplificado, y muchas veces ICP/entidad local† | [NO VERIFICADO]† |
| **VK, OK, Dzen, Telegram (Rusia)** | **No investigado.** | Telegram/VK son los canales de comunidad rusófona† | Pagos y operación desde Argentina: ver 5 | [NO VERIFICADO]† |
| **Naver Blog / Cafe / 지식iN, Kakao (KakaoTalk/Daum)** | Naver 64–68 % de búsquedas en Corea [S7]; Blog/Cafe son las superficies que Naver prioriza† | Alto si se apuesta por Corea | Contenido coreano nativo, Search Advisor, publicar en Blog/Cafe además del sitio [S24, S25] | [EVIDENCIA vendors]+† |
| **LINE (Japón/Tailandia/Taiwán), Zalo (Vietnam)** | **No investigado** (Zalo: Vietnam; LINE: JP/TH/TW†) | Cuentas oficiales/Stickers/contacto† | — | [NO VERIFICADO]† |
| **Comunidades tipo Ravelry para costura** | **No hay un equivalente único**†; hay sitios de reseñas/comunidad (p. ej. PatternReview, The Fold Line, Makerist) † | Medio-alto en inglés/alemán | Fichas y reseñas con enlaces | [NO VERIFICADO]† |

### 4.2 Qué significa para el nicho

El patrón consistente es: **descubrimiento visual/vídeo (Pinterest, YouTube, TikTok) → comunidad (Facebook, WhatsApp, Reddit) → compra en sitio propio o marketplace de digitales**. Los asistentes de IA citan sobre todo YouTube y Reddit, así que un molde "visible" necesita **un vídeo y un hilo/ficha independientes**, no solo la página de producto. [OPINIÓN apoyada en S50, S52]

---

## 5. Marketplaces regionales y política de productos digitales

> Ninguna política fue verificada en esta sesión. Todo lo de esta tabla es **† hipótesis**: **leer los términos del vendedor de cada plataforma antes de listar**. Subir archivos descargables a un marketplace de bienes físicos suele violar sus normas y puede suspender la cuenta [OPINIÓN].

| Plataforma | Región | ¿Acepta productos digitales? † | Nota |
|---|---|---|---|
| **Etsy** | Global (EN/DE/FR/ES/IT/NL/PT/TR/JA/PL) | **Sí** (descargas instantáneas; categoría grande de patrones de costura) | Verificar si **Etsy Payments opera en Argentina** (cobro/retiro) y comisiones. Competencia muy alta. |
| **Creative Market** | Global | Sí (curado, requiere aprobación) | Más diseño gráfico que costura. |
| **Gumroad, Payhip** | Global | **Sí** | Gumroad opera como comerciante de registro (impuestos) † ; Payhip maneja IVA UE †. |
| **Hotmart, Eduzz, Kiwify** | Brasil (Hotmart también LatAm/España) | **Sí** (infoproductos: cursos, PDF) | Clave para portugués; usan PIX y boleto †. |
| **BOOTH (Pixiv), note, Minne/Creema** | Japón | BOOTH y note: **sí** para digital; Minne/Creema: orientados a artesanía física, digital limitado † | Para patrones japoneses (型紙) † verificar. |
| **Shopee, Lazada, Tokopedia (+TikTok), Bukalapak** | SE Asiático | **Mayormente NO** (bienes físicos; digital muy restringido) | No para archivos. Sí para ads y TikTok Shop si se vendiera físico. |
| **Mercado Libre** | LatAm | **Probablemente NO** para archivos descargables | Verificar. |
| **Trendyol, Hepsiburada** | Turquía | **Probablemente NO** | Etsy ha sido canal habitual de vendedores turcos †. |
| **Allegro** | Polonia | Probablemente NO | — |
| **Naver Smartstore, Coupang** | Corea | Probablemente NO (físico) | Class101/Idus †: no verificado. |
| **Taobao/Tmall, Pinduoduo, Xianyu** | China | Taobao tiene categoría virtual pero **exige entidad china** | Fuera de alcance etapa 1. |
| **Ozon, Wildberries, Yandex Market, Avito** | Rusia | Probablemente NO; además **sin pagos Visa/Mastercard internacionales** desde 2022 † | Fuera de alcance etapa 1. |
| **Jumia, Konga** | África | Probablemente NO | Pagos locales (M-Pesa, Paystack/Flutterwave) † . |
| **Flipkart, Meesho** | India | Probablemente NO | UPI y pagos locales † . |
| **Noon, Amazon.ae** | Golfo | Probablemente NO | — |
| **Kaspi** | Kazajistán | Probablemente NO | — |

---

## 6. Hábitos de búsqueda y consumo por macro-región

> Esta sección es mayormente **† hipótesis**; los únicos anclajes con fuente son las cifras entre corchetes. No hallé datos de voz, imagen, % Android ni velocidad móvil por región.

| Macro-región | Hábitos probables † | Anclas con fuente |
|---|---|---|
| **Sur de Asia** (India, Pakistán, Bangladesh, Sri Lanka, Nepal) | Móvil-first, Android dominante, WhatsApp, YouTube y Meta; búsqueda por voz y en idioma local; conexión variable; mucho consumo de contenido en hindi/bengalí/tamil. | YouTube India ≈518 M [S53]; ChatGPT India 100 M semanales [S27]; Meta AI India ≈21 % de MAU [S31]. |
| **Sudeste Asiático** | Móvil-first, Facebook/TikTok/Shopee; social commerce; Zalo (VN), LINE (TH). | TikTok Indonesia 180 M [S55]; Coc Coc 3,6 % en Vietnam [S13]. |
| **Asia Oriental** | Ecosistemas propios (Baidu/WeChat; Naver; Yahoo/LINE). | Naver 66,7 %/Google 26,1 % [S7]; Bing 44,9 % en escritorio japonés [S9]; Baidu 47–51 % (poca fiabilidad) [S3]. |
| **Medio Oriente / Norte de África** | Móvil-first, WhatsApp, Instagram, TikTok, Snapchat (Golfo); mezcla árabe/dialecto/francés/inglés. | Pinterest añadió árabe [S47]. |
| **África subsahariana** | Móvil con datos caros, WhatsApp/Facebook/TikTok/YouTube; pagos móviles; inglés/francés/suajili/hausa/amárico. | Sin dato. |
| **Europa Oriental/Central** | Google dominante salvo Rusia, Kazajistán (Yandex), Chequia (Seznam). | Rusia Yandex 71 %, Kazajistán Yandex ≈28 %, Chequia Seznam 13,5 % [S4–S6, S11]. |
| **Europa Occidental** | Google ~91 %, Pinterest/YouTube/Instagram, cultura de patrones PDF consolidada (alemán, francés, neerlandés). | Google 91 % [S14]; Pinterest Alemania ≈23 M [S45]; Pinterest Europa 159 M MAU [S43]. |
| **Latinoamérica** | WhatsApp-first, Facebook grupos, Instagram, TikTok, Pinterest; el español y el portugués dominan la compra. | Pinterest Brasil ≈40 M y México ≈27 M [S45]; TikTok Brasil 131 M, México 99 M [S55]; Meta AI Brasil ≈9 % [S31]. |
| **Norteamérica** | Google+Bing, Pinterest/YouTube/Reddit/Etsy; compra en inglés; ChatGPT/Gemini/Perplexity más usados. | Pinterest EE. UU. ≈96 M [S45]; TikTok EE. UU. 153 M [S55]. |
| **Oceanía** | Similar a Norteamérica; inglés. | Sin dato. |

**Reglas generales [OPINIÓN]:** (a) la **velocidad y el peso de la página** importan por la cuota móvil (Google ≈95 % móvil europeo [S14]); (b) las **imágenes** (pins, miniaturas de patrones, vista previa del PDF) son una vía de entrada en todas las regiones; (c) el idioma local gana al inglés al comprar, salvo en vertical de nicho técnico; (d) **fuentes tipográficas Unicode** (birmano, jemer, lao) y evitar Zawgyi †.

---

## 7. Cuadro final: región/idioma → dónde ser visible

> Es una **síntesis mía** apoyada en las cifras de las secciones 2–6; lo marcado † no tiene fuente en esta sesión. Prioridad sugerida: **A** (etapa 1), **B** (etapa 2), **C** (etapa 3 o solo si hay señal de demanda).

| Idioma / grupo | Buscador (prioridad) | Plataformas de descubrimiento | Asistente de IA | Venta/marketplace † | Prior. |
|---|---|---|---|---|---|
| **Inglés** | Google; Bing/Bing WMT | Pinterest, YouTube, Reddit, Instagram, TikTok, Etsy | ChatGPT, Gemini/AI Overviews, Perplexity, Copilot, Claude | Sitio propio, Etsy, Gumroad/Payhip | **A** |
| **Español** (LatAm + España) | Google | Pinterest (México ≈27 M), YouTube, Facebook grupos, Instagram, TikTok, WhatsApp | ChatGPT, Gemini, **Meta AI (WhatsApp)** | Sitio propio, Etsy; Hotmart (LatAm) | **A** |
| **Portugués** (Brasil) | Google | Pinterest (≈40 M), TikTok (131 M), YouTube, Instagram, WhatsApp | Meta AI, ChatGPT, Gemini | Hotmart/Eduzz/Kiwify, sitio propio | **A** |
| **Francés** (Francia, Bélgica, Canadá, África francófona) | Google (Ecosia/Qwant marginales) | Pinterest, YouTube, Instagram, Facebook; WhatsApp en África | ChatGPT, Gemini, Le Chat† | Etsy, sitio propio | **A/B** |
| **Alemán** | Google; Ecosia (algo) | Pinterest (≈23 M), YouTube, Instagram; Makerist† | ChatGPT, Gemini | Etsy, sitio propio | **B** |
| **Italiano** | Google | Pinterest, Instagram, YouTube, Facebook grupos † | ChatGPT, Gemini | Etsy | **B** |
| **Neerlandés** | Google | Pinterest, YouTube, Instagram, Facebook† | ChatGPT, Gemini | Etsy | **B** |
| **Ruso / ucraniano** | **Yandex (≈71 %)** + Google (≈27 %); Ucrania: Google | VK, Telegram, Dzen, YouTube (acceso variable†) | **Alice AI/YandexGPT**, GigaChat, DeepSeek | Fuera de alcance (pagos†) | **C** |
| **Polaco / checo / húngaro / rumano** | Google; **Seznam (CZ 13,5 %)** | Facebook grupos, YouTube, Pinterest, Instagram | ChatGPT, Gemini | Allegro (PL)†, Etsy | **B/C** |
| **Turco** | Google (Yandex minoritario, sin dato) | Instagram, YouTube, Pinterest | ChatGPT, Gemini | Etsy; Trendyol (físico) † | **B** |
| **Árabe** (MSA + dialectos) | Google | Instagram, TikTok, YouTube, Snapchat (Golfo)†, Pinterest (árabe disponible), WhatsApp/Telegram | ChatGPT, Gemini, Meta AI; Jais/Falcon (sin datos) | Etsy; Noon (físico) | **B** |
| **Persa** | Google; (restricciones locales †) | Telegram/Instagram con VPN, Aparat† | Poco | Pagos internacionales imposibles † | **C** |
| **Hebreo** | Google | Facebook, Instagram, WhatsApp | ChatGPT, Gemini | Etsy | **C** |
| **Hindi / urdu / bengalí / marathi / tamil / telugu / gujarati / kannada / malayalam** | Google | **YouTube (≈518 M)**, WhatsApp, Facebook, Instagram | **ChatGPT (100 M sem.)**, **Meta AI (≈21 %)**, Gemini | Instamojo/Razorpay† , Gumroad | **B** |
| **Nepalí / cingalés** | Google | Facebook, YouTube | ChatGPT, Gemini | — | **C** |
| **Chino simplificado** | **Baidu** + Bing CN; ICP | Xiaohongshu, Douyin, WeChat, Bilibili, Zhihu | **Doubao (382 M)**, Qwen (167 M), DeepSeek (130 M), Yuanbao, Kimi, Ernie | Taobao/Tmall (entidad china) | **C** |
| **Chino tradicional** (Taiwán/HK) y **cantonés** | Google | Facebook, Instagram, YouTube, LINE (TW)† | ChatGPT, Gemini, Copilot | Shopee TW, Etsy† | **C/B** |
| **Japonés** | Google + **Bing (escritorio)** + Yahoo! Japón | Pinterest (sin dato), YouTube, X†, Instagram, LINE†; **BOOTH/note** | ChatGPT, Gemini, Copilot | BOOTH, note, Etsy | **B** |
| **Coreano** | **Naver (≈66 %)**, Google | **Naver Blog/Cafe/지식iN**, YouTube, Instagram, Kakao | Naver AI Briefing/AI Tab, Gemini, ChatGPT | Etsy, Class101†, sitio propio | **B/C** |
| **Vietnamita** | Google (≈96 %), Coc Coc (3,6 %) | Facebook, TikTok, Zalo†, YouTube | ChatGPT, Gemini | Shopee/Lazada (físico) | **C** |
| **Tailandés** | Google | Facebook, LINE†, TikTok, YouTube | ChatGPT, Gemini | Shopee/Lazada (físico) | **C** |
| **Indonesio / malayo / javanés** | Google | **TikTok (180 M)**, YouTube, Instagram, WhatsApp, Facebook | **Meta AI (≈7 % MAU)**, ChatGPT, Gemini | Tokopedia/Shopee (físico) | **B/C** |
| **Filipino / cebuano** | Google | Facebook-first, YouTube, TikTok | ChatGPT, Meta AI, Gemini | Shopee/Lazada (físico) | **C** |
| **Birmano / jemer / lao** | Google | Facebook, Telegram, YouTube; **Unicode** (no Zawgyi) † | ChatGPT, Gemini | — | **C** |
| **Kazajo / uzbeko / azerí** | Kazajistán: Google 68 % + Yandex 28 %; Uzbekistán/Azerbaiyán: sin dato | Telegram, Instagram, YouTube | ChatGPT, Gemini, Alice† | Kaspi (físico) † | **C** |
| **Suajili / hausa / yoruba / igbo / amárico / oromo / somalí / zulú / xhosa** | Google | WhatsApp, Facebook, TikTok, YouTube | ChatGPT, Meta AI, Gemini (soporte limitado en idiomas de pocos recursos †) | Pagos móviles; Selar† | **C** |

**Nota de método:** la columna de buscador solo está respaldada con cifras en EE. UU./Europa/Rusia/Kazajistán/Corea/Japón/China/Chequia/Vietnam; en el resto es una hipótesis †.

---

## 8. Contradicciones y puntos controvertidos

1. **Cuota global**: StatCounter jul-2026 (Google ≈91,3 %) vs. compilación de ene-2026 (≈89,3 %) y abril (89,85 %). Yandex 1,0 % ↔ 2,5 %; Baidu 0,5 % ↔ 1,0 %. [S1, S2] Variación mensual alta: no tomar un mes aislado.
2. **China**: StatCounter (Baidu 47–51 %, Bing 23 %, "Yandex" 10–13 %) vs. un analista (Baidu ≈72 %). La cifra de StatCounter mezcla desktop/tablet donde Bing lidera. **Ninguna es fiable**. [S3]
3. **Corea**: Naver 64–68 % vs. Google 26–28 % según firma; pero Google ya iguala en MAU de app y gana en escritorio. [S7, S8]
4. **Japón**: Yahoo! Japón aparece en 6–7 % en StatCounter pese a su importancia histórica. [S9]
5. **ChatGPT**: 900 M semanales (oficial, feb-2026) vs. 1.200 M (única fuente, sep-2026). [S28, S29]
6. **Meta AI**: 640 M vs 1.200 M según definición. [S31, S32]
7. **Reddit/YouTube en citas de IA**: tres estudios, tres rankings. [S50–S52]
8. **ICP**: las guías discrepan sobre si una empresa extranjera puede tramitarlo sin socio local. [S22]
9. **Pinterest**: DataReportal ene-2025 (por país) vs. 10-Q 2026 (por región): períodos distintos; cifras por país de agregadores 2026 inconsistentes.

---

## 9. Fuentes (solo URLs que aparecieron en los resultados de búsqueda)

- [S1] StatCounter global: https://gs.statcounter.com/search-engine-market-share (jun/jul-2026)
- [S2] https://searchlab.nl/en/statistics/search-engine-market-share-statistics-2026
- [S3] StatCounter China: https://gs.statcounter.com/search-engine-market-share/all-worldwide/china
- [S4] https://www.intellinews.com/yandex-captures-70-of-russia-s-search-market-outpacing-google-436161/ (abr-2026)
- [S5] https://gs.statcounter.com/search-engine-market-share/all-platforms/russian-federation
- [S6] https://gs.statcounter.com/search-engine-host-market-share/all/kazakhstan
- [S7] https://www.link-assistant.com/blog/google-vs-naver-why-cant-google-dominate-search-in-korea/ ; https://www.seoulz.com/naver-vs-google-korea/
- [S8] https://www.interad.com/en/insights/google-overtakes-naver-in-monthly-users-what-does-it-mean-for-marketing-in-korea
- [S9] https://gs.statcounter.com/search-engine-market-share/all-platforms/japan
- [S10] https://japanbuzz.info/data/popular-search-engines-in-japan/
- [S11] https://gs.statcounter.com/search-engine-host-market-share/all/czech-republic
- [S12] https://www.wmtips.com/technologies/webmaster-tools/country/cz/
- [S13] https://gs.statcounter.com/search-engine-market-share/all-platforms/viet-nam ; https://gs.statcounter.com/search-engine-host-market-share/all/viet-nam
- [S14] https://ahrefs.com/benchmarks/search-engine-market-share/europe (act. 8-oct-2026)
- [S15] https://gs.statcounter.com/search-engine-market-share/europe/france
- [S16] https://brave.com/learn/best-search-api-2026
- [S17] https://piunikaweb.com/2026/06/30/brave-claude-cowork-web-research/
- [S18] https://cloro.dev/blog/brave-search-api-vs-serp-api/
- [S19] https://geotoolbox.ai/blog/bing-webmaster-tools.md
- [S20] https://apps.shopify.com/indexnow
- [S21] https://brunch.co.kr/@beusable/391
- [S22] https://appinchina.co/blog/the-complete-guide-to-chinas-icp-filing/ ; https://www.registrationchina.com/articles/apply-China-icp-license/
- [S23] https://intl.aliyun.com/icp ; https://edgeone.ai/blog/details/the-ultimate-guide-to-icp-filing
- [S24] https://inblog.ai/docs/seo-tutorial-domain-setup/registering-with-naver-search-advisor
- [S25] https://www.linguise.com/blog/guide/naver-seo-guide/
- [S26] https://www.koreatimes.co.kr/amp/business/tech-science/20251215/navers-ai-powered-search-surpasses-20-milestone
- [S27] https://proaisearch.com/chatgpt-users-india/
- [S28] https://www.demandsage.com/chatgpt-statistics/
- [S29] https://technologychecker.io/blog/chatgpt-statistics
- [S30] https://vertu.com/ai-tools/gemini-one-billion-users-alphabet-q2-2026 ; https://www.getpanto.ai/blog/google-gemini-statistics
- [S31] https://presenc.ai/research/meta-ai-usage-statistics-2026
- [S32] https://aibusinessweekly.net/p/meta-ai-statistics
- [S33] https://www.demandsage.com/whatsapp-statistics/
- [S34] https://technode.com/2026/07/14/questmobile-chinas-ai-native-apps-reach-499-million-monthly-active-users/ (14-jul-2026)
- [S35] https://www.secondtalent.com/resources/top-5-chinese-ai-search-engines/
- [S36] https://aisearch.similarweb.com/blog/gen-ai-stats/
- [S37] https://ppc.land/chatgpt-drops-to-52-7-as-claude-triples-its-ai-traffic-share/
- [S38] https://officechai.com/ai/geminis-traffic-share-rises-above-25-in-march-2026-chatgpt-slips-to-56-similarweb-data/
- [S39] https://techcrunch.com/2025/06/05/perplexity-received-780-million-queries-last-month-ceo-says/
- [S40] https://www.gradually.ai/en/perplexity-statistics/
- [S41] https://www1.ru/en/news/2026/04/21/ii-iandeksa-obognal-chatgpt-i-deepseek-po-populiarnosti-v-rossii.amp.html (21-abr-2026)
- [S42] https://www.sec.gov/Archives/edgar/data/0001506293/000150629326000102/q2-26xpressrelease.htm (Pinterest 8-K T2-2026)
- [S43] https://www.sec.gov/Archives/edgar/data/0001506293/000150629326000104/pins-20260630.htm ; T1: https://www.sec.gov/Archives/edgar/data/0001506293/000150629326000068/pins-20260331.htm
- [S44] https://socialmediatoday.com/news/pinterest-leans-on-ai-to-drive-improved-performance-in-q2/827033
- [S45] https://www.socialpilot.co/es/blog/pinterest-statistics
- [S46] https://www.ypulse.com/newsfeed/2022/11/30/speaking-of-diverse-languages-pinterest-is-broadening-their-global-accessibility-by-adding-new-languages-to-the-app/
- [S47] https://ppc.land/pinterest-now-supports-arabic
- [S48] https://www.tailwindapp.com/blog/?p=13458
- [S49] https://alttext.ai/blog/pinterest-description-visual-search
- [S50] https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138
- [S51] https://machinerelations.ai/research/reddit-most-cited-domain-ai-search-mri-citation-rate-data-2026
- [S52] https://quickseo.ai/blog/how-reddit-affects-ai-visibility-2026 (agregador; cita a LLM Pulse)
- [S53] https://www.statista.com/statistics/280685/number-of-monthly-unique-youtube-users/
- [S54] https://www.socialpilot.co/youtube-marketing/youtube-statistics
- [S55] https://statista.com/statistics/1299807 (TikTok, oct-2025)
- [S56] https://searchlab.nl/en/statistics/tiktok-statistics-2026
- [S57] https://countly.net/s/countly/tiktok-users-by-country-2026-top-rankings-growth-trends
- [S58] https://www.stackmatix.com/blog/naver-seo
- [S59] https://seoquick.com.ua/en/bing-webmaster/

**Lagunas a cerrar en un seguimiento** (requieren más búsquedas): ecosistema chino (Xiaohongshu/Douyin/WeChat) y sus reglas para cuentas extranjeras; VK/Dzen/Telegram; Zalo/LINE/Kakao; políticas de productos digitales (Etsy en Argentina, Mercado Libre, Shopee, BOOTH); Rich Pins y Shopping en Pinterest; cifras de Copilot, Claude, Kimi, Ernie, GigaChat, Sarvam, Jais; hábitos móviles (Android, voz, imagen) por región; cuotas en India/LatAm/MENA/África.

---

## 10. Qué hacer en moldey.com (priorizado)

Escala: **Impacto** (A/M/B) × **Esfuerzo** (B/M/A). Se hacen primero las de impacto alto y esfuerzo bajo.

| # | Acción | Impacto | Esfuerzo | Por qué (fuente) |
|---|---|---|---|---|
| 1 | **Alta en Google Search Console y Bing Webmaster Tools; activar IndexNow** (plugin o CMS); enviar sitemaps por idioma con hreflang. | **A** | **B** | Bing alimenta Copilot y, según la industria, ChatGPT Search; Bing pesa en escritorio (Japón 44,9 %, Europa ≈12 %) [S9, S14, S19–S21]. |
| 2 | **Mantener abiertos los rastreadores de búsqueda y de IA** (Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, PerplexityBot) en `robots.txt`; decidir aparte los de entrenamiento †. | **A** | **B** | Sin acceso no hay cita posible. |
| 3 | **Pinterest como canal principal de descubrimiento**: cuenta de empresa, reclamar dominio, pines verticales 2:3 con título/descr./nombre de archivo en el idioma de cada mercado, un tablero por tipo de prenda. Empezar en **inglés, español (México), portugués (Brasil) y alemán**. | **A** | **M** | 640 M MAU; el crecimiento es fuera de EE. UU./Canadá; Brasil ≈40 M, México ≈27 M, Alemania ≈23 M [S42–S45]. Verificar si Rich Pins/Shopping aceptan producto digital. |
| 4 | **YouTube**: vídeo por molde ("cómo imprimir y armar PDF A4/Letter/A0", "cómo coser"), con títulos, descripciones y subtítulos traducidos. | **A** | **M** | YouTube entre los dominios más citados por IA y 518 M de alcance en India [S50, S52, S53]. |
| 5 | **Etapa 1 de idiomas: inglés, español, portugués (BR); etapa 2: francés, alemán, italiano, neerlandés, turco, árabe, hindi, indonesio, japonés.** Contenido nativo, no solo traducción. | **A** | **M-A** | Sección 7. |
| 6 | **Vender en dos o tres canales de digitales además del sitio**: Etsy (EN; confirmar pagos desde Argentina), Hotmart/Kiwify (BR), Gumroad/Payhip como respaldo; BOOTH/note (JP) en etapa 2. | **A** | **M** | Aceptan digitales †; verificar términos y retención de impuestos. |
| 7 | **Comunidades**: canal de WhatsApp y/o Telegram para novedades; presencia útil en 2–3 grupos de Facebook por idioma; participación honesta en r/sewing y r/sewingpatterns. | **M** | **M** | WhatsApp 3.300–3.500 M MAU; Meta AI fuerte en India, Brasil, Indonesia, México [S31, S33]; Reddit citado por IA con controversia [S50–S52]. |
| 8 | **Medir tráfico desde IA** en analítica (referers de chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai) y revisar mensualmente si el asistente cita la marca. | **M** | **B** | StatCounter no mide IA [S1]; las cuotas de asistentes cambian rápido (ChatGPT 77 %→56 %, Gemini 6 %→25 % en un año) [S36, S38]. |
| 9 | **Rendimiento móvil**: páginas livianas, miniaturas WebP, vista previa del PDF liviana, texto alt descriptivo por molde. | **M** | **M** | Móvil ≈95 % de Google en Europa [S14]; Pinterest/imagen como vía de entrada [S48, S49]. |
| 10 | **Corea (etapa 2, condicionada a demanda)**: Naver Search Advisor, contenido coreano revisado por nativo, versión en Naver Blog/Cafe. | **M** | **A** | Naver 64–68 %, AI Briefing >20 % de búsquedas [S7, S24–S26]. |
| 11 | **Yandex Webmaster / Seznam solo si se publica en ruso o checo**; en ese caso con IndexNow. | **B** | **B** | Yandex 71 % en Rusia, Seznam 13,5 % [S5, S11]. |
| 12 | **Pagos locales** (PIX en Brasil, UPI en India, Mercado Pago/transferencias en LatAm) o un comerciante de registro que los cubra; confirmar retiro de fondos a Argentina. | **A** | **M** | Condiciona la conversión † [OPINIÓN]. |
| 13 | **Cerrar las lagunas de la sección 9** antes de decidir China/Rusia/Japón. | **M** | **M** | — |

---

## 11. Qué NO hacer

1. **No invertir en Baidu/ICP, Tmall o Xiaohongshu en etapa 1**: el ICP exige entidad china, 20–60 días hábiles y USD 3.000–15.000 según proveedores, más PSB y licencias si hay cobro [S22, S23]; Baidu es solo ~0,5 % global [S1]. Reevaluar si hay socio local.
2. **No asumir que posicionar en Google implica visibilidad en Naver, Yandex o Baidu**: son índices distintos con registro propio [S24, S25].
3. **No subir archivos descargables a marketplaces de bienes físicos** (Shopee, Lazada, Mercado Libre, Trendyol, Ozon, Wildberries, Flipkart, Jumia, etc.) sin leer sus términos †: riesgo de baja de la cuenta.
4. **No usar traducción automática sin revisión en coreano, japonés, árabe, hindi o ruso**: la calidad de la búsqueda en idioma local depende de términos nativos de costura [S25].
5. **No citar cifras de blogs agregadores como si fueran oficiales** (ChatGPT 1.200 M, Meta AI 1.200 M, WhatsApp India 853 M, Reddit "40 % de las citas de IA") [S29, S32, S33, S52].
6. **No tratar a Reddit/Facebook como buzón de promoción**: baneos, y el peso de Reddit en citas de IA depende del asistente [S51].
7. **No abrir 100 idiomas de golpe** con páginas finas o duplicadas: priorizar por la tabla de la sección 7 y por señal de demanda.
8. **No bloquear rastreadores de búsqueda de IA por precaución genérica** (puede quitar a moldey.com de ChatGPT/Perplexity/Claude/Copilot) sin distinguirlos de los de entrenamiento †.
9. **No vender hacia Rusia o Irán** sin resolver pagos y cumplimiento (sanciones/restricciones) †.
10. **No basar la estrategia en la cuota de un solo mes de StatCounter**: Yandex y Baidu fluctúan 2–3× entre compilaciones [S1, S2].
