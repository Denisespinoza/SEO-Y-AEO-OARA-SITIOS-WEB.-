# 05 · Guía operativa de AEO/GEO (visibilidad en respuestas de IA)

> Base de evidencia y límites: `01` §1 y §3, `research/raw/T1-*` y `V2-G1-*`. Premisa: **AEO/GEO sigue siendo SEO** (según la guía oficial de Google de 15-may-2026) más presencia externa verificable. No hay "hack" estable: los datos cambian rápido (top-10 76 %→38 % de las citas de AI Overviews en 8 meses, según Ahrefs).

## 1. Cómo escribir una página "citable" (patrón)

Aplicar a fichas, categorías y guías, en cada idioma (redactado por nativo, no clonado):

1. **Respuesta primero:** en las primeras 2–3 líneas, la definición o respuesta directa ("Un molde de costura en PDF es…"; "Para imprimir a escala correcta…"). ~44 % de las citas de ChatGPT salen del primer 30 % de la página (un estudio; solidez media-baja).
2. **Encabezados en forma de pregunta** que coincidan con cómo pregunta la gente (de `03` y del autosuggest local).
3. **Afirmaciones con dato:** medidas, número de hojas por talla, rendimiento de tela, pruebas de compatibilidad (con fecha y versión de software).
4. **Datos propios** que otros no tienen (tablas de tallas por país, comparativas de formatos, fotos de prendas cosidas). Google prioriza contenido "no commodity".
5. **Fecha de actualización real** (importa sobre todo para ChatGPT; no se actualiza por cosmética).
6. **Una página = un tema.** Mejor una página enfocada que una "guía definitiva" gigante.
7. **Tablas y pasos numerados** cuando el contenido lo pide (no hay prueba de que aumenten citas por sí solos; ayudan al lector).
8. **Autoría y experiencia:** quién traza los moldes, cómo se prueban, fotos reales.
9. **Sin "chunking" artificial ni versiones Markdown "para bots"** (Google lo desaconseja; el cloaking es riesgo).

## 2. Qué decir y qué no sobre uno mismo (alucinaciones de marca)

- Tener una página clara de **Acerca de / Licencias / Políticas / Precios** en HTML, y datos idénticos en todos los perfiles. Los motores pueden inventar o desactualizar precios, formatos y licencias.
- Reforzar la entidad "Moldey" (hay riesgo de lectura "moldy" = mohoso en inglés): "Moldey — moldes de costura digitales / digital sewing patterns" en título, descripción y perfiles.
- Auditar mensualmente las respuestas de marca (§5) y corregir en la fuente (la página propia o el perfil que la IA cita).

## 3. Rastreadores: qué permitir, qué decidir

| Bot | Función | Estado de verificación (`T1`/`V2-G1`) | Recomendación |
|---|---|---|---|
| Googlebot | Búsqueda de Google (alimenta AI Overviews/AI Mode) | Guía de Google 2026 | Permitir |
| Bingbot | Bing; alimenta Copilot y, según reportes, parte de otros asistentes | No verificado en detalle | Permitir |
| OAI-SearchBot | Aparecer en la búsqueda de ChatGPT | `[HECHO]` doc de OpenAI | **Permitir** |
| ChatGPT-User | Acción iniciada por el usuario | `[HECHO]`; robots.txt "puede no aplicar" | Permitir |
| GPTBot | Entrenamiento de OpenAI | `[HECHO]` | Decisión de negocio (ver abajo) |
| PerplexityBot / Perplexity-User | Índice / fetch del usuario | `[HECHO]` roles | Permitir |
| ClaudeBot | Entrenamiento de Anthropic; respeta robots.txt y Crawl-delay; sin rangos de IP publicados | `[HECHO]` | Decisión de negocio |
| Claude-SearchBot / Claude-User | Indexación para búsqueda / fetch a pedido | `[HECHO]` artículo oficial de Anthropic (confirmado en la 2.ª pasada, `V2-G1`) | Permitir |
| Google-Extended | Token de robots.txt (no es un rastreador): exclusión de entrenamiento/uso en Gemini; **no afecta a Search ni a AI Overviews/AI Mode** | `[HECHO vía secundarios concordantes]` (`V2-G1`) | Decisión de negocio |
| Applebot / Applebot-Extended | Siri/Spotlight / exclusión de entrenamiento | No verificado | Permitir / decidir |
| Meta-ExternalAgent, Bytespider, CCBot, Amazonbot, otros | Entrenamiento/indexación | No verificado | Decidir; los UA se falsifican |

