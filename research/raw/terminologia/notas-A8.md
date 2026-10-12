# Notas grupo A8 (sueco, danés, noruego, finés, georgiano, armenio, suajili, hausa, yoruba, igbo, amárico, oromo, somalí)

## Advertencia principal: nada de esto está verificado en la web

El presupuesto de WebSearch del turno (200 búsquedas, compartido entre todos los agentes) estaba agotado cuando empecé. Los 5 intentos que hice fueron rechazados y no ejecuté ninguna búsqueda con éxito. No usé curl, lectores ni proxies para esquivarlo.

Consecuencias:
- Los 13 idiomas llevan `confianza=baja` y `evidencia_urls` vacío. No inventé URLs.
- Todos los términos salen de conocimiento previo y de las pistas de la asignación. En cada fila, `ambiguedades_y_trampas` empieza con "SIN VERIFICACIÓN WEB" y lista lo más dudoso.
- Hay que repetir este grupo cuando haya presupuesto de búsqueda. Las consultas prioritarias están al final.

Certeza subjetiva previa, de mayor a menor. No es `confianza` en el sentido de las instrucciones:
1. Finés, sueco, danés y noruego: los compuestos base (`ompelukaava`, `kaava`, `mönster`, `symønster`, `PDF-mønster`) son estándar y muy probables.
2. Armenio y georgiano: la palabra de préstamo ruso `լեկալո` / `ლეკალო` y los verbos de coser son probables. El término autóctono dominante es incierto.
3. Suajili y amárico: coser (`kushona`, `ስፌት`) y sastre (`fundi cherehani`, `ልብስ ሰፊ`) son sólidos. "Molde" como `mchoro wa nguo` o `የልብስ ንድፍ` no está comprobado como uso real.
4. Hausa, yoruba, igbo, oromo y somalí: hay vocabulario cultural fiable (`atamfa`, `babbar riga`, `aso ebi`, `isi agu`, `dirac`, `guntiino`) pero ningún término nativo comprobado para "molde". Probablemente no exista un uso establecido.

## Hallazgos transversales

### Nórdicos (sv, da, nb) y finés
- Los tres son mercados de alto poder adquisitivo con cultura de costura fuerte y comunidad en Facebook. Usan A4 y cm; la ropa infantil se talla por altura en cm.
- El sueco, el danés y el noruego usan el mismo patrón: `mönster`/`mønster` solo, o el compuesto `sömnadsmönster`/`symönster`. La grafía con guion `sy-mönster` de la asignación no es la estándar: el nórdico escribe el compuesto en una sola palabra. Conviene cubrir ambas.
- Diferencias reales:
  - El danés y el noruego usan `opskrift`/`oppskrift` ("receta") también para instrucciones de costura y punto. Esa palabra arrastra resultados de cocina.
  - El noruego usa `-ksjon`, el danés `-ktion`.
  - El sueco no usa "receta" para costura.
  - `snitmønster` (da) tiene un uso formal; su equivalente noruego no está confirmado.
- Danés y noruego bokmål son casi intercomprensibles. Se puede servir una sola página con vocabulario común, pero el SEO exige ortografía propia (`tøj`/`klær`, `stof`/`stoff`).
- Finlandia: `kaava` es la palabra clave. `kaavoitus` (patronaje) significa sobre todo urbanismo, así que no sirve como palabra de captación. El finés flexiona mucho, por lo que se busca en formas variadas (`kaavat`, `kaavoja`, `kaavan`). Para SEO, la página debe incluir varias formas.
- Marcas y tiendas finlandesas citadas en la asignación: Ottobre Design, Finlayson, Eurokangas. No las pude verificar. Ottobre es probablemente la referencia cultural principal y define cómo se busca la ropa infantil.
- Pago: Swish/Klarna (SE), MobilePay/Dankort (DK), Vipps (NO), banca en línea (FI). Noruega está en el EEE pero no en la UE (MVA propio); no lo verifiqué.

