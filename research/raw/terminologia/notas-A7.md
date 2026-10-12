# Notas grupo A7 (ruso, ucraniano, polaco, rumano, húngaro, griego, checo, serbio, croata, búlgaro, eslovaco, esloveno, lituano, letón, estonio)

Fecha de trabajo: 2026-10-12.

## 0. Límite de verificación (leer primero)
- Solo pude ejecutar **4 búsquedas web** (ru, uk, pl, ro). La quinta (húngaro) y todas las siguientes fueron rechazadas: **el presupuesto de WebSearch del turno (200, compartido entre todos los agentes) estaba agotado**. WebFetch no funciona en este entorno. No usé curl ni terceros para saltear el límite.
- Las 4 búsquedas devolvieron sobre todo tiendas en inglés/español (Etsy, Gumroad, blogs genéricos). **No obtuve ninguna tienda, editorial ni marketplace nativo** (Allegro, eMAG, Skroutz, Seznam, Yandex, Ozon, Wildberries, VK, Dzen, Avito, Telegram) con el término buscado.
- Lo que sí se vio de verdad:
  - **ru:** un resultado `qna.habr.com` titulado "Для электронных товаров (выкройки)" (uso real de "выкройки" para productos digitales), y un snippet con "цифровые лекала" y precios de una vendedora (900 RUB por 3 tallas, 1700 RUB por 14 tallas). El snippet menciona también BurdaStyle y Бюро «Миллиметр» como fuentes de выкройки gratuitas; no confirmé la URL exacta de cada mención.
  - **pl:** PDFs gratuitos de un sitio personal con "wykrój" y "szablon-PL" (ropa de muñecas, instrucción "faktyczny rozmiar", "podziałka 1 cm"), y un listado de Etsy con interfaz polaca (17,18 zł, A4+A0, margen 1 cm, sin devoluciones en digitales). Ese snippet describió el producto como "wzór", no "wykrój".
  - **uk y ro:** nada nativo. Ni un solo uso real verificado.
- **Resultado en confianza: 0 alta, 2 media (ru, pl), 13 baja.** Todo lo demás (términos de 13 idiomas, plataformas, pagos, tallas, sanciones) viene de conocimiento de fondo y está marcado "sin verificar" en el CSV. Los términos listados por la asignación (p. ej. "выкройки для печати", "střihy PDF", "tipar de rochie", "iškarpos", "piegriezumi", "õmblusmustrid") los volqué tal cual cuando eran plausibles; no son evidencia propia.
- Dónde dudo más: búlgaro (la asignación sugiere "кройка/кройки"; creo que para "patrón" la palabra más específica es **изкройка/изкройки**, y "кройка" es sobre todo "corte" y "кройка и шиене"), esloveno ("krojni list" vs "krojna pola"), letón ("piegriezumi" también puede ser "corte/ajuste"), estonio ("lõiked" vs "lõikemustrid/lõikemuster"), serbio ("šnit mustra").

## 1. Hallazgos transversales (conocimiento de fondo, sin verificar)
- **Influencia de Burda y del alemán.** Burda Moden (con edición rusa desde la era soviética) puso en Europa del Este el modelo "revista + pliego de patrones": en ruso "Бурда" casi equivale a "revista de выкройки"; los términos para el pliego (cs "střihový arch", sr/hr "krojna lista", sl "krojna pola"?, hu "szabásmintalap") vienen de ahí. Muchos términos son **calcos del alemán Schnittmuster/Schnitt**: hu *szabásminta* (szabás+minta), et *lõikemuster*, cs/sk *střih/strih* (Schnitt), sr/hr/sl *šnit/mustra* (germanismos coloquiales). En cambio ru *выкройка*, pl *wykrój* y uk *викрійка* son derivados eslavos de "cortar". Ver la marca Burda en el término es una señal SEO útil ("Burda" + término local).
- **Familias léxicas:** (1) *-krój/-kroj/-крой* (ru, uk, pl, bg, sr, hr, sl, además "krojna lista"); (2) *střih/strih* (cs, sk); (3) *tipar* (ro); (4) *szabásminta* (hu); (5) *πατρόν* (el, del francés *patron*); (6) bálticos con términos distintos entre sí (lt *iškarpos/lekalai*, lv *piegriezumi/šabloni*, et *lõiked/lõikemustrid*). No existe un término común: **no sirve traducir uno a otro**.
- **Calco ruso "лекала".** Se usa en ru, y por herencia en uk (producción, sublimación) y en lt (*lekalai*) y lv (*lekalas*, sin verificar). En ru "лекало" es además la plantilla/curva francesa, y Lekala es una marca de patrones por medidas.
- **Anglicismos:** bajos/medios en ru-pl-cs-hu (domina el término nativo), medios-altos en balcánicos, bálticos y rumano, altos en estonio (población chica, poco contenido local). Etsy es el vector principal del inglés "sewing pattern"/"PDF pattern".
- **Trampas semánticas principales:** cs/sk *střih/strih* = corte de pelo/montaje; ro *tipar* = impresión/imprenta (y "tipar sublimare" significa imprimir por sublimación); pl *wykrój* = recorte troquelado y *wzór* = diseño; sl/hr *kroj* = además traje folclórico; lt *iškarpa* = recorte; lt *siuvinėjimas* = bordado; hu *minta* = muestra/estampado; ru *паттерн* = estampado.
- **Diacríticos:** en todos los idiomas con latín extendido la gente busca también sin diacríticos (wykroj, strih, szabasminta, sivenje). Conviene cubrir ambas formas en títulos y URLs.
- **Escritura serbia.** Servir latín y cirílico. Sospecho (sin verificar) que el comercio online es mayormente latino. Evitar duplicar contenido: usar una sola fuente y transliterar automáticamente.

