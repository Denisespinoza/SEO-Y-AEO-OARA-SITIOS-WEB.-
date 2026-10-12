# 02 · Estrategia para llegar a los 100 idiomas más hablados (por oleadas)

> Datos de apoyo: `data/idiomas-master.csv` (113 idiomas: 100 + 13 extras), `data/oleadas.csv` (oleada y "atendido con"), `data/terminologia-100-idiomas.csv` (cómo se dice y busca "molde de costura").
> Reglas de método y calidad: `01` §4–5. Plan específico para moldey.com: `06`.

## 1. Primero, qué significa realmente "100 idiomas"

1. **La lista es de trabajo, no una cita oficial.** Se armó con el ranking de hablantes totales de Ethnologue (ediciones 2024–2026) *reconstruido de varias fuentes*: el orden exacto cambia entre ediciones y desde la posición ~20 no se pudo confirmar en las fuentes accesibles. Lo que importa para el plan es **qué idiomas** y **en qué orden se atacan**, no el puesto exacto.
2. **Ranking de hablantes ≠ ranking de oportunidad comercial.** Hay idiomas con cientos de millones de hablantes que casi no se escriben en la web comercial (hausa, yoruba, igbo, oromo…), o que se compran en otro idioma (inglés, francés, español).
3. **Las 100 entradas no son 100 sitios.** De las 100: **72 son idiomas con presencia web propia** y **28 son variedades habladas** que se escriben/buscan con otro idioma (árabe egipcio→árabe estándar; bhojpurí/maithili/awadhi…→hindi; wu/jin/xiang/hakka→chino; javanés/sundanés→indonesio; cebuano→filipino; pidgin nigeriano→inglés; min nan→chino tradicional/cantonés escrito). Con los **13 extras** relevantes para moldería (catalán, danés, noruego, finés, eslovaco, esloveno, lituano, letón, estonio, georgiano, armenio, mongol, lao) resultan **85 destinos de contenido propio** (incluidos 23 "hub mínimo") y 28 variedades que **no tienen sitio propio**: reciben vocabulario local dentro del idioma "padre".
4. **No todo idioma merece sitio completo.** Para los de poca búsqueda: un *hub* de una página (ver §6).

## 2. Principios no negociables

1. **Medir antes de traducir** (Search Console por carpeta, Bing WMT, GA4 con `content_language`, canal "IA"). Sin línea base no se sabe qué oleada funcionó.
2. **Investigar palabras clave en cada idioma**, no traducirlas (`03`). "Molde" (Río de la Plata) ≠ "patrón" (España/México) ≠ "patronaje" ≠ "plantilla"; en India se busca "blouse cutting" más que "pattern".
3. **Calidad como puerta de publicación:** nada se indexa sin revisión nativa del nivel que le corresponde (`01` §5). Lo no aprobado: `noindex, follow`, fuera del sitemap y del clúster hreflang.
4. **Una URL por molde e idioma**; talla, formato y papel son selectores en la misma página (no URLs indexables por combinación).
5. **Despliegue escalonado y atribuible:** no lanzar una oleada durante un rollout de core/spam update de Google ni mezclar varios cambios a la vez.
6. **Pagos, impuestos y legal antes de empujar tráfico** a un mercado (`01` §8). Un idioma sin forma de cobrar no es un mercado.
7. **Honestidad cultural:** prendas tradicionales (sari blouse, kurti, hanbok, kimono, abaya, thobe, kaftán, dashiki, áo dài, cheongsam, dirndl…) con revisión de nativos; nombrar con el término propio.

## 3. Modelo de priorización (hipótesis a reemplazar con datos)

`Puntaje (0–100) = 20·Mercado + 25·Demanda del nicho + 15·Brecha competitiva + 15·Poder adquisitivo y pagos + 15·Viabilidad de traducción + 10·Canales` (cada factor 1–5, normalizado a su peso).

