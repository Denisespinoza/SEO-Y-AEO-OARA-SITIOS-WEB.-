# Notas grupo A9 (zulú, malgache, shona, chichewa/nyanja, kinyarwanda, lingala, akan/twi, fula, quechua, xhosa, tigriña)

## 0. Advertencia de honestidad (leer primero)

- **El presupuesto de WebSearch se agotó tras la primera consulta** (límite de 200 búsquedas por turno, compartido entre todos los agentes). Solo se ejecutó **1 búsqueda real** (zulú/shweshwe); las otras 5 consultas de la tanda inicial devolvieron "presupuesto agotado" y no se reintentó por otras vías.
- Consecuencia: **las 11 filas tienen `confianza=baja`**. Ninguna cumple "alta" (≥2 usos reales) ni "media" para el término de molde. Los términos nativos de `part-A9.csv` salen de conocimiento léxico general (cognados bantúes, léxico escolar, etc.), **no de uso comercial comprobado**. Cada fila lo declara al comienzo de `ambiguedades_y_trampas` ("SIN VERIFICAR EN WEB...").
- Lo único con respaldo en resultados reales: que **shweshwe/isishweshwe** es el término clave de prenda/tela en Sudáfrica y que el comercio y los medios lo tratan **en inglés** (Dictionary of South African English, IOL, Business Day, un listado de Etsy). Esas URLs están en las filas `zu` y `xh`. Eso respalda la tela y el contexto, **no** un término nativo de "molde".
- `evidencia_urls` queda **vacío** en las otras 9 filas a propósito: no se inventaron URLs.

## 1. Hallazgo central: la búsqueda comercial NO se hace en estos idiomas

Para ninguno de los 11 idiomas se verificó (ni hay motivo para esperar) un término nativo consolidado de "molde/patrón de costura" usado en tiendas. Lo probable, y lo coherente con la asignación (`mapeo_web`), es:

| Idioma | Dónde se busca de verdad (hipótesis) | Idioma de la consulta comercial |
|---|---|---|
| Zulú, xhosa (Sudáfrica) | Google/YouTube/Facebook/TikTok/Takealot/Etsy | **inglés** ("shweshwe dress pattern", "sewing patterns South Africa") |
| Shona (Zimbabue), chichewa/nyanja (Malaui/Zambia) | WhatsApp, Facebook, TikTok | **inglés** |
| Akan/twi (Ghana) | Instagram, Facebook, TikTok, Jiji/Tonaton | **inglés** ("style", "Ghana styles", "kaba and slit") |
| Kinyarwanda (Ruanda) | Instagram, WhatsApp, YouTube | **inglés + francés** (Ruanda cambió la enseñanza al inglés en 2008) |
| Lingala (RDC, Congo-Brazzaville) | Facebook, WhatsApp, TikTok | **francés** ("patron", "modèle", "couture", "pagne") |
| Malgache (Madagascar) | Facebook (casi sinónimo de internet) | **francés**, malgache en redes |
| Fula (Sahel/Camerún/Nigeria) | WhatsApp, Facebook | **francés**, **inglés** o **hausa** según país |
| Quechua (Perú/Bolivia/Ecuador) | Google, YouTube, Facebook, Mercado Libre | **español** ("moldes de pollera", "corte y confección") |
| Tigriña (Eritrea/Tigray/diáspora) | YouTube, Facebook, Telegram, Etsy | **inglés**, amárico en Etiopía |

**Recomendación**: no invertir en páginas de producto con términos nativos para estos idiomas. Servir con **en / fr / es / pt** más etiquetas culturales nativas (nombres de prendas) como complemento, no como palabra clave principal.

## 2. Prendas tradicionales de alto potencial (los términos de nicho que SÍ se buscan)

Estos nombres de prenda son los candidatos reales para captar tráfico, casi todos en inglés, francés o español. Son fiables como vocabulario general, pero **no se verificó volumen ni uso en tiendas de moldes** (salvo shweshwe parcialmente).

