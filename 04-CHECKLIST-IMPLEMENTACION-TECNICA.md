# 04 · Checklist de implementación técnica (para ejecutar en el repo de moldey.com)

Cada tarea tiene **qué**, **cómo** y **criterio de aceptación (CA)** verificable. Prioridad: P0 (antes de cualquier idioma nuevo), P1 (con la oleada 1), P2 (después).
Convención: `[ ]` pendiente. Hacer cada bloque en una rama y un commit claro. **Nunca** tocar DNS, dominio, pagos ni producción sin confirmar con la persona dueña.

## A. Auditoría inicial (Fase 0) — solo lectura

- [ ] **A1 · Detectar la plataforma y el despliegue (P0).** Leer el repo/config: CMS o framework (Shopify, WooCommerce, Next.js, Astro, estático…), i18n (librería, carpeta de traducciones), hosting/CDN, base de datos, cómo se entregan los PDF. **CA:** `AUDITORIA-INICIAL.md` con el stack y el diagrama de flujo de compra/descarga.
- [ ] **A2 · Inventariar los idiomas del sitio (P0).** Listar idiomas activos (los 13: español, inglés + 11), su URL base, % de contenido traducido, método de traducción (humana/automática), qué está indexable. **CA:** tabla `idioma | URL | cobertura % | método | indexable | hreflang | revisado por nativo (sí/no)`.
- [ ] **A3 · Rastrear el sitio como lo ve un bot (P0).** `curl -s -A "Mozilla/5.0 (compatible; GPTBot/1.0)" <url>` en home, categoría y ficha de 3 idiomas: ¿están el título, el texto, los enlaces, hreflang y JSON-LD **en el HTML inicial** (sin JS)? **CA:** informe por tipo de página.
- [ ] **A4 · Revisar robots.txt, sitemaps, canónicos, hreflang, redirecciones, 404/soft-404, noindex accidentales (P0).** Usar `scripts/validar_hreflang.py` sobre los sitemaps actuales. **CA:** lista de errores con URL y gravedad.
- [ ] **A5 · Revisar bloqueos de WAF/CDN a bots legítimos (P0).** Comprobar que Googlebot, Bingbot, OAI-SearchBot, PerplexityBot y Claude-SearchBot no reciben 403/captcha (revisar reglas de Cloudflare/WAF y logs). **CA:** tabla bot → respuesta.
- [ ] **A6 · Medir rendimiento (P1).** Lighthouse/PageSpeed móvil en 5 páginas clave (LCP/INP/CLS); peso del HTML, JS e imágenes; carga de fuentes por escritura. **CA:** línea base guardada.
- [ ] **A7 · Datos de Search Console/GA4 si hay acceso (P0).** Impresiones/clics por país e idioma, consultas sin página en ese idioma, páginas "descubiertas, no indexadas". **CA:** línea base de 90 días (si no hay acceso, anotarlo).
- [ ] **A8 · Revisar entrega de PDF/DXF (P0).** ¿URLs adivinables, enlaces públicos indexables, sin caducidad, sin marca de agua? **CA:** riesgos documentados.

## B. Base técnica (P0)

- [ ] **B1 · HTML completo en servidor (SSR/SSG).** Todo el contenido principal, enlaces internos, hreflang y JSON-LD deben estar en la respuesta inicial. **CA:** `curl` con UA de GPTBot muestra `<h1>`, la caja de especificaciones y los enlaces de idioma.
- [ ] **B2 · Una URL por idioma y por molde, autocanónica.** `<link rel="canonical">` apuntando a sí misma; nunca a otro idioma. HTTPS, una sola forma de la URL (con/sin `www`, barra final, minúsculas). **CA:** crawler sin canónicos cruzados.
- [ ] **B3 · robots.txt separado por función** (ver `plantillas/robots.txt`). Cerrar `/descargas/`, `/mi-cuenta/`, `/checkout/`. **CA:** archivo publicado y probado con el probador de robots.
- [ ] **B4 · Sitemaps por idioma + índice, generados por script** a partir de la base de datos de productos (clave = ID estable). Solo URL 200, indexables y aprobadas. `lastmod` real. **CA:** `scripts/generar_sitemaps_hreflang.py` produce los archivos; `validar_hreflang.py` sin errores.
- [ ] **B5 · Search Console (dominio + prefijo por idioma), Bing Webmaster Tools; IndexNow** al publicar/actualizar/eliminar URL **aprobadas** (Bing, Yandex, Naver, Seznam; Google no lo usa). **CA:** propiedades verificadas y sitemaps enviados.
- [ ] **B6 · Protección de descargas.** Archivos fuera de la raíz pública; URL firmada con caducidad atada al pedido; límite de descargas; `X-Robots-Tag: noindex, noarchive, nosnippet` en la ruta de descargas; marca de agua o ID del comprador en el PDF; vistas previas de baja resolución. **CA:** no existe URL pública directa a un PDF/DXF de pago.
- [ ] **B7 · Rendimiento móvil.** Imágenes WebP/AVIF con `srcset`, LCP < 100 KB, JS diferido, `font-display: swap`, caché de borde con `stale-while-revalidate`, HTTP/2-3, Brotli. **CA:** LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 en móvil (laboratorio) en las páginas clave.

