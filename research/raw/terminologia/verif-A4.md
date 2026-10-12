# Verificación A4 (2.ª pasada) — hindi, urdu y variedades

**Búsquedas usadas: 14 de 14.** CSV: `part-A4.v2.csv` (13 filas, 16 columnas, validado con `csv`: mismas filas y orden que `part-A4.csv`).
Truco que funcionó: el buscador sesgado a EE. UU. devolvió basura en consultas "limpias" (PDFs spam, Fiverr, Etsy); con `allowed_domains` (YouTube, Amazon.in, Flipkart, Meesho, Daraz, Facebook, Etsy) salió uso real.

## Búsquedas
| # | Consulta (resumen) | Resultado |
|---|---|---|
| 1-2 | hindi "ब्लाउज कटिंग … PDF डाउनलोड" / "कुर्ती कटिंग … ड्राफ्टिंग" | solo PDFs spam en dominios ajenos y tiendas ucranianas; ninguna tienda hindi |
| 3 | "blouse cutting kurti cutting paper pattern PDF free download" | Hackaday (generador gratuito SVG/PDF, A3), Sikana |
| 4-5 | urdu "کٹنگ … پیٹرن پی ڈی ایف" / Roman Urdu "paper pattern Daraz" | Fiverr y spam; nada en urdu |
| 6 | sublimation jersey India | IndiaMART, Etsy (Sialkot), Fiverr |
| 7 | hindi, YouTube+Meesho+Amazon.in+Flipkart | 10 títulos reales "ब्लाउज कटिंग" |
| 8 | urdu, YouTube+Daraz+Facebook | 7 títulos reales "قمیض/شلوار کی کٹنگ" |
| 9 | Etsy "blouse kurti salwar sewing pattern PDF" | 10 listados PDF (A4/A0, inglés) |
| 10 | "kurti paper pattern …" Amazon.in/Meesho/Flipkart/Daraz/IndiaMART | Meesho, Flipkart, Amazon.in: "Paper Cutting Patterns", "Farma" |
| 11 | hindi "सब्लिमेशन जर्सी" | solo inglés EE. UU.; nada hindi |
| 12 | urdu+inglés sublimación Sialkot | B2B (gov.pk, Globy, Rozee.pk, ensun) |
| 13 | hindi "कुर्ती फर्मा ब्लाउज फर्मा" | páginas /-/hi/ de Amazon.in con "फार्मा" |
| 14 | Roman Urdu "shalwar kameez paper pattern" Daraz/OLX/YouTube/FB/Pinterest | Daraz (plantilla de madera), YouTube, Facebook, Pinterest |

## Verificado
- **hi (alta):** la palabra del molde/oficio es **"cutting"** (ब्लाउज कटिंग, कटोरी/प्रिंसेस कट ब्लाउज कटिंग, "…cutting in Hindi") en YouTube; el producto en papel se llama **"Paper Cutting Pattern / कटिंग पैटर्न / फार्मा (farma)"** en Amazon.in, Flipkart y Meesho (sets por talla: blusa 28-42 in, kurti 30-42). El PDF solo existe en inglés (Etsy, Hackaday).
- **ur (alta, solo el término "cutting"):** قمیض کی کٹنگ, شلوار کی کٹنگ, کٹنگ اینڈ سٹیچنگ y Roman Urdu ("kameez shalwar cutting", "Selai Course", "Simple Suit Cutting") en YouTube, Daraz, Facebook. Sialkot confirmado como polo de sublimación (Rozee.pk, Pakistan Trade Portal, Globy, Etsy).
- **Sublimación (en inglés/latín):** "sublimation jersey / sublimated polyester T-shirts" en IndiaMART; "sublimation patterns of sportswear" (Fiverr, Etsy). No hay vendedor indio de plantillas.

## Cambios respecto a la 1.ª pasada
1. **Término nuevo: "farma / फार्मा"** = molde de papel de sastre (trampa probable: "pharma"; inferido, no buscado).
2. Corregido: "pattern/पैटर्न" **sí** es el nombre del producto cuando va con "paper cutting"; suelto sigue siendo ambiguo.
3. Corregido: formato dominante en India = **papel físico en sets**, no PDF. En Pakistán (Daraz) "cutting pattern" = **plantilla física de madera**.
4. Ortografía urdu: **سٹیچنگ** (visto) en lugar de اسٹیچنگ (no visto); "selai" visto, "silai" no.
5. "shirt" = kameez en títulos urdu.
6. Trampa: PDFs spam ("Designer Blouse Cutting Pattern.pdf", "Salwar Kameez Cutting Technique.pdf") replicados en dominios ajenos. No usarlos como evidencia.

## Sigue SIN verificar
- Todo término de PDF/digital, imprimir en casa y sublimación **en escritura nativa** (devanagari, nastaliq). No apareció ninguna página nativa.
- "कुर्ती कटिंग" y "सलवार सूट कटिंग" en devanagari; "پیٹرن" y "سلائی" en nastaliq; ड्राफ्टिंग/कटिंग मास्टर/दर्जी.
- Telegram, WhatsApp, TikTok, ShareChat, asistentes de IA; pagos (UPI, COD, Easypaisa, JazzCash); unidades girah/gaz.
- **Variedades** (bho, mai, awa, mag, hne, raj, bgc, dcc, skr, pnb): no se gastaron búsquedas, `confianza=baja`, siguen "SIN VERIFICACIÓN WEB" en lo específico; heredan los términos verificados de hi (bho, mai, awa, mag, hne, raj, bgc) o ur (pnb, skr, dcc). Hindi y urdu cubren su búsqueda por inferencia, no por evidencia.
- **Sindhi** (sd): no buscado (sin presupuesto). Ortografía ڪ/ٽ/ي sin comprobar; fallback verificado en la fila ur.
- Precios/tallas de listados: tomados de resúmenes del buscador, volátiles.