### Georgiano y armenio
- El comercio de patrones en ambas lenguas es casi inexistente. Se busca en ruso (`выкройка`, `лекало`) y en inglés.
- `ლეკალო` y `լեկալո` son préstamos rusos de `лекало`. Ese término también significa "regla curva" o "plantilla", así que hay ambigüedad.
- La palabra autóctona dominante (`ნიმუში`/`ნახაზი` en georgiano, `կաղապար`/`կտրվածք`/`նմուշ` en armenio) no está comprobada.
- Recomendación: servir en ruso e inglés primero, y en georgiano o armenio solo como complemento para captar búsquedas nativas de nicho.
- El armenio tiene dos estándares (oriental y occidental) y dos ortografías (clásica y reformada).

### África subsahariana (sw, ha, yo, ig, am, om, so)
- En todas estas lenguas el comercio y los tutoriales se hacen en inglés (o amárico, en Etiopía). El `uso_de_anglicismos` es alto o muy alto.
- Lo que la gente busca no es un molde, sino estilos y galerías de fotos para llevar al sastre. Ejemplos: `ankara styles`, `aso ebi styles`, `mitindo ya vitenge`, `habesha kemis`. La intención es inspiración, no comprar un PDF.
- El mercado de moldes digitales para autoconfección dentro de África parece pequeño. Los compradores más probables son la diáspora (Reino Unido, EE. UU., Canadá, Escandinavia) y los diseñadores o sastres que quieran moldes editables (DXF/AAMA). Esto es una hipótesis sin datos.
- Servir con otro idioma:
  - Hausa, yoruba e igbo: inglés de Nigeria (`en-NG`).
  - Suajili: inglés de Kenia más suajili.
  - Amárico y oromo: amárico más inglés.
  - Somalí: inglés más las lenguas de la diáspora (sueco, noruego, finés).
- Trampas generales:
  - Diacríticos omitidos (yoruba, igbo, hausa con letras ganchudas).
  - Homofonía en ge'ez (`ሀ/ሐ/ኀ`).
  - `jarida` es "revista" en suajili y quizá "periódico" en somalí.
  - `pattern` = estampado de tela y molde.

## Cómo se busca la ropa tradicional

Todo lo siguiente es de conocimiento previo, sin verificar con búsquedas.

| Término | Región y lengua | Qué significa | Cómo se busca / riesgo |
|---|---|---|---|
| ankara | África occidental, Nigeria y Ghana | Tela de algodón estampada tipo wax print (en otros contextos es la ciudad turca) | `ankara styles`, `ankara gown`, `ankara dress`, `ankara tops`: galería de estilos para inspirarse. `ankara sewing pattern` o `ankara dress pattern PDF` es el uso de molde, sobre todo en Etsy. **`ankara pattern` suele ser el estampado de la tela.** |
| African print | Inglés, diáspora y tiendas Etsy/Shopify | Paraguas inglés para telas estampadas africanas | `African print dress pattern`, `African print fabric`. Aquí "pattern" también es ambiguo. |
| kitenge / vitenge | África oriental, suajili | Equivalente local de tela estampada tipo ankara | `kitenge styles`, `kitenge designs`, `mitindo ya vitenge`. No confundir con `kanga` (rectángulo con proverbio) ni `kikoi`. |
| dashiki | Inglés y diáspora; origen yoruba (`dàńṣíkí`) | Camisa o túnica holgada, con cuello en V y bordado | `dashiki sewing pattern` es un término fuerte en EE. UU. y Etsy. Las ventas son sobre todo en inglés. |
| agbada | Yoruba (`àgbádá`); hausa `babbar riga`; francófono `grand boubou` | Túnica masculina ancha de 3 piezas | `agbada styles`, `agbada pattern`, `agbada sewing pattern`. Es prenda de alto valor para eventos. |
| kaftan / caftan | Árabe/persa/turco; inglés global; Nigeria, `senator wears` | Túnica larga y suelta. En moda occidental es una prenda de verano. En Nigeria hay una versión masculina ("senator") | `kaftan sewing pattern` es muy buscado en inglés. `caftan` en francés y árabe del Magreb. |
| buba | Yoruba (`bùbá`) | Blusa o top. `iro and buba` (mujer): wrapper + blusa. `buba and sokoto` (hombre): top + pantalón | Se busca casi siempre en inglés. Sin diacríticos es ambiguo con nombres propios (Buba). |
| boubou / bubu | África occidental francófona (Senegal, Mali); Nigeria `bubu gown` | Túnica larga y holgada, a veces bordada | `boubou` en francés, `bubu gown` en Nigeria (vestido suelto de mujer). |

