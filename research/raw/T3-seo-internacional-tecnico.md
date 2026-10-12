# T3 — SEO internacional/multilingüe TÉCNICO (2025–2026) para llegar a ~100 idiomas de forma escalonada, aplicado a moldey.com

Fecha del informe: 12 de octubre de 2026. Tienda: moldes de costura digitales (PDF A4/Letter/A0, DXF/vectorial, plantillas para sublimar), multi-idioma, vendedor en Argentina.

## 0. Aviso de cobertura y método (leer primero)

- **El presupuesto de búsquedas web de la sesión (límite compartido entre agentes) se agotó** tras unas 20 consultas útiles; WebFetch no funciona (DNS). No hice las 30–60 búsquedas pedidas. Qué quedó cubierto con evidencia de esta sesión y qué no:
  - **Con evidencia de esta sesión:** hreflang (sintaxis, x-default, errores, motores que lo usan), arquitectura (documentación de Google de 2010 y vigente), informe de segmentación internacional retirado, páginas adaptadas por locale, rastreo/sitemaps, traducción automática y política de spam (incluido el caso Reddit 2025–2026), IndexNow, Yandex, Bing (parcial), Baidu/Naver (solo fuentes secundarias), rastreadores de IA y JavaScript.
  - **Sin búsqueda (redactado con conocimiento previo del modelo):** gran parte de las secciones 5 (escrituras), 6 (Core Web Vitals/fuentes/CDN), 8 (datos estructurados y cambios de rich results 2025–2026), 9 (imágenes/vídeo/Pinterest), 10 (medición). Van marcadas **[HECHO*]** (documentación oficial que conozco con alta confianza, **no reconfirmada en esta sesión, sin URL**) o **[NO VERIFICADO]**. Tratarlas como hipótesis de trabajo hasta una segunda pasada.
- **Leyenda.** **[HECHO]** = documentado por la plataforma y visto en resultados de esta sesión. **[HECHO\*]** = documentación oficial conocida de antes, no reconfirmada ahora. **[EVIDENCIA]** = datos/prensa de terceros con fuente identificable. **[OPINIÓN]** = consejo de la industria o criterio propio sin prueba. **[NO VERIFICADO]** = sin respaldo suficiente.
- **Advertencia de método:** los resultados del buscador son **resúmenes automáticos** de las páginas, no el texto completo. Donde el resumen cita una frase de Google la trato como [HECHO], pero conviene releer la página original antes de decisiones caras. Las fechas de varias fuentes no se veían en el resultado; lo indico.

---

## 1. Arquitectura de URLs

### 1.1 Subdirectorios vs subdominios vs ccTLD vs parámetros

| Opción | A favor | En contra | Veredicto para moldey.com (100 idiomas) |
|---|---|---|---|
| **Subdirectorios** `moldey.com/es/`, `/pt-br/` | Todo el prestigio (enlaces, historia) se acumula en un solo dominio; un solo certificado/CDN/CMS; fácil de segmentar en Search Console (propiedades por prefijo); fácil de escalar por etapas | La carpeta no indica país, solo idioma (ambigüedad `/de/` país o idioma [EVIDENCIA, guías secundarias]); Naver trabaja a nivel de dominio/subdominio, no de carpeta [EVIDENCIA débil: linguise] | **Recomendado.** |
| Subdominios `es.moldey.com` | Servidores separados por región; equipos independientes | Cada subdominio se trata como propiedad aparte en las herramientas de webmaster; 100 DNS/certs; dilución de señales [OPINIÓN] | Descartado salvo que se necesite hosting en China (ver 7.5). |
| **ccTLD** `moldey.es`, `moldey.jp` | Señal geográfica fuerte: Google usa el ccTLD como señal fuerte de país [HECHO: blog de Google 2010] | Un dominio por país (no por idioma): imposible con 100 idiomas; costo y administración; cada dominio parte de cero en autoridad | Descartado. Solo ccTLD tiene sentido para una región concreta con negocio local (no es el caso). |
| **Parámetros** `?lang=fr` | Fácil de programar | Google lo desaconseja; la indexación limpia no está garantizada [EVIDENCIA, guía secundaria: WooRank/guías 2026]; no sirve para segmentar | Prohibido para indexables. Solo para preferencias no indexables. |

