# Notas del grupo A3 (árabe y variedades, persa, hebreo, pastún, kurdo kurmanyí)

## Advertencia principal: nada de este grupo está verificado

- El presupuesto de WebSearch se agotó (límite compartido por todos los agentes del turno) tras **una sola búsqueda**, hecha en árabe (`باترون خياطة PDF تحميل باترونات جاهزة للطباعة`). Devolvió únicamente páginas en inglés sin relación real (dominios de museos, universidades y sitios gubernamentales con contenido duplicado), inservibles como evidencia.
- Por eso las **14 filas están en `confianza=baja`** y **`evidencia_urls` está vacío en todas**. No se incluyó ninguna URL inventada.
- Todo el contenido proviene de conocimiento previo del modelo y de los términos sugeridos en el encargo (باترون, نماذج خياطة, قصات, تفصيل وخياطة, رسم باترون, باترون بي دي اف, باترون جاهز للطباعة, سبليميشن/تسامي, الگو, پترن, תבנית תפירה, סובלימציה, etc.). Ninguno se comprobó con uso real en tiendas o blogs.
- Tampoco se pudo verificar la **situación actual (octubre de 2026) de filtrado y bloqueos en Irán**. Solo se anota lo que recuerdo sin comprobar: Telegram filtrado desde 2018, Instagram desde 2022, WhatsApp y Google Play desbloqueados en dic. 2024 y fuertes restricciones durante la guerra de junio de 2025.
- Se recomienda repetir la verificación cuando haya presupuesto de búsqueda (ver lista al final).

## Hallazgos transversales (hipótesis a validar)

1. **Un solo árabe escrito.** Las 10 filas árabes (ar, arz, apc, apd, ary, acm, ars, arq, aeb, afb) se buscan en árabe estándar con alfabeto árabe. Las variedades coloquiales casi no se escriben para buscar productos. La diferencia útil entre ellas está en el **vocabulario de prendas**, no en el término "molde".
2. **El término núcleo es un préstamo:** باترون / باترونات (del francés *patron*, escrito sin /p/). En árabe estándar formal aparecen también نموذج, قالب, نمط, pero con muchas falsas amistades (formulario, molde de repostería, estilo). Probablemente conviene que el contenido use **باترون** como término principal y **نماذج خياطة** como secundario.
3. **Prendas locales (donde hay demanda de nicho):**
   - عباية / عباءة (abaya), ambas grafías.
   - جلابية: significa cosas distintas según país (vestido de casa en Egipto, túnica masculina en Sudán, vestido femenino en el Golfo). La **جلابة / djellaba** marroquí es otra prenda.
   - قفطان / كفتان (caftán), con peso especial en Marruecos y Argelia.
   - دشداشة, كندورة, ثوب (thobe): cambian según país. En Sudán ثوب/توب es el tobe femenino y en Palestina/Jordania suele ser el vestido bordado.
   - Prendas del Magreb con nombre propio: gandoura, karakou, blouza oranaise, takchita, jabador, jebba.
4. **Magreb (ary, arq, aeb): la búsqueda real es en francés.** Esperar consultas como *patron couture PDF*, *patron djellaba*, *patron caftan*, *modèle de couture*, *patron gratuit*, con árabe y arabizi como complemento. Un sitio `fr` bien localizado (fr-MA / fr-DZ / fr-TN en términos de prendas y pagos) probablemente rinde más que uno `ar` para estos tres países. Sin verificar.
5. **Golfo (afb, parte de ars): el inglés pesa mucho**, sobre todo en EAU y Catar por la alta población expatriada. Términos plausibles: *tailoring*, *stitching*, *abaya pattern*, *PDF pattern*. Marcado en `afb` como "inglés real" en EAU/Catar.
6. **Egipto y Levante** usan mucho باترون y YouTube/Facebook; las diferencias son de prendas (جيبة frente a تنورة para "falda").
7. **Arabizi:** se supone que aparece en chat y redes más que en búsquedas de producto. No hay evidencia de que sea un canal de búsqueda relevante para moldes. Sin verificar.
8. **Sublimación:** سبليميشن / سبلميشن (transliteración del inglés) probablemente más usado que التسامي (término técnico). Trampa: تسامي también significa "elevarse".
9. **Ortografía y matching:** ب por پ (el árabe no tiene /p/), أ/ا, ة/ه, ى/ي, ك/ک y ي/ی (teclados persas), عباية/عباءة, y términos en latín dentro de frases RTL ("باترون pdf", "A4"). Conviene indexar variantes.

