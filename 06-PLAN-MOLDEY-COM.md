# 06 · Plan completo para moldey.com

> **Qué es esto:** el plan de ejecución para mejorar la visibilidad global (SEO + AEO/GEO) de **moldey.com**, un sitio que vende moldes digitales de costura (PDF para imprimir, archivos editables y plantillas de sublimación) **a todo el mundo**.
> **Punto de partida (dado por la persona dueña):** español e inglés ya están bastante avanzados; hay **otros 11 idiomas presentes en el sitio pero sin avanzar**. Meta: llegar, por oleadas, a los 100 idiomas más hablados.
> **Qué NO se sabe todavía** (se resuelve en la Fase 0 con acceso al sitio real): plataforma y hosting, estructura de URLs, cuáles son los 11 idiomas, estado de indexación, analítica, pasarela de pago, cómo se entregan los archivos.
> Material de apoyo: `01` (investigación), `02` (idiomas/oleadas), `03` (terminología), `04` (checklist técnico con criterios de aceptación), `05` (AEO), `data/` y `plantillas/`.

## 0. Reglas de trabajo (para quien ejecute, humano o Claude Code)

1. **Auditar antes de cambiar.** Nada se modifica hasta tener `AUDITORIA-INICIAL.md` y haber acordado el plan ajustado con la persona dueña.
2. **No romper lo que funciona ni lo que vende.** Ramas por tarea, commits claros, despliegue a un entorno de prueba primero, y plan de reversa. Registrar cada despliegue en `CHANGELOG-SEO.md` (fecha, qué, por qué).
3. **Pedir confirmación antes de:** cambiar DNS o dominio, tocar pasarelas de pago/impuestos/facturación, borrar o redirigir páginas con tráfico, publicar textos legales, contratar o pagar servicios, enviar datos a terceros.
4. **No inventar:** ni datos de mercado, ni reseñas, ni cifras, ni términos en idiomas que no se dominan (usar `03` y marcarlos como pendientes de revisión nativa).
5. **Calidad antes que cantidad:** ninguna página traducida sin revisión del nivel correspondiente entra al índice (`noindex` hasta aprobar).
6. **Una variable a la vez** en cada oleada, para poder atribuir efectos y detectar caídas ligadas a updates de Google.
7. **No es asesoramiento legal ni fiscal:** pagos, impuestos y textos legales los valida un contador y un abogado.

## 1. Diagnóstico de partida (hipótesis a confirmar en la Fase 0)

| Tema | Lo que sabemos | Lo que hay que averiguar |
|---|---|---|
| Idiomas | ES y EN avanzados; 11 más "sin avanzar" | Cuáles son, qué % está traducido, cómo (humano/máquina), qué está indexable, si hay tráfico |
| Riesgo de calidad | Páginas traducidas sin revisar e indexables pueden contar como contenido a escala de bajo valor | Si hoy esos 11 idiomas están indexados y con qué calidad |
| Marca | "Moldey" puede leerse "moldy" (mohoso) en inglés `[OPINIÓN]` | Si hay búsquedas de marca y qué devuelven los buscadores/IA |
| Producto | Formatos PDF (A4/Letter/A0/proyector), editables/CAD, sublimación | Si la ficha declara todo lo que los compradores exigen (`T5`) |
| Ventas globales | Se vende a todo el mundo | Cómo cobra, qué impuestos gestiona y si hay MoR (`01` §8) |
| Descargas | Archivos de pago | Si hay URLs adivinables/públicas, caducidad, marca de agua |

## 2. Plan por fases

### Fase 0 — Auditoría (semanas 1–2) · solo lectura

Ejecutar `04` bloque A (A1–A8). Entregables:
- `AUDITORIA-INICIAL.md` (stack, flujo de compra/descarga, rendimiento, indexación, hallazgos por gravedad).
- **Inventario de los 13 idiomas** (los 2 avanzados + los 11) con la tabla `idioma | URL | cobertura % | método | indexable | hreflang | revisado por nativo | impresiones/clics 90 días`.
- `PLAN-AJUSTADO.md`: este plan corregido con lo que se encontró.
- **Reunión de decisiones** con la persona dueña (§7).

**Hecho cuando:** todas las tablas están completas, los riesgos priorizados y la persona dueña aprobó el plan ajustado.

### Fase 1 — Fundamentos y "quick wins" (semanas 2–6)

