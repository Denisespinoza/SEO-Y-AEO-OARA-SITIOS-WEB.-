# Notas grupo A1 (en, es, fr, pt, de, pcm, it, nl, ht, af, ca)

## Advertencia principal: nada de este grupo está verificado en la web

- El presupuesto de WebSearch del turno (200 llamadas, compartido entre todos los agentes) estaba agotado cuando intenté la primera búsqueda. Las 5 consultas que lancé devolvieron "web search budget is used up". WebFetch falla por DNS (`getaddrinfo ENOTFOUND`), como avisaba INSTRUCCIONES.md.
- Resultado: **0 búsquedas efectivas**. Todo `part-A1.csv` sale de conocimiento previo, no de evidencia vista en esta sesión.
- Por eso las 11 filas llevan `confianza=baja` y `evidencia_urls` vacío. No inventé URLs. Los términos más dudosos van marcados con `(?)` dentro de cada campo, y cada `nota_localizacion` termina con la marca `[SIN VERIFICAR EN WEB ...]`.
- **No se cumplió el pedido de investigar en profundidad los términos de búsqueda reales de tiendas competidoras.** Lo único que hay son nombres de marcas recordados de memoria (abajo), sin comprobar.
- Siguiente paso recomendado: repetir A1 cuando haya presupuesto de búsqueda (o subir `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) y subir de `baja` a `media`/`alta` solo lo que se confirme con ≥1/≥2 usos reales.

Convención de los campos: en `sinonimos_y_variantes` y `ambiguedades_y_trampas` separé términos con `;` y bloques regionales con ` | ` (etiqueta de región seguida de dos puntos).

## Hipótesis transversales (a confirmar)

**Núcleo léxico probable por idioma** (el que, por conocimiento previo, es casi seguro que domina las tiendas):

| idioma | término principal | oficio |
|---|---|---|
| en | sewing pattern (UK/AU también dressmaking pattern) | pattern making / drafting / cutting |
| es | patrón (ES, MX) / molde (AR, UY, CL) / ambos (CO, PE) | patronaje / moldería |
| fr | patron de couture | modélisme / modéliste |
| pt | molde (BR y PT) | modelagem (BR) |
| de | Schnittmuster (+ "Ebook", "Freebook") | Schnittkonstruktion |
| it | cartamodello | modellistica |
| nl | naaipatroon | patroontekenen |
| af | naaipatroon (pero se busca en inglés) | patroonmaak (?) |
| ca | patró de costura | patronatge |
| ht, pcm | sin término propio verificado | sin término propio verificado |

**Variantes regionales que justifican páginas o textos distintos**
- Español: es-ES "patrón" vs Cono Sur "molde/moldería/molde base" vs MX/CO/PE mixto. Papel: Carta en MX/CO/CL, A4 en ES/AR/PE (?). "Talle" (AR/UY) vs "talla". "Playera/polera/polo/remera/camiseta" para sublimación.
- Inglés: US Letter vs resto A4. "Sloper" (US) = "block" (UK). "Pattern cutting" (UK) vs "pattern making" (US). India y Nigeria buscan "cutting and stitching" / "styles", no "sewing pattern".
- Portugués: "baixar" (BR) vs "descarregar" (PT); "camisola" cambia de sentido; BR tiene un mercado de moldes para sublimación con archivos CorelDRAW (.cdr) que conviene confirmar (?).
- Francés: Québec usa papel Letter; África francófona dice "modèle" y "coupe et couture" más que "patron".
- Alemán: ß vs ss en Suiza; "Ebook" es nombre de producto; tallas infantiles por altura (92-164); "Nahtzugabe" y "Beamer" son atributos de producto.
- Neerlandés: NL vs BE casi idénticos; BE tiene un término propio "coupe" (?).

**Qué idioma sirve a quién**
- `pcm` (pidgin): las búsquedas son en inglés de Nigeria (en-NG). Servir con en-NG; "style/styles" es la intención del cliente final, y el comprador real de moldes es el tailor o diseñador.
- `ht` (criollo): las búsquedas escritas van en francés e inglés (diáspora). Servir con fr/en; ht solo como capa de apoyo. No tengo ninguna forma criolla verificada para "molde"; "patwon" y "modèl" son hipótesis.
- `af` (afrikáans): la mayoría de búsquedas sudafricanas serán en inglés (en-ZA). Afrikáans como capa secundaria.
- `ca` (catalán): muchos usuarios buscan en castellano; ca funciona como segunda capa sobre es-ES.

## Riesgos de traducción y trampas semánticas (alta prioridad)

1. **"Plantilla/template/Vorlage/gabarit/sjabloon" para sublimación** suele significar diseño gráfico para tazas o tumblers, no molde de prenda. Para prendas usar "camisetas/jersey sublimado", "full print", "Trikot", "maillot sublimé", etc.
2. **"Pattern/patrón/patron/Muster/patroon" = estampado o motivo** en diseño gráfico y sublimación ("seamless pattern", "patrón sin costuras"). Conviene que el contenido sobre sublimación aclare "molde de prenda" frente a "estampado continuo".
3. **"Molde/mold/moule/mal/stampo/Form" = recipiente** (repostería, resina). En España "moldes" devuelve repostería.
4. **"Patron/patrón/patró/patroon/patwon" = jefe** o patrón de barco, y en francés/inglés también patrón de tejido ("patron de tricot", "knitting pattern"). Calificar siempre con costura.
5. **"Naaien" (nl) y "naai" (af) tienen acepción vulgar.** Anclar con "naaipatroon", "kleding", "naaimachine"; ojo con anuncios y SafeSearch.
6. **"Tallista" (es)** es tallador de madera, no graduador de tallas. No usarlo como término de oficio. En francés "patronage" no es patronaje.
7. **Ortografía y escritura:** Suiza sin ß; "e-book/ebook/eBook"; "t-shirt/tee-shirt/tshirt"; criollo "kreyòl" vs "kreyol" (teclados sin ò).

## Oportunidades de nicho (hipótesis)

- Proyector ("pattern projector", "Beamer", "proyector de patrones", "projecteur"), A0/plotter y capas son atributos de búsqueda reales entre costureras indie (al menos en en/de/fr/es; sin verificar volumen).
- Editable/CAD (DXF, AAMA, vectorial, Illustrator/CorelDRAW) y sublimación deportiva (camisetas de fútbol, ciclismo, rugby en Sudáfrica) parecen menos competidos que el PDF de costura casera.
- India y Nigeria: segmento profesional (tailors y boutiques) más que costura doméstica; pagos locales y datos limitados condicionan el formato (PDF ligeros).

## Competidores y fuentes recordados de memoria (no verificados en esta sesión)

- Inglés: Etsy; Burda Style; Simplicity/McCall's/Butterick/Vogue (Big 4); Closet Core, Cashmerette, Tilly and the Buttons, Seamwork, Named, Papercut, Style Arc, Jalie, Makerist, PatternReview.
- Alemán: Makerist, Farbenmix, Lillesol & Pelle, pattydoo, Studio Schnittreif, Burda, Ottobre.
- Neerlandés: Knipmode, La Maison Victor, Fibre Mood (revistas).
- Portugués BR: Mercado Livre, Elo7, Hotmart (canales de venta de moldes digitales y cursos).
- Español: Mercado Libre, Tiendanube, Etsy; revista Patrones y Burda en España.
- Para es/fr/it/ca/pt/af/ht/pcm no tengo nombres de tiendas lo bastante seguros para citar.

## Lo que NO pude verificar (todo, en la práctica)

Cualquier término de las 11 filas; en particular los marcados `(?)`. Los más inciertos: criollo haitiano (todo), afrikáans (patroonmaak, snypatroon, kleremaakpatroon, snyer), pidgin nigeriano (sin forma pidgin propia), "coupe" en flamenco, "modelação" (PT), "gradeamento" (BR), "trazo" (CO), "moldería" en Perú, hábitos de pago locales, tallas por país, y la existencia/volumen de búsqueda de "moldes CDR" para sublimación en Brasil.
