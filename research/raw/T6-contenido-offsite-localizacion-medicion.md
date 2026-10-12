# T6 — Contenido multilingüe a escala, SEO off-site y medición (2025–2026)

**Para:** moldey.com (moldes digitales de costura: PDF A4/Letter/A0, DXF/CAD, plantillas para sublimar). **Fecha del informe:** 12-oct-2026.

## 0. Método, límites y cómo leer las etiquetas

- **Límite de la investigación (importante).** Hice ~24 búsquedas efectivas; después el tope de búsquedas del turno (compartido entre agentes) se agotó y no pude seguir. WebFetch tampoco funciona (DNS). Por eso:
  - Las secciones **1 (parte), 2, 5 y 6 (parte)** tienen fuentes de esta sesión con URL.
  - Las secciones **3, 4, 6 (benchmarks de plazos) y 7** descansan sobre todo en conocimiento previo y criterio propio. Están marcadas **[OPINIÓN]** o **[NO VERIFICADO]**. No les pongo URL inventadas.
  - Nunca vi la política de spam de Google ni la documentación oficial de las herramientas en su fuente primaria. Todo lo que cito de Google sale de su blog, de su Search Status Dashboard (vía resultados de búsqueda) o de prensa especializada.
- **Etiquetas:** **[HECHO]** = fuente primaria o casi primaria. **[EVIDENCIA]** = estudio o dato de terceros con método. **[OPINIÓN]** = consejo de industria o criterio mío sin prueba. **[NO VERIFICADO]** = no lo pude confirmar.
- **Sesgo de las fuentes:** la mayoría de las guías de "SEO multilingüe" y "costos de traducción" son de agencias de traducción o vendedores de herramientas. Tienen interés comercial. Las cifras sin metodología se tratan como orientativas.
- **Contexto del proyecto:** `data/idiomas-master.csv` lista 100 idiomas más 13 extra. De los 100, **71 tienen sitio propio** y **29 se atienden con otro idioma**. Son variedades del árabe, lenguas del grupo hindi, variedades del chino, javanés y sundanés vía indonesio, cebuano vía filipino/inglés, etc. Es decir, hay unos **~71–84 sitios localizados reales**, no 113. Además, **21 idiomas están marcados "poca búsqueda escrita"** (hausa, yoruba, igbo, oromo, zulú, tigriña, quechua, etc.).

---

## 1. Localización vs. traducción y keyword research multilingüe