| Factor | Qué mide | Dato a usar |
|---|---|---|
| Mercado (20 %) | Tamaño digital/e-commerce del idioma | Usuarios de internet, compras online |
| Demanda del nicho (25 %) | Búsquedas de "molde/patrón de costura" per cápita y tendencia | Trends, Wordstat, Naver, Keyword Planner, Semrush/Ahrefs |
| Brecha competitiva (15 %) | 5 = pocas tiendas locales fuertes de patrones PDF | Top 10 manual |
| Poder adquisitivo y pagos (15 %) | ¿Se puede cobrar? tarjeta/PayPal/Pix/UPI/Mercado Pago | MoR/pasarela; sanciones |
| Viabilidad de traducción (15 %) | Nivel A/B/C, disponibilidad de revisores, complejidad de escritura | `03`, bolsa de traductores |
| Canales (10 %) | Comunidad activa; Pinterest/YouTube/Facebook/WhatsApp | Observación local |

**Los puntajes del informe `T6` son hipótesis del autor del informe, no mediciones.** Se usan solo para el orden inicial. Reemplazarlos con Search Console (consultas sin página en ese idioma) y herramientas de keywords antes de decidir cada oleada. Los cortes de oleada (≥75 / 65–74 / 55–64 / <55) se fijaron antes de mirar los números.

## 4. Oleadas

| Oleada | Idiomas (código web) | Cuándo | Qué hacer |
|---|---|---|---|
| **0 · Base** | Inglés `en` (raíz y `x-default`), español `es` (con variantes `es-AR`/`es-MX`/`es-ES` solo si el contenido difiere) | Ya | Consolidar hreflang, medición, glosario maestro, ficha-modelo y gate de calidad |
| **1 · Rentables** | Portugués de Brasil `pt-br`, alemán `de`, indonesio `id`, francés `fr`, ruso `ru`* | Meses 0–4 | Traducción automática nivel A + post-edición; keyword research nativa; pagos locales (Pix si `pt-br` rinde) |
| **2 · Grandes y viables** | Turco `tr`, hindi `hi`, árabe `ar`, vietnamita `vi`, italiano `it`, polaco `pl`, neerlandés `nl`, japonés `ja`, filipino `fil` | Meses 4–10 | Revisión nativa completa de páginas núcleo; RTL (árabe); UPI/Mercado de pagos a resolver antes de India |
| **3 · Media prioridad** | Ucraniano, tailandés, malayo, bengalí, urdu, coreano, persa, rumano, checo, húngaro, griego, sueco, danés, noruego `nb`, finés, hebreo, tamil, telugu, maratí, guyaratí, canarés, malayalam, chino simplificado `zh-Hans`**, chino tradicional/cantonés `yue` (`zh-HK`/`zh-TW`) | Meses 10–18 | Post-edición completa y revisor nativo; Naver Search Advisor para coreano; escrituras índicas con WOFF2 subset |
| **4 · Largo plazo** | Nepalí, cingalés, jemer, birmano (solo Unicode), lao, kazajo, uzbeko, azerí, serbio, croata, búlgaro, eslovaco, esloveno, lituano, letón, estonio, georgiano, armenio, mongol, suajili, afrikáans, catalán | Meses 18–24 | Solo con revisión humana completa y datos de las oleadas previas |
| **5 · Hub mínimo** | Hausa, yoruba, igbo, oromo, zulú, xhosa, shona, chichewa, kinyarwanda, lingala, akan, fula, somalí, malgache, tigriña, amárico, quechua, criollo haitiano, sindhi, pastún, kurdo, asamés, odia | Cuando el presupuesto lo permita | 1 página + glosario; ampliar solo con tráfico real (ver §6) |
| **Variedades** (sin sitio propio) | Árabe: egipcio, levantino, sudanés, marroquí, mesopotámico, najdí, argelino, tunecino, del Golfo → `ar`. Hindi: bhojpurí, maithili, awadhi, magahi, chhattisgarhi, rajastaní, haryanvi → `hi`. Urdu: panyabí occidental, saraiki, decanés → `ur`. Chino: wu, jin, xiang, hakka → `zh-Hans`; min nan → `yue`/chino tradicional. Javanés, sundanés → `id`. Cebuano → `fil`. Pidgin nigeriano → `en` | Con su "padre" | Vocabulario local dentro del idioma padre (p. ej. en `ar`, variantes de "abaya/jalabiya/kaftán"; en Magreb, versión `fr`) |