- **Entrenamiento (GPTBot, ClaudeBot, Google-Extended…):** no hay evidencia de que permitirlo mejore la mención de la marca; bloquearlo **no** te saca de la búsqueda de ChatGPT/Claude según la documentación de OpenAI y Anthropic. Postura equilibrada: permitir páginas públicas de marketing/guías y cerrar `/descargas/`, `/mi-cuenta/`, `/checkout/`, `/*.pdf$`, `/*.dxf$`. Plantilla: `plantillas/robots.txt`.
- **robots.txt no protege archivos de pago.** Control de acceso: URLs firmadas con caducidad, límite de descargas, marca de agua con ID del comprador, `X-Robots-Tag: noindex, noarchive, nosnippet` en la ruta de descargas.
- **Revisar el WAF/CDN:** Cloudflare **bloquea por defecto rastreadores de IA en dominios nuevos desde el 1-jul-2025** `[HECHO vía prensa]`; con eso (o con "Bot Fight Mode") puede estar bloqueando OAI-SearchBot o PerplexityBot sin que lo sepas. Revisar el panel y los logs. Existe `Content-Signal: search=yes, ai-input=yes, ai-train=no` en robots.txt (declarativo, no vinculante). Una novedad de Cloudflare del 15-sep-2026 aparece sin verificar (`V2-G1`).
- **`llms.txt`:** sin efecto medible (Google lo desaconseja; estudios de logs y de ~300 mil dominios no encuentran relación). Opcional, 30 minutos, sin expectativas. **Nunca `llms-full.txt` con el catálogo.**

## 4. Medición del tráfico de IA (GA4 y logs)

1. **Canal personalizado "IA"** con regex de fuente: `chatgpt\.com|chat\.openai\.com|perplexity|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|deepseek|grok|meta\.ai|you\.com`. ChatGPT suele añadir `utm_source=chatgpt.com`.
2. **Límites:** los clics desde AI Overviews/AI Mode cuentan dentro de Google orgánico; parte del tráfico de apps llega como "directo"; el tráfico de referidos de IA es pequeño frente a la búsqueda (la IA es ~1/5 del tamaño de la búsqueda según Similarweb, may-2026) y desde mayo de 2026 los referidos de ChatGPT aterrizan más en la **home**.
3. **Logs del servidor:** qué páginas piden OAI-SearchBot, PerplexityBot, Claude-SearchBot, Googlebot, Bingbot. Sin visitas de esos bots no hay cita posible.
4. **Search Console y Bing WMT:** revisar consultas nuevas por idioma/país (Bing WMT tiene reportes de rendimiento en IA: ver `V2-G1`).

## 5. Protocolo manual de auditoría (≈2–3 h por ronda, mensual)