Fuentes: [Google, "Working with multi-regional websites" (2010)](https://developers.google.com/search/blog/2010/03/working-with-multi-regional-websites): ccTLD = señal fuerte de país; ciertos ccTLD "vanity" (.tv, .me) se tratan como genéricos; conviene una estructura que permita segmentar. [Doc vigente de Google, "Managing multi-regional and multilingual sites"](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites): recomienda **URLs distintas por versión de idioma** + hreflang, y evitar traducciones "lado a lado" en la misma página. **Contexto clave:** el ajuste de "segmentación por país" de Search Console **ya no existe** (ver 7.1): para un sitio por idiomas la señal principal es el idioma del contenido + hreflang, no el país.

[HECHO\*] Google detecta el idioma por el **contenido visible**, no por el atributo `lang` ni por metaetiquetas; la documentación pide: toda la página traducida (menús, pie, botones, no mezclar idiomas), una URL por idioma y **no** usar cookies para cambiar de idioma. Todo lo anterior hay que reconfirmarlo contra la página vigente.

**Estructura sugerida:**

```
https://moldey.com/                      -> inglés (en + x-default)
https://moldey.com/es/                   -> español (genérico)
https://moldey.com/pt-br/  /fr/  /de/  /ja/  /ar/  /hi/ ...
https://moldey.com/languages/            -> selector rastreable (ver 4)
https://moldey.com/es/moldes/vestido-camisero-0042/
https://moldey.com/ja/patterns/shirt-dress-0042/   (slug ASCII + ID estable, ver 1.2)
```

Notas de diseño [OPINIÓN]: (a) la raíz en inglés concentra la autoridad en la URL más enlazada; si el contenido fuente lo escribe la dueña en español, mantener `/es/` como fuente y el inglés como primera traducción: el `x-default` no tiene que ser el idioma fuente. (b) **Idioma, no país:** una carpeta por idioma. Solo crear variante regional (`/pt-br/` vs `/pt-pt/`, `/es-mx/`, `/en-gb/`) si el contenido realmente difiere (terminología, tallas, moneda, IVA); si no, Google tiende a agrupar páginas casi idénticas del mismo idioma y elige un canónico (ver el caso fr-be en 2.4). (c) **Formato de papel (A4/Letter), unidades (cm/in) y tallas (EU/US/UK/AR)** se resuelven dentro de una misma página con selectores/pestañas, no con una URL por país.

### 1.2 Slugs traducidos vs inglés; caracteres no latinos; canonicalización

- **Slugs traducidos:** [OPINIÓN] el peso de las palabras de la URL como factor de ranking es mínimo; el valor es de legibilidad/CTR. Con 100 idiomas el costo operativo (mapa slug↔idioma, colisiones, redirecciones 301 si cambia el título) es alto. **Regla:** idiomas de escritura latina (es, pt, fr, de, it, nl, pl, tr, id, vi…) → slug traducido y sin diacríticos (ver tabla 5.3); idiomas de escritura no latina (ar, hi, ja, ko, zh, th, ru, fa…) → **slug ASCII (inglés o transliterado) + ID numérico estable** y el título nativo en `<title>`/H1. El ID (`-0042`) permite que `hreflang`, canónicos y sitemaps se generen por clave (ID de producto), sin depender del texto.
- **URLs con caracteres no latinos:** [HECHO\*] Google admite URLs con caracteres no ASCII si están codificados en UTF-8 con percent-encoding; dominios IDN se representan en punycode. Problemas prácticos [OPINIÓN]: un slug japonés de 30 caracteres se vuelve ~270 caracteres al copiarlo; las discrepancias entre la versión decodificada y la codificada generan duplicados si no se normaliza; los errores de encoding en sitemaps/hreflang son una fuente clásica de fallos. **No usar dominios IDN** (un solo dominio `moldey.com`). Si alguna vez se usan slugs nativos: normalizar a **NFC** antes de codificar, y que canónico, hreflang y sitemap usen **exactamente la misma cadena codificada**.
- **Canonicalización:** (1) cada URL de idioma es **autocanónica** (`rel=canonical` apuntando a sí misma); **nunca** canonicalizar una traducción hacia la versión original: le dice a Google que ignore la traducción y contradice el hreflang; (2) la URL del canónico tiene que ser idéntica a la del hreflang; (3) una sola forma por URL: https, sin `www` (o con), minúsculas, barra final consistente, carpeta de idioma en minúsculas (`/pt-br/`); (4) parámetros de seguimiento/orden/filtro → canónico a la URL limpia y no incluirlos en sitemaps; filtros combinados (talla × tela × formato) sin indexar (`noindex` o robots.txt según el caso); (5) ninguna URL redirigida/404/noindex dentro de clústeres hreflang ni en sitemaps.

### 1.3 Escala: 100 idiomas × catálogo → rastreo y sitemaps

- [HECHO] La guía de Google sobre presupuesto de rastreo está dirigida a sitios con **más de 1 millón de páginas con cambios semanales o más de 10.000 con cambios diarios**; para el resto basta con mantener el sitemap al día y revisar la cobertura ([Google, guía de presupuesto de rastreo](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget); URL normalizada, se quitó un sufijo malformado). Un catálogo de 2.000 moldes × 100 idiomas = **200.000 URLs de producto** + categorías/blog: se acerca a ese régimen.
- [OPINIÓN] En un sitio **nuevo**, el límite real suele ser la *demanda* de rastreo/indexación (autoridad, enlaces), no la capacidad del servidor: es frecuente ver "descubierta, actualmente sin indexar" cuando se lanzan cientos de miles de URLs casi idénticas de golpe. Por eso el despliegue **escalonado** y la regla "solo lo revisado se indexa" (sección 3) son también una estrategia de rastreo.
- **Límites de sitemap** [EVIDENCIA: protocolo de sitemaps; resumen en [Linkbot](https://library.linkbot.com/what-are-the-url-and-file-size-limits-for-sitemaps-and-how-can-large-sites-adapt/)]: 50.000 URLs y 50 MB sin comprimir por archivo; se agrupan con un índice de sitemaps. No pude abrir la página oficial de Google de sitemaps en esta sesión.
- **Trampa matemática con hreflang en sitemap** [cálculo propio, estimación]: cada `<xhtml:link>` pesa ~113 bytes; con N idiomas cada URL lleva N+1 enlaces. Con 100 idiomas ≈ 11,7 KB por entrada ⇒ el tope de 50 MB se alcanza a **~4.300–4.500 URLs por archivo**, no a 50.000. Con 25 idiomas ≈ 16.000 URLs; con 10 ≈ 33.000. Fuente de la mecánica: los `xhtml:link` no cuentan para el tope de 50.000 URLs pero sí para el tamaño [EVIDENCIA débil, resumen de buscador]. Consecuencia: 200.000 URLs de producto ⇒ ~45–50 sitemaps; es manejable con un índice, pero **generarlos por script a partir de la base de datos** (clave = ID de producto).
- **Estructura recomendada:** `/sitemap.xml` (índice) → `sitemaps/{idioma}-productos-{n}.xml`, `{idioma}-categorias.xml`, `{idioma}-blog.xml`, `imagenes-…`; ≤ 5.000–10.000 URLs por archivo para poder diagnosticar por archivo en Search Console [OPINIÓN]; `lastmod` real (solo cuando cambia el contenido). Declarar el índice en `robots.txt`. Incluir en el sitemap **solo** URLs indexables 200 y aprobadas.
- Existe una afirmación de una guía alemana de que Googlebot trunca el HTML por encima de 2 MB: **[NO VERIFICADO]** (resumen de buscador, no contrastado con Google). Mantener el HTML de producto muy por debajo (< 300 KB sin comprimir) lo hace irrelevante.

---

## 2. hreflang

### 2.1 Qué es y cómo se declara

- [HECHO] Google ([Tell Google about localized versions of your page](https://developers.google.com/search/docs/specialty/international/localized-versions)): `<link rel="alternate" hreflang="…" href="…">`; **cada variante lleva el mismo conjunto de enlaces, incluida ella misma**; tres métodos válidos: **HTML `<head>`**, **cabecera HTTP `Link`** (útil para archivos no HTML como PDF) y **sitemap XML**. El anuncio de 2012 dice que el marcado en sitemap funciona igual que las etiquetas ([Google 2012](https://developers.google.com/search/blog/2012/05/multilingual-and-multinational-site)).
- [EVIDENCIA] Google combina señales de HTML y sitemap ([SEJ](https://www.searchenginejournal.com/google-combines-hreflang-signals-from-html-sitemaps/389219/)); el orden de los atributos no importa ([Hall Analysis](https://hallanalysis.com/google-says-order-hreflang-attributes-dont-matter/)). Varias guías aconsejan **no mezclar métodos en las mismas URLs** (mantenimiento, riesgo de contradicción) [OPINIÓN].
- **Qué método con 100 idiomas:**
  - **HTML head:** ~11 KB sin comprimir de `<link>` en cada página (se comprime muy bien con gzip/Brotli, pero es peso y obliga a regenerar todas las páginas cuando se agrega el idioma 12).
  - **Cabecera HTTP:** impráctica con muchos idiomas (límites de tamaño de cabeceras) [OPINIÓN]; solo para PDFs si se quieren indexar.
  - **Sitemap:** recomendado para clústeres grandes ([Propellic](https://www.propellic.com/blog/scaling-hreflang-moving-international-seo-markup-from-html-to-xml-sitemaps), [spec](https://specification.website/spec/i18n/sitemap-hreflang.md)): agregar un idioma = regenerar sitemaps, sin tocar plantillas. Aviso: un único hilo de consultoría (Telegram, **anecdótico**) dice que la validación vía sitemap tarda días o semanas más en asentarse. **Decisión:** sitemap como método único para URLs de producto/categoría; HTML head solo para las ~10 páginas clave (home, selector) si se desea redundancia.

### 2.2 Códigos de idioma, región y escritura

- [HECHO] Google solo admite **idioma ISO 639-1** y **región ISO 3166-1 Alpha 2**; "otros códigos no incluidos en esos estándares, como **es-419**, no son compatibles" (resumen de la página oficial). `en-UK` es erróneo (es `en-GB`). La región sola (p. ej. `hreflang="us"`) no funciona: hay que indicar idioma.
- **Escritura (script):** conflicto de fuentes. La doc de Google (en el resumen) no menciona subetiquetas de escritura; terceros dicen que Google acepta `zh-Hans`/`zh-Hant` ([http.dev](https://http.dev/hreflang), [FlyRank](https://flyrank.com/blogs/seo-hub/how-to-handle-hreflang-for-languages-with-multiple-scripts-e-g-chinese-simplified-vs-traditional)) y que el estándar RFC 5646 las contempla. Estado: **[NO VERIFICADO]** que Google las documente hoy. **Decisión conservadora [OPINIÓN]:** `zh-CN` y `zh-TW` (dentro de lo documentado) y carpetas `/zh-cn/`, `/zh-tw/`; revisar en pruebas reales si `zh-Hans/zh-Hant` se respetan antes de migrar.

| Caso | Recomendación | Estado |
|---|---|---|
| Chino simplificado / tradicional | `zh-CN` / `zh-TW` (+ `zh-HK` solo si contenido distinto) | Conservador; `zh-Hans/Hant` [NO VERIFICADO] |
| **Cantonés (`yue`)** | No existe ISO 639-1. Servir **chino tradicional como `zh-HK`**; el cantonés escrito en la web comercial casi siempre es chino estándar tradicional con léxico de HK [OPINIÓN]. `yue` existe en otros sistemas de Google (p. ej. Cloud Speech usa `yue-Hant-HK`, [doc](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.LanguageCodes.ChineseCantonese)), pero eso no prueba soporte en hreflang | [NO VERIFICADO] que `yue` valga en hreflang |
| Serbio (`sr`) | Una sola escritura por URL. Publicar **latín** (`sr`) al inicio; cirílico solo con evidencia de demanda | [OPINIÓN] |
| Filipino/tagalo | `tl` (639-1) en vez de `fil` (639-2) bajo la regla de Google | [NO VERIFICADO] que `fil` se ignore; probar |
| Hebreo | `he` | [OPINIÓN] |
| Noruego | `no` | [OPINIÓN] |
| Español latinoamericano | `es` genérico; `es-MX`/`es-AR` solo si hay diferencias reales; **`es-419` no vale** | [HECHO] |
| Variedades sin 639-1 (cebuano `ceb`, sorani `ckb`, bhojpurí, maithili, wu, hakka, min nan, árabe magrebí…) | Servirlas **con el idioma estándar** (árabe `ar`, hindi `hi`, chino) y no crear clúster propio; si se publica una versión propia, autocanónica, **fuera del clúster hreflang** o con código de 3 letras bajo prueba | [OPINIÓN]; ver carpeta `terminologia/` del proyecto |

(Para variedades que se buscan en el idioma estándar, el proyecto ya tiene agentes de terminología con la forma escrita real de búsqueda; este informe no la repite.)

### 2.3 `x-default`

- [HECHO] ([Google, 2023](https://developers.google.com/search/blog/2023/05/x-default)): `x-default` es la URL **neutra en idioma y región** para usuarios cuyo idioma no cubre el sitio; puede ser un selector de idioma, una URL de redirección para regiones sin contenido o simplemente la versión que se considere por defecto; las URLs de hreflang (incluido x-default) **también pueden usarse para descubrir URLs**. Yandex lo documenta igual para páginas cuyo idioma se elige automáticamente ([Yandex](https://yandex.com/support/webmaster/en/yandex-indexing/locale-pages)).
- Estudio Ahrefs (374.756 dominios): **67% con al menos un problema**, **56,3% sin x-default**, 18% con páginas sin autorreferencia ([Ahrefs](https://ahrefs.com/blog/hreflang-study); fecha no visible). Estudio de Search Engine Land (SALT.agency, ~2023): 31% de sitios internacionales con errores; 16% sin autorreferencia ([SEL](https://searchengineland.com/study-31-of-international-websites-contain-hreflang-errors-395161)). Las cifras difieren porque las muestras son distintas [EVIDENCIA]. Una cifra muy repetida de "75% con errores" no pude rastrearla a fuente: **[NO VERIFICADO]**.

### 2.4 Errores frecuentes y qué es una "señal"

1. **Sin reciprocidad** (A apunta a B, B no a A): Google ignora el par/clúster [EVIDENCIA, guías].
2. **Sin autorreferencia** (Google lo trata como buena práctica; Ahrefs lo menciona como "más bien buena práctica y no estrictamente necesario"; incluirla siempre).
3. Códigos inválidos (`en-UK`, `es-419`, `iw` vs `he`, `zh_TW` con guion bajo).
4. Apuntar a URLs que redirigen, dan 404 o están en `noindex`/canonicalizadas a otra.
5. **Canonical ≠ URL del hreflang**, o canonical apuntando a otro idioma.
6. Mezclar métodos con datos distintos.
7. hreflang a nivel de página para una sección y no para otra (clústeres incompletos).

[HECHO/EVIDENCIA] **hreflang es una pista, no una directiva** ([SEJ, reporte de una respuesta de Mueller](https://www.searchenginejournal.com/google-reminds-that-hreflang-tags-are-hints-not-directives/546428/); fecha no visible): no garantiza indexación; en variantes del mismo idioma (caso `fr-be`) Google puede consolidar en un canónico y **cambiar la URL mostrada en los resultados** según idioma/país, aunque Search Console informe sobre la URL canónica ([Gabe, "hreflang magic trick"](https://www.gsqi.com/marketing-blog/hreflang-magic-trick-revealed/)). Tampoco "da ranking": intercambia qué URL se muestra [OPINIÓN de un consultor; no hay declaración oficial en contra].

### 2.5 Cuándo NO es necesario

- Sitio de un solo idioma; idiomas sin traducción real; páginas `noindex` o no aprobadas (no deben entrar al clúster).
- Páginas sin equivalente: no inventar clústeres parciales; el clúster solo incluye idiomas que existen para esa URL.
- No es un mecanismo de ranking ni de "geotargeting" por sí mismo [OPINIÓN]. Aun sin hreflang, Google indexa cada URL por separado y detecta el idioma por contenido; con hreflang evitás mostrar `/es/` a un usuario que busca en portugués y facilitás el descubrimiento.

### 2.6 Qué motores lo usan

| Motor | Uso de hreflang | Qué usar además | Fuente / estado |
|---|---|---|---|
| **Google** | Sí (pista) | Contenido visible, canónico, sitemaps | [HECHO] |
| **Yandex** | Sí; ISO 639-1 + ISO 3166-1 (o ISO 3166-2:RU); `x-default` | Webmaster regional | [HECHO: Yandex](https://yandex.com/support/webmaster/en/yandex-indexing/locale-pages) |
| **Bing** | **Señal débil o no usada.** Fabrice Canel (2020): "hreflang es una señal mucho más débil que content-language en Bing" ([X](https://x.com/facan/status/1304120691172601856), [SERoundtable](https://www.seroundtable.com/bing-hreflang-weak-signal-30099.html)). **Pero** el blog de Bing de diciembre de 2025 sobre contenido duplicado menciona hreflang entre las señales de claridad ([Bing, dic. 2025](https://blogs.bing.com/webmaster/December-2025/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility), [SEJ](https://www.searchenginejournal.com/microsoft-explains-how-duplicate-content-affects-ai-search-visibility/563823/)) | `Content-Language` (cabecera y/o `<meta http-equiv>`) + `<html lang>` + contenido | **Contradicción:** [Lumar](https://www.lumar.io/learn/seo/international-seo/hreflang/) dice que Bing no lo soporta; [Mangools](https://mangools.com/blog/hreflang/) dice que lo recomienda pero pesa menos. Poner ambos: no entran en conflicto |
| **Baidu** | Sin evidencia de soporte; una fuente de los resultados afirma que Baidu y Bing se apoyan en `Content-Language` en lugar de hreflang (no pude identificar cuál de las páginas lo decía) | `Content-Language: zh-CN`, contenido en chino simplificado | [NO VERIFICADO] |
| **Naver** | Guías de terceros aconsejan hreflang con varios locales, pero no hay doc oficial vista | Señales claras de coreano; Search Advisor | [NO VERIFICADO] ([Linguise](https://www.linguise.com/blog/guide/naver-seo-guide/)) |
| Seznam | Sin datos | — | [NO VERIFICADO] |

**Plan:** emitir (a) hreflang en sitemap, (b) `<html lang="xx">` y `Content-Language: xx` por página. Cuesta poco y cubre Google, Yandex y Bing.

### 2.7 Validación

- Search Console **ya no tiene** informe de hreflang ni de segmentación internacional (ver 7.1) ⇒ validar fuera: rastreadores (Screaming Frog, Sitebulb, auditorías de Ahrefs/Semrush) y probadores como [technicalseo.com](https://technicalseo.com/tools/pages/docs/hreflang.html).
- **Validador propio recomendado [OPINIÓN]:** script que, para cada ID de producto, comprueba que (1) todas las URLs del clúster devuelven 200, (2) son indexables y autocanónicas, (3) cada una lista a todas las demás y a sí misma, (4) los códigos pertenecen a una lista blanca, (5) el idioma detectado del contenido coincide con el hreflang (detector tipo `fastText lid.176` o CLD3) y (6) no hay caracteres de otro alfabeto en idiomas latinos (detecta traducciones fallidas/mezcla de idiomas). Ejecutarlo en CI antes de generar sitemaps.
- Inspección de URL en Search Console: ver el "canónico seleccionado por Google" vs el declarado.

---

## 3. Traducción automática, IA y spam

### 3.1 Qué dice Google (cronología)

| Cuándo | Qué | Calidad de fuente |
|---|---|---|
| Hasta 2024 | La política de "contenido generado automáticamente de forma spam" incluía **texto traducido por una herramienta automática sin revisión humana antes de publicar**; con "elemento humano", no | [HECHO]: documentación citada por [Slator](https://slator.com/google-shares-current-view-on-using-ai-for-website-translation/) |
| 2018–2019 | Mueller: la traducción automática ya es tan fluida que puede engañar al ranking; **depende de la intención**; usar DeepL/Google Translate **no** dispara por sí solo una acción manual | [EVIDENCIA] secundaria ([McKaye](https://jamiemckaye.com/how-does-google-feel-about-machine-translation)) |
| 2022 | Mueller (Office Hours): traducir automáticamente **todo** el sitio ⇒ "probablemente lo veríamos como sitio de menor calidad"; retocar con traductores competentes "está perfectamente bien" | [HECHO/EVIDENCIA] ([SEJ](https://www.searchenginejournal.com/is-google-okay-with-minor-tweaks-to-machine-translations/468763/)) |
| ~2024 | Office Hours: **revisión por hablantes nativos**; no existe marcado especial para "traducción automática" | [EVIDENCIA] ([Slator](https://slator.com/google-shares-current-view-on-using-ai-for-website-translation/); fecha aproximada) |
| Mar 2024 en adelante | La política vigente es **"scaled content abuse"** (abuso de contenido a escala): generar muchas páginas con el fin principal de manipular rankings, **sea con IA, humano o scraping**; no se prohíbe la IA ni el volumen por sí mismos | [HECHO\*]; resumen en guías ([SEJ, análisis de la actualización](https://www.searchenginejournal.com/in-depth-look-at-google-spam-policies-updates/511005/)) |
| May–jun 2025 | **Caso Reddit:** Reddit tradujo con IA decenas de millones de URLs y afirmó que estaba "totalmente sancionado" por Google ([Gabe, X, mayo 2025](https://x.com/glenngabe/status/1919725258459758822)). Google respondió (a Gabe) que no comenta sitios concretos, que su política **no define estrictamente como spam el contenido traducido con IA**, pero que "scaled content abuse" menciona las transformaciones automatizadas, **incluidas traducciones** ([Gabe, X, jun. 2025](https://x.com/glenngabe/status/1932820373587763485)); [Search Engine Land](https://searchengineland.com/google-comments-on-reddits-use-of-ai-to-translate-its-pages-456908) concluye que Google **no** dijo que toda traducción con IA esté bien | [HECHO/EVIDENCIA] |
| Jun 2025 | Google **quitó de su documentación multilingüe el consejo de bloquear con robots.txt las páginas autotraducidas**; lo describió como cambio solo de documentación; ahora apunta a controles por página (`meta robots`) ([SERoundtable: "Google softens its stance…"](https://www.seroundtable.com/google-softens-automated-translation-stance-39579.html); [análisis de Gabe](https://www.gsqi.com/marketing-blog/auto-translating-content-google-scaled-content-abuse/)) | [HECHO/EVIDENCIA]. La página oficial vigente no menciona hoy la traducción automática en el resumen que vi |
| Jul 2026 | Gabe reporta que las páginas con traducción IA de Reddit **están cayendo** en Google, incluidas AI Overviews/AI Mode, y lo vincula con la core update de mayo de 2026 y la spam update de junio de 2026 ([Gabe, X](https://x.com/glenngabe/status/2075271515012997341)) | **[NO VERIFICADO]**: solo vi el resumen del post; confirmar antes de citar |

**Lectura honesta [OPINIÓN]:** (1) Google *no* prohíbe la traducción automática per se; sí penaliza (por algoritmo o acción manual) el **volumen sin valor**. (2) **El caso Reddit no es extrapolable:** contenido original de usuarios (UGC) en una de las webs con más autoridad del mundo; en 2025 "subió" y en 2026 habría caído, es decir, ni siquiera ahí es estable. (3) Hay **controversia**: Reddit dice "sancionado"; Google solo reitera la política general. (4) Casos/estudios *con metodología* de sitios pequeños con traducción masiva por IA (subidas/caídas): **no pude encontrarlos** en esta sesión (presupuesto agotado). Las historias de la industria son anecdóticas y no las cito.

### 3.2 Umbrales de calidad prácticos (propios, no de Google)

Google no publica umbral numérico. Propuesta [OPINIÓN], inspirada en prácticas de localización (MQM):

| Nivel de página | Ejemplos | Proceso | Criterio de publicación |
|---|---|---|---|
| **A** (≈5%) | Home, categorías, top 50 productos, guía de tallas, selector, políticas, checkout | Traducción humana o MT + post-edición completa por nativo | 100% revisado |
| **B** (≈85%) | Fichas de producto restantes (nombre, descripción, atributos) | MT con **glosario** + estimación automática de calidad (p. ej. COMET/xCOMET) para priorizar + **muestreo** 10–20% por lote e idioma | Lote aprobado si 0 errores críticos y ≤ ~1 error mayor cada 1.000 palabras en la muestra; si falla, todo el lote vuelve a revisión |
| **C** | Blog/guías de cola larga | Solo con revisión nativa completa | 100% |

- **Flujo seguro:** MT → post-edición nativa → glosario de costura (margen de costura, pinza, hilo del tejido/derecho, piquete, holgura, ancho de tela, "tiled print", plotter A0…) → LQA por muestreo → **publicar**. Mientras no esté aprobada la página: `noindex, follow`, **fuera del sitemap y del clúster hreflang**, sin enlaces destacados desde el selector. **No** bloquearla con robots.txt (Google no podría ver el `noindex`) [HECHO\*]; coincide con la decisión de Google de preferir controles por página.
- **La traducción literal falla en palabras clave, no solo en estilo:** "molde" en rioplatense vs "patrón" en España/México, "patron de couture", "Schnittmuster", "型紙", "выкройка"… [OPINIÓN]. El detalle por idioma está en la carpeta `terminologia/` del proyecto.
- **Evitar "plantilla repetida":** fichas casi idénticas salvo el nombre = riesgo de contenido delgado/duplicado *dentro* de cada idioma. Agregar datos reales localizados (rango de tallas, nº de hojas A4, rendimiento de tela, nivel de dificultad, formato, tabla de medidas, FAQ de impresión).
- **Etiquetado:** no existe marcado para "traducido por máquina" [EVIDENCIA, Mueller]. Un aviso visible tipo "traducción automática, ayúdanos a mejorarla" en páginas B pendientes puede ser honesto para el usuario, pero esas páginas deberían estar `noindex`.
- **Despliegue escalonado [OPINIÓN]:** Ola 0 (idioma fuente + inglés, gate completo) → Ola 1 (~10 idiomas de escritura latina con alta demanda y pagos disponibles) → Ola 2 (RTL, CJK, cirílico) → Ola 3 (índicas, sudeste asiático) → Ola 4 (cola larga ~50+). Criterio para pasar de ola: evidencia de demanda en Search Console (impresiones/consultas de ese idioma sin tener página), tasa de revisión aprobada, indexación de la ola anterior > ~70–80% de lo enviado y ausencia de caída global.

---

## 4. Detección y redirección por idioma/IP

- [HECHO\*] Google: **evitar redirigir automáticamente según idioma percibido** (puede impedir que usuarios y buscadores vean todas las versiones); usar URLs distintas y enlaces entre versiones; no usar cookies para decidir el idioma de una URL.
- [HECHO] ([Google, páginas adaptadas por locale](https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages?authuser=1), [blog 2015](https://developers.google.com/search/blog/2015/01/crawling-and-indexing-of-locale)): el rastreador por defecto **no envía `Accept-Language` y usa IPs de EE. UU.**; también rastrea desde IPs de otros países y puede enviar `Accept-Language`; aun así Google **sigue recomendando URLs separadas con hreflang**. Si servís otro contenido en la misma URL según IP/idioma, Google puede no rastrear/indexar todo.
- **Qué hacer [OPINIÓN]:**
  1. Cero redirecciones automáticas por IP/idioma a bots *ni* a personas en URLs profundas.
  2. **Banner no bloqueante** ("¿Preferís ver moldey en Español? / Ver en español") basado en `navigator.language`/`Accept-Language`; recordar la elección en `localStorage`/cookie funcional (revisar consentimiento); el banner no cambia el contenido principal del HTML.
  3. `Vary: Accept-Language` solo si la **misma URL** devuelve contenido distinto según esa cabecera (no recomendado: fragmenta la caché del CDN). Con banner client-side no hace falta.
  4. Moneda/tallas/formato de papel: por defecto según el **idioma** de la URL y cambiables por el usuario; no por IP en servidor (Googlebot vería siempre USD/EE. UU.). El precio visible tiene que coincidir con el JSON-LD (sección 8).
  5. Raíz `/` = inglés y `x-default`; si algún día se prefiere selector como `x-default`, no redirigir desde ahí.
- **Selector de idioma rastreable y accesible:**
  - Enlaces `<a href>` reales (no `<select>` con JS ni banderas); texto en el **endónimo** ("Español", "Português (Brasil)", "日本語", "العربية"); banderas representan países, no idiomas.
  - Cada enlace con `lang` y `hreflang`: `<a href="/ja/" lang="ja" hreflang="ja">日本語</a>`.
  - Con ~100 idiomas: no poner 100 enlaces en la cabecera de cada página; un menú breve (idioma actual + ~8) y enlace "Todos los idiomas" a `/languages/` (página estática con la lista completa, indexable) desde el pie.
  - Accesibilidad: teclado, `aria-current="true"` en el idioma actual, no depender de hover.

---

## 5. Contenido específico por escritura y lengua

> Sección redactada sin búsquedas propias (presupuesto agotado): todo es **[HECHO\*]** (estándares W3C/Unicode/MDN conocidos) u **[OPINIÓN]** salvo indicación. Verificar los puntos marcados.

### 5.1 Reglas transversales

- `<html lang="xx" dir="ltr|rtl">` correcto en cada página (afecta a navegadores, lectores de pantalla, traducción de Chrome y variantes de glifos, no a la detección de idioma de Google, que usa el contenido visible).
- Guardar y servir todo en **UTF-8**, texto en **NFC** (URLs, slugs, búsqueda interna).
- El `<title>`, H1 y metadescripción se **redactan** en el idioma (no se traducen mecánicamente): los límites de píxeles cambian con la escritura [OPINIÓN].

### 5.2 Por escritura

| Escritura / lengua | Puntos técnicos clave |
|---|---|
| **CJK** (zh, ja, ko) | Sin espacios entre palabras: los buscadores segmentan internamente; no hace falta "agregar espacios". `lang` correcto es obligatorio por la **unificación Han** (misma codepoint, glifos distintos en ja/zh-Hans/zh-Hant/ko): sin `lang`, un kanji puede renderizarse con la forma china. Títulos: los glifos CJK son ~2× más anchos que los latinos y Google trunca por píxeles ⇒ ~28–35 caracteres de título y ~70–100 de descripción como orden de magnitud [OPINIÓN, probar en SERP real]. CSS: `word-break: keep-all` (coreano), `line-break: strict` (japonés). Búsqueda interna: normalizar **NFKC** (ancho completo/medio ancho: `ＰＤＦ` vs `PDF`), y kana/kanji/romaji (ja) |
| **Árabe, hebreo, persa, urdu (RTL)** | `dir="rtl"` en `<html>`; usar **propiedades lógicas** de CSS (`margin-inline-start`) y plantillas espejadas; no espejar logotipos, iconos de reproducción ni números de teléfono. Fragmentos LTR dentro de RTL ("A4", "PDF", "DXF", "moldey") con `<bdi>`/`unicode-bidi`. **Números:** el árabe usa dígitos occidentales (Magreb, mucho comercio) u orientales ٠١٢٣ (Oriente Medio); persa y urdu usan ۰۱۲۳ (variante extendida): elegir por idioma y probar con `Intl.NumberFormat`. Normalizar en búsqueda interna las letras árabes vs persas (ي/ی, ك/ک) y quitar *tashkeel*/*niqqud*; persa: respetar el ZWNJ (U+200C) |
| **Índicas** (hi, bn, ta, te, mr, gu, kn, ml, pa, or…) | Pesos de fuente altos y conjuntos de caracteres complejos. Usar la fuente del sistema como primera opción (Android/iOS traen las principales) y WOFF2 *subset* por escritura (Noto Sans Devanagari/Bengali/Tamil…) solo como respaldo; `font-display: swap`. Normalizar nukta y conjuntos (NFC) en búsqueda y slugs. **Punjabi:** Gurmukhi (India) vs Shahmukhi (Pakistán, escritura árabe) ⇒ códigos y versiones distintas (`pa-IN`, `pa-PK`). Hindi/urdú comparten lengua hablada pero se escriben con escrituras distintas ⇒ páginas distintas |
| **Birmano** | **Zawgyi (codificación heredada) vs Unicode:** publicar **solo Unicode**. Google y otros migraron a Unicode (cambio nacional hacia 2019) [NO VERIFICADO en esta sesión]; hay librerías de detección de Zawgyi (Google "myanmar-tools") para convertir la entrada del buscador interno [NO VERIFICADO] |
| **Tailandés, jemer, lao** | Sin espacios entre palabras (segmentación por diccionario en el navegador/buscador). `lang="th"`; no insertar espacios artificiales. Fechas: el año budista (2569 = 2026) se muestra en la UI con `Intl` (`th-TH-u-ca-buddhist`) pero en datos estructurados siempre ISO gregoriano |
| **Serbio y otros doble escritura** | Serbio (cirílico/latín), kazajo (transición cirílico→latino en curso, calendario incierto [NO VERIFICADO]), uzbeko (latino oficial, cirílico aún usado), punjabi. Regla: **una escritura por URL**; si ofrecés ambas, URLs separadas y canónicos propios, o una sola con conmutador que no cambie la URL (y entonces el buscador solo ve una escritura) |
| **Latín con diacríticos** (vi, tr, pl, cs, de, es…) | El **vietnamita** se busca con y sin tonos ("ao dai" por "áo dài"): publicar el texto **con** tonos (Google lo entiende) y usar slugs sin tonos; búsqueda interna con *diacritic folding*. **Turco:** la `İ/ı` rompe las conversiones de mayúsculas/minúsculas: usar `toLocaleLowerCase('tr-TR')` y `lang="tr"` con `text-transform`; slug: `ı→i, ş→s, ğ→g, ç→c, ö→o, ü→u`. Letras que no descomponen en NFD (`ł`, `ø`, `đ`) y `ß` necesitan tabla de transliteración explícita para slugs |
| **Transliterado ("romanized") como se busca** | **Hinglish** ("silai pattern"), **arabizi** (árabe con números), persa en latinas, bengalí/tamil en latín, "greeklish", ruso en latín. Es consulta real pero Google la mapea parcialmente a la escritura nativa [NO VERIFICADO]. **No crear páginas romanizadas** (duplicados/spam): incluir de forma natural la variante romanizada en texto secundario (subtítulo, etiquetas, FAQ) solo en los mercados donde Search Console muestre esas consultas |

### 5.3 Fuentes web: tamaños orientativos [NO VERIFICADO, órdenes de magnitud]

| Familia | Fuente completa | Estrategia |
|---|---|---|
| Latín/cirílico/griego | ~20–50 KB por peso en WOFF2 | Autoalojar, *subset*, `font-display: swap`, 1–2 pesos |
| Índicas | ~50–300 KB por escritura | Pila del sistema primero; WOFF2 subset con `unicode-range` |
| **CJK** | 1–20 MB (según cantidad de glifos) | **No cargar fuente web:** pila del sistema por idioma (`:lang(ja)`, `:lang(zh-CN)`, …); si se exige marca, usar rebanadas `unicode-range` (Google Fonts parte las fuentes CJK en muchas rebanadas) |
| Árabe/hebreo | ~50–200 KB | Subset por idioma, ligaduras necesarias |

```css
/* Pilas del sistema por idioma: cero bytes de fuente en CJK */
:lang(ja){font-family:"Hiragino Sans","Yu Gothic UI","Noto Sans JP",system-ui,sans-serif}
:lang(zh-CN){font-family:"PingFang SC","Microsoft YaHei","Noto Sans SC",system-ui,sans-serif}
:lang(zh-TW){font-family:"PingFang TC","Microsoft JhengHei","Noto Sans TC",system-ui,sans-serif}
:lang(ko){font-family:"Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",system-ui,sans-serif;word-break:keep-all}
:lang(ar),:lang(fa),:lang(ur),:lang(he){font-family:system-ui,"Noto Sans Arabic","Noto Sans Hebrew",sans-serif}
```

---

## 6. Rendimiento y rastreo global

### 6.1 Renderizado: ¿los rastreadores de IA ejecutan JavaScript?

- [EVIDENCIA] El análisis de **Vercel con MERJ** concluye que ninguno de los rastreadores de IA principales (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Bytespider) **renderiza JavaScript**; descargan archivos .js (Claude ~23,8% de sus peticiones, ChatGPT ~11,5%) pero no los ejecutan. **Excepciones:** Gemini (usa la infraestructura de Googlebot) y Applebot renderizan; CCBot (Common Crawl) no ([Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler?ref=t01.li), [copia en examples.vercel.com](https://examples.vercel.com/blog/the-rise-of-the-ai-crawler)). Escala observada: GPTBot ~569 M y Claude ~370 M de peticiones en un mes, ≈20% del volumen de Googlebot (4.500 M). **La fecha no se veía en el resultado** (a mi memoria es de fines de 2024): **puede haber cambiado en 2025–2026 ⇒ [NO VERIFICADO] que siga siendo así**; verificar con los logs.
- [EVIDENCIA débil] TripleDart (secundario) afirma que ChatGPT y Claude gastan ~34–35% de sus peticiones en páginas 404 frente a 8% de Googlebot ([TripleDart](https://www.tripledart.com/research/why-your-site-is-invisible-to-chatgpt-and-claude)): ojo con redirecciones y 404 de URLs viejas. Adobe recomienda probar con `curl` y un *user-agent* de GPTBot ([Adobe](https://experienceleague.adobe.com/en/perspectives/make-your-aem-content-visible-to-ai-a-practitioner-guide)).
- **Decisión [OPINIÓN]:** HTML completo en la respuesta inicial (SSG/ISR o SSR): título, texto de la ficha, enlaces de navegación, hreflang, JSON-LD y enlaces del selector **sin depender de JS**. Googlebot sí renderiza, pero con retraso y coste de recursos; para 100 idiomas el HTML estático es más barato y más seguro. Prueba de aceptación: `curl -s -A "Mozilla/5.0 (compatible; GPTBot/1.0)" URL | grep -c "<h1"`.

### 6.2 Core Web Vitals y conexiones lentas

- [HECHO\*] INP sustituyó a FID como métrica de Core Web Vitals en marzo de 2024. Umbrales "buenos" (percentil 75): **LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1**. El efecto en ranking existe pero es modesto frente a la relevancia [OPINIÓN].
- **Por región:** Search Console y PageSpeed Insights agregan por origen/grupo; los datos de campo por país requieren CrUX en BigQuery (dimensión país) o **RUM propio** (`web-vitals.js` + dimensión país en GA4) [NO VERIFICADO]. Con poco tráfico por idioma, CrUX no tendrá datos: RUM propio.
- **India/África/Sudeste asiático** (móvil, latencia alta, equipos modestos) [OPINIÓN]: presupuesto objetivo para ficha de producto: HTML < 100 KB comprimido; JS < ~150 KB comprimido y diferido; imagen LCP < 100 KB (AVIF/WebP, `fetchpriority="high"`, `srcset`); sin carruseles pesados; respetar `Save-Data`; **los PDF/DXF nunca se cargan en la ficha** (previsualizaciones en WebP; el archivo A0 se entrega tras la compra por descarga reanudable con URL firmada del CDN).
- **CDN/edge:** HTML estático cacheado en el borde (con `stale-while-revalidate`) + imágenes por CDN con negociación de formato; HTTP/2 y HTTP/3, Brotli [HECHO\* Googlebot soporta HTTP/2; el beneficio para bots es pequeño, para usuarios móviles es real].
- **Cuidado con el WAF/CDN:** bloquear por error a Googlebot, Bingbot o a rastreadores de IA que sí se quieren permitir. [NO VERIFICADO en esta sesión] Cloudflare empezó a bloquear por defecto rastreadores de IA en dominios nuevos (jul. 2025): revisar el panel y robots.txt gestionado.

---

## 7. Indexación y descubrimiento

### 7.1 Google Search Console

- [HECHO] El **informe de Segmentación internacional fue retirado** (anunciado para el 22/09/2022): se perdió la verificación de hreflang y el ajuste de país; Google sigue usando hreflang ([Ayuda de Google](https://support.google.com/webmasters/answer/12474899), [Search Engine Land](https://searchengineland.com/google-search-console-to-remove-international-targeting-report-387477)). La Búsqueda Central también organizó sesiones sobre hreflang y sitios transfronterizos en 2025 ([Search Central Live APAC 2025](https://developers.google.com/search/blog/2025/12/scl-eoy)); no vi cambios de doc de hreflang en 2025.
- [HECHO\*] **Propiedad de dominio** `moldey.com` (DNS) + **propiedades de prefijo de URL por idioma** (`https://moldey.com/es/`…) para ver rendimiento y sitemaps por idioma; exportación masiva a BigQuery; el filtro "La URL contiene `/es/`" sirve para segmentar. Los informes Product snippets/Merchant listings dependen de los datos estructurados (sección 8).
- [HECHO\*] **Indexing API:** solo para `JobPosting` y `BroadcastEvent` (directos); **no sirve para moldey**. **Google no admite IndexNow** [NO VERIFICADO en esta sesión, alta confianza]: para Google, sitemaps con `lastmod` fiable y enlaces internos.

### 7.2 Bing y IndexNow

- Bing Webmaster Tools: verificar `moldey.com`, enviar el índice de sitemaps, usar IndexNow.
- [EVIDENCIA] **IndexNow** lo soportan Microsoft Bing, Naver, Seznam.cz, Yandex y Yep, y los participantes comparten entre sí las URLs enviadas ([ficha de app de Shopify](https://apps.shopify.com/indexnow?locale=it), [Wikipedia](https://en.wikipedia.org/wiki/IndexNow)); no encontré confirmación en indexnow.org esta sesión. Un foro de 2025 advierte que algunos plugins solo envían a Bing: comprobar el endpoint real. **Plan:** archivo de clave en la raíz y llamada (POST masivo) al publicar/actualizar/eliminar una URL **aprobada** (hasta 10.000 URLs por petición según mi recuerdo de la doc [NO VERIFICADO]); enviar solo URLs que ya pasaron el gate de calidad.

### 7.3 Yandex

- [HECHO] Yandex admite hreflang con ISO 639-1 e ISO 3166-1 (o ISO 3166-2:RU), sin importar la estructura de dominios, y `x-default` ([Yandex](https://yandex.com/support/webmaster/en/yandex-indexing/locale-pages)). Registrar `moldey.com` en Yandex Webmaster, enviar sitemap, IndexNow. Relevante para ru, kk, be y parte de tr [OPINIÓN].

### 7.4 Naver y Seznam

- [EVIDENCIA débil] Naver **no descubre bien los sitios nuevos por sí solo**: registrar en **Naver Search Advisor** (verificación por archivo HTML, metaetiqueta o DNS), enviar sitemap y robots.txt, permitir el rastreador **Yeti**; el registro es a nivel dominio/subdominio, **no subcarpeta**; el panel está en coreano ([Linguise](https://www.linguise.com/blog/guide/naver-seo-guide/), [Inquivix](https://inquivix.com/seo-checklist-for-korean-market-entry-what-global-brands-miss-on-naver/); la guía más detallada es de ~2020). Naver prioriza su propio ecosistema (blogs, cafés, shopping) [OPINIÓN]: una carpeta `/ko/` traducida compite con poco peso; ganar tracción en Naver exige contenido coreano nativo y plataformas propias.
- **Seznam** (República Checa): Seznam Webmaster + IndexNow; prioridad baja salvo demanda checa [OPINIÓN].

### 7.5 Baidu (China)

- [EVIDENCIA] La licencia/registro **ICP es obligatorio para alojar en China continental**, y una empresa extranjera suele necesitar una entidad local ([AppInChina](https://appinchina.co/blog/the-complete-guide-to-chinas-icp-filing/), [MS Advisory](https://msadvisory.com/icp-license-china/)); **no es estrictamente obligatorio para aparecer en Baidu**: sitios alojados fuera pueden salir, aunque la velocidad de carga desde fuera de China los perjudica ([Chinafy](https://www.chinafy.com/blog/do-you-need-an-icp-license-to-rank-on-baidu)); recomiendan registrar en Baidu Webmaster/Search Resource Platform, enviar sitemap y tener contenido en chino simplificado ([We Interactive](https://we-interactive.com/?p=2559), [Mlytics](https://mlytics.com/blog/proven-tactics-to-optimize-your-website-for-seo-on-baidu)). Todo son consultoras: **[EVIDENCIA débil]**. Sin soporte de hreflang comprobado (ver 2.6).
- **Decisión [OPINIÓN]:** dejar China para la última ola. Primero indexar `/zh-cn/` en Google/Bing (donde el acceso es limitado) y medir; considerar Baidu solo si hay evidencia de demanda y un socio local (ICP, alojamiento).

### 7.6 Descubrimiento adicional

- Sitemaps (principal); RSS/Atom para blog y novedades; enlaces internos (selector `/languages/` y hreflang también sirven para descubrir [HECHO: Google dice que las URLs de hreflang pueden usarse para descubrimiento]); feeds de producto para Merchant Center y Pinterest (tema T2).

---

## 8. Datos estructurados multilingües

> Sin búsquedas propias (agotadas): [HECHO\*]/[NO VERIFICADO], salvo indicación. Ver también T2 (feeds de producto y compras).

- **Reglas:** JSON-LD en el HTML inicial; el marcado debe coincidir con lo visible; **todos los textos en el idioma de la página** (name, description, nombres de migas); URLs del mismo idioma.
- **`Organization`:** una sola entidad con `@id` estable (`https://moldey.com/#organization`), definida en la home (o en cada idioma con el mismo `@id`) y **referenciada** con `{"@id": …}` desde `Product`/`WebSite`; `sameAs` con perfiles oficiales (YouTube, Pinterest, Instagram, etc.); `name` constante, `alternateName` si procede por escritura (ej. "モルディ").
- **`WebSite` + `SearchAction`:** [NO VERIFICADO] Google dejó de mostrar el cuadro de búsqueda de sitelinks (retirado a fines de 2024); es opcional y de baja prioridad. `inLanguage` va en tipos `CreativeWork`/`WebPage`, no en `Product`: declararlo en el `WebPage` (`"inLanguage":"pt-BR"`, etiqueta BCP 47).
- **`BreadcrumbList`:** nombres localizados que coincidan con las migas visibles.
- **`Product`/`Offer`:** una entidad por URL de idioma; `priceCurrency` en ISO 4217; **un precio y una moneda por URL**, los mismos que muestra la página; para bienes digitales sin envío, omitir `shippingDetails`; considerar política de devoluciones a nivel organización (`MerchantReturnNotPermitted` para descargas) [NO VERIFICADO].
- **Cambios 2025–2026 en rich results [NO VERIFICADO en esta sesión]:** Google simplificó la página de resultados en junio de 2025 retirando varios tipos (p. ej. Book Actions, Course Info, Claim Review, Special Announcement, Vehicle Listing); FAQ restringido a sitios gubernamentales/de salud desde 2023 y HowTo retirado; siguen vigentes Product snippets / Merchant listings, Breadcrumb, Organization, VideoObject. Consultar `developers.google.com/search/updates` ([página de novedades](https://developers.google.com/search/updates)), que apareció en los resultados pero cuyo contenido no leí.
- Para IA/AEO: la afirmación de que el marcado ayuda a los LLM se apoya en declaraciones de empleados de Microsoft/Bing [NO VERIFICADO] y no hay estudio concluyente: **no vender el marcado como "truco de citaciones"**; sirve sobre todo para elegibilidad de rich results y claridad de entidad.

---

## 9. Imágenes, vídeo, Pinterest y búsqueda visual

> Sin búsquedas propias: [HECHO\*]/[OPINIÓN]/[NO VERIFICADO].

- **ALT** descriptivo y localizado (describe la imagen, no keyword-stuffing); nombre de archivo ASCII legible. Con 100 idiomas: **una sola URL de imagen compartida entre idiomas** (caché CDN) y ALT por idioma; archivos con nombre localizado solo en los idiomas de primera ola.
- **Texto dentro de imágenes:** los motores aplican OCR (Lens, Cloud Vision) pero no es fiable ni indexable como texto HTML. No hornear el texto (tallas, instrucciones) en el JPG: ponerlo como HTML/leyenda. Para imágenes de previsualización con texto (etiquetas de piezas), generar variantes por idioma solo para mercados prioritarios.
- **`ImageObject`:** para licencia/crédito (`license`, `acquireLicensePage`, `creator`, `creditText`, `copyrightNotice`) puede activar insignias de imagen licenciable [HECHO\*]; el `image` del Product puede ser una lista de URLs.
- **Sitemaps de imagen/vídeo:** [NO VERIFICADO] Google retiró en 2022 varias extensiones del sitemap de imágenes (solo `image:loc` útil). Sitemap de vídeo con título, descripción, miniatura y `content_loc`/`player_loc`. `VideoObject` con `name`, `thumbnailUrl`, `uploadDate`.
- **YouTube:** localización de títulos/descripciones y subtítulos por idioma [HECHO\*]; los tutoriales de costura son un canal de descubrimiento por sí mismos [OPINIÓN].
- **Pinterest:** los Pines enriquecidos (producto) se alimentan de metadatos/feeds; descripciones en el idioma local; el texto superpuesto en la imagen del Pin sí pesa en Pinterest. Costura/patrones es un sector con presencia fuerte allí [OPINIÓN, sin cifra verificada].
- **Google Lens / búsqueda visual:** imágenes limpias, de alta resolución, múltiples ángulos, fondo neutro; mismos datos estructurados que Product.

---

## 10. Medición

> [HECHO\*]/[NO VERIFICADO], sin búsquedas propias.

- **Search Console:** propiedad de dominio + prefijo por carpeta de idioma (7.1); informe de rendimiento filtrado por país y por "URL contiene"; **exportación masiva a BigQuery** para cruzar idioma × país × página sin el límite de filas de la UI/API. Mirar siempre la **relación idioma de la URL vs país de las impresiones** (ej. `/es/` con impresiones en México, Argentina, España).
- **GA4:** parámetro de evento/dimensión personalizada `content_language` (idioma de la página, enviado en cada `page_view`), distinto de la dimensión *Idioma* de GA4 (idioma del navegador); dimensión *País*; segmentos por origen IA (referrers `chatgpt.com`, `perplexity.ai`, `copilot.microsoft.com`, `gemini.google.com`) [NO VERIFICADO el set exacto de dominios].
- **Looker Studio:** conectores de Search Console y GA4 (o BigQuery) con filtros de idioma/país y una pestaña de "salud de la ola" (URLs enviadas vs indexadas, impresiones, clics, conversión por idioma).
- **Seguimiento de posiciones por país/idioma:** herramientas con geolocalización y parámetros de idioma (`hl`, `gl`) para una canasta fija de consultas por idioma; para consultas manuales usar `&hl=xx&gl=YY`. Mantener una lista de 20–30 consultas por idioma (sacadas de la investigación de terminología).
- **KPI por ola:** % URLs enviadas indexadas; impresiones y CTR por idioma; porcentaje de consultas con ficha del idioma correcto; errores de hreflang detectados por el validador propio; INP/LCP de campo por país.

---

## 11. Contradicciones y controversias

| Tema | Posiciones | Qué haría |
|---|---|---|
| ¿Bing usa hreflang? | Canel (2020): señal mucho más débil que `content-language`; blog de Bing (dic. 2025) lo menciona entre señales; Lumar: no lo soporta; Mangools: lo usa poco | Usar ambos (hreflang + `Content-Language`) |
| Escritura en hreflang (`zh-Hans`, `sr-Latn`) | Doc de Google habla solo de ISO 639-1 + 3166-1; terceros dicen que se aceptan | `zh-CN/zh-TW`; probar scripts antes |
| Traducción con IA y Google | Reddit: "sancionado"; Google: no define estrictamente como spam pero menciona traducciones en scaled content abuse; Gabe: Reddit sube en 2025 y cae en 2026 | IA solo con post-edición nativa y gate; indexar lo aprobado |
| Método hreflang | Google: equivalentes; consultor anecdótico: sitemap tarda más en asentarse | Sitemap + validador propio; vigilar con muestras |
| Rastreadores de IA y JS | Vercel/MERJ: ninguno renderiza (salvo Gemini/Applebot); fecha incierta | SSR/SSG de todos modos; verificar en logs |
| Baidu | ICP "obligatorio" (alojar en China) vs "no obligatorio para rankear" | Aplazar China |

---

## 12. Qué hacer en moldey.com (priorizado)

Impacto/esfuerzo: A = alto, M = medio, B = bajo.

| # | Acción | Impacto | Esfuerzo | Cuándo |
|---|---|---|---|---|
| 1 | Subdirectorios por idioma en **un solo dominio** (`/es/`, `/pt-br/`…), raíz en inglés + `x-default`; sin parámetros ni subdominios | A | M | Antes del lanzamiento |
| 2 | HTML estático/SSR/ISR con CDN: contenido, enlaces, hreflang, JSON-LD en el HTML inicial (verificar con `curl` y UA de GPTBot) | A | M | Antes del lanzamiento |
| 3 | Gate de calidad: MT + glosario + post-edición nativa + muestreo; `noindex` y fuera de sitemap/hreflang hasta aprobar | A | A | Desde la Ola 0 |
| 4 | Sitemaps por idioma (índice), hreflang **solo** en sitemap, generados por script por ID de producto; ≤ ~4.000 URLs por archivo con 100 idiomas | A | M | Ola 0–1 |
| 5 | Validador propio de hreflang/canónicos/idioma en CI | A | M | Ola 0–1 |
| 6 | Autocanónico por URL; nunca canonicalizar traducciones al original | A | B | Ola 0 |
| 7 | Search Console (dominio + prefijo por idioma), Bing Webmaster, Yandex Webmaster; IndexNow al publicar lo aprobado | M | B | Ola 0 |
| 8 | Selector `/languages/` con `<a>` y endónimos; banner no bloqueante; **cero redirecciones automáticas** | M | B | Ola 0 |
| 9 | JSON-LD Product/Offer/Organization(@id)/BreadcrumbList/WebPage localizados (ejemplos abajo) | M | M | Ola 0–1 |
| 10 | Fichas con datos reales localizados (tallas, hojas A4, formatos, rendimiento) para evitar plantillas delgadas | M–A | M | Ola 0–1 |
| 11 | Fuentes: pilas del sistema para CJK; subsets para índicas/árabe; presupuesto de peso por ficha | M | M | Ola 2 |
| 12 | RUM con `web-vitals` + `content_language` en GA4; panel en Looker Studio | M | M | Ola 1 |
| 13 | ALT por idioma, imagen compartida, texto no horneado; sitemap de imágenes/vídeo | M | B | Ola 1 |
| 14 | Naver Search Advisor y Baidu solo con evidencia de demanda y socio local | B | A | Ola 3+ |

**Ejemplo 1 — hreflang en sitemap (una entrada; repetir el mismo bloque, con las mismas alternativas, en cada URL del clúster):**

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://moldey.com/es/moldes/vestido-camisero-0042/</loc>
    <lastmod>2026-10-01</lastmod>
    <xhtml:link rel="alternate" hreflang="es"    href="https://moldey.com/es/moldes/vestido-camisero-0042/"/>
    <xhtml:link rel="alternate" hreflang="en"    href="https://moldey.com/patterns/shirt-dress-0042/"/>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="https://moldey.com/pt-br/moldes/vestido-camisa-0042/"/>
    <xhtml:link rel="alternate" hreflang="ja"    href="https://moldey.com/ja/patterns/shirt-dress-0042/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://moldey.com/patterns/shirt-dress-0042/"/>
  </url>
</urlset>
```

**Ejemplo 2 — `<head>` mínimo de una ficha (autocanónico + idioma; hreflang en sitemap):**

```html
<html lang="es" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>Molde de vestido camisero – PDF A4, Letter y A0 | Moldey</title>
  <link rel="canonical" href="https://moldey.com/es/moldes/vestido-camisero-0042/">
  <meta http-equiv="content-language" content="es">
  <!-- Aprobada: indexable. Pendiente de revisión: <meta name="robots" content="noindex, follow"> -->
</head>
```

(Con `Content-Language: es` también como cabecera HTTP.)

**Ejemplo 3 — selector de idioma rastreable:**

```html
<nav aria-label="Idioma">
  <a href="/" lang="en" hreflang="en">English</a>
  <a href="/es/" lang="es" hreflang="es" aria-current="true">Español</a>
  <a href="/pt-br/" lang="pt-BR" hreflang="pt-BR">Português (Brasil)</a>
  <a href="/ja/" lang="ja" hreflang="ja">日本語</a>
  <a href="/languages/">Todos los idiomas</a>
</nav>
```

**Ejemplo 4 — JSON-LD de Product en `/es/` (mismo patrón por idioma; textos, URL y moneda coherentes con la página visible):**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://moldey.com/es/moldes/vestido-camisero-0042/#webpage",
      "url": "https://moldey.com/es/moldes/vestido-camisero-0042/",
      "inLanguage": "es",
      "isPartOf": { "@id": "https://moldey.com/#website" },
      "mainEntity": { "@id": "https://moldey.com/es/moldes/vestido-camisero-0042/#product" },
      "breadcrumb": { "@id": "https://moldey.com/es/moldes/vestido-camisero-0042/#breadcrumb" }
    },
    {
      "@type": "Product",
      "@id": "https://moldey.com/es/moldes/vestido-camisero-0042/#product",
      "name": "Molde de vestido camisero (PDF A4, Letter y A0)",
      "description": "Molde digital de vestido camisero en tallas 34–50. Incluye PDF para imprimir en casa (A4/Letter), PDF A0 para plotter y DXF editable.",
      "sku": "MLD-0042",
      "image": ["https://moldey.com/img/vestido-camisero-0042-1.webp"],
      "brand": { "@type": "Brand", "name": "Moldey" },
      "offers": {
        "@type": "Offer",
        "url": "https://moldey.com/es/moldes/vestido-camisero-0042/",
        "price": "9.90",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "seller": { "@id": "https://moldey.com/#organization" }
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://moldey.com/es/moldes/vestido-camisero-0042/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://moldey.com/es/" },
        { "@type": "ListItem", "position": 2, "name": "Moldes de vestidos", "item": "https://moldey.com/es/moldes/vestidos/" },
        { "@type": "ListItem", "position": 3, "name": "Vestido camisero" }
      ]
    }
  ]
}
```

(`Organization` y `WebSite` se definen una vez, con `@id` `https://moldey.com/#organization` y `https://moldey.com/#website`, y `sameAs` de perfiles oficiales; el resto los referencia por `@id`. Validar el JSON-LD con las pruebas de Google antes de generalizar.)

**Ejemplo 5 — `robots.txt`:**

```
User-agent: *
Disallow: /cart/
Disallow: /*?sort=
Disallow: /*?filter=
Sitemap: https://moldey.com/sitemap.xml
```

(No bloquear carpetas de idioma ni páginas `noindex`; si se decide permitir o no rastreadores de IA concretos, hacerlo por *user-agent* de forma explícita y probada: tema de otros informes.)

---

## 13. Qué NO hacer

1. **No** redirigir automáticamente por IP o `Accept-Language` (ni a bots ni a personas en URLs profundas); **no** usar cookies para decidir el idioma de una URL.
2. **No** publicar y enviar a indexación 100 idiomas con traducción automática sin revisión: riesgo de "scaled content abuse" y de gastar la demanda de rastreo en páginas sin valor. **No** basar la estrategia en "Reddit lo hace".
3. **No** canonicalizar las traducciones al original; **no** incluir en el clúster hreflang páginas `noindex`, 404, redirigidas o sin aprobar.
4. **No** usar parámetros (`?lang=`), subdominios ni ccTLD para los idiomas; **no** dominios IDN.
5. **No** usar códigos inválidos (`es-419`, `en-UK`, región sola) ni `yue` en hreflang; **no** asumir que `zh-Hans/zh-Hant` valen sin probar.
6. **No** mezclar métodos de hreflang con datos distintos, ni olvidar la autorreferencia y la reciprocidad.
7. **No** crear páginas por país solo para cambiar A4/Letter, moneda o unidad: duplican contenido y diluyen señales.
8. **No** esconder el contenido tras JavaScript (rastreadores de IA que no lo ejecutan; ver 6.1).
9. **No** hornear texto en imágenes ni cargar fuentes web CJK completas.
10. **No** crear páginas romanizadas (hinglish, arabizi) ni páginas con escritura doble en la misma URL.
11. **No** poner un precio en el JSON-LD distinto del visible, ni cambiar la moneda por IP.
12. **No** vender el marcado ni `llms.txt` como mecanismo garantizado de citación por IA: no hay estudio sólido (otros informes del proyecto lo tratan).
13. **No** invertir en Baidu/Naver antes de tener demanda demostrada y un plan local.

---

## 14. Lo que quedó sin poder verificar (siguiente pasada)

- Texto vigente de la doc de Google sobre: lista exacta de códigos aceptados en hreflang (¿escrituras?), recomendación textual sobre redirecciones por idioma, política de la sección "traducción automática" tras el cambio de junio de 2025, límites actuales de sitemaps, y tamaño máximo de HTML rastreado.
- Casos con metodología de sitios con traducción IA masiva (subidas/caídas) fuera de Reddit, y confirmar la caída de Reddit en 2026.
- Soporte real de hreflang en Baidu, Naver, Seznam; requisitos actuales de registro en Baidu/Naver.
- Datos estructurados: cambios de rich results 2025–2026, estado de `inLanguage`, retornos para productos digitales, sitemaps de imagen.
- Fuentes web: tamaños reales, CrUX por país; rastreadores de IA y JS en 2025–2026 (el estudio de Vercel/MERJ no mostraba fecha); política de Cloudflare sobre rastreadores de IA.
- Estado de IndexNow en Google, límites de IndexNow y de la API de envío de URL de Bing.
