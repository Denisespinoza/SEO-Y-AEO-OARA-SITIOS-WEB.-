# Estructura de la ficha de producto (molde digital) — por idioma

1. **H1:** `[Prenda] — molde de costura PDF | [Rango de tallas] | A4, Carta, A0 y proyector` (redactado en el idioma; ver `data/terminologia-100-idiomas.csv` para el término real de "molde").
2. **Resumen de 2–3 líneas, respuesta primero** (qué es, para quién, qué incluye).
3. **Caja de especificaciones (arriba):** formatos y hojas por talla (A4/Carta/A0/proyector), capas, margen de costura (cuánto), cuadrado de prueba (medida y página), tallas y sistema (cm y pulgadas), tela (plana/punto), dificultad, idiomas de las instrucciones, licencia, "descarga inmediata, sin bloqueo geográfico".
4. **Galería:** dibujo técnico, prenda cosida en distintos cuerpos, foto del PDF y de la impresión armada.
5. **Qué incluye:** lista de archivos con nombre y cantidad de páginas.
6. **Tabla de tallas:** medidas del cuerpo y de la prenda terminada; equivalencias locales (revisadas por nativo).
7. **Guía de telas:** plana vs punto, elasticidad, rendimiento por talla y ancho de tela, avíos.
8. **Cómo imprimir y armar:** 5 pasos + enlace a la guía y al vídeo.
9. **Selector de licencia:** personal / venta pequeña / fabricación, con precio.
10. **FAQ:** escala, tallas, formatos, reembolso de digitales, licencia.
11. **Relacionados y reseñas verificadas.**
12. **Datos estructurados:** `Product`+`Offer`+`additionalProperty`, `BreadcrumbList`, `WebPage.inLanguage` (ver `jsonld-product-digital.json`).

**Moldes editables/CAD:** convención (AAMA/ASTM D6673), unidades, versión de DXF, software **probado** (Optitex, Gerber/AccuMark, Clo3D, Lectra), tallas anidadas, hilo, piquetes. **Sublimación:** dimensiones del dieline, resolución (300 dpi), sangrado, zona segura, modo de color (consultar el RIP del taller), formatos entregados (PDF/AI/EPS/CDR).
**No** usar atributos de ropa física (`size`, `gender`, `color`) como si se vendiera una prenda: se vende un archivo.
