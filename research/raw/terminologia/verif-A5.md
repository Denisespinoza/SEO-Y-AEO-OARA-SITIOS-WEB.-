# Verificación A5 (2.ª pasada): resumen

**Búsquedas usadas: 14 de 14** (WebSearch `standard`). Salida: `part-A5.v2.csv` (11 filas, 16 columnas, validado con `csv`).
**Resultado: 0 de 11 filas con evidencia en escritura nativa para los términos de molde/patrón/corte.** Confianza: 3 media (te, ta, ml, solo por uso latino/inglés), 8 baja.

## Qué se buscó (en orden)
| # | Idioma | Resultado |
|---|---|---|
| 1 | bn | `ব্লাউজ কাটিং ও সেলাই প্যাটার্ন পিডিএফ ডাউনলোড`: solo spam PDF inglés (baseballprospectus.com, wcbi.com, ufpa.br) |
| 2 | bn | `...ছাঁচ প্যাটার্ন দর্জি বুটিক`: inglés, cursos de arts.ac.uk/PSDF; nada bengalí |
| 3 | bn | `"কাটিং ও সেলাই" ব্লাউজ কামিজ`: **primera consulta con páginas bengalíes** (Bikroy, Deshrupantor, Samakal, Jagonews24), pero de moda/clasificados, sin "প্যাটার্ন" ni "কাটিং ও সেলাই" |
| 4-6 | ta | 3 intentos (`பேட்டர்ன்`/`ப்ளவுஸ் கட்டிங்`, `சுடிதார் பேட்டர்ன்`, `"சுடிதார் கட்டிங்"`): spam "Blouse Cutting And Stitching In Tamil" e inglés; 0 páginas en tamil |
| 7 | te | `బ్లౌజ్ కటింగ్ కుట్టు శిక్షణ ప్యాటర్న్`: spam PDF inglés |
| 8 | mr | `"शिवणकाम" पॅटर्न कुर्ती...`: inglés; apareció el curso de Udemy en malayalam |
| 9 | ne | `सिलाई कटाई तालिम...`: tratada como hindi (NIOS, Usha); 0 nepalí |
| 10 | si | `ෆ්‍රොක් රටා මැහුම් පන්ති...`: spam "Frock Suit/Umbrella Frock Cutting"; 0 cingalés |
| 11 | ml | `ചുരിദാർ കട്ടിംഗ് തയ്യൽ ക്ലാസ് പാറ്റേൺ`: Udemy (curso en malayalam), Tailo Tech (canal tamil), sílabo Usha; 0 páginas en malayalam |
| 12 | kn | `ಹೊಲಿಗೆ ತರಬೇತಿ ರವಿಕೆ ಕಟಿಂಗ್ ಪ್ಯಾಟರ್ನ್`: patentes de cortapelos y cursos ingleses; 0 canarés |
| 13 | gu | `સીવણ ક્લાસ ચણિયાચોળી કટિંગ પેટર્ન દરજી`: cursos ingleses; 0 guyaratí |
| 14 | te (latina) | `blouse cutting in Telugu youtube channel...`: canal Pasha Tailors, Tailo Tech, guía Usha "Princess Blouse Telugu" |

Desviación del plan (1 búsqueda por idioma): gasté 3 en bengalí y 3 en tamil porque las primeras devolvieron spam. Por eso **odia y asamés no se buscaron** y no quedó una 2.ª búsqueda dedicada al préstamo "pattern".

## Qué se verificó
- **bn:** la grafía `ব্লাউজ` (4 dominios) y que `নকশা` en prensa de moda significa diseño/estilo de blusa, no patrón de costura. Bikroy (bikroy.com/bn) existe como marketplace en bengalí; su categoría "ব্লাউজ" lista blusas hechas. Esto encaja con la hipótesis de intención "inspiración/galería".
- **te, ta, ml (solo uso latino/inglés):** un canal telugu y uno tamil (listados de qoruz.com) se describen como "blouse cutting and stitching in Telugu/Tamil", "blouse drafting", "princess cut", "churidar cutting and stitching"; un curso de Udemy en malayalam se titula "Kurti Cutting & Stitching Mastery"; Usha publica `P27-Princess-Blouse-Telugu_compressed.pdf`. Es indicio indirecto de que **"cutting" (+ "stitching", "drafting") es la etiqueta comercial dominante**. Las descripciones de qoruz proceden del texto que devolvió el buscador; no pude abrir las páginas (WebFetch no funciona).
- Ambigüedad "cutting" = corte de pelo: observada de rebote (la consulta canaresa devolvió patentes de cortapelos).

## Qué cambió en el CSV
- `confianza`: te, ta, ml pasan de baja a **media** (1-2 usos reales, solo en escritura latina). Los demás siguen en baja.
- `evidencia_urls` rellenadas: bn (3), te (2), ta (1), ml (1). Solo URLs vistas en resultados.
- bn: `নকশা` reescrito como diseño/motivo con evidencia; Bikroy añadido a plataformas. te: añadidos "princess cut blouse", "boat neck blouse", "blouse drafting". ml: añadido "kurti cutting stitching malayalam". gu: variante `પૅટર્ન` (solo vista en un resumen generado, marcada como tal).
- `nota_localizacion`: la frase de estado de la 1.ª pasada se sustituyó por "VERIFICADO PARCIALMENTE: ..." (bn, te, ta, ml) o "SIN VERIFICACIÓN WEB (...)" (mr, gu, kn, ne, si, or, as).
- Ningún término de la 1.ª pasada resultó incorrecto; tampoco se pudo confirmar ninguno en escritura nativa, así que no se corrigió ni se quitó ninguno.

## Sigue sin verificar
- **Todos los términos en escritura nativa** (`প্যাটার্ন`, `ప్యాటర్న్`, `பேட்டர்ன்`, `पॅटर्न`, etc.) y los falsos amigos de "molde" (`ছাঁচ`, `साचा`, `అచ్చు`...).
- **Pregunta del préstamo "pattern":** sin respuesta definitiva en escritura nativa. Lo visto apunta a que el comercio usa inglés/latino ("cutting", "stitching", "drafting"), y "pattern" solo apareció dentro de títulos ingleses. Los resúmenes generados por el buscador transcribieron "pattern" (`ప్యాటర్న్`, `પૅટર્ન`, `पॅटर्न`), pero eso es texto generado, **no uso web**.
- mr, gu, kn, ne, si: 0 evidencia. or y as: no buscados. Pagos, papel, medidas y plataformas: conocimiento previo en todos.

## Notas sobre la herramienta (para el resto de pasadas)
- Las consultas con "blouse/cutting/pattern/PDF/download/ডাউনলোড" atraen spam PDF espejo. Las únicas que devolvieron páginas nativas fueron cortas y con vocabulario de prensa/clasificados (caso bn nº 3).
- El devanagari nepalí se interpreta como hindi.
- Pistas no verificadas: `ushasew.com` (Usha) publica guías por idioma (el nombre `...-Telugu_compressed.pdf` sugiere versiones en otros idiomas); `qoruz.com/<canal>/youtube` indexa canales de costura por idioma; NIOS tiene el curso "Cutting, Tailoring and Dress Making" (705706). Los tres sirven como punto de partida para una verificación con otra herramienta.