Otras prendas con potencial de producto en este grupo:
- Yoruba: `aso ebi`, `aso oke`, `gele`.
- Igbo: `isi agu`, `George wrapper`.
- Etiopía: `habesha kemis`, `netela`, `gabi`.
- Somalí: `dirac`, `guntiino`.

Implicación: la mayor parte de este tráfico es inspiración o compra de tela, no molde. Para captar la intención de molde conviene escribir "[prenda] + sewing pattern + PDF" en inglés, con fotos de estilo para atraer el tráfico de galerías.

## Riesgos de traducción
- No traducir `pattern` como `mönster`/`kaava` sin comprobar uso. Los términos nórdicos y finlandeses son sólidos, pero los términos autóctonos africanos propuestos ("molde de costura") no se usan en la práctica.
- En el grupo africano, un título en yoruba/igbo/hausa/oromo/somalí probablemente rinda menos que uno en inglés. No hay evidencia del tráfico de esas búsquedas.
- Trampas semánticas ya señaladas: `kaavoitus` (urbanismo, fi), `jarida` (so/sw), `ლეკალო` (regla curva), `opskrift`/`oppskrift` (receta de cocina), `akwa` (igbo, varias palabras con tono), `ንድፍ` (diseño en general, am).
- Los términos con la marca "no verificado" (en `sinonimos_y_variantes` y `ambiguedades_y_trampas`) no deben usarse en títulos sin comprobación.

## Lo que NO pude verificar
- Todo. Cero usos reales vistos en esta ejecución.
- Pistas de la asignación sin confirmar:
  - `ნაკეთობის ნიმუში` y `ლეკალა` (ka).
  - `patroni` y `mchoro wa nguo` (sw).
  - `ịkwa uwe` (ig).
  - `caasaa uffataa` y `hodhaa` (om).
  - `jarida` y `tolidda` (so).
  - `tsarin dinki` y `dinkin tufafi` (ha).
  - `àpẹẹrẹ aṣọ` (yo).
- Marcas citadas sin comprobar: Ottobre Design, Finlayson, Eurokangas; Lillesol & Pelle (nb; ni siquiera confirmé que sea noruega).
- Además de lo anterior, no se comprobó la tabla de plataformas y pagos de cada fila (Vipps, MobilePay, M-Pesa, Telebirr, list.am, mymarket.ge, Jiji, etc.) ni los tamaños de papel y unidades.

## Consultas prioritarias para repetir con búsqueda disponible
1. `ompelukaava PDF` / `ompelukaava tulostettava A4` / `Ottobre Design PDF-kaava` (fi).
2. `PDF-mönster sy kläder` / `sömnadsmönster barn` (sv); `PDF-mønster sy tøj` / `snitmønster` (da); `PDF-mønster symønster` / `sybeskrivelse` (nb).
3. `ლეკალო PDF` / `ტანსაცმლის ლეკალო` (ka); `կաղապար հագուստի PDF` / `լեկալո կարել` (hy); en ambos casos comparar con `выкройка PDF`.
4. `mitindo ya vitenge` y `jinsi ya kushona` (sw); `ankara sewing pattern`, `agbada sewing pattern`, `dashiki sewing pattern` (para volumen en inglés).
5. `የልብስ ንድፍ` / `ልብስ ስፌት` (am); `uffata aadaa` / `hodhuu` (om); `dirac` y `guntiino` + `pattern` (so); `tsarin dinki` / `dinkin atamfa` (ha); `àpẹẹrẹ aṣọ` / `iro and buba pattern` (yo); `ụdị uwe` / `isi agu pattern` (ig).
