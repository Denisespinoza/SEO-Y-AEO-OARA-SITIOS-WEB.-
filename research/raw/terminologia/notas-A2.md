# Notas grupo A2 (chino y variedades, japonés, coreano, vietnamita, mongol)

## 0. Aviso de verificación (leer primero)

**Ningún término de `part-A2.csv` quedó verificado por búsqueda.** El presupuesto de WebSearch del turno se agotó (límite compartido entre todos los agentes): solo una búsqueda en chino llegó a ejecutarse y devolvió páginas en inglés, spam y una web japonesa de cosplay (dr-cos.info) sin uso real de los términos. No usé curl/WebFetch ni otros rodeos. Por eso:

- Las 11 filas llevan `confianza=baja` y `evidencia_urls` vacío (no inventé URLs).
- Los términos salen del conocimiento previo del modelo y de la lista que pidió el solicitante; los marqué `(inferido)` o `SIN VERIFICAR`.
- La certeza propia varía mucho entre grupos de términos (ver sección 5). `baja` significa "no verificado", no "dudoso" en todos los casos.

## 1. Mapeo recomendado de idiomas a versiones web

| Código | Qué se busca realmente | Servir con |
|---|---|---|
| zh-Hans | mandarín simplificado (纸样, 打版, 电子版) | versión propia zh-Hans (CN/SG/MY) |
| zh-Hant-TW | 紙型 / 紙樣 / 手作服, 列印, 熱昇華 | variante propia, no conversión automática |
| zh-Hant-HK | 紙樣, 打板, 車縫/車衫, 熱昇華/熱升華 | variante propia (puede ser la base de `yue`) |
| yue | chino tradicional estándar de HK; cantonés escrito solo en consultas coloquiales y redes | zh-Hant-HK; el cantonés escrito solo como tono de marca |
| wuu, cjy, hsn | mandarín simplificado (nadie busca en wu/jin/xiang) | zh-Hans, sin versión propia |
| nan | mandarín (zh-Hant en Taiwán, zh-Hans en Fujian/Singapur/Malasia) y inglés/malayo en diáspora | zh-Hant-TW + zh-Hans + en |
| hak | chino tradicional (Taiwán) o simplificado (Guangdong) | zh-Hant-TW + zh-Hans |
| ja, ko, vi, mn | idioma propio | versión propia |

## 2. Hallazgos transversales

- **Cinco variedades chinas (wu, jin, xiang, min del sur, hakka) no necesitan contenido propio.** La escritura web es el mandarín estándar; lo único local que identifiqué (衣裳/做衣裳 en el norte y Jiangnan, 做衫 y 針車 en hokkien) es léxico hablado y no verificado.
- **Excepción cantonesa (HK):** hay consultas y publicaciones en cantonés escrito (嘅 係 唔 冇 咗 點樣 邊度; ej. 有冇免費紙樣) sobre todo en Facebook/IG/LIHKG/YouTube, pero las tiendas y los cursos usan chino tradicional estándar con vocabulario de HK (紙樣, 打板, 車縫). Recomendación: contenido en zh-Hant-HK, con guiños en cantonés solo en el tono.
- **Taiwán vs. continente vs. HK:** hay una divergencia léxica real. Taiwán usa 紙型 (influencia de los libros japoneses de 手作, "附原寸紙型"), HK usa 紙樣/打板, y el continente usa 纸样/版型/打版. Además: 熱昇華 (TW) vs 升华 (CN); 列印 (TW) vs 打印 (CN). No convertir con un conversor automático.
- **Canales:** en China la intención de compra pasa por Taobao/Xiaohongshu/Douyin/Bilibili, no por Google/Etsy. Los productos digitales se venden en Taobao como "电子版/自动发货". Si moldey.com no puede operar allí, el SEO en zh-Hans tendrá alcance limitado; Taiwán, HK, Singapur y Malasia sí son alcanzables con Google.
- **Japón** compra mucho por libros con "実物大型紙付き" y por BOOTH/minne/Creema/note/Mercari. Los 型紙 japoneses suelen venir **sin margen de costura** (縫い代なし) y con tallas superpuestas para calcar: conviene explicarlo.
- **Corea:** Naver domina (blog, cafe, Smart Store); la búsqueda mezcla 옷본 (término nativo), 패턴 (préstamo) y 도안 (genérico de manualidades).
- **Vietnam:** mucha gente busca sin tildes; "rap" sin tilde choca con la música. El término del oficio es rập, y "in 3D" es la forma comercial de la camiseta sublimada integral.
- **Mongolia:** web de costura en mongol muy escasa; hay un nicho cultural claro (дээл, la prenda tradicional) y herencia rusa (лекал, выкройка).