## Por lengua

- **Persa (fa):** términos centrales الگو / الگوی دوخت / الگوی خیاطی, oficio الگوسازی / الگوکشی, sublimación سابلیمیشن. Trampas: `پترن` suele ser estampado, `الگو` también es "modelo a seguir". Ecosistema local (Digikala, Divar, Torob, Basalam, Aparat, Bale, Eitaa, Rubika, Telegram/Instagram vía VPN). **Riesgo comercial relevante:** sanciones y ausencia de pasarelas de pago internacionales; consultar asesoría legal antes de apuntar a Irán.
- **Hebreo (he):** términos centrales תבנית תפירה / תבניות תפירה y גזרה (corte/patrón en el mundo de la costura), oficio בניית גזרות, sublimación סובלימציה. Trampa fuerte: `תבנית` sola es molde de repostería o plantilla digital. Mercado con tarjetas y apps locales, inglés frecuente.
- **Pastún (ps):** casi sin contenido escrito de costura. Se dejó el campo de oficio vacío y se aportaron solo términos probables (`نمونه`, `قالب`, `خیاطي`). La búsqueda real parece ocurrir en **urdu (Pakistán), dari (Afganistán) o inglés**. Recomendación: no localizar completo en pastún y servir esas audiencias con dari/urdu/inglés. Condiciones de mercado muy difíciles en Afganistán (restricciones, pagos, conectividad).
- **Kurdo kurmanyí (ku):** poco contenido web de costura. La búsqueda real parece estar en **turco** (kurdos de Turquía: *kalıp*, *patron*, *dikiş*), árabe (Siria/Irak), alemán (diáspora) o inglés. El sorání (alfabeto árabe) es otra lengua escrita y no se mezcla. Recomendación: servir con turco/árabe/inglés antes que con kurmanyí.

## Oportunidades de nicho (hipótesis)

- Abayas, djellabas, caftanes, gandouras, karakou, thobes: términos locales de alta intención, probablemente con menos oferta de moldes digitales en PDF.
- "Plantillas para sublimación" (equipos deportivos, camisetas): término sencillo en árabe (سبليميشن), persa y hebreo.
- Contenido AEO: responder en árabe "ما هو الباترون؟" / "كيف أطبع الباترون وأجمعه؟" para que los asistentes de IA citen el sitio.

## Qué no se pudo verificar

- Todo término de las 14 filas. En especial los más inciertos:
  - `باترونيست` (patronista), `فصّال`, `تفصال` (darija), `دراعة` (Najd), `نمط خياطة` (descartado por incierto).
  - `الگوکشی` y `چاپ تصعیدی` (persa).
  - `גזרה` como término dominante frente a `פטרון` / `תבנית` (hebreo).
  - `الګو`, `نمونه`, `قالب` como términos de producto en pastún.
  - `model`, `qalib`, `dirûn`, `dakêşandin` en kurmanyí.
- Estado actual de plataformas en Irán (filtrado, apagones) y en Afganistán, Sudán y Siria.
- Plataformas de pago y marketplaces citados por país (Mada, Tabby, Tamara, Fawry, Bankak, ZainCash, CMI, Edahabia, Tayara, Ouedkniss, Avito, Haraj, Miswag, Zarinpal) y la disponibilidad de PayPal en Argelia y Túnez.
- Tamaños y convenciones de talla (abayas, thobes) por país.
- Uso real de arabizi en búsquedas de moldes.

## Lista de consultas pendientes (cuando haya presupuesto de búsqueda)

1. `باترون خياطة PDF` + `تحميل` / `شراء` y `نماذج خياطة` (ver si tiendas reales usan estos términos y cuáles dominan).
2. `باترون عباية PDF`, `باترون قفطان`, `باترون جلابية` (nicho de prendas).
3. `patron couture PDF djellaba` / `patron caftan PDF` / `patron gandoura` (confirmar francés en el Magreb).
4. `abaya sewing pattern PDF` y `ladies tailoring Dubai` (confirmar inglés en el Golfo).
5. `الگوی دوخت PDF`, `الگوسازی`, `الگوکشی`, `چاپ سابلیمیشن` + situación actual de filtrado en Irán (Google/Instagram/Telegram).
6. `תבנית תפירה PDF`, `גזרות תפירה להדפסה`, `פטרון תפירה`, `סובלימציה`.
7. `نمونه جامې پښتو`, `خیاطي پښتو` y `kalıp PDF`, `model dirûnê kurdî`.