## C. Arquitectura multilingüe (P0–P1)

- [ ] **C1 · Estructura de URL:** raíz en inglés + `x-default`; `/es/`, `/pt-br/`, `/fr/`… (subdirectorios). Sin parámetros `?lang=` indexables, sin subdominios ni ccTLD. Slug traducido sin diacríticos en idiomas latinos; **slug ASCII + ID estable** en no latinos. **CA:** esquema documentado y probado con 3 idiomas (uno latino, uno RTL, uno CJK).
- [ ] **C2 · Estado de publicación por página e idioma:** campo `estado` ∈ {`borrador`, `traducido_mt`, `revisado_nativo`, `publicado`}. **Solo `publicado` entra en sitemap, hreflang e índice.** El resto: `noindex, follow`, sin bloquear por robots.txt. **CA:** ninguna página `traducido_mt` es indexable; test automático lo comprueba.
- [ ] **C3 · hreflang solo en sitemap** (más `<html lang>` y `Content-Language`). Códigos ISO 639-1 + región (`pt-BR`, `es-AR`…). Reciprocidad y auto-referencia obligatorias; clúster solo con idiomas existentes y aprobados. `x-default` = raíz en inglés (o `/languages/`). Variedades sin 639-1 (cantonés, árabes…) se sirven con el idioma estándar y **fuera del clúster propio**. **CA:** `validar_hreflang.py` sin errores; revisar zh (`zh-CN`/`zh-TW`) antes de usar `zh-Hans/Hant`.
- [ ] **C4 · Selector de idioma rastreable y accesible:** enlaces `<a href lang hreflang>` con endónimos ("Español", "Português (Brasil)", "日本語", "العربية"), sin banderas; menú corto (idioma actual + ~8) y enlace "Todos los idiomas" a `/languages/` (página estática con la lista completa). `aria-current="true"`. **CA:** navegable por teclado; los bots ven todos los idiomas desde `/languages/`.
- [ ] **C5 · Cero redirecciones automáticas por IP/idioma.** Banner no bloqueante ("¿Preferís ver moldey en Español?") con `navigator.language`; preferencia en `localStorage`. **CA:** `curl` con distintos `Accept-Language` devuelve el mismo contenido en la misma URL.
- [ ] **C6 · Reglas de escritura:** `<html lang dir>`; propiedades lógicas de CSS para RTL; `:lang()` con pilas del sistema para CJK (sin fuente web); WOFF2 subset para índicas/árabe; NFC en URLs/slugs/búsqueda; birmano solo Unicode; una escritura por URL (serbio, uzbeko, kazajo). **CA:** prueba visual en los 3 idiomas de C1.
- [ ] **C7 · Localización de la ficha:** unidades (cm/in), papel (A4/Letter) y tallas como selectores dentro de la misma URL; moneda por idioma/URL (no por IP en el servidor); precio visible = precio del JSON-LD. **CA:** cambiar de selector no cambia la URL indexable.
- [ ] **C8 · Validador propio en CI (P1):** por ID de producto comprobar que todas las URL del clúster son 200, indexables y autocanónicas; que cada una lista a todas y a sí misma; códigos en lista blanca; idioma detectado (fastText `lid.176`/CLD3) = hreflang; sin caracteres de otro alfabeto en idiomas latinos. **CA:** el build falla si algo se rompe.

## D. Datos estructurados (P0–P1)