Ejecutar `04` bloques B, D1–D2, F y la parte de `E5`. Prioridades:
1. HTML renderizado en servidor/estático; canónicos autorreferentes; robots.txt separado por función (`plantillas/robots.txt`); revisar bloqueos de WAF/CDN a bots legítimos (`04` A5).
2. Search Console (dominio + prefijo por idioma), Bing Webmaster Tools, IndexNow; GA4 con `content_language` y canal "IA"; logs de bots.
3. Protección de descargas (URLs firmadas, marca de agua, `X-Robots-Tag`).
4. `Organization` y `Product`/`Offer` correctos en ES/EN; ficha-modelo (`plantillas/ESTRUCTURA-FICHA-PRODUCTO.md`) en los 20–50 productos más vendidos.
5. **Triage inmediato de los 11 idiomas** (§3): detener el daño potencial (`noindex` en lo no revisado) sin borrar nada.

**Hecho cuando:** `curl` con UA de GPTBot muestra contenido completo; sitemaps y robots publicados; mediciones activas; ningún idioma sin revisar es indexable; descargas protegidas.

### Fase 2 — Arquitectura multilingüe y contenido núcleo (semanas 5–12)

Ejecutar `04` bloques C y E, y H1.
1. Estructura `/es/`, `/pt-br/`… con raíz en inglés + `x-default` (adaptar a la estructura existente si ya funciona; migrar solo con redirecciones 301 planificadas y sin perder tráfico).
2. Estado de publicación por página e idioma (`borrador → traducido_mt → revisado_nativo → publicado`) y sitemaps/hreflang **solo de lo publicado** (`scripts/generar_sitemaps_hreflang.py`, `scripts/validar_hreflang.py` en CI).
3. Selector `/languages/` rastreable; banner no bloqueante; sin redirecciones automáticas por IP.
4. **Contenido evergreen de ES/EN** (respuesta primero): imprimir y armar un PDF, formatos de papel, cuadrado de prueba, tallas, margen de costura, DXF/AAMA/ASTM, preparar plantilla de sublimación, licencias (`T5` §8.4). Es también el contenido que se localizará en las oleadas.
5. **Glosario maestro** (`plantillas/glosario-base.csv` + `data/terminologia-100-idiomas.csv`) y **tabla de tallas por país**.
6. Páginas legales ES/EN (borrador para revisión de abogado) y página de marca/autor.

**Hecho cuando:** el pipeline de CI valida hreflang, canónicos, estados y JSON-LD; ES y EN cumplen el checklist de ficha y guías; glosario inicial aprobado.

### Fase 3 — Oleada 1 (meses 3–6): pt-BR, de, id, fr (y ru solo si se decide)

Para cada idioma, "kit de idioma" completo (`02` §7):
1. Investigación de palabras clave **nativa** (no traducida): semillas de `03` + Search Console/Keyword Planner/Trends/autosuggest local; lista de 20–30 consultas objetivo por idioma.
2. Traducción automática con glosario → **post-edición por hablante nativo** → muestreo de calidad → publicación (nivel A: home, categorías, top-50 productos, tallas, políticas; nivel B: resto del catálogo con muestreo; nivel C: guías con revisión completa).
3. Localización de ficha: unidades, papel (A4/Letter), tallas locales (revisadas), moneda, impuestos vía MoR, métodos de pago heredados del MoR (Pix si `pt-br` rinde).
4. Canales: Pinterest (EN, ES-MX, PT-BR, DE primero), YouTube con títulos/descripciones/subtítulos por idioma, comunidades locales.
5. Medición y puerta de salida (`02` §5).

**Hecho cuando:** se cumplen las 5 condiciones de la puerta de salida de la oleada 1.

### Fase 4 — Oleada 2 (meses 6–12): tr, hi, ar, vi, it, pl, nl, ja, fil

Igual que la fase 3, con salvedades: RTL en árabe; en India se busca "cutting" más que "pattern" y el PDF casi solo aparece en inglés (`03`); japonés con confianza alta (型紙) y canales BOOTH/note; resolver pagos locales antes de empujar tráfico (UPI, etc.).

### Fase 5 — Oleadas 3–5 y variedades (meses 12–24+)

Solo si la oleada anterior pasó su puerta. Oleada 3 (24 idiomas), oleada 4 (22), oleada 5 como **hub mínimo** (23 idiomas) y variedades dentro de su idioma padre. Corea (Naver Search Advisor) y China (ICP/entidad local) solo con evidencia de demanda y socio local. Revisión trimestral expandir/mantener/recortar.

### Continuo (cada mes)