1. **Set de prompts por idioma:** usar `plantillas/prompts-auditoria-ia.csv` (11 idiomas, 6 tipos). Para el resto de idiomas: redactarlos con un hablante nativo usando el término real de `03`. Tipos: informativo (imprimir/armar; formatos de papel), comercial (dónde comprar), comparativo (mejores sitios), marca (qué es / confiable), producto (sublimación, DXF).
2. **Plataformas:** ChatGPT con búsqueda (sesión sin cuenta si es posible), Google (AI Overviews y AI Mode, ventana privada, país/idioma fijados con `&hl=xx&gl=YY`), Perplexity, Copilot, Gemini, Claude con búsqueda web.
3. **Corridas:** 3 por prompt y plataforma (las respuestas son no deterministas); no decidir con una sola captura.
4. **Registrar** en una hoja: fecha, plataforma, idioma, prompt, ¿nombró a Moldey?, ¿citó una URL de moldey.com?, top-5 de dominios citados, competidores nombrados, **idioma de las fuentes** vs idioma de la consulta, exactitud (sí/no + nota), corrida 1/2/3.
5. **Métricas:** *mention rate* (% de prompts donde se nombra la marca), *citation rate* (% con URL propia), *share of voice* (menciones propias / menciones de todos), exactitud y sentimiento.
6. **Línea base esperable:** cercana a cero en consultas genéricas; el objetivo inicial es salir bien en consultas de marca y en cola larga. Los **competidores nombrados** y los **dominios citados** muestran dónde hay que tener presencia (suele aparecer Reddit, YouTube, Etsy, blogs).
7. **Herramientas de pago** (Profound, Peec, Otterly, Semrush AI, Ahrefs Brand Radar…): solo cuando exista línea base y presupuesto; exigir cobertura de **idiomas y países** (muchas funcionan sobre todo en inglés/EE. UU.). Son proveedores con interés comercial: evaluar sus "estudios" con cautela.

## 6. AEO multilingüe: lo que se sabe y lo que no

- **Evidencia disponible (`V2-G1`, calidad baja a media: vendors y preprints):** los AI Overviews citan mayormente fuentes **en el idioma de la consulta** (85 %–96 % según vendors); otros asistentes (Grok) cambian al inglés con frecuencia; los preprints muestran sesgo al inglés **más fuerte en idiomas de pocos recursos** y menos fuentes en consultas no inglesas (p. ej. hindi). No hay estudios de e-commerce. Los AI Overviews/AI Mode se apoyan en el índice de Google, así que **las reglas de calidad de Search (incluido el spam de contenido a escala/traducción sin valor) aplican**.
- **Hipótesis a testear (no hechos):** (1) si no hay página en el idioma, la IA cita fuentes en inglés y traduce al responder; (2) en idiomas de poca competencia, una buena página puede ganar; en los de pocos recursos, la IA puede ni encontrarla ni valorarla; (3) hreflang y URL por idioma son prácticas de búsqueda clásica, su efecto en IA no está verificado.
- **Cómo cerrar el hueco con bajo costo:** repetir 8–10 prompts clave en 8–10 idiomas (ES, EN, PT, FR, DE, IT, ID, HI, AR, TR) con ubicación coherente; registrar idioma de las fuentes citadas y si aparece moldey.com. Con 2–3 rondas se ve el patrón.

## 7. Presencia externa (la palanca más correlacionada, con la salvedad de que es correlación)

- **YouTube:** tutoriales ("cómo imprimir y armar un molde PDF A4/Letter/A0", "cómo coser X"), con títulos/descripciones/subtítulos por idioma. Entre las fuentes más citadas por IA.
- **Pinterest:** pines verticales 2:3 con título/descripción/nombre de archivo en el idioma de cada mercado; un tablero por tipo de prenda; empezar por EN, ES (México), PT (Brasil), DE. Verificar si los Product Pins admiten producto digital.
- **Comunidades:** Reddit (r/sewing, r/sewingpatterns), grupos de Facebook, canales de WhatsApp/Telegram: **aportar valor y declarar la relación comercial**; el spam daña y los moderadores lo detectan.
- **Reseñas verificadas** de compradores (nunca fabricadas) y **menciones en blogs/prensa de manualidades**; creadores locales por oleada.
- **Wikipedia/Wikidata:** una tienda nueva probablemente no cumple notabilidad; **no crear páginas propias**.

## 8. Qué NO hacer

- Contratar servicios que **garanticen** citas en ChatGPT/Google; pagar por "llms.txt/schema para IA".
- Bloquear todos los bots de IA por miedo (desaparecés de sus respuestas) o dejarlos bloqueados por defecto sin saberlo.
- Publicar `llms-full.txt` o el PDF de pago en una URL pública/adivinable.
- Spam en comunidades, reseñas falsas, menciones compradas.
- Decidir con una captura; confundir correlación con causa (menciones, schema, longitud).
- Abandonar el SEO clásico: es la base de lo que Google y Bing citan.
