# Verificación A9 (2.ª pasada): zulú, xhosa, shona, chichewa, kinyarwanda, lingala, akan, fula, malgache, quechua, tigriña

**Búsquedas usadas: 8 de 8 (WebSearch, modo `standard`). Ninguna devolvió "budget used up".** Salida: `part-A9.v2.csv` (11 filas, 16 columnas, mismo orden de filas y columnas que `part-A9.csv`; validado con `csv`).

## Qué se buscó y qué salió

| # | Consulta | Resultado |
|---|---|---|
| 1 | `shweshwe dress sewing pattern PDF download` | Solo patrones genéricos (Etsy, tiendas británicas). **Ningún molde de shweshwe.** |
| 2 | `shweshwe dress patterns South Africa seamstress sewing patterns buy Takealot OR Etsy OR Spotlight` | Solo tela, prensa y un blog (2013) que cose shweshwe con el molde occidental Colette "Hazel Dress". **Sin listados de moldes; Takealot y Spotlight no aparecieron.** |
| 3 | `kitenge ankara African print dress sewing pattern PDF instant download` | Casi todo tela (Spoonflower, eBay, Anka marketplace). Un gig de Fiverr vende moldes PDF a medida ("Ankara PDF pattern"). |
| 4 | `patron de couture PDF boubou pagne wax modèle africain à télécharger` | Ningún patrón PDF de boubou/pagne. Wikipedia "Pagne" y un libro impreso, *Couture wax* (Mango, 2020, BnF). |
| 5 | `manjaitra akanjo modely couture Madagascar lamba hoany patron robe` | Lamba/lambahoany (Wikipedia, L'Express de Madagascar sep. 2026, Anka marketplace). **Ninguno de manjaitra/akanjo/modely.** |
| 6 | `moldes de pollera cusqueña paceña patrones corte y confección polleras comprar` | **Ningún molde de pollera andina.** Salieron la pollera panameña (TVN-2), polleras de Cuenca (El Universo) y un documento Scribd de patronaje. |
| 7 | `habesha kemis sewing pattern PDF Eritrean zuria traditional dress pattern ንድፊ ክዳን` | Resultados en inglés y un artículo de AFP en francés; **cero resultados en ge'ez**; gigs de Fiverr de moldes PDF. |
| 8 | `ubudozi kudoda imyenda igitenge umudozi Kigali tailor kitenge designs` | Solo páginas en inglés (The New Times, Heaven Rwanda, NatGeo). Ningún término kinyarwanda ni francés. |

## Qué quedó verificado (poco)

- [EVIDENCIA] **Shweshwe es tela y el mercado habla inglés** (Etsy, Brand South Africa, Business Day, DSAE, IOL). Se cose con moldes occidentales en inglés (blog de 2013). `zu` y `xh` suben a `media`, **solo con ese alcance**; sus términos zulúes/xhosas siguen en baja. Ancho de tela: 80 cm (blog) a 90 cm (Business Report, de la 1.ª pasada, no re-verificado); conviene que el molde dé metraje para tela estrecha [OPINIÓN].
- [EVIDENCIA] **"pattern" = estampado** se confirma en resultados reales (listado Etsy "geometric pattern fabric"; Spoonflower "African Ankara Pattern").
- [EVIDENCIA] **Trampa de "pollera" confirmada** (`qu`): la búsqueda en español devuelve Panamá y Ecuador, no moldes andinos. `qu` sube a `media` solo para los términos españoles "patrón/molde" (Scribd); los términos quechuas siguen en baja.
- [EVIDENCIA] **Existe oferta de moldes PDF africanos a medida en inglés (Fiverr)**, con A4/Letter/A0 y margen de costura. Es señal de competencia/servicio, no de volumen de búsqueda.
- [EVIDENCIA] Francés: *pagne* = corte de tela (Wikipedia); existe un libro impreso *Couture wax* (BnF), señal indirecta de demanda de patrons wax en papel.

## Qué cambió en el CSV

- `zu`/`xh`: `termino_molde_costura` pasa a inglés primero ("sewing pattern; dress pattern; PDF sewing pattern"); `iphethini` queda como préstamo conjetural no verificado. `confianza` baja a media (scoped). Ancho de shweshwe en `nota_localizacion` (zu).
- `mg`: añadida la grafía de una palabra `lambahoany` (se mantiene `lamba hoany`) y `lambamena` (tejido funerario, no prenda cotidiana).
- `qu`: `patrón / molde` pasa a primer término; `confianza` media (scoped); trampa de pollera confirmada.
- `ti`: Wikipedia señala que "Habesha kemis" es nomenclatura amhara, no inherentemente tigray ni eritrea; el kemis tradicional es tejido a mano, no cosido desde un molde, así que la demanda de moldes sería de piezas modernas/híbridas [OPINIÓN].
- En las 11 filas: se retiró "SIN VERIFICAR EN WEB", se escribió "VERIFICADO PARCIALMENTE: sí = ...; no = ..." y se antepuso la ADVERTENCIA de que el comercio busca en inglés/francés/español/portugués.
- `confianza` final: **3 media** (zu, xh, qu; con alcance limitado), **8 baja** (mg, sn, ny, rw, ln, ak, ff, ti). Ninguna alta.

## Qué sigue sin verificar

- **Todo término nativo** de molde, PDF, imprimir, sublimación, coser y patronaje en los 11 idiomas (iphethini, modely, pateni, chitsanzo cha zovala, kotonga, pam, sirkay/sipiy, ንድፊ, igitenge/ubudozi, mbubba, etc.). Ninguno apareció en los resultados.
- **Plataformas del punto 2:** Jumia, Jiji, Kilimall, Tonaton, Classifieds.co.zw, Mercado Libre, OLX, Yape/Plin, telebirr, Qefira y WhatsApp como canal de venta de moldes: **ninguno apareció en ningún resultado**; no se pudo medir. Solo se vio Anka marketplace (telas, fichas fr/en) y Fiverr.
- No se buscó: kente, nwentoma, kaba and slit (akan); mbubba/dinki (fula); shona y chichewa en su propia lengua; lingala directo; zulú/xhosa en su lengua (`isishweshwe ukuthunga`).
- Volumen de búsqueda de cualquier término: no medible con este instrumento.

## Salvedades de método

- WebSearch está sesgado a EE. UU.: la ausencia de resultados **no prueba** que no exista oferta local (Takealot, Jiji, Mercado Libre, grupos de Facebook/WhatsApp no se indexan bien).
- Varias consultas mezclaban idiomas (p. ej. la nº 8 incluía "tailor kitenge designs" en inglés; la nº 7 mezclaba ge'ez y latín). Eso sesga hacia resultados en inglés: es evidencia débil de "se busca en inglés", no una medición.
- Evidencia fechada: el blog de shweshwe es de 2013; el artículo de L'Express es de septiembre de 2026.

## Recomendación (sin cambio respecto de la 1.ª pasada) [OPINIÓN]

No invertir en páginas de producto con términos nativos para estos 11 idiomas. Servir con **en / fr / es / pt** y usar los nombres de prenda y tela (shweshwe, kitenge/chitenge, ankara, boubou, pagne, lambahoany, pollera, habesha kemis) como etiquetas culturales de apoyo, no como palabra clave principal. Para `qu`, cuidar la ambigüedad de "pollera" (Panamá/Ecuador).
