# Verificación 2.ª pasada, grupo A2

**Búsquedas:** 14 de 14 (WebSearch, modo `standard`). Dos de ellas (con `naver.com` y `taobao.com` en `allowed_domains`) fallaron con error 400 porque esos dominios no son accesibles para el buscador; las conté igual por prudencia. Si el arnés no cuenta los errores, quedan 2 de reserva (uso sugerido: 1 mongol y 1 sublimación).

**Método:** las consultas largas o mezcladas, y las consultas nativas sin filtro, devolvieron casi solo inglés y spam duplicado ("How to Effortlessly Convert a Sewing Pattern to A4 Paper" en 10+ dominios basura). Lo que funcionó fue una consulta corta en el idioma nativo más `allowed_domains` con sitios nativos (note.com, booth.pm, yahoo.co.jp, pixnet.net, books.com.tw, youtube.com).

## Búsquedas y resultado

| # | Consulta (resumen) | Resultado |
|---|---|---|
| 1 | ja: 型紙 PDF ダウンロード A4 印刷 洋裁 縫い代なし | BOOTH (2 ítems de ropa de muñecas); resto inglés/spam |
| 2 | ko: 옷본 PDF 다운로드 A4 출력 패턴 도안 | 0 resultados en coreano |
| 3 | zh-Hans: 纸样 电子版 PDF A4打印 拼接 | 0 tiendas chinas (solo dr-cos.info, inglés) |
| 4 | zh-Hant: 紙型 PDF 下載 列印 A4 手作服 | 0 resultados nativos |
| 5 | ja con dominios nativos | **Éxito:** note.com (varias URLs), Yahoo!クリエイターズ |
| 6 | ko con `naver.com` | Error 400 (contada) |
| 7 | zh-Hans con `taobao.com` | Error 400 (contada) |
| 8 | zh-Hant TW con pixnet / books.com.tw | **Éxito:** >=8 URLs TW |
| 9 | ko nativo sin filtro | Solo spam en inglés |
| 10 | zh-Hans nativo sin filtro | Solo inglés + 1 tutorial zh-cn (Seamly2D) |
| 11 | vi: file rập PDF ... | 100 % inglés |
| 12 | vi: in thăng hoa áo thun đồng phục thiết kế rập | Talleres de uniformes, sin la palabra rập |
| 13 | ko con tistory / youtube / ko.wikipedia | YouTube: 패턴, 제도, 봉제, 기본원형 |
| 14 | zh-Hant HK con hk01 / pinkoi / youtube | YouTube: 打版, 平面紙樣, 車縫; nada de HK |

## Qué quedó verificado

- **Japonés (confianza alta):** 型紙, 洋裁, 文化式原型, 製図, 型紙配布 / 無料配布, A4 出力 / 貼り合わせ, コンビニ + 実物大プリント, "PDFでダウンロード販売". Dominios: note.com, creators.yahoo.co.jp, booth.pm. Nicho nuevo: ドール服 型紙 (ropa de muñecas) en BOOTH.
- **Chino tradicional de Taiwán (dentro de la fila zh-Hans, confianza media):** 紙型, 免費紙型, 紙型下載, 手作服, PDF電子檔, 打版, 立裁, 原型版, 平面紙樣, y 版型 usado como archivo de patrón ("免費版型"). Dominios: pixnet.net, books.com.tw, youtube.com.
- **Chino simplificado (indirecto):** 纸样, 打版, 测试方块, 分页打印, 100% Actual Size, en un tutorial zh-cn y un video de YouTube. No son tiendas de China continental.
- **Coreano (confianza media):** 패턴, 봉제 (y la grafía errónea 봉재), 제도, 기본원형, 미싱, 옷 만들기, en 3 URLs de YouTube.
- **Vietnamita (baja):** solo "in áo đồng phục", "in chuyển nhiệt" y "may áo thun đồng phục" en yellowpages.vn y páginas de talleres.

## Qué cambió

- **zh-Hans:** corregido el punto 3 de trampas. En blogs de Taiwán 版型 también es "archivo de patrón", no solo "corte de prenda". Añadidos 紙型下載, PDF電子檔, 立裁, 原型版, 平面紙樣, 型紙 (kanji conservado en libros traducidos). Aviso nuevo: 紙型 también es molde de bolsos, patchwork y muñecas.
- **ja:** añadidos 型紙配布, 仮型紙, 製図する, 出力, ドール服; confirmada la trampa 和裁 vs 洋裁. Aviso de competencia gratuita: bloggers de note.com regalan 型紙 con condiciones por artículo.
- **ko:** añadidos 제도 (con aviso de homónimo 制度), 기본원형, 미싱, 봉재. 옷본 no apareció en ningún resultado.
- **vi:** "dập mẫu" marcado como dudoso y no apto como keyword; no se buscó explícitamente.
- **nan, hak, wuu, cjy, hsn:** reciben la evidencia de las filas de chino y confianza media indirecta, solo para el léxico escrito compartido. Nota: se sirven con chino escrito (zh-Hant-TW / zh-Hans), sin contenido propio.
- **yue:** confianza baja, con evidencia indirecta en chino tradicional. Se sirve con zh-Hant-HK.
- Se eliminó la frase obsoleta "presupuesto agotado; solo 1 búsqueda en chino" de todas las filas.

## Sigue sin verificar

- **Sublimación en todos los idiomas** (昇華転写, 승화전사, 热升华 / 熱昇華, in thăng hoa, сублимаци). Ninguna búsqueda la cubrió.
- **Coreano:** 옷본, 도안, "PDF 옷본". Naver, Smart Store e Idus no son accesibles con esta herramienta.
- **Vietnamita:** rập, file rập, thiết kế rập, giác sơ đồ, nhảy size, "dập mẫu".
- **Mongol:** toda la fila (0 búsquedas).
- **Chino:** 紙樣 / 打板 de HK, cantonés escrito, 电子版 / 自动发货, Taobao / Xiaohongshu / Douyin / Baidu.
- **Japonés:** パタンナー, 立体裁断, 縫い代なし, 電子型紙 / DL版, A0.
- **Todas las filas:** tallas, pagos y A4 vs Letter siguen siendo conocimiento previo.

## Recomendación

Si hay otra pasada, usar `allowed_domains` desde el principio y evitar `naver.com` y `taobao.com`. Para la sublimación, buscar en tiendas de uniformes con consultas cortas ("昇華転写 ユニフォーム", "승화전사 유니폼", "热升华 球衣", "in thăng hoa áo bóng đá"). Para el vietnamita, dominios como shopee.vn o zalo.me pueden estar bloqueados: probar con un dominio a la vez.