- Protocolo de auditoría de IA (`05` §5) y hoja de seguimiento; informe de salud por oleada (URL enviadas vs indexadas, impresiones, clics, conversión, costo).
- Revisión de logs de bots y de errores de hreflang; revisar cambios de Google/Bing/IA que afecten el plan.
- Pedir reseñas reales; publicar un contenido evergreen nuevo por idioma activo.

## 3. Triage de los 11 idiomas ya presentes (decisión caso por caso)

Para cada idioma del inventario, aplicar esta regla usando `data/oleadas.csv`:

| Situación | Decisión | Acción concreta |
|---|---|---|
| Está en **oleada 1–2** (pt, de, id, fr, ru, tr, hi, ar, vi, it, pl, nl, ja, fil) | **Avanzar** | Mantener `noindex` hasta la revisión nativa del nivel A; completar traducción núcleo con post-edición; se incluye en su oleada |
| Está en **oleada 3–4** | **Congelar** | `noindex, follow`, fuera del sitemap y del clúster hreflang; seguir accesible a usuarios; sin invertir hasta su oleada |
| Está en **oleada 5 o es una variedad** (hausa, yoruba, zulú, árabe egipcio, bhojpurí…) | **Reducir** | Convertir en hub mínimo o unificar con su idioma padre (con 301 solo si no hay tráfico ni enlaces; confirmarlo antes) |
| Tiene **tráfico o enlaces reales** y calidad aceptable | **Conservar** | No tocar; priorizar su revisión nativa; documentar |
| Tiene **tráfico** pero calidad mala | **Reparar primero** | Revisión nativa urgente de las páginas con tráfico; no redirigir ni borrar a ciegas |

Reglas: **nunca borrar** páginas; **nunca bloquear por robots.txt** lo que se quiere sacar del índice (usar `noindex` por página para que Google lo vea); no generar 404 masivos; guardar el estado anterior para poder revertir.

## 4. Productos y ficha: qué debe tener cada molde (síntesis de `T5`)

Arriba de la ficha, en una caja: formatos y hojas por talla (A4/Carta/A0/proyector), capas, **margen de costura incluido o no (cuánto)**, cuadrado de prueba (medida), tallas y sistema (cm y pulgadas) con equivalencias locales, tela, dificultad, idiomas de las instrucciones, **licencia** (personal / venta pequeña / fabricación), "descarga inmediata, sin bloqueo geográfico". Moldes editables: convención (AAMA/ASTM D6673), unidades, versión DXF y **software probado** (Optitex, Gerber/AccuMark, Clo3D, Lectra): no declarar compatibilidad sin probar. Sublimación: dieline vectorial, 300 dpi, sangrado, zona segura, modo de color (consultar el RIP del taller), formatos entregados. Patrón observado en fichas reales (`research/raw/terminologia/verif-A1.md`): título = *molde + prenda + nombre + PDF + formatos (A4/A3/A0/US Letter) + atributos (capas por talla, videoproyección)*, rango de tallas explícito con equivalencias, instrucciones/tutorial incluidos, "uso personal, sin reventa", packs y un freebie.
**Nunca titular con "pattern" o "molde" a secas**; siempre "molde de costura / sewing pattern + prenda". En sublimación, "plantilla/dieline", no "sublimation pattern" sola.

## 5. Pagos, impuestos, legal y entrega (con contador y abogado)

- **Decisión de la persona dueña, no del ejecutor:** elegir un Merchant of Record (candidatos con Argentina plausible: Polar, Creem, Lemon Squeezy, Gumroad, Paddle sin confirmar; verificar en la página oficial: `01` §8 y `V2-G3`). Antes del primer pago a un MoR, hablar con el contador (monotributo/exportación de servicios, facturación a un MoR extranjero, régimen cambiario).
- Diseñar **packs/bundles y precio mínimo**: una comisión "5 % + US$ 0,50" cuesta ~13 % en un molde de US$ 6.
- **No vender ni promocionar** a Rusia ni a países sancionados.
- Checkout con tarjetas, Apple/Google Pay y PayPal; métodos locales según lo que ofrezca el MoR (Pix, UPI…), no integrar uno por uno.
- Páginas legales (términos, privacidad, reembolsos, licencia anti-reventa) revisadas por abogado; derecho de desistimiento en contenido digital (UE/UK); CMP de cookies para UE/UK/BR; accesibilidad (EAA/WCAG 2.2).
- **Entrega:** inmediata, enlaces firmados con caducidad, límite de descargas, marca de agua con ID del comprador, hoja de prueba, instrucciones en 3–5 idiomas.
- **Google Shopping:** zona de riesgo para digitales (los eBooks se rechazan y pueden suspender la cuenta): no presentarlos como libros; probar solo listados gratuitos con pocos productos y sin vincular una cuenta de Ads valiosa.