| Prenda / tela | Región | Cómo se busca | Trampa |
|---|---|---|---|
| **shweshwe / isishweshwe / seshweshwe** | Sudáfrica, Lesoto, Botsuana | en inglés: "shweshwe dress pattern", "shweshwe dresses"; ortografía múltiple (origen sesotho según DSAE) | "pattern" = **estampado**, no molde; shweshwe es tela, no prenda |
| **kitenge / vitenge / chitenge / chitenje / igitenge** | África oriental, Ruanda, Zambia, Malaui | inglés "kitenge dress patterns/styles"; Zambia "chitenge", Malaui "chitenje", Ruanda "igitenge/ibitenge" | misma palabra, ortografía distinta por país; "styles" = modelos de vestido, no moldes |
| **ankara / African print / wax** | Nigeria, Ghana, diáspora | inglés "ankara styles", "ankara dress patterns"; Hausa "atamfa" (sin verificar) | "ankara" es tela estampada; la gente busca "styles" (fotos), no patrones técnicos |
| **kente / nwentoma** | Ghana (akan) | inglés "kente styles/dress"; akan "nwentoma" (sin verificar) | "kente print" industrial vs tejido auténtico |
| **kaba and slit; dansinkran; batakari/fugu** | Ghana | inglés | "style" es la palabra de búsqueda para el modelo |
| **pagne / wax / liputa / boubou / bazin** | África francófona (RDC, Congo, Sahel) | francés "patron pagne", "modèle de couture africaine", "patron boubou"; lingala "liputa" | "pagne" es tela envolvente (falsa amistad con el sentido general del francés); "patron" = jefe |
| **boubou / mbubba** | Sahel, fula | francés "boubou", "grand boubou"; fula "mbubba" (sin verificar) | prenda unisex en muchos contextos |
| **lamba / lamba hoany / akanjo / salovana** | Madagascar | francés "lamba", "tenue malgache"; malgache "akanjo" (ropa, sin verificar) | "lamba" es tela/chal; "lamba hoany" lleva proverbios estampados |
| **pollera, chullo (ch'ullu), aguayo (awayu), lliklla, unku, poncho (punchu), anaco (kichwa)** | Perú, Bolivia, Ecuador | español "moldes de pollera", "molde de pollera cusqueña/paceña", "patrón de chullo", "traje típico andino" | "pollera" varía por país (Argentina/Panamá = otra prenda); "molde" = recipiente de cocina; chullo es tejido, no se cose |
| **habesha kemis / zuria / netela** | Eritrea, Etiopía, diáspora | inglés "habesha dress pattern", "Eritrean traditional dress"; escritura etiópica: ሀበሻ ቀሚስ, ነጠላ | términos distintos Eritrea vs Etiopía; teclado Ge'ez poco usado |

## 3. Diferencias entre variedades y riesgos de traducción

- **Quechua**: familia con variedades poco intercomprensibles (Cusco-Collao, Ayacucho-Chanka, boliviano, kichwa de Ecuador) y ortografías distintas. `p'acha` (ropa, Cusco-Collao) lleva apóstrofe eyectivo; sin él, `pacha` = tierra/tiempo, y un buscador que ignora apóstrofes mezclará resultados. Las formas de "coser" `sirkay` / `sipiy` vienen del encargo y **no pude confirmarlas**; la ortografía cambia por variedad. La búsqueda real es **en español** ("moldes de pollera", "corte y confección").
- **Fula**: macrolengua (`ff`) con dialectos (pulaar, pular, fulfulde); la asignación usa `fub` (Adamawa: Camerún/Nigeria). No se verificó ningún término fula para coser, molde ni sublimación; en la práctica domina el francés, el inglés o el hausa. Los términos hausa de las filas (`dinki`, `tela`, `babbar riga`) son referencia cruzada **sin verificar**.
- **Akan**: familia (twi asante/akuapem, fante). `pam` (coser) y `ɔpamfoɔ` están **sin verificar**. En Ghana el término de búsqueda es "style" en inglés.
- **Chichewa/nyanja**: Malaui (chichewa) y Zambia (nyanja, con "Town Nyanja" mezclado con inglés/bemba) son dos mercados distintos con dos monedas.
- **Kinyarwanda/kirundi**: muy cercanos entre sí; no se cubrió kirundi (fuera de la asignación).
- **Lingala**: Kinshasa mezcla lingala y francés; `kotonga` (coser) **sin verificar**, y también significa "construir".
- **Tigriña vs amárico**: misma escritura, términos distintos (ልብሲ vs ልብስ). En Etiopía la ruta de búsqueda es amárico/inglés; en Eritrea el acceso a internet es muy limitado y la audiencia en línea está en la diáspora.
- **Falsas amistades**: "pattern" = estampado (inglés); "molde" = recipiente de cocina (es); "pagne" = tela envolvente en África; "patron" = jefe (fr); "pollera" cambia según el país.

## 4. Canales y conectividad (para `nota_localizacion`)

- **WhatsApp y Facebook** son los canales dominantes en casi todos estos mercados; **TikTok** crece para tutoriales; **YouTube** para costura.
- **Marketplaces** (varía por país, no verificado país por país): Jiji (p. ej. Ghana, Nigeria, Etiopía), Jumia, Kilimall, Takealot y Gumtree (Sudáfrica), Shein/Temu, Mercado Libre (Perú, Ecuador), OLX (Bolivia).
- **Pagos**: mobile money (MTN MoMo, Airtel Money, Orange Money, M-Pesa, EcoCash, MVola, Telecel Cash, TNM Mpamba, Yape/Plin en Perú, telebirr en Etiopía). Mucho comprador sin tarjeta internacional: pagos por tarjeta internacional serán una barrera.
- **Datos móviles caros y conectividad baja** (Malaui, RDC, Madagascar fuera de la capital, Eritrea muy baja): los PDF pesados (A0, DXF) son un obstáculo; ofrecer archivos ligeros y descarga por enlace compartible por WhatsApp.
- **Papel y medidas**: A4 y cm en casi todos; en Bolivia es probable el tamaño carta/oficio (sin verificar). En Ghana, Zimbabue y Malaui los sastres pueden usar pulgadas (sin verificar). Como gran parte del mercado hace ropa **a medida con sastre**, el molde digital tiene más encaje como herramienta del sastre/modista que como producto de costura doméstica.

## 5. Oportunidades de nicho

1. **Shweshwe / Xhosa-Zulu traditional attire** (Sudáfrica): es el único nicho con evidencia real parcial; búsqueda en inglés.
2. **Kitenge/chitenge/ankara para sastres** (África oriental/austral/occidental) en inglés.
3. **Polleras y trajes andinos** en español para Perú/Bolivia/Ecuador (confección artesanal; escasa oferta digital probable, sin comprobar).
4. **Boubou y pagne** en francés (África francófona).
5. **Diáspora** (eritrea, etíope, ghanesa, congoleña, ruandesa, malgache): compra en inglés/francés en Etsy y redes con prendas tradicionales.

## 6. Lo que NO se pudo verificar

- Todo término nativo de la tabla del CSV (molde, PDF, imprimir, sublimación, coser, patronaje) en los 11 idiomas. Los marcados "sin verificar" o con `[sin término nativo verificado]` son lo mínimo honesto.
- Volúmenes de búsqueda y uso real en tiendas locales/Etsy/Jiji/Mercado Libre.
- Presencia exacta de Jumia/Jiji/Kilimall/Mercado Libre por país; tamaños de papel y unidades por país.
- Las formas quechuas `sirkay`/`sipiy`; el término tigriña para coser/molde; `iphethini`, `pateni`, `modely`, `chitsanzo cha zovala` como términos de molde.

## 7. Plan de verificación sugerido (cuando haya presupuesto de búsqueda)

Consultas en modo `standard`, mirando solo tiendas/blogs/YouTube de costura locales:

1. `shweshwe dress pattern PDF` y `isishweshwe ukuthunga` (confirmar en tiendas SA).
2. `chitenge dress pattern PDF`, `kitenge sewing pattern` y `igitenge ubudozi`.
3. `patron couture pagne PDF`, `patron boubou PDF`, `modèle couture africaine patron`.
4. `moldes de pollera cusqueña`, `moldes de pollera paceña`, `p'acha sirkay`, `chullo patrón`.
5. `habesha kemis sewing pattern`, `Eritrean zuria pattern`, `ንድፊ ክዳን` y `የልብስ ንድፍ`.
6. `manjaitra akanjo`, `mpanjaitra`, `lamba hoany`, `salovana`.
7. Akan: `pam ntoma`, `kente styles`, `kaba and slit pattern`.
8. Fula: `mbubba`, `dinki boubou`, `Fulfulde sewing`.