## 3. Riesgos de traducción

- **Chino:** 打样/打樣 = hacer la prenda muestra (no patronaje). 版型 = corte/ajuste de una prenda, no el archivo. 图案 = estampado. 样板 puede ser muestra. 电子版 puede ser ebook. 制/製, 板/版, 升/昇 varían por región.
- **Japonés:** 型紙 = también plantilla de teñido (伊勢型紙) y patrones de kimono (和裁): añadir 洋裁/ソーイング. パターン = patrón/motivo/diseño en general. 縫製 devuelve fábricas (B2B).
- **Coreano:** 패턴 = también estampado; 도안 = dibujo, punto, bordado, tatuaje; 재단 = corte pero también "fundación" (재단법인); 나염 ≠ 승화전사 (estampado textil en general vs. sublimación).
- **Vietnamita:** rập / rạp (cine) / dập (estampar); 'thăng hoa' también es "elevarse" en sentido figurado; 'pattern' en inglés = họa tiết. "dập mẫu" (pedido por el solicitante) probablemente es variante homófona/ortográfica de "rập mẫu" en el norte, no verificada.
- **Mongol:** хэв = molde/forma (de ahí хэвлэх = imprimir); загвар es muy amplio (diseño, modelo, estilo); Mongolia Interior usa la escritura mongola tradicional, no cubierta en `mn`.

## 4. Oportunidades de nicho (hipótesis, sin verificar)

- Taiwán: 紙型 / 手作服 / 原寸紙型 y las plataformas Pinkoi/Shopee/Dcard; ropa tradicional hakka (客家藍衫, 客家花布).
- Japón: PDF A4 y A0 para el público de BOOTH/minne/Creema/note; lolita/cosplay (型紙 vendidos en BOOTH).
- Corea: 승화전사 para 단체복/유니폼/저지 y 옷본 de hanbok.
- Vietnam: DXF/CAD y "file rập" para talleres y pymes de confección; sublimación ("in thăng hoa", "áo in 3D") para ropa de equipo y uniformes.
- Mongolia: patrones de deel y ropa deportiva sublimada de equipos.
- Wu (Hangzhou, Changshu, Zhili): público profesional que busca 样板/CAD/DXF (cadena de moda y e-commerce); en la práctica se atiende con zh-Hans.

## 5. Certeza propia por grupo de términos (no es evidencia web)

- **Muy probable:** 纸样/紙樣/紙型, 打版/打板/制版, 版型 (zh); 型紙, パターン, 洋裁, 縫製, ソーイング, 昇華転写, BOOTH/minne/Creema/note (ja); 옷본, 패턴, 도안, 재단, 봉제, 승화전사, 나염 (ko); rập, cắt may, in thăng hoa (vi).
- **Probable:** 熱昇華 (TW), 隊衣 (HK), パタンナー, 立体裁断, 원형, 패턴사, giác sơ đồ, nhảy size; plataformas listadas.
- **Dudoso o no verificado:** "dập mẫu", "file rập" como cadena de búsqueda real, 满印/满版, 升华模板, léxico hokkien/hakka/wu/jin/xiang, todo el mongol (оёдлын загвар, хувцасны хэв, лекал, сублимаци), nombres de CAD locales (富怡, 博克, ET), ejemplos de consultas cantonesas, hábitos de pago y tallas.

## 6. Pendiente cuando haya presupuesto de búsqueda

1. Buscar en chino simplificado, tradicional y cantonés: `纸样 PDF 电子版 A4`, `紙型 PDF 下載 手作`, `紙樣 下載 免費`, `熱昇華 球衣 客製`, y confirmar el cuadro TW/HK/CN con tiendas y blogs reales.
2. Japonés: `型紙 PDF ダウンロード A4`, `実物大型紙`, `BOOTH 型紙`, `昇華転写 ユニフォーム`.
3. Coreano: `옷본 PDF 다운로드`, `패턴 도안 무료`, `승화전사 유니폼`.
4. Vietnamita: `file rập PDF`, `rập giấy`, `thiết kế rập`, `in thăng hoa áo`; confirmar si "dập mẫu" existe.
5. Mongol: `оёдлын загвар`, `хувцасны загвар PDF`, `дээлний загвар`; confirmar si hay uso real o si domina el inglés/ruso.
6. Anotar 1-3 URLs reales por idioma y subir `confianza` a media/alta donde se confirme.
