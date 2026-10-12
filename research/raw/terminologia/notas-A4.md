# Notas grupo A4 (hindi, urdu, panyabí occidental, bhoyapurí, maithili, sindhi, awadhi, magahi, chhattisgarhi, rajastaní, haryanvi, decanés, saraiki)

## 0. Aviso de verificación (leer primero)
- **No se pudo verificar nada.** El presupuesto de WebSearch del turno (200 llamadas compartidas entre todos los agentes) ya estaba agotado cuando empecé: las 6 primeras consultas devolvieron "web search budget is used up" y no se reintentó ni se rodeó el límite.
- Por eso las 13 filas llevan `confianza=baja` y `evidencia_urls` **vacío** (no se inventó ninguna URL). Todos los términos salen de conocimiento general del modelo y se marcan "SIN VERIFICACIÓN WEB" en `ambiguedades_y_trampas`.
- Los términos más probables (muy altos en mi estimación, pero sin comprobar): "कटिंग", "ब्लाउज कटिंग", "कुर्ती कटिंग", "पैटर्न/पेपर पैटर्न", "ड्राफ्टिंग", "सिलाई" (hindi); "کٹنگ", "سلائی", "پیٹرن", "کپڑوں کی کٹنگ" (urdu); "cutting and stitching", "kameez cutting", "shalwar cutting", "paper pattern" (Roman Urdu/hinglish). Los términos locales de bhoyapurí/maithili/sindhi/saraiki/panyabí son inferencias y los menos fiables.

## 1. Hallazgos transversales (hipótesis a validar)
- **La palabra clave real es "cutting", no "pattern".** En India/Pakistán el oficio se nombra "cutting and stitching"; "pattern" suele significar *diseño/estilo* (p. ej. "blouse back neck patterns"). El molde en papel se dice "paper pattern"; el trazado, "drafting"; el maestro, "cutting master".
- **Escritura latina dominante.** Hinglish (hi) y Roman Urdu (ur) concentran la búsqueda y los títulos de YouTube/Facebook. Incluso en devanagari/nastaliq las palabras clave son préstamos del inglés (कटिंग, स्टिचिंग, پیٹرن, کٹنگ). `uso_de_anglicismos` = alto en las 13 filas.
- **Las 8 variedades hindi/urdu no tienen búsqueda propia** (bho, mai, awa, mag, hne, raj, bgc → hindi; dcc, skr, pnb → urdu). Se escriben y buscan en el idioma estándar; las filas son breves y repiten los términos de hi/ur. Diferencias locales no verificadas; solo hay pistas de nicho (ghagra/Rajputi poshak en raj; damaan/kurti en bgc; chikankari en awa; Madhubani en mai; khada dupatta/sharara en dcc; ajrak/ralli en skr/sd).
- **Sindhi**: dos ortografías conviven (ڪ ٽ ي vs ک ٹ ی); poca búsqueda escrita, probablemente la gente usa urdu/Roman Urdu/inglés.

## 2. Qué servir con qué
- Páginas **hi-IN** (devanagari con keywords hinglish en título/meta/FAQ) cubren hi + bho/mai/awa/mag/hne/raj/bgc.
- Páginas **ur-PK** (nastaliq con Roman Urdu en metadatos/FAQ) cubren ur + pnb/skr/sd/dcc; para dcc y el público indio de urdu, **ur-IN**.
- **Alto valor: páginas en inglés localizadas (en-IN, en-PK)** optimizadas para "kurti cutting", "blouse cutting", "salwar suit cutting and stitching", "paper pattern", "suit pattern", "blouse pattern PDF", "sublimation jersey pattern". Muy probablemente el mayor volumen está ahí y no en escritura nativa.
- Variedades como idioma web propio (bho, mai, awa, mag, hne, raj, bgc, dcc, skr, pnb) no se justifican por volumen de búsqueda.
- Antes de usar `hi-Latn`/`ur-Latn` como hreflang o 3 letras (pnb, bho...) comprobar soporte real de los buscadores.

## 3. Riesgos de traducción
- Falsos amigos: "कटिंग" (cutting chai, hair cutting, edición de video), "साँचा" (molde/plantilla; no se usa para patrón), "सूट"/"suit" (salwar suit, no traje), "ड्राफ्टिंग/ڈرافٹنگ" (redacción legal), "Punjabi suit" (prenda, no idioma), "पैटर्न/pattern" (diseño/estampado).
- "सिलाई के डिज़ाइन"/"سلائی کے ڈیزائن"/"blouse designs" = galerías de estilos; no es intención de compra de moldes.
- "ڈیجیٹل پرنٹنگ" en Pakistán suele ser tela estampada digitalmente (lawn), no sublimación de ropa deportiva; "sublimation" en India a menudo remite a tazas/regalos. Para el nicho jersey, usar "sublimation jersey/sportswear/custom jersey".
- "सिलाई मशीन योजना" (programas estatales de máquinas gratis) y "unstitched suit" (tela sin coser, Pakistán) son intenciones ajenas.
- Ortografía múltiple: पैटर्न/पेटर्न, डिज़ाइन/डिजाइन, सब्लिमेशन/सब्लीमेशन, kameez/qameez/kamiz, shalwar/salwar; dígitos urdu-arábigos vs occidentales; fuente Nastaliq necesaria.

## 4. Oportunidades de nicho (hipótesis)
- Saree blouse (princess cut, katori, padded, boat neck), kurti, salwar/patiala, palazzo, anarkali, lehenga/ghagra, petticoat, frock infantil, gents kurta-shalwar. Costura a medida: el comprador está acostumbrado a drafting por medidas en pulgadas y a tutoriales gratis; el valor diferencial es PDF con tallas por busto, capas, A4 + A0.
- Competencia: YouTube, canales de Telegram/WhatsApp con PDF y libros gratis, Meesho/Flipkart/Daraz (papel y libros).
- B2B sublimación: Sialkot (Pakistán) y talleres de jerseys en India; plantillas listas para sublimar.
- Unidades de sastre a tener en cuenta (a verificar): pulgadas, girah ≈ 2,25 in, gaz = yarda; jerga de medidas en Roman Urdu: lambai, chhati, teera, gala, bazu/astin, daman, ghera, paincha. Pagos probables: UPI/COD (India); COD/Easypaisa/JazzCash (Pakistán); tarjetas internacionales/PayPal poco prácticos en Pakistán.

## 5. Pendiente de verificar (reintentar cuando haya presupuesto de búsqueda)
1. Todo `evidencia_urls` (vacío) y subir `confianza` a media/alta para hi y ur.
2. Consultas sugeridas: "ब्लाउज कटिंग PDF", "कुर्ती कटिंग पेपर पैटर्न", "paper pattern kurti Meesho/Etsy", "blouse pattern PDF download India", "سلائی پیٹرن PDF", "کٹنگ اینڈ اسٹیچنگ", "kameez cutting paper pattern Daraz", "सब्लिमेशन जर्सी पैटर्न", "sublimation jersey pattern Sialkot", Wikipedia hi/ur del artículo "sewing pattern".
3. Léxico local real de bho/mai/awa/mag/hne/raj/bgc/skr/pnb/sd (verbo coser, sastre, corte) y si existe contenido de costura propio en esas variedades.
4. Ortografía sindhi (ڪٽنگ/پيٽرن) y volumen real de búsqueda sindhi.
5. Términos de impresión doméstica (A4 "जोड़कर", "صفحات جوڑیں"), proyector y plotter, y términos de PDF/descarga en cada escritura (todos inferidos).
6. Hábitos de pago y tamaños de papel/tallas (todo hipótesis).