## 2. Qué idiomas conviene servir con otro / cruces
- **sr / hr:** vocabulario casi idéntico (*kroj, krojna lista, šivanje, krojač*); diferencia ekavski/ijekavski (odeća/odjeća), tisak/štampa, ispis/štampanje, y moneda/pagos. No fusionar en una sola página, pero se puede compartir base léxica. Bosnio y montenegrino (fuera de este grupo) sirven con hr/sr.
- **cs / sk:** casi misma palabra con distinta ortografía; público eslovaco consume contenido en checo. Páginas separadas con hreflang, pero ojo con canibalización.
- **ru como lengua puente:** audiencias rusohablantes en Ucrania, Bielorrusia, Kazajistán, Letonia (~⅓), Estonia (~¼) y Lituania. En Letonia y Estonia vale la pena evaluar páginas en ruso aparte del lv/et.
- **uk vs ru:** NO ofrecer ruso por defecto a usuarios de Ucrania; mantener ucraniano propio (hay búsqueda residual en ruso). Evitar "лекала" en el contenido principal uk salvo como variante.
- **Oportunidades de nicho (no verificadas):** sublimación para ropa deportiva (ru "велоформа/хоккейная форма", pl/cs/sk/hu "dresy", "sublimace/sublimácia/sublimacja"), con plantillas editables DXF/AAMA y A0 para plotter; y "tallas por medidas" al estilo Lekala en ru.
- **Mercados con menos competencia local en digitales (hipótesis):** Rumania, Bulgaria, Grecia, bálticos, Eslovenia. Probable demanda vía Etsy/Facebook con términos en inglés; verificar.

## 3. Buscadores y plataformas (todo sin verificar en esta sesión)
- **Rusia:** Yandex (dominante) + Google; VK, Dzen, Telegram, Rutube/VK Video; Ozon, Wildberries, Yandex Market, Avito, Livemaster. IA: Alisa/YandexGPT, GigaChat. Instagram/Facebook bloqueados desde 2022 (VPN).
- **Chequia:** Seznam.cz + Google; Fler.cz (handmade), Heureka, Zboží.cz, Aukro. **Polonia:** Allegro, Allegro Lokalnie, OLX. **Rumania:** eMAG, OLX.ro. **Grecia:** Skroutz, Public. **Eslovaquia:** Heureka.sk, Bazoš. **Croacia:** Njuškalo. **Serbia:** Kupindo, Limundo. **Bulgaria:** OLX.bg, Bazar.bg. **Letonia:** SS.lv. **Lituania:** Vinted, Skelbiu. **Eslovenia:** Bolha. **Estonia:** Osta.ee. En todos, Google domina fuera de Rusia/Chequia; Etsy y Facebook (grupos de costura) son canal común. No verifiqué que ningún marketplace local admita bien productos digitales tipo patrón PDF: en Allegro, eMAG y Skroutz es una pregunta abierta.

## 4. Rusia y Bielorrusia: sanciones y pagos (qué verifiqué: NADA)
No pude buscar sobre sanciones ni pagos (presupuesto de búsqueda agotado). Lo siguiente es lo que recuerdo; **no usar como asesoría y no tomarlo como verificado**:
- Visa y Mastercard suspendieron operaciones en Rusia en 2022: las tarjetas emitidas en Rusia no funcionan en comercios extranjeros; PayPal y Stripe no sirven a Rusia. Las vías locales son Mir, SBP (СБП), YooKassa, Robokassa, T-Bank, CloudPayments, Prodamus, Boosty; para cobrarlas normalmente hace falta una entidad o intermediario ruso.
- Marketplaces y plataformas occidentales (Etsy, etc.) restringieron o cortaron operaciones con Rusia/Bielorrusia (no verifiqué el estado exacto de Etsy hoy).
- Paquetes de sanciones UE/EE. UU./Reino Unido, desconexión SWIFT de bancos, y obligaciones de IVA/ley rusa para servicios electrónicos extranjeros B2C (registro del vendedor extranjero; tasa 20% hasta 2025, 22% desde 2026 según recuerdo). Bielorrusia sufre sanciones similares, y allí se compra en ruso (Kufar, 21vek, Onliner, Wildberries; Instagram sí funciona).
- Riesgo adicional: bloqueos de Roskomnadzor, restricciones de publicidad en plataformas extranjeras, y la sensibilidad de vender con pago ruso desde una entidad de la UE.
- **Recomendación:** antes de dirigir ventas/publicidad a RU/BY, confirmar con asesoría legal y de pagos (cumplimiento de sanciones del país de la empresa, pasarela, IVA). Para SEO/AEO, el contenido en ruso sigue sirviendo a ru-hablantes de otros países sin necesidad de vender en Rusia.

## 5. Pendiente de verificar (siguiente ronda de búsquedas)
- Por idioma, buscar el término nativo + "PDF" + "купить/kupić/cumpără/vásárol/αγορά/koupit/kupiti/pirkti/pirkt/osta" y revisar tiendas locales: Vikisews, Lekala, Grasser, Burda ru; Allegro/Etsy PL; eMAG/Etsy RO; Fler.cz/Etsy CZ; Skroutz/Etsy GR; Etsy HU/LT/LV/EE.
- Confirmar bg *изкройка* vs *кройка*; sl *krojni list* vs *krojna pola*; lv *piegriezumi*; et *lõiked/lõikemuster*; sr *šnit mustra*.
- Sublimación: confirmar uso real de "лекала/макеты для сублимации", "wykroje do sublimacji", "střihy pro sublimaci", "sublimation" en Greek.
- Estado actual de Etsy y de pagos con Rusia/Bielorrusia; cuota real de Seznam.cz en 2026; cuota de Yandex en RU.