### 1.1 Principio
- **[OPINIÓN, con respaldo de la lógica del propio proyecto]** No se traducen las palabras clave del inglés; se investigan en cada idioma. El caso típico es "molde": en español puede ser un recipiente de cocina, y "pattern" en inglés también es "estampado". Lo mismo vale para "imprimir en casa", "hoja A4/Carta" y "sublimación", que la gente nombra distinto en cada lugar. Las guías de agencias dicen lo mismo: [adhoc-translations (2026)](https://www.adhoc-translations.com/blog/multilingual-seo), [translated.com](https://translated.com/resources/search-queries-dont-translate-multilingual-keyword-strategy).
- **Contradicción/cautela:** una guía afirma que los sitios traducidos "rinden 40–60% menos" en mercados no ingleses ([adhoc-translations, 2026](https://www.adhoc-translations.com/?p=47775)), pero **no cita fuente**. Otra ([betranslated](https://betranslated.com/digital/services/seo/multilingual-keyword-research/)) dice que la investigación nativa da más tráfico, sin datos independientes. **[NO VERIFICADO]** como cifra; el principio sí es razonable.
- **Transcreación** (adaptar, no solo traducir): en moldería significa cambiar el ejemplo de prenda, el sistema de tallas, la unidad (cm/pulgadas), el papel (A4/Carta), las telas locales y los métodos de pago. No encontré estudios que midan su efecto en SEO. **[OPINIÓN]**

### 1.2 Herramientas de keyword research por mercado

| Mercado / fuente | Qué da | Costo / acceso | Estado de verificación |
|---|---|---|---|
| **Google Search Console** | Consultas reales por país/página una vez que hay impresiones | Gratis | **[HECHO]** conocido; no sirve para descubrir demanda antes de lanzar |
| **Bing Webmaster – Keyword Research** | Volumen (en impresiones, datos orgánicos "crudos"), consultas relacionadas y preguntas; selector de país e idioma | Gratis, pero hay que verificar un sitio en Bing WMT | **[EVIDENCIA]** [Practical Ecommerce](https://www.practicalecommerce.com/using-bings-keyword-research-tool), [Search Engine Watch](https://searchenginewatch.com/?p=145991). No hallé cambios 2025–26 en la metodología |
| **Yandex Wordstat** (ru, uk, kk, uz, az, tr) | Frecuencias por región, "dinámica" de 2 años mensual, histórico desde ene-2018 | Requiere login Yandex; hay API en Yandex Cloud con cuota | **[HECHO]** docs de Yandex: [interfaz](https://yandex.com/support2/wordstat/en/interface/new), [API](https://yandex.cloud/en/docs/search-api/operations/wordstat-gettop). Si es gratis o no el acceso de web: no confirmado |
| **Baidu Index / 5118 / Aizhan** (zh-Hans) | Tendencias, demografía, minería de palabras | Cuentas chinas; el trámite suele pedir datos locales | **[EVIDENCIA débil]** [Chinafy](https://www.chinafy.com/blog/how-to-conduct-keyword-research-for-baidu-seo), [Daxue](https://daxueconsulting.com/baidu-seo-make-optimisation-for-china/). Advierten no traducir keywords del inglés. Hostear fuera de China es lento y para hostear en China hace falta licencia ICP |
| **Naver SearchAd (keyword tool) y DataLab** (ko) | Volumen mensual (no promedio) estilo Keyword Planner "recortado"; DataLab da tendencias con filtros de edad/género | SearchAd exige cuenta de anunciante, a veces con registro/teléfono local | **[EVIDENCIA débil]** [The Egg](https://www.theegg.com/seo/korea/naver-keyword-tool-explained/), [Interad](https://interad.com/en/insights/introduction-to-naver-data-lab). Naver favorece contenido dentro de su propio ecosistema (blogs/cafés) |
| **Google Keyword Planner, Google Trends, YouTube autosuggest, Pinterest Trends, AnswerThePublic, Semrush/Ahrefs (bases por país), Keyword Insights** | Volúmenes, estacionalidad, preguntas, long tail | Keyword Planner gratis con cuenta Ads (rangos si no hay gasto); Semrush/Ahrefs de pago; Pinterest Trends gratis con cuenta | **[NO VERIFICADO en esta sesión]** (conocimiento previo, sin URL). Verificar disponibilidad por país antes de apoyarse en ellas |

**Flujo propuesto por idioma (barato, ~1–2 días por idioma) [OPINIÓN]:**
1. Partir de los términos nativos del trabajo de terminología (archivos `terminologia/` A1–A9, que ya piden verificar uso real en tiendas locales, no diccionarios).
2. Autosuggest y "Otras preguntas de los usuarios" en el idioma local, con ajuste de país y ubicación. Anotar variantes de ortografía y anglicismos.
3. Mirar a 5–10 competidores locales (tiendas y editoriales de patrones, Etsy/Shopee/Tokopedia/Trendyol/Mercado Libre, según la región) y registrar cómo titulan sus categorías.
4. Validar con una fuente de volumen disponible en ese mercado (Trends, Wordstat, Naver, Bing, Semrush/Ahrefs, Pinterest Trends).
5. Mapear a intención: informacional (cómo imprimir, tabla de tallas), comercial (molde de X en PDF) y transaccional.
6. Desde el mes 2–3 de vida, corregir con consultas reales de GSC por carpeta.

### 1.3 Idiomas con muy poco volumen
- **[OPINIÓN]** Para los 21 idiomas marcados "poca búsqueda escrita" en el CSV (ha, yo, ig, om, zu, ti, sn, ny, rw, ln, ak, ff, qu, ht, xh, mg, sd, as, ps, ku, pcm), no conviene un sitio completo. La búsqueda real en esos mercados suele hacerse en inglés/francés/español/portugués.
- **Alternativa:** una *página hub* en el idioma local (qué es un molde digital, cómo imprimir y armar, glosario de 30–50 términos, tabla de tallas), con enlaces al catálogo en el idioma de comercio. Sirve a visitantes, cuesta poco y deja la puerta abierta para ampliar con datos.
- **AEO, caso aparte:** Slator reporta que Google traduce automáticamente contenido en inglés dentro de AI Overviews cuando falta contenido nativo ([Slator](https://slator.com/google-flips-stance-on-automatic-ai-translations-requires-content-creators-to-opt-out/), título "requiere opt-out"; solo vi el adelanto). Implicación posible: en idiomas sin contenido local, una buena página en inglés podría alimentar respuestas en ese idioma. **[NO VERIFICADO]** el mecanismo, el alcance y cómo se hace el opt-out.

---

## 2. Flujos de traducción IA + humanos en 2026

### 2.1 Qué dice la evidencia sobre calidad

| Hallazgo | Fuente | Tipo |
|---|---|---|
| WMT25 (tarea general): 30 pares de idiomas; Gemini 2.5 Pro quedó en el grupo ganador en 14 de 15 pares con evaluación humana; las traducciones humanas de referencia solo en 6 de 15 | [machinetranslate.org/wmt25](https://machinetranslate.org/wmt25); informe: [Findings WMT25](https://aclanthology.org/anthology-files/pdf/wmt.real/2025.wmt-1.1.pdf) | **[EVIDENCIA]** |
| Los propios resultados WMT25 indican que los sistemas de punta aún fallan en idiomas de pocos recursos y que las métricas automáticas pierden confiabilidad ahí: correlación con juicio humano < 0,4 en la mayoría de los pares y ~0,1 en portugués–emakhuwa | resumen de búsqueda sobre WMT25 (ACL Anthology); ver el informe general arriba | **[EVIDENCIA]** (no leí el PDF completo; verificar) |
| LLM vs NMT en idiomas de pocos recursos: **resultados mixtos**. En un corpus de salud (OpenWHO, 2025) la ventaja del LLM sobre NMT es mayor en idiomas de pocos recursos, aunque entre modelos abiertos el mejor sigue siendo NLLB-54B. Un estudio en lituano halló LLM por debajo de NMT. Otro en lenguas indígenas halló LLM competitivo | [OpenWHO 2025](https://arxiv.org/pdf/2508.16048), [R2LM 2025](https://aclanthology.org/2025.r2lm-1.13/) | **[EVIDENCIA]**, contradictoria |
| Amárico y oromo con modelos de 2024: Google Translate en chrF++ ≈ 38,8 (am→en) y ≈ 25,0 (en→am); oromo ≈ 41,4 (om→en) y ≈ 34,8 (en→om); Claude (versión de 2024) apenas por debajo | [Claude vs NMT, 2024](https://arxiv.org/pdf/2404.13813) | **[EVIDENCIA]** pero **vieja** (modelos 2024); lo útil es el orden de magnitud: traducir *hacia* estos idiomas es mucho peor que desde ellos |
| Tigriña: un modelo MarianMT sin ajuste da chrF ≈ 10 (casi inutilizable); hizo falta ajuste fino | [arXiv 2509.20209](https://arxiv.org/pdf/2509.20209) | **[EVIDENCIA]** (no es un LLM de frontera) |
| **Omnilingual MT (Meta, mar-2026):** dice cubrir 1.600 idiomas (entiende desde ~1.600, genera hacia ~1.200). Que la salida sea "no trivial" no es lo mismo que de calidad publicable. Un comentarista dice que el resultado es muy malo en idiomas oscuros; no hay evaluación independiente | [paper](https://arxiv.org/pdf/2603.16309), [Slator](https://slator.com/meta-1600-languages-ai-translation/), [HN](https://news.ycombinator.com/item?id=47421749) | **[EVIDENCIA]** de autor, sin replicar |
| **TranslateGemma (Google, ene-2026):** 55 idiomas evaluados (WMT24++), ~500 pares extra sin evaluación completa | [InfoQ](https://www.infoq.com/news/2026/01/google-translategemma-models/) | **[HECHO]** del anuncio |
| Google Translate: **243 idiomas** desde jun-2024 (+110). "Soportado" no es "bueno" | [APH Networks](https://aphnetworks.com/news/28881-google-translate-adds-support-110-languages-its-largest-expansion-ever) | **[EVIDENCIA]** (2024; no hallé cifra 2025–26) |
| DeepL: 36 idiomas en el lanzamiento de vietnamita/tailandés/hebreo; algunos sitios de 2026 dicen "más de 100". Fuentes contradictorias | [DeepL blog](https://www.deepl.com/en/blog/vietnamese-thai-hebrew-launch) | **[NO VERIFICADO]**: revisar la lista oficial |
| Comparativas LLM vs DeepL: un estudio de informes de errores (2025) dio ventaja a GPT-4o sobre DeepL y AWS en métricas automáticas; un preprint con médicos nativos (modelos 2024) puso a Claude > Gemini > ChatGPT en español y urdu, con Gemini mejor en árabe; las guías de vendedores dicen que DeepL gana en idiomas europeos | [arXiv 2502.14338](https://arxiv.org/pdf/2502.14338), [medRxiv](https://www.medrxiv.org/content/10.1101/2024.09.23.24314229.full.pdf), [MachineTranslation.com](https://www.machinetranslation.com/blog/accurate-ai-translators) | **[EVIDENCIA débil]**; no hay ranking fiable por idioma |

**Conclusión práctica [OPINIÓN]:** no existe un "mejor motor" universal. Para cada idioma conviene una **prueba ciega propia**: 30–50 segmentos reales de moldey (título de producto, instrucción de armado, FAQ) traducidos por 2–3 motores, evaluados por 1–2 hablantes nativos. Elegir un motor por idioma y volver a probar cada 6 meses.

### 2.2 Mapa de riesgo por idioma (mi clasificación)
**[OPINIÓN] derivada de la evidencia anterior y del estado general de recursos; validar con la prueba ciega.**

| Nivel | Idiomas del CSV (ejemplos) | Qué hacer |
|---|---|---|
| **A – MT sólida** | es, pt, fr, de, it, nl, ru, pl, tr, ja, ko, zh, id, vi, ar (estándar), uk, cs, ro, sv, el, he | MT + post-edición *ligera* (muestreo) + glosario bloqueado |
| **B – media** | hi, bn, ta, te, mr, ur, fa, th, ms, fil, kn, ml, gu, hu, bg, hr, sr, kk, az, uz | MT + post-edición *completa* de las páginas clave; revisión nativa |
| **C – alto riesgo** | **ne, my, am, ti, om, km, si, lo, sd, ps, ku, as, or**, ha, yo, ig, zu, xh, sn, ny, rw, ln, ak, ff, so, mg, qu, ht | No publicar MT sin editar. Hub corto, traducción humana de lo esencial, 100% revisado por nativo |

**Riesgos específicos:**
- **Birmano:** coexisten Unicode y Zawgyi (el CSV ya lo marca). Hay que verificar que lo que se publica se renderice y se busque en Unicode. **[HECHO en el CSV]**, el impacto SEO no lo medí.
- **Etíopes (am, ti), jemer, lao, cingalés:** escritura con pocas fuentes web, poco texto paralelo y errores sutiles. Los valores chrF++ de arriba lo ilustran.
- **Árabe y variedades:** el CSV indica escribir en estándar con vocabulario local; la MT mezcla a veces dialecto con estándar.
- **Serbio y uzbeko:** cirílico y latín conviven. Una URL = un guion; decidir cuál y no mezclar.
- **Números, fechas y unidades** (separador decimal, calendarios, A4 vs Carta): fallos frecuentes. Resolverlos por plantilla en el sitio, no en la traducción.

**Mitigación [OPINIÓN]:** traducir **una vez** las cadenas de interfaz y las plantillas por humano nativo; glosario obligatorio (200–500 términos de costura, formatos y tallas); retro-traducción (a inglés) de una muestra; revisión nativa de lo que se indexa; todo lo no revisado en **`noindex`** hasta aprobar. SEJ recomienda controles a nivel de página (noindex) y no bloquear con robots.txt ([SEJ](https://www.searchenginejournal.com/google-removes-robots-txt-guidance-for-blocking-auto-translated-pages/548870)).

### 2.3 Herramientas

| Herramienta | Qué es | Precio visto (verificar) |
|---|---|---|
| **DeepL, Google Cloud Translation (NMT / LLM / Adaptive), Microsoft Translator, LLMs (Claude, GPT, Gemini)** | Motores. LLMs permiten instrucciones y glosario en el prompt | Cloud Translation: orden de **~$10–25 por millón de caracteres** (LLM $10, Adaptive ≈ $25 inferido de un ejemplo) según [Google pricing](https://cloud.google.com/translate/pricing). **Inferencia mía; confirmar en la tabla oficial.** El costo del motor es despreciable frente al humano |
| **Lokalise, Crowdin, Smartling (TMS)** | Gestión de traducciones, memorias (TM), glosarios, flujos con revisores | Smartling: humano $0,12–0,20/palabra y "AI translation desde $0,06" ([Smartling](https://smartling.com/blog/translation-rates)). Lokalise y Crowdin: **[NO VERIFICADO]**, se agotó mi cupo de búsqueda |
| **WPML, Polylang, TranslatePress** (WordPress) | Plugins | WPML €39/99/199 al año (créditos de IA en los planes altos); Polylang Pro €99/año (DeepL solo en Pro); TranslatePress ~€95–99/año con cupos de 50.000–500.000 palabras de IA ([NexterWP](https://nexterwp.com/blog/wpml-vs-polylang-vs-translatepress/), [Donweb](https://blog.donweb.com/alternativas-wpml-traduccion-wordpress-barata/)) |
| **Weglot, GTranslate** (superposición/proxy) | Traducen "al vuelo" | Weglot desde ~€150–180/año, topes de palabras sin confirmar. **[NO VERIFICADO]** si el plan gratuito de GTranslate indexa o solo traduce en el navegador (si es del lado del cliente, no sirve para SEO) |
| **ProZ, Upwork, Gengo, Unbabel** | Mercados de traductores/servicios | Gengo ≈ $0,08/palabra ([Toolradar](https://toolradar.com/tools/gengo/pricing)); Unbabel cotiza por mezcla humano/IA, sin tarifa pública ([Vendr](https://www.vendr.com/marketplace/unbabel)) |

**Decisión abierta:** hay que saber en qué plataforma está moldey.com (¿WordPress, Shopify, a medida?). Eso determina si se usan plugins o una TMS con exportación a archivos, y cómo se sirven las URLs por idioma (subdirectorios).

### 2.4 Costos realistas (cálculo propio con las tarifas citadas)
Tarifas de las fuentes: humano completo **$0,08–0,30/palabra** (Alconost: fr $0,10, de $0,11, ja $0,14, es/it $0,08; [Alconost](https://alconost.com/en/blog/localization-cost)); MTPE **$0,03–0,15** (liviana $0,03–0,08, completa $0,06–0,15; [guía MTPE](https://chatscontrol.com/blog/mtpe-rates-pricing-models-agencies)). La ganancia de productividad del MTPE depende del par: en 90 millones de palabras, en→fr fue 130% más rápido, en→pl 18% y en→sv 7% **más lento** ([SwissGlobal vía ChatsControl](https://chatscontrol.com/blog/post-editing-productivity-words-per-hour-benchmarks)). Son datos de vendedores, no una encuesta independiente. Para idiomas de nivel C no hallé tarifas; **espere un recargo de 1,5–3x por escasez de traductores [NO VERIFICADO]**.

Supuestos: **corpus núcleo = 15.000 palabras** (portada, categorías, interfaz y checkout, legales, FAQ, glosario, 10 guías); **corpus ampliado = 60.000** (núcleo + 40 guías + plantillas de producto).

| Escenario | Por idioma (núcleo) | Wave 1 (6 idiomas) | ~35 idiomas | ~71 idiomas propios |
|---|---|---|---|---|
| MT + post-edición (0,05–0,12 $/pal.) | $750–1.800 | $4,5–11 mil | $26–63 mil | $53–128 mil |
| Humano completo (0,10–0,20) | $1.500–3.000 | $9–18 mil | $53–105 mil | $107–213 mil |
| Corpus ampliado (×4) | $3.000–7.200 (MTPE) | ~$18–43 mil | — | $213–512 mil |

Mantenimiento: cada producto nuevo (~300 palabras) × N idiomas. **Reducirlo con plantillas y datos estructurados** (tipo de prenda, talla, formato) traducidos desde un glosario, no con texto libre. **[OPINIÓN]**

### 2.5 LQA (control de calidad)
**[OPINIÓN / conocimiento previo]** Marco MQM simplificado: muestrear 10–20% de segmentos por lote, contar errores críticos/mayores/menores, aceptar con p. ej. < 1 error crítico por 1.000 palabras. Revisar siempre: glosario, unidades/medidas, nombres de formatos (DXF, A0), instrucciones de armado y marcado de tallas. Un revisor que *cose* detecta errores que un traductor genérico no. Dado el hallazgo WMT25 de que las métricas automáticas fallan en idiomas de pocos recursos, no confiar en puntajes automáticos para el nivel C.

---

## 3. Contenido que posiciona en moldería y se puede localizar

**Todo este apartado es [OPINIÓN]**: no encontré estudios sobre qué contenido de patrones de costura posiciona mejor. Las ideas siguen la lógica de intención de búsqueda.

| Tipo de contenido | Por qué escala | Cómo hacerlo único por idioma |
|---|---|---|
| **Tablas de tallas por país** y conversor | Alta demanda y fácil de enlazar | Tabla con sistemas locales (UE/US/UK/JP/KR/BR/AR…), medidas en cm o pulgadas, y cómo medirse. Datos propios, no copiados |
| **Cómo imprimir y armar un PDF** (A4/Carta/A0, escala 100%, cuadrado de prueba, proyector, copistería) | Pregunta recurrente y específica de producto | Papel y unidades locales, capturas del programa en el idioma local, errores típicos de cada país |
| **Guías de telas por prenda** | Complementa el molde | Nombres de telas locales y lo que se consigue en ese mercado (a menudo no hay equivalente 1:1) |
| **Glosario de costura multilingüe** | Recurso enlazable y citable por IA | Una entrada por término *con foto y contexto*, no una lista traducida |
| **Tutoriales y vídeo** (YouTube) | Cubre intención "cómo hacer" | Mejor un video local por mercado importante que traducir uno solo |
| **FAQ de formatos** (PDF vs DXF/AAMA vs SVG, A0 para plotter, sublimación) | Diferencial de moldey | Adaptar a las máquinas y proveedores del país |
| **Prendas culturalmente relevantes** (kurta/blusa, abaya, kimono, hanbok, sarong…) | Evita clonar el catálogo | Decisión de catálogo: moldes para prendas locales dan páginas únicas |

**E-E-A-T [OPINIÓN, criterios generales de Google sin URL de esta sesión]:** autoría visible (quién traza los moldes), fotos de prendas *realmente cosidas*, probadores/testers, galería "hecho por vos" con permiso, datos de contacto y política de reembolso claros. **No** crear autores o reseñadores "locales" falsos: es engañoso, y la FTC (EE. UU., 2024) prohibió reseñas falsas **[NO VERIFICADO aquí]**. Si se usa traducción asistida, declarar el flujo y mostrar el nombre del revisor nativo es un buen diferenciador.

---

## 4. Off-site, PR y enlaces por idioma

**Aviso:** no pude buscar esta sección; es conocimiento previo y criterio **[OPINIÓN]** salvo donde indico.

| Palanca | Cómo aplicarla | Riesgos |
|---|---|---|
| **Creadores locales** (bloggers/YouTubers de costura) | Enviar el molde gratis a cambio de una reseña con enlace y código de afiliado. En cada idioma, un creador pequeño y real rinde más que una campaña masiva | Declarar el vínculo comercial (rel="sponsored" o "nofollow" en enlaces pagos/afiliados) |
| **Escuelas de moda y ferias** | Licencias educativas gratis a cambio de mención en recursos del curso | Es esfuerzo humano; poco escalable |
| **Comunidades** (Reddit, Facebook, Pinterest, Telegram, VK, LINE, Zalo, WhatsApp, Naver Cafe) | Participar con ayuda real; Pinterest como canal de descubrimiento visual | Autopromoción se ve como spam; cada comunidad tiene reglas |
| **Corea:** Naver prefiere contenido dentro de Naver (blogs/cafés) más que enlaces externos | Presencia en blog de Naver ([The Egg](https://www.theegg.com/seo/korea/naver-keyword-tool-explained/)) | **[EVIDENCIA débil]** |
| **Digital PR con datos propios** | "Tabla de tallas por país", conversor de talles, calculadora de tela, "mapa del molde más descargado por país" (con datos agregados de moldey) | Solo funciona con datos reales |
| **Reseñas** (Trustpilot y equivalentes locales: Reclame Aqui, Trusted Shops, Avis Vérifiés…) | Pedir reseña a *todos* los compradores, no solo a los contentos | **[NO VERIFICADO]** cobertura de cada plataforma; no ofrecer incentivos solo por reseñas positivas |
| **Wikipedia / Wikidata** | Notabilidad exige cobertura independiente. Una marca chica casi seguro no la tiene; no crear la página uno mismo (conflicto de interés) | Riesgo de borrado y daño reputacional. Valor real: contribuir a artículos de técnica de costura con fuentes |
| **Afiliados** | Programa propio con comisión por venta | Fraude de cupones; vigilar |
| **Outreach multilingüe con IA** | Redactar con IA, **revisar por nativo** y personalizar con algo concreto del destinatario | Correo masivo = spam y daña la entrega; cumplir leyes anti-spam |

**Reglas de Google que no hay que romper [HECHO general, sin URL primaria vista]:** comprar enlaces, redes de blogs privadas (PBN) y esquemas de enlaces violan las políticas de spam. El spam update de marzo 2026 fue descrito por agregadores como dirigido a "link schemes y scaled content abuse", pero **Google no confirmó objetivos** y Search Engine Roundtable dice que el de septiembre no apunta a enlaces ([SER](https://www.seroundtable.com/google-september-2026-spam-update-42163.html)). Otro dato a verificar: Semrush menciona un **cambio en la política de "site reputation abuse" el 28-ago-2026** ([Semrush](https://www.semrush.com/blog/google-spam-update-september-2026/)). **[NO VERIFICADO]** el contenido exacto.

---

## 5. SEO programático seguro y actualizaciones de Google

### 5.1 Qué dice Google
- **[HECHO]** Marzo 2024: la política de *scaled content abuse* apunta a producir contenido a escala para posicionar, **independientemente de si lo hace automatización, humanos o una combinación** ([Google](https://blog.google/products/search/google-search-update-march-2024/)).
- **[HECHO, vía periodismo]** En 2025 Google dijo a Glenn Gabe que sus políticas **no definen estrictamente como spam** el contenido traducido por IA, pero que la política menciona las transformaciones automáticas, incluidas traducciones, y que traducir con IA está bien **si el contenido es de calidad y valioso** ([GSQi](https://www.gsqi.com/marketing-blog/auto-translating-content-google-scaled-content-abuse/), [Search Engine Land](https://searchengineland.com/google-comments-on-reddits-use-of-ai-to-translate-its-pages-456908)). El texto exacto de ese enunciado no lo pude contrastar con la fuente primaria. Fecha: 2025 (los resultados no la muestran).
- **[HECHO]** Google quitó de su documentación multilingüe la sugerencia de bloquear con robots.txt las páginas autotraducidas; el registro de cambios dice "docs-only change, no change in behavior" ([SEJ](https://www.searchenginejournal.com/google-removes-robots-txt-guidance-for-blocking-auto-translated-pages/548870), ~2025). Gabe cree que fue un descuido ([Multilingual.com](https://multilingual.com/google-automated-translation-policy-update/)).
- **No hay umbrales numéricos publicados** (mínimo de palabras, % de IA, cantidad de páginas) según las fuentes que consulté. **[EVIDENCIA débil]**, de agregadores. Cualquier "regla de X% de unicidad" es folklore.
- **[EVIDENCIA débil, secundaria]** Las guías de evaluadores de calidad (ene-2025) añadieron una sección sobre scaled content abuse y en abr-2025 se indicó que el contenido masivo con poco esfuerzo puede recibir la calificación más baja ([PPC Land](https://ppc.land/scaled-content-abuse/)).
- **[NO VERIFICADO]** Que la documentación de spam ya cubra la manipulación de respuestas de IA generativa (algunos sitios lo afirman, con fechas distintas).

### 5.2 El caso Reddit: la prueba más cercana (y por qué no se puede copiar)
- Las traducciones por IA de Reddit crecieron durante 2025 hasta decenas de millones de URLs con buen posicionamiento ([GSQi 1](https://www.gsqi.com/marketing-blog/reddit-ai-translations-google/), [GSQi 2](https://www.gsqi.com/marketing-blog/reddit-ai-translations-expand-boom/)).
- **Cayeron fuerte** tras el core update de mayo-2026 y el spam update de junio-2026, también en buscadores de IA ([GSQi](https://www.gsqi.com/marketing-blog/reddit-ai-translations-drop/)). Según Gabe, **volvieron a subir** con el spam update de septiembre-2026 en Italia, Alemania, Brasil y Francia ([X, 1-oct-2026](https://x.com/glenngabe/status/2105638422102561193)). No lo corroboré con otra fuente.
- **Lectura:** Google tolera hoy a Reddit (autoridad enorme, contenido de usuarios genuino), pero con oscilaciones fuertes. Distribb lo resume: lo que Google tolera de Reddit no prueba que autotraducir su blog sea seguro ([Distribb](https://distribb.io/blog/september-2026-spam-update)). Para un sitio chico, el riesgo es asimétrico.

### 5.3 Línea de tiempo 2025–2026 (para correlacionar con tus datos)

| Fecha | Evento | Fuente / nota |
|---|---|---|
| ago-2025 | Spam update, ~4 semanas | mencionado en [SEJ](https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/) |
| dic-2025 | Core update; un agregador dice que 52% de los e-commerce perdieron visibilidad | [Dataslayer](https://www.dataslayer.ai/blog/google-core-update-december-2025-what-changed-and-how-to-fix-your-rankings), **[EVIDENCIA débil]** |
| 24–25 mar-2026 | Spam update de ~19,5 h (el más rápido registrado) | agregadores; Google no dio detalle |
| 27 mar–8 abr-2026 | Core update. Afiliados golpeados más (71% según un tracker); páginas finas de comparación, reseñas con plantilla y cupones programáticos entre los perdedores | [Affiverse](https://www.affiversemedia.com/googles-march-2026-core-update-hit-affiliate-sites-harder-than-any-other-category/), [Orangemonke](https://orangemonke.com/blogs/google-march-core-update-complete/). **[EVIDENCIA débil]**: cifras discrepan entre fuentes |
| 21 may–2 jun-2026 | Core update (más fuerte que marzo según algunos) | [GSQi](https://www.gsqi.com/marketing-blog/core-roars-back-google-may-2026-core-update-analysis/) |
| 24–26 jun-2026 | Spam update; un sitio reporta caídas de 25%+ en algunos e-commerce | [Dashboard](https://status.search.google.com/incidents/YUX1peHev5a4fkxLDiUQ), [Gromerce](https://gromerce.com/en/blog/google-june-2026-spam-update-ecommerce-paid-search) |
| 18–21 ago-2026 | Spam update ("normal") | [Dashboard](https://status.search.google.com/incidents/LEubPCm2octf2uMqCFKE) |
| 24 sep–8 oct-2026 | Spam update, ~14 días, global, todos los idiomas | [Dashboard](https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu), [SEJ](https://www.searchenginejournal.com/google-september-2026-spam-update-complete/592283/) |

**Lo que no se sabe:** Google no dijo qué atacó cada spam update ni dio cifras de impacto. Todo "qué golpeó" viene de trackers privados con metodologías distintas.

### 5.4 Cómo hacer programático sin caer en abuso (moldey)
El riesgo concreto: **prenda × talla × formato × idioma** explota combinatoriamente (p. ej., 500 moldes × 12 tallas × 4 formatos × 70 idiomas ≈ 1,7 millones de URLs). **[OPINIÓN]**

1. **Una URL por molde y por idioma**; talla y formato son *selectores* dentro de la página, no URLs indexables (o con canonical al molde). Páginas "talla 38 en PDF A4" solo existirían si hay consulta real y contenido propio.
2. **Regla de "merecer el índice"** (checklist; indexar solo con ≥5 de 7): (a) hay búsqueda real en ese idioma; (b) texto escrito/revisado por nativo; (c) tabla de tallas local; (d) fotos propias de prenda cosida; (e) instrucciones específicas del formato y papel local; (f) enlaces internos y estructurados (breadcrumbs, schema Product); (g) no es casi idéntica a otra página del mismo idioma.
3. **Escalado por etapas:** lanzar 20–50 páginas por idioma, `noindex` lo no revisado, y ampliar según impresiones en GSC ("ganarse las próximas 100 páginas").
4. **No lanzar una oleada durante un rollout de update** (spam o core) para no confundir causalidad. Esperar ~2 semanas tras el cierre.
5. **hreflang** bien armado (cada versión enlaza a todas; auto-referencia; `x-default`), una lengua y un guion por URL, y sitemaps por idioma. **[HECHO, doc de Google conocida; sin URL de esta sesión]**
6. Recordar que la señal de calidad es de sitio: una sección con traducciones flojas puede arrastrar a las demás. **[OPINIÓN]** La advertencia de Gabe es que la mayoría de los sitios no puede escalar traducción automática sin castigo (citado en el resumen de búsqueda de GSQi).

---

## 6. Medición

### 6.1 Pila de medición

| Capa | Qué configurar | Notas |
|---|---|---|
| **Google Search Console** | Propiedad de dominio + una propiedad por carpeta de idioma (`/de/`, `/pt-br/`…); filtro por país; exportación por API/BigQuery porque la interfaz limita filas | **[HECHO]** conocido; sin URL de esta sesión |
| **Bing Webmaster** | Verificar el sitio; usar Keyword Research; revisar el informe de rendimiento en IA si existe | Hay indicio de un "AI Performance report" ([Search Engine Watch](https://searchenginewatch.com/?p=145991)). **[NO VERIFICADO]** |
| **Yandex Webmaster / Baidu / Naver Search Advisor** | Solo si se entra a ru/zh/ko en serio | **[NO VERIFICADO]** requisitos de cuenta |
| **GA4** | Dimensiones: idioma del navegador, país, canal; parámetro propio `site_language`; grupo de canales personalizado "IA" para referidos de `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`, `claude.ai`; eventos de e-commerce (`purchase`) con moneda | **[OPINIÓN]**. El idioma del navegador ≠ mercado: el español en EE. UU. no es España. Medir ingresos por **carpeta/mercado** |
| **Rank tracking** | 20–50 keywords por idioma y país, móvil, semanal (Semrush, Ahrefs, SE Ranking, AccuRanker) | **[OPINIÓN]** |
| **Cuota en IA (AEO)** | Lista fija de 20–30 prompts por idioma, repetida mensualmente en ChatGPT, Gemini, Perplexity, Copilot, AI Overviews; registrar menciones y citas | Herramientas comerciales existen; **[NO VERIFICADO]** |

### 6.2 Embudo y KPIs por idioma
Impresiones → CTR → clics → sesiones → engaged sessions → add-to-cart → compras → ingresos.
- **Cobertura:** % de páginas indexadas / enviadas (objetivo ≥ 80% de las que debían indexarse).
- **Calidad:** clics por página indexada; % de páginas con ≥ 1 clic en 90 días.
- **Negocio:** conversión, ingreso por sesión, margen tras costos de traducción/mantenimiento.
- **Costo:** costo acumulado de traducción y revisión / ingreso acumulado (payback).
- **Punto de equilibrio:** `sesiones_equilibrio = costo_mensual_idioma / (conversión × ticket × margen)`.

### 6.3 Plazos y metas (hipótesis a calibrar con la Oleada 1)
**[OPINIÓN]**: no encontré estudios con plazos de SEO en idiomas nuevos de tiendas de infoproductos. La regla general de la industria es "meses, no semanas". Los números de abajo son puntos de partida, no promesas.

| Horizonte | Meta de proceso | Señal de mercado (nivel A) | Señal de mercado (nivel B/C) |
|---|---|---|---|
| **3 meses** | Páginas núcleo indexadas ≥ 90%; hreflang sin errores; glosario cerrado | Primeras impresiones y consultas en GSC | Primeras impresiones |
| **6 meses** | LQA aprobado; 20–50 páginas por idioma; primeros enlaces propios | Clics crecientes; primeras ventas | Clics aislados |
| **12 meses** | Decisión expandir/mantener/recortar con datos | Ingreso positivo sobre el costo del idioma en los de mejor desempeño | Evaluar si el hub rinde |
| **24 meses** | Cartera estable de idiomas rentables | Ingresos por idioma y mercado reportados | Mantener solo hubs con tráfico |

### 6.4 Criterios cuantitativos para ampliar o cortar un idioma (a los 6 y 12 meses)
**[OPINIÓN]** Ajustar umbrales con datos reales.
- **Expandir** si cumple ≥ 3: (1) ≥ 80% indexación; (2) impresiones creciendo 3 meses seguidos; (3) CTR en posiciones 1–10 ≥ al de tu mediana; (4) conversión ≥ 50% de la del sitio principal; (5) ingreso acumulado ≥ 1× costo del idioma; (6) ≥ 3 enlaces externos o menciones locales.
- **Mantener/optimizar** si: indexado y con impresiones, pero sin conversión → revisar precio, pago local, traducción del checkout.
- **Recortar o consolidar** si a los 9–12 meses: ≥ 80% indexado y 0–pocos clics, **o** ingresos < costo de mantenimiento por 2 trimestres. Recortar = pasar a `noindex` o consolidar hacia el idioma "padre" (p. ej., variantes al estándar), sin borrar sin plan de redirección.
- **Alerta:** caída > 30% de clics en las 2 semanas posteriores a un update de Google, en más de la mitad de los idiomas → pausar nuevas oleadas y auditar calidad.

---

## 7. Priorización de idiomas

### 7.1 Fórmula
`Puntaje (0–100) = 20 × (Mercado/5) + 25 × (Demanda del nicho/5) + 15 × (Brecha competitiva/5) + 15 × (Poder adquisitivo y pagos/5) + 15 × (Viabilidad de traducción/5) + 10 × (Canales/5)`, con cada factor en escala 1–5.

| Factor | Qué mide | Dato a usar |
|---|---|---|
| Mercado (20%) | Tamaño digital/e-commerce de los países del idioma | Usuarios de internet, compras en línea |
| Demanda del nicho (25%) | Búsquedas de "molde/patrón de costura" per cápita y tendencia | Trends, Wordstat, Naver, Semrush/Ahrefs |
| Brecha competitiva (15%) | 5 = pocas tiendas locales fuertes de patrones PDF | Top 10 manual |
| Poder adquisitivo y pagos (15%) | Se puede cobrar: tarjeta/PayPal/Pix/UPI/Mercado Pago; precio local | Medios de pago de tu pasarela; sanciones |
| Viabilidad de traducción (15%) | Nivel A/B/C, disponibilidad de revisor, complejidad de escritura | Sección 2.2 |
| Canales (10%) | Comunidad de costura activa, Pinterest/YouTube/Facebook | Observación local |

### 7.2 Ejemplo ilustrativo
**Los puntajes de cada factor son mis hipótesis [OPINIÓN]**, no datos medidos. Sustituirlos con la investigación de demanda real. La suma ponderada sí está calculada.

| Idioma | M | D | C | P | T | K | **Puntaje** |
|---|---|---|---|---|---|---|---|
| pt-BR | 5 | 5 | 3 | 3 | 5 | 5 | **88** |
| de | 4 | 5 | 2 | 5 | 5 | 4 | **85** |
| id | 4 | 5 | 4 | 2 | 4 | 5 | **81** |
| fr | 4 | 4 | 3 | 4 | 5 | 4 | **80** |
| ru | 4 | 5 | 3 | 2 | 4 | 4 | **76** |
| tr | 4 | 4 | 4 | 2 | 4 | 4 | **74** |
| hi | 5 | 4 | 4 | 1 | 3 | 5 | **74** |
| ar (estándar) | 4 | 4 | 4 | 3 | 3 | 4 | **74** |
| vi | 3 | 4 | 4 | 2 | 4 | 4 | **70** |
| it | 3 | 3 | 3 | 4 | 5 | 3 | **69** |
| pl / nl | 3 / 2 | 4 / 3 | 3 | 3 / 5 | 4 / 5 | 3 | **68** |
| ja | 4 | 3 | 2 | 4 | 4 | 3 | **67** |
| fil | 3 | 3 | 4 | 2 | 4 | 4 | **65** |
| uk / th / ms / bn | | | | | | | **62–64** |
| ur | 3 | 3 | 5 | 1 | 3 | 3 | **60** |
| ko / fa | | | | | | | **56** |
| ne / sw | | | | | | | **41–42** |
| my / ha / am | | | | | | | **32–39** |

*(en y es son la oleada 0 base. Los idiomas de alto riesgo como ne, my, am quedan abajo aunque la población sea grande: el puntaje castiga la baja viabilidad de traducción y la poca búsqueda escrita.)*

### 7.3 Oleadas (cortes fijados antes de mirar los números: ≥75 / 65–74 / 55–64 / <55)
Referencia al CSV maestro: las variedades "se atiende con otro" no suman sitios.

| Oleada | Idiomas (propuesta) | Cuándo / tamaño | Qué se espera |
|---|---|---|---|
| **0 – Base** | en, es (es-419 / es-AR / es-ES) | Ya | Consolidar hreflang, medición y glosario |
| **1 – Rentables** | pt-BR, de, id, fr, ru (≥75) | Meses 0–4 | MT nivel A + post-edición ligera; mayor retorno esperado |
| **2 – Grandes y viables** | tr, hi, ar, vi, it, pl, nl, ja, fil (65–74) | Meses 4–10 | Pagos locales (UPI, etc.) a resolver antes |
| **3 – Media prioridad** | uk, th, ms, bn, ur, ko, fa, ro, cs, hu, el, sv, da, no, fi, he, ta/te/mr/gu/kn/ml | Meses 10–18 | Post-edición completa y revisor nativo |
| **4 – Largo plazo** | ne, si, km, my, lo, kk, uz, az, sr, hr, bg, sk, sl, lt, lv, et, ka, hy, mn, sw, af | Meses 18–24 | Solo con revisión humana y datos de las oleadas previas |
| **5 – Hub** | ha, yo, ig, om, zu, xh, sn, ny, rw, ln, ak, ff, so, mg, ti, am, qu, ht, sd, ps, ku, as, or | Cuando el presupuesto lo permita | Hub corto + glosario; ampliar solo si hay tráfico real |
| **Variedades** | árabes (arz, apc…), grupo hindi (bho, mai, awa…), chinas, jv, su, ceb, pcm | Con su "padre" | Sin sitio propio; vocabulario local en el padre |

### 7.4 Cuándo pasar a la siguiente oleada (puerta de salida)
**[OPINIÓN]** Pasar de oleada N a N+1 cuando se cumplan **todas**:
1. ≥ 70% de los idiomas de la oleada con ≥ 80% de indexación y primeras consultas en GSC.
2. Tasa de errores LQA bajo el umbral acordado en las 2 últimas entregas.
3. Costo por idioma real ≤ 120% del presupuestado y capacidad de revisores confirmada.
4. Al menos un idioma de la oleada con ingreso ≥ su costo, o tendencia clara de payback.
5. Ningún update de Google (core/spam) en rollout en las 2 semanas previas, y sin caída anómala atribuible a calidad.

---

## 8. Contradicciones y puntos controvertidos
1. **¿Traducir con IA es spam?** Google dice que no estrictamente, pero lo lista entre las "transformaciones automáticas" de su política y exige calidad y valor. Un documento se retiró "sin cambio de comportamiento". La interpretación de Gabe es que fue un descuido. Todo depende de que cada página aporte valor.
2. **Caso Reddit:** subió, cayó (mayo–jun 2026) y volvió a subir (sep 2026 según Gabe). No generalizable.
3. **DeepL vs LLM:** vendedores dicen que DeepL gana en idiomas europeos; estudios con métricas automáticas ponen a GPT-4o por encima. Sin ranking fiable.
4. **Cifras de updates:** los trackers privados no coinciden (por ejemplo, volatilidad del core de marzo 2026: 79,5% frente a "menor volatilidad" según otra fuente).
5. **Naver:** 50–59% de cuota según la fuente.
6. **DeepL:** 36 idiomas vs "100+".

## 9. Qué quedó sin verificar (por el tope de búsquedas)
Texto literal de las políticas de spam de Google; precios de Lokalise/Crowdin/Microsoft/Weglot; tarifas de traducción para idiomas de nivel C; plazos de resultados SEO en idiomas nuevos; reglas y alcance de Trustpilot y equivalentes locales; criterios de notabilidad de Wikipedia; políticas de afiliados; Pinterest Trends/AnswerThePublic/Keyword Insights; requisitos de cuenta en Baidu/Naver/Yandex Webmaster; cuota real de Google en cada mercado; demanda real por idioma para moldería (sección 7 es un modelo, no un resultado).

---

## 10. Qué hacer en moldey.com (priorizado)

| # | Acción | Impacto | Esfuerzo |
|---|---|---|---|
| 1 | **Medición antes de traducir:** GSC con propiedad por carpeta, Bing WMT, GA4 con `site_language`, canal "IA" y panel de embudo por idioma | Alto | Bajo |
| 2 | **Glosario maestro** (200–500 términos: moldería, formatos, tallas) revisado por nativos de la oleada 1, usado como glosario bloqueado en toda herramienta | Alto | Medio |
| 3 | **Prueba ciega de motores** por idioma de la oleada 1 (30–50 segmentos, 2–3 motores, 1–2 revisores) | Alto | Bajo |
| 4 | **Oleada 1** (pt-BR, de, id, fr, ru): keyword research nativa, páginas núcleo con MTPE y revisión nativa, `noindex` hasta aprobar | Alto | Medio-alto |
| 5 | **Contenido localizable de mayor valor:** tabla de tallas por país y conversor, guía "imprimir y armar", glosario con fotos, FAQ de formatos, con datos y ejemplos locales | Alto | Medio |
| 6 | **Prueba de E-E-A-T:** biografía real de quien traza los moldes, fotos de prendas cosidas, galería de clientes con permiso, política de reembolso en cada idioma | Medio-alto | Medio |
| 7 | **Arquitectura programática mínima:** una URL por molde e idioma, talla/formato como selectores, regla "merecer el índice" y hreflang correcto | Alto | Medio |
| 8 | **Digital PR con recurso enlazable** (conversor de tallas / datos propios) y programa de creadores locales por oleada | Medio | Medio |
| 9 | **Hub de 1 página** para idiomas de poca búsqueda en lugar de sitio completo | Medio | Bajo |
| 10 | **Puertas de oleada** y revisión trimestral de expandir/mantener/recortar con la tabla de la sección 6.4 | Medio | Bajo |
| 11 | Revisar cuenta/pagos locales (Pix, UPI, Mercado Pago, etc.) antes de la oleada 2 | Medio | Medio |
| 12 | Decidir si activar o no la traducción automática de Google dentro de AI Overviews (cuando se confirme cómo funciona el opt-out) | Bajo-medio | Bajo |

## 11. Qué NO hacer
- **No** traducir en masa todo el catálogo a 100 idiomas con MT sin edición ni revisión nativa y publicarlo indexable. Es el patrón que Google describe como abuso a escala; el caso Reddit muestra volatilidad incluso para un gigante.
- **No** traducir las keywords del inglés; no clonar las páginas cambiando solo el idioma.
- **No** crear URLs indexables para cada combinación prenda × talla × formato × idioma.
- **No** publicar nivel C (ne, my, am, ti, om, km…) con MT sola; ni usar puntajes automáticos como prueba de calidad en esos idiomas.
- **No** bloquear idiomas flojos con robots.txt; usar `noindex` por página (SEJ).
- **No** comprar enlaces, usar PBNs ni redes de blogs; no comprar reseñas ni inventar autores o reseñadores locales.
- **No** hacer outreach masivo con IA sin revisión nativa y sin personalizar.
- **No** lanzar una oleada en medio de un rollout de update de Google, ni mezclar varios cambios a la vez (no se podrá atribuir el efecto).
- **No** crear la página de Wikipedia de la marca ni editar con conflicto de interés.
- **No** prometer plazos de posicionamiento: no hay datos fiables para idiomas nuevos de este nicho; calibrar con la oleada 1.