- [ ] **D1 · `Organization`** única con `@id` estable y `sameAs` (ver `plantillas/jsonld-organization.json`); referenciada desde las demás entidades.
- [ ] **D2 · `Product` + `Offer` por URL de idioma** (ver `plantillas/jsonld-product-digital.json`): un precio y una moneda por URL, **igual a lo visible**; `additionalProperty` con formatos, margen de costura, tallas, licencia. Producto digital: sin `shippingDetails`; política de devolución a nivel organización. **Validar con el Rich Results Test y Merchant Center** (las reglas para bienes digitales no están confirmadas: ver `research/raw/V2-G2-*`). No marcar reseñas que no existan.
- [ ] **D3 · `BreadcrumbList`** localizada; **`WebPage` con `inLanguage`** (BCP 47) en cada página; `VideoObject` para tutoriales.
- [ ] **D4 · No esperar** rich results de FAQ/HowTo ni vender el marcado como "truco de citas de IA": sirve para claridad de entidad y elegibilidad en búsqueda clásica.

## E. Contenido y plantillas (P0–P1)

- [ ] **E1 · Ficha-modelo** (ver `plantillas/ESTRUCTURA-FICHA-PRODUCTO.md`) en español e inglés; replicable por idioma con datos reales localizados (tallas, hojas, rendimiento). **CA:** responde en el primer pantallazo las quejas verificadas (A0, margen, páginas, escala, licencia).
- [ ] **E2 · Guías evergreen** (respuesta primero): imprimir y armar un molde PDF (A4/Letter/A0/proyector), cuadrado de prueba, tomar medidas y elegir talla, margen de costura, tejido plano vs punto, DXF/AAMA/ASTM, preparar plantilla de sublimación, licencias. **CA:** cada guía con definición breve al inicio, tabla/pasos y fecha de actualización.
- [ ] **E3 · Páginas de categoría (hubs)** prenda → público/cuerpo → formato → tradicionales; 150–300 palabras de texto propio; **indexar solo combinaciones con demanda real**.
- [ ] **E4 · Página de marca:** quién traza los moldes, método, fotos reales, política de licencias, contacto; refuerza entidad y E-E-A-T. Evitar la lectura "moldy" en inglés ("Moldey — digital sewing patterns").
- [ ] **E5 · Páginas legales** (términos, privacidad, reembolso, licencia) en ES/EN primero; resto de idiomas con revisión. Marcadas como pendientes de revisión legal.

## F. Medición (P0)

- [ ] **F1 · GA4:** parámetro de evento `content_language` en cada `page_view` (distinto del idioma del navegador); dimensión país; **grupo de canales "IA"** con regex de fuente `chatgpt\.com|chat\.openai\.com|perplexity|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|deepseek|grok|meta\.ai|you\.com`. Aclarar que AI Overviews/AI Mode cuentan dentro de Google orgánico.
- [ ] **F2 · Search Console:** informe por carpeta de idioma, filtro por país, exportación a BigQuery si hay volumen. Mirar idioma de la URL vs país de las impresiones.
- [ ] **F3 · Logs del servidor:** qué páginas piden OAI-SearchBot, PerplexityBot, Claude-SearchBot, Googlebot, Bingbot (sin ellos no hay cita posible); detectar 404 en masa.
- [ ] **F4 · Protocolo AEO mensual** (ver `05`) y hoja de seguimiento.
- [ ] **F5 · Tablero** (Looker Studio): URL enviadas vs indexadas, impresiones, clics, CTR, conversión y costo por idioma; "salud de la oleada".

## G. Pagos, entrega y legal (P0, con la persona dueña)

- [ ] **G1 · No cambiar pagos sin autorización.** Documentar el estado actual (pasarela, impuestos, moneda). Proponer MoR (Polar / Lemon Squeezy / Gumroad / Paddle: verificar Argentina en la doc oficial) como decisión de la persona dueña con su contador. **CA:** documento de decisión, no implementación.
- [ ] **G2 · Entrega inmediata** (email + área de descargas) con enlaces firmados; hoja de prueba; instrucciones en 3–5 idiomas.
- [ ] **G3 · CMP de cookies** para UE/UK/BR y analítica en modo consentimiento.
- [ ] **G4 · Países sancionados:** bloqueo en checkout (lo hace el MoR); no promocionar allí.

## H. Calidad y regresión (P1)

- [ ] **H1 · Tests/CI:** (1) sitemap solo con `publicado`, (2) hreflang recíproco, (3) canónicos autorreferentes, (4) ninguna página `traducido_mt` indexable, (5) JSON-LD válido con precio/moneda = visibles, (6) HTML con contenido sin JS. **CA:** pipeline verde antes de desplegar cada oleada.
- [ ] **H2 · Registro de cambios (`CHANGELOG-SEO.md`)** con fecha de cada despliegue y oleada, para atribuir efectos y detectar caídas ligadas a updates de Google.