\* **Rusia:** no cobrar ni empujar tráfico pagado (sanciones/pagos); el idioma ruso sirve también a Kazajistán, Asia Central y diáspora. Decidir con asesoría.
\*\* **China continental:** exige ICP/entidad local para alojar y pagos propios (Alipay/WeChat); sin eso, tráfico solo por Google/Bing (acceso limitado). Aplazar Baidu/Taobao hasta que haya evidencia de demanda y socio local.

**Observaciones de mercado por oleada** (de `T4`/`T6`, a validar): Pinterest y YouTube son los canales de mayor relación alcance/relevancia; WhatsApp/Meta AI pesan en India, Brasil, Indonesia y México; Naver domina Corea (≈64–68 %); Yandex domina Rusia (≈71 %).

## 5. Puerta de salida entre oleadas

Pasar de la oleada N a la N+1 solo cuando se cumplan **todas**:
1. ≥ 70 % de los idiomas de la oleada con ≥ 80 % de las URL enviadas indexadas y primeras consultas en Search Console.
2. Tasa de errores del control de calidad lingüístico (LQA) bajo el umbral en las dos últimas entregas.
3. Costo real por idioma ≤ 120 % del presupuestado y revisores confirmados para la siguiente.
4. Al menos un idioma de la oleada con ingreso ≥ su costo, o tendencia clara de recuperación.
5. Sin update de Google (core/spam) en rollout en las 2 semanas previas y sin caída anómala atribuible a calidad.

**Revisión trimestral** idioma por idioma: expandir / mantener / recortar (a `noindex` o hub) según impresiones, clics, conversión y costo de mantenimiento.

## 6. El "hub mínimo" para idiomas de poca búsqueda

- **Qué es:** una página (no un sitio) en el idioma: H1 y descripción redactados por nativo, glosario básico de costura (10–20 términos), enlaces a las versiones inglesa/española del catálogo, aviso de formatos y cómo imprimir, contacto.
- **Cuándo no publicar:** si no hay revisor nativo disponible. En nivel C (nepalí, birmano, amárico, tigriña, oromo, jemer) **no publicar con traducción automática sola**.
- **Indexación:** `noindex` hasta revisión; después indexable. Medir 90 días: si no hay impresiones, mantener como está (costo cero) y no invertir.

## 7. Qué necesita cada idioma antes de abrirse ("kit de idioma")

1. Glosario aprobado (términos de `03` + 200–500 de moldería/formatos/tallas, bloqueado en las herramientas de traducción).
2. Revisores nativos para su nivel (A/B/C) y plan de muestreo.
3. Reglas de escritura: `dir`, fuente (CJK: pila del sistema; índicas: subset), numerales, normalización, una escritura por URL.
4. Localización de la ficha: unidades (cm/in), papel (A4/Letter), tabla de tallas local, moneda, impuestos (vía MoR).
5. Políticas legales traducidas y revisadas (términos, privacidad, reembolsos, licencia).
6. Métodos de pago/entrega viables y sanciones verificadas.
7. Lista de 20–30 consultas objetivo (de `03`) para seguimiento de posiciones por país/idioma.
8. Canales: Pinterest (título/descr./nombre de archivo en el idioma), YouTube (títulos y subtítulos), comunidades locales.

## 8. Qué NO hacer (resumen)

- Traducir en masa el catálogo a 100 idiomas con MT sin edición y publicarlo indexable (patrón de "scaled content abuse").
- Traducir las palabras clave del inglés; clonar páginas cambiando solo el idioma.
- Crear URL indexables por prenda × talla × formato × idioma.
- Usar robots.txt para ocultar idiomas flojos (usar `noindex` por página).
- Lanzar una oleada en medio de un rollout de Google o junto con otros cambios.
- Prometer plazos de posicionamiento: no hay datos fiables para idiomas nuevos de este nicho; se calibran con la oleada 1.