## 6. Medición y metas

| Frecuencia | Qué mirar | Fuente |
|---|---|---|
| Semanal | Errores de rastreo/indexación, URLs enviadas vs indexadas, caídas anómalas | Search Console, Bing WMT, logs |
| Mensual | Impresiones/clics/CTR por idioma y país; conversión y costo por idioma; tráfico "IA"; auditoría de prompts (mention/citation rate, exactitud) | GSC, GA4, `05` §5 |
| Trimestral | Puerta de oleada; expandir/mantener/recortar por idioma; revisión de gasto en traducción | Tablero (`04` F5) |

**Metas orientativas (a calibrar con la oleada 1; no hay datos fiables de plazos para este nicho):**
- A 90 días: línea base completa, 13 idiomas auditados y ordenados, ES/EN con fichas y guías completas, 0 páginas sin revisar indexables, medición funcionando.
- A 6 meses: oleada 1 publicada (≥ 80 % de las URL enviadas indexadas en ≥ 70 % de los idiomas) y primeras consultas en Search Console.
- A 12 meses: oleada 2 publicada; al menos un idioma nuevo con ingresos ≥ su costo.

## 7. Decisiones y datos que debe aportar la persona dueña

1. **Acceso** al repositorio/CMS de moldey.com, hosting/CDN, Search Console, GA4 y pasarela (solo lectura al principio).
2. **Cuáles son los 11 idiomas** actuales y quién los tradujo.
3. **Revisores nativos:** presupuesto y disponibilidad (por idioma de la oleada 1 primero: pt-BR, de, id, fr).
4. **Merchant of Record / pasarela:** decisión con el contador.
5. **Marca:** si "Moldey" está registrada (INPI/EUIPO/USPTO) y si hay perfiles propios (YouTube, Pinterest, Instagram) con el mismo nombre.
6. **Catálogo:** cuántos moldes hay, cuáles venden más, qué formatos entrega cada uno, qué compatibilidad CAD se probó.
7. **Tiempo semanal** disponible para aprobar contenido y revisar resultados.
8. **Apetito de riesgo** sobre entrenamiento de IA (permitir o bloquear GPTBot/ClaudeBot/Google-Extended en páginas públicas).

## 8. Riesgos principales y mitigación

| Riesgo | Mitigación |
|---|---|
| Traducción masiva sin revisión penalizada por Google | Gate de calidad, `noindex` hasta aprobar, oleadas pequeñas, muestreo de calidad |
| WAF/CDN bloqueando bots de búsqueda/IA | Revisar reglas y logs desde la Fase 0 |
| Descargas públicas o piratería | URLs firmadas, marca de agua con ID, licencia clara, vigilancia/DMCA, registro de marca |
| Obligaciones de IVA/impuestos en el exterior | MoR + contador antes de empujar tráfico |
| Palabras trampa ("pattern", "molde", "moldey/moldy") | Titular con prenda; contexto de marca; revisión de términos en `03` |
| Cambios de Google/IA durante una oleada | No lanzar en pleno rollout; una variable a la vez; `CHANGELOG-SEO.md` |
| Mercados sin forma de cobrar (Irán, Rusia, China sin entidad) | Fuera del alcance de las primeras oleadas |
| Dependencia de datos de baja confianza | Marcar confianza en `03`; revisión nativa; reemplazar hipótesis con Search Console/Keyword Planner |

## 9. Primeras 10 acciones (si solo hay una semana)

1. Dar acceso de solo lectura al sitio y a Search Console/GA4 y listar los 11 idiomas.
2. Ejecutar la Fase 0 (A1–A8) y generar `AUDITORIA-INICIAL.md`.
3. Verificar que Googlebot, Bingbot, OAI-SearchBot, PerplexityBot y Claude-SearchBot no reciben 403.
4. Poner `noindex, follow` a las páginas de los idiomas no revisados (sin tocar robots.txt ni borrar nada).
5. Publicar robots.txt por función y sitemaps solo con lo aprobado.
6. Activar IndexNow, Bing Webmaster y el canal "IA" en GA4.
7. Cerrar el acceso público a descargas y activar URLs firmadas.
8. Reescribir 10 fichas top (ES/EN) con la caja de especificaciones.
9. Publicar la guía "cómo imprimir y armar un molde PDF" en ES/EN.
10. Elegir MoR con el contador y definir el presupuesto de revisión nativa para la oleada 1.
