# T7 — Pagos, impuestos, legal, entrega y confianza para vender moldes digitales a ~100 mercados desde Argentina

Fecha de la investigación: 12 de octubre de 2026. Alcance: lo que decide si el tráfico SEO/AEO de moldey.com se convierte en ventas cobrables, legales y entregables.

> **Aviso: esto NO es asesoramiento legal ni fiscal.** Es un mapa de investigación. Todo lo que toque impuestos, cambio/divisas, monotributo, sociedades, privacidad y propiedad intelectual debe validarlo un contador y un abogado (lista concreta al final, sección 10).

## 0. Límites de esta investigación (leer primero)

- Hice 34 búsquedas efectivas. Luego la herramienta alcanzó su tope de búsquedas por turno (200, compartido entre agentes) y **no pude hacer las búsquedas restantes** sobre: métodos de pago locales por región y cuáles soporta cada MoR, legal/privacidad (GDPR, EAA, LGPD, PIPL, DPDP), DMCA/OFAC, entrega técnica de archivos y señales de confianza.
- Esas secciones están escritas con **conocimiento previo del modelo** y llevan la etiqueta **[NO VERIFICADO·previo]**: sin URL, sin fecha, hay que confirmarlas. No son "hechos de esta sesión".
- Etiquetas: **[HECHO]** = fuente primaria/oficial vista en los resultados; **[EVIDENCIA]** = dato de terceros con metodología; **[OPINIÓN]** = consejo de industria o inferencia mía; **[NO VERIFICADO]** = sin respaldo, contradictorio o solo de una fuente débil.
- **Sesgo de fuentes:** la mayoría de las comparativas de MoR y guías de impuestos vienen de empresas que compiten entre sí (Dodo Payments, Fungies, PayNow, Kintsugi, Fonoa, Avalara, etc.). Sirven para orientarse, no para decidir. Casi ningún resultado mostró fecha de publicación; indico la fecha solo cuando apareció. Referencias [S#]/[T#] en la sección 11.

## 1. Resumen ejecutivo (los 8 puntos que importan)

1. **Para vender B2C global de PDFs desde Argentina, un Merchant of Record (MoR) es casi obligatorio en la práctica.** Sin MoR el vendedor es responsable de IVA/GST en decenas de jurisdicciones; varias exigen registro desde la primera venta, sin umbral: UE (OSS no-Unión), Reino Unido, India, Turquía, Corea, Arabia Saudita y Brasil, entre otras (sección 4). [EVIDENCIA, fuentes de terceros]
2. **Stripe directo NO es una opción simple para una cuenta de comerciante argentina.** Fuentes de terceros listan ~46 países soportados y Argentina no figura como país de comerciante; las vías descritas son abrir una sociedad en EE. UU. o Reino Unido (con implicancias fiscales en Argentina). Pero Stripe Connect sí paga a Argentina: Polar, que paga con Stripe Connect Express, lista a Argentina en su documentación oficial. [HECHO para Polar; EVIDENCIA para Stripe]
3. **Candidatos MoR con Argentina plausible:** Polar (Argentina en la lista oficial de payouts), Lemon Squeezy (Argentina en la lista de payouts bancarios en un snapshot viejo; PayPal a 200+ países; pagos siempre en USD), Gumroad (MoR desde 1-ene-2025; comisión alta). Paddle y Creem: **no pude confirmar Argentina**. Verificar cada una en su página oficial antes de abrir cuenta.
4. **El costo fijo por transacción pesa mucho en tickets de USD 5-12.** Con "5% + 0,50" una venta de USD 6 pierde ~13%; de USD 20, ~7,5% (cálculo propio, sección 3.2). Conviene diseñar packs/bundles y un precio mínimo.
5. **Los métodos locales mueven conversión, pero no se integran uno por uno:** Pix fue 42% del valor del e-commerce brasileño en 2025; Alipay+WeChat Pay 89% en China; UPI domina India. [EVIDENCIA, Worldpay GPR 2026 vía prensa] La estrategia práctica es heredar los métodos de tu MoR/PSP y priorizar por tráfico real.
6. **Cobrar en Argentina:** PayPal convierte a pesos con spread propio (fuentes: 3%-4,5% sobre referencia); Payoneer a cuenta bancaria en USD cuesta "hasta 2%" según su propia página; el régimen cambiario cambió en 2025 y las condiciones para personas humanas vs. jurídicas difieren. Todo esto cambia rápido y debe validarlo un contador.
7. **Piratería y entrega:** enlaces firmados con caducidad, límite de descargas y marca de agua con datos del comprador funcionan mejor que el "bloqueo" de PDF, que es débil. [OPINIÓN / NO VERIFICADO·previo]
8. **Rusia y países sancionados:** no cobrar. Polar bloquea Cuba, Rusia, Irán, Corea del Norte y Siria; Paddle bloquea por sanciones y declara restricciones regionales (Ucrania). [HECHO, docs oficiales]

## 2. Pagos

### 2.1 Qué dicen los datos (con fuente)

| Dato | Fuente |
|---|---|
| Billeteras digitales: ~56% del valor del e-commerce global en 2025 y 33% en punto de venta (Worldpay Global Payments Report, 11ª edición, publicada 31-mar-2026; 42 mercados). EE. UU.: 39% e-commerce. | [S37] [EVIDENCIA, resumen de prensa 1-abr-2026] |
| China: Alipay + WeChat Pay = 89% del e-commerce. India: ecosistema UPI/billeteras = 68% online. | [S37] [EVIDENCIA] |
| Brasil: Pix = 42% del valor del e-commerce en 2025 (34% en POS); tarjeta de crédito sigue fuerte por cuotas; billeteras solo 10% en Brasil. | [S36] [EVIDENCIA] |
| Proyecciones anteriores (Ebanx: Pix 40% en 2026; Worldpay 2023: 35%) quedaron superadas por los datos reales. Las fuentes miden cosas distintas (valor vs. cantidad de compras) y no son comparables entre sí. | [S36] contradicción metodológica |

### 2.2 Métodos por región y prioridad para moldey (conocimiento previo, [NO VERIFICADO·previo] salvo cifras de 2.1)

| Región | Métodos relevantes | Notas de conversión | Prioridad |
|---|---|---|---|
| Global | Visa/Mastercard/Amex, Apple Pay, Google Pay, PayPal | Base mínima. Wallets son mayoría del valor global [S37]. | Imprescindible |
| Brasil | Pix, tarjeta con cuotas (parcelamento), Boleto | Pix es ya casi la mitad del e-commerce [S36]. Sin Pix se pierde mucho en PT-BR. Requiere procesador local (dLocal/Ebanx/Astropay u otro) o MoR que lo incluya. | Alta si PT-BR rinde |
| México | Tarjetas, OXXO (voucher en efectivo), SPEI, Mercado Pago | Efectivo y transferencia siguen importando. | Media |
| Argentina (venta local) | Mercado Pago, tarjetas con cuotas, transferencia/CVU, Rapipago/Pago Fácil | Mercado Pago cobra ~2,99% + IVA según una guía de pasarelas [S4]. | Media (venta doméstica) |
| Colombia/Chile/Perú | PSE, Nequi (CO); Webpay/Khipu (CL); Yape/PagoEfectivo (PE) | Dependen de agregador. | Baja-Media |
| Europa | iDEAL (NL), Bancontact (BE), BLIK y Przelewy24 (PL), Klarna (DACH/Nordics), Swish/Vipps/MobilePay, SEPA, Wero (EPI) | Giropay fue discontinuado y Wero está absorbiendo iDEAL/Bancontact/Giropay de forma gradual: **estado exacto a oct-2026 no verificado**. | Media-Alta por mercado |
| India | UPI (68% online [S37]), Razorpay como pasarela, Paytm | Tarjetas emitidas en India suelen tener restricciones para comercios extranjeros; precio muy sensible. | Media (con PPP) |
| China | Alipay, WeChat Pay (89% [S37]) | Sin ellos, casi no hay conversión; además ICP/GFW (sección 5). | Baja hasta tener evidencia |
| Japón | Tarjetas (JCB), konbini (pago en tienda), PayPay, Rakuten Pay | Konbini es lento (pago diferido); entrega inmediata es la clave. | Media |
| Corea | KakaoPay, Naver Pay, Toss, tarjetas locales | Tarjetas extranjeras a veces fallan en comercios locales. | Media-Baja |
| Sudeste Asiático | Indonesia: QRIS, GoPay, OVO, DANA, ShopeePay, transferencia virtual; Filipinas: GCash, Maya; Vietnam: MoMo; Malasia: FPX | Las billeteras dominan; tarjetas minoritarias. | Media-Baja |
| Golfo | mada (débito KSA), STC Pay, Apple Pay, BNPL Tabby/Tamara | Poder adquisitivo alto; BNPL ayuda en tickets altos, menos en PDFs baratos. | Media |
| África | M-Pesa (Kenia), Flutterwave/Paystack (Nigeria/Ghana) | Tarjetas internacionales limitadas; muchas filiales de MoR no cubren. | Baja |
| Rusia | Mir, YooMoney | Visa/Mastercard suspendieron operaciones en Rusia en 2022; rieles bloqueados por sanciones. **No vender.** | No |
| Cripto | Stablecoins (USDC) | Stripe reporta aceptación de stablecoins en 70+ países, sin que Argentina figure en lo visto [S38]. Impacto en conversión de moldes: marginal. | Baja |

**Conclusión práctica [OPINIÓN]:** moldey no debe integrar 30 métodos. Debe (a) elegir un MoR/PSP cuyo checkout incluya tarjetas+wallets+PayPal y los métodos europeos principales, (b) agregar Pix/UPI/QRIS solo cuando un país muestre tráfico y compras, y (c) verificar en la página oficial de cada MoR qué métodos activa por país. Lemon Squeezy tiene una página de "Payment Methods" (docs.lemonsqueezy.com/help/checkout/payment-methods) que apareció en los resultados pero **no pude leer su contenido**; idem para Paddle.

### 2.3 Argentina como país del comerciante: limitaciones reales

| Opción | Qué dicen las fuentes | Etiqueta |
|---|---|---|
| **Stripe directo** | ~46 países soportados en listas de terceros (2026); Argentina no figura como país de comerciante. Una guía 2026 dice que en Argentina Stripe no opera directamente (vía dLocal/partners). Vías descritas: sociedad (LLC en EE. UU. con cuenta bancaria local de EE. UU., o empresa en Reino Unido). Un agregador poco confiable menciona Stripe Atlas por ARS 435.000 (no confiable). Mercor y Bandcamp listan Argentina, pero en contexto de payouts/cuentas de pago, no de comerciante. | [EVIDENCIA débil] [S1][S2][S3][S4][S5][S6] |
| **Stripe Connect (payouts)** | Polar paga con Stripe Connect Express y lista Argentina y Chile como países de payout. Esto reconcilia la contradicción: Argentina es destino de payout, no país de comerciante directo. (Inferencia mía.) | [HECHO] Polar; inferencia [OPINIÓN] [S15] |
| **PayPal** | Retiro a banco argentino posible; se convierte automáticamente a pesos con tipo de cambio de PayPal (3%-4,5% sobre la tasa de referencia según una fuente), demora 3-5 días hábiles (iProfesional, 19-jun-2026). Cifras de comisión inconsistentes: "sin comisión fija" vs. "USD 10 + IVA por retiro" (guía vieja de Global66) vs. "pérdida total 8-15%" (blog comercial). No hay consenso sobre dólares sin convertir. | [EVIDENCIA débil, contradictoria] [S30][S31] |
| **Payoneer** | Retiro de USD a cuentas argentinas "hasta 2%" según Payoneer; tarjeta hasta 3,5%; acreditación mismo día a ~2 días; el banco receptor puede pedir documentación; hay costo adicional por tipo de cambio. | [HECHO para la tarifa publicada] [S32][S33][S34] |
| **Mercado Pago** | Útil para ventas a clientes en Argentina/LatAm (2,99% + IVA; acreditación inmediata en cuenta o hasta 10 días hábiles al retirar [S4]). **No recibe transferencias SWIFT directas** del exterior (blog 2026) [S35]. No sirve como cobrador global. | [EVIDENCIA] |
| **Agregadores LatAm** | dLocal, Kushki y Astropay permiten cobrar a clientes del exterior con liquidación en USD/EUR [S4]. No verifiqué requisitos para vendedores argentinos ni costos. | [NO VERIFICADO] |

**Régimen cambiario y fiscal (solo panorama; consultar contador):**

- Fuentes 2026 describen la salida progresiva del "cepo" desde abril de 2025 [S28]. Una fuente (calculadora, baja confiabilidad) cita la Comunicación A 8330 (BCRA, septiembre 2025) que eliminó el tope de USD 36.000/año y la obligación de convertir a pesos para personas humanas; personas jurídicas (SAS/SRL/SA) seguirían liquidando al tipo oficial [S29]. Global66 (2026) indica que esa excepción aplica cuando los fondos se acreditan en cuenta en moneda extranjera de una entidad financiera local, y que muchas fintechs/billeteras no lo son [S27]. **Hay discrepancias de plazo de liquidación entre fuentes (20 días hábiles vs. 30 días corridos vs. 5 días en notas viejas).** [NO VERIFICADO, contradictorio]
- Contablix (2026) afirma que la factura E (IVA 0%) usa el tipo de cambio BNA vendedor y que las exportaciones con factura E no suman al tope del monotributo, y que ARCA reforzó cruces entre comprobantes y liquidaciones de divisas [S26]. **Esa afirmación sobre el tope del monotributo proviene de una sola fuente y puede ser incorrecta: validar.** [NO VERIFICADO]
- Existe cobertura periodística de un "nuevo régimen" para freelancers monotributistas (iProUP) que no pude leer en detalle [NO VERIFICADO].
- **Pregunta clave para el contador con un MoR:** el MoR es quien compra/licencia al cliente final; el vendedor argentino le factura al MoR (entidad extranjera). ¿Cómo se emite el comprobante (factura E), a quién, con qué concepto (exportación de servicios/licencias), y cómo se liquida el cobro (cuenta, plazo)? [OPINIÓN: pregunta, no respuesta]

### 2.4 Moneda local, precios psicológicos y PPP

- **Moneda local:** mostrar el precio en la moneda del visitante reduce fricción y cargos de conversión del banco emisor del comprador. [OPINIÓN / NO VERIFICADO·previo] Lemon Squeezy publica una página de monedas (incluye ARS como moneda de venta) y un anuncio de soporte de moneda en 95 países [S8]; Paddle se describe con 29+ monedas (tercero) [S12 y afines]. El pago al vendedor es en USD en Lemon Squeezy ("Payouts are always made in USD") [S7/S8].
- **Impuesto incluido:** en UE/UK/Australia el consumidor espera ver el precio con IVA/GST incluido; en EE. UU./Canadá se suma al final. Un MoR lo resuelve en el checkout, pero el precio publicado en la página debe ser coherente. [NO VERIFICADO·previo]
- **Precios psicológicos:** terminaciones locales (.99/.90 en Europa/EE. UU., números redondos en Japón/Corea, precios enteros en monedas de baja denominación como INR o IDR). [OPINIÓN]
- **PPP (precio por poder adquisitivo):**
  - Pros: mejora conversión en India, Sudeste Asiático, África, parte de LatAm. En moldes baratos el riesgo económico es bajo. [OPINIÓN]
  - Contras/riesgos: arbitraje por VPN o tarjeta de otro país; percepción de injusticia; complejidad contable y de soporte; y dentro de la UE, el Reglamento de geobloqueo (2018/302) puede limitar discriminar por residencia: consultar abogado. [NO VERIFICADO·previo]
  - Mitigación: exigir coincidencia entre país de facturación/emisor de la tarjeta y la región de precio; empezar con 3 tiers y probar A/B antes de extender. [OPINIÓN]
  - No encontré evidencia independiente sobre magnitud de mejora de conversión por PPP: **tratarlo como hipótesis a testear.**

## 3. Merchant of Record y plataformas

### 3.1 Panorama (qué dice cada fuente)

| Plataforma | Rol fiscal | Comisión publicada | Argentina como vendedor | Observaciones y fuentes |
|---|---|---|---|---|
| **Lemon Squeezy** (Stripe) | MoR: calcula, cobra y remite impuestos globales | 5% + 0,50 (reseña 2026 de Dodo, competidor) [S10] | En el snapshot de la página oficial (muy antiguo, ~1.935 días) Argentina está en la lista de payouts bancarios; home actual dice "bank payouts globally"; PayPal payout a 200+ países; payouts siempre en USD [S7][S9] | Stripe lo adquirió en 2024: una fuente dice julio de 2024, otra abril de 2024 [S10][S11] (contradicción de fecha, irrelevante para operar). Futuro del producto bajo Stripe: no verificado. |
| **Paddle** | MoR | 5% + 0,50 (varias reseñas de competidores, 2026); custom para tickets < USD 10 (según un tercero); FX/payout aparte [S12] | **No confirmado.** Docs: vende bienes digitales en 200+ países; hay países bloqueados por sanciones; a junio-2026 la única restricción regional es Ucrania [S13][S14]. Tabla de países de payout inaccesible en mis resultados. | Históricamente orientado a software/SaaS: **confirmar que acepta moldes PDF** [NO VERIFICADO·previo]. Payout según cuenta bancaria; liquidación 1-7 días hábiles (tercero). |
| **Polar** | MoR (Stripe Connect Express para payouts) | Terceros: 4% + 0,40; otra reseña (Dodo) titula "nuevo 5% + 50c con planes escalonados" [S18]: **contradictorio; ver polar.sh/pricing** | **Sí en lista oficial: Argentina y Chile**; Brasil y México no pude verlos [S15][S16] | Cobra desde cualquier país excepto Cuba, Rusia, Irán, Corea del Norte y Siria [S15]. Conversión de payout entre divisas 0,25% (UE) hasta 1% fuera [S15/S17]. Orientado a desarrolladores: probar adecuación a un catálogo de PDFs. |
| **Gumroad** | MoR desde 1-ene-2025 ("Gumroad handles ALL your tax obligations") [S19] | 10% + 0,50 en ventas directas; 30% en ventas vía Discover [S19]; procesamiento: una fuente lo suma aparte (~12,9% + 0,80 total en venta directa en EE. UU.), otra lo incluye en Discover [S20] (contradicción) | No verifiqué payouts a Argentina | Sencillo para creadores; comisión alta para tickets bajos. Útil como canal secundario/descubrimiento. |
| **Payhip** | **MoR parcial**: IVA UE/UK sí; ventas de EE. UU., Canadá y Australia siguen siendo del vendedor; chargebacks por tu Stripe/PayPal | Plan gratis 5%; Plus USD 29/mes 2%; Pro USD 99/mes 0% (julio 2026) [S21][S22] | No verifiqué | Las fuentes contradicen si remite el IVA UE o solo lo calcula [S21][S22]: **verificar en la documentación de Payhip**. Depende de Stripe/PayPal propios (Stripe no sirve en AR directo). |
| **Creem** | MoR | Ejemplo oficial = 3,9% + 0,40; payout 7 EUR/USD o 1% (lo mayor) [S24] | Payouts a 86 países por transferencia local; **Argentina no confirmada**; mínimo USD/EUR 50; pagos días 1 y 15; sin PayPal; Alipay para China; USDC en Polygon [S23][S24][S25] | Las dos páginas oficiales listan países distintos [S23][S25]. |
| **FastSpring, Digistore24, Hotmart, Kiwify, Shopify, WooCommerce** | FastSpring: MoR; Digistore24: marketplace/reseller de la UE; Hotmart/Kiwify: plataformas brasileñas con MoR; Shopify/WooCommerce: vos sos el vendedor | No investigado | No investigado | [NO VERIFICADO·previo]. Hotmart/Kiwify están orientadas a infoproductos en BR con liquidación en BRL: poco adecuadas para moldes globales. Shopify Payments no opera en Argentina (entiendo); Shopify/Woo sin MoR dejan el IVA internacional en tu cabeza. |

### 3.2 Impacto de la comisión fija en tickets chicos (cálculo propio con tarifas publicadas por terceros; verificar)

| Precio | 5% + 0,50 (LS/Paddle) | 4% + 0,40 (Polar, no confirmado) | 3,9% + 0,40 (Creem, ejemplo oficial) | 10% + 0,50 (Gumroad, sin procesamiento) |
|---|---|---|---|---|
| USD 6 | USD 0,80 = 13,3% | 0,64 = 10,7% | 0,63 = 10,6% | 1,10 = 18,3% |
| USD 10 | 1,00 = 10,0% | 0,80 = 8,0% | 0,79 = 7,9% | 1,50 = 15,0% |
| USD 20 | 1,50 = 7,5% | 1,20 = 6,0% | 1,18 = 5,9% | 2,50 = 12,5% |

Lectura [OPINIÓN]: a USD 6, 13% de comisión dejan poco margen tras impuestos, retiro y conversión. Armar **packs (por ejemplo 3-5 moldes), colecciones por tamaño y un precio mínimo de USD 8-10** mejora el margen sin tocar el conversion rate unitario.

### 3.3 Qué resuelve el MoR y qué queda del lado del vendedor

- **Resuelve** (según descripciones de las plataformas y reseñas de terceros): cálculo, cobro y remisión de IVA/GST/sales tax, facturación al consumidor, gestión de reembolsos y chargebacks, adaptación del checkout (moneda, impuestos incluidos), y reducción del riesgo de registros en decenas de países. Gumroad documenta que desde 2025 asume todas las obligaciones fiscales [S19]; Lemon Squeezy y Paddle se presentan como MoR completos.
- **No resuelve (queda en el vendedor):** impuesto a las ganancias y obligaciones en Argentina (monotributo/inscripción, facturación), cómo declarar el cobro, régimen cambiario, validación de que tu producto cumple la política de contenido del MoR, propiedad intelectual de tus moldes, privacidad de tu propio sitio y newsletter (el MoR es responsable de los datos de pago, no de tu analítica), accesibilidad de tu sitio, y soporte al cliente.
- **Trampa de percepción:** en el resumen de la tarjeta puede aparecer el nombre del MoR (no "moldey") y generar contracargos por desconocimiento. Mitigar con email de confirmación claro y descriptor reconocible si la plataforma lo permite. [OPINIÓN]

### 3.4 Recomendación tentativa de plataforma [OPINIÓN]

1. **Verificar hoy, en las páginas oficiales,** Argentina como país de payout y la aceptación de "sewing patterns / PDF templates" en: Polar, Lemon Squeezy, Paddle, Creem.
2. Si Argentina figura en Polar o Lemon Squeezy y el catálogo es aceptado: usar **uno** como checkout principal con descargas y emails de entrega nativos; dejar Gumroad como canal secundario de descubrimiento si la comisión lo justifica.
3. No abrir una sociedad en EE. UU./UK solo para Stripe sin contador (implicancias fiscales en Argentina).
4. Mantener **Mercado Pago** como opción separada para clientes de Argentina (en pesos), con asesoramiento contable sobre IVA y facturación local.

## 4. Impuestos al consumo de bienes digitales (B2C)

Todos los datos de esta tabla provienen de guías de terceros (consultoras fiscales y software de compliance), no de las autoridades, salvo donde indico "fuente oficial". **Con un MoR, esto lo gestiona la plataforma;** esta tabla sirve para entender qué está resolviendo y por qué no conviene vender directo.

| Jurisdicción | Regla para vendedor extranjero B2C de descargas digitales | Umbral / tasa / mecanismo | Confianza y fuentes |
|---|---|---|---|
| **UE** | IVA del país del consumidor; el vendedor no-UE usa el **OSS "no-Unión"**: se registra en un Estado miembro de identificación y presenta declaraciones trimestrales; B2C únicamente (B2B = inversión del sujeto pasivo). No hay que registrarse antes en IVA normal. | Tasas por país (ej. 19% Alemania, 20% Francia). Sin umbral para vendedores no-UE: el umbral de EUR 10.000 aplica solo a micro-vendedores establecidos en la UE (conocimiento previo, NO VERIFICADO·previo). | EVIDENCIA [T1][T2][T3][T4] |
| **Reino Unido** | Fuera del OSS desde el Brexit. Vendedor no-UK debe registrarse en HMRC **desde la primera venta**, sin umbral (UK-establecidos: GBP 90.000). | IVA 20%; registro por Government Gateway, sin representante ni dirección en UK. | EVIDENCIA [T5][T6] |
| **Noruega, Suiza, Nueva Zelanda** | No investigué. Conocimiento previo: Noruega (régimen VOES para e-servicios, umbral aprox. NOK 50.000), Suiza (umbral CHF 100.000), NZ (GST 15%, umbral NZ$60.000). | | NO VERIFICADO·previo |
| **Australia** | GST sobre productos digitales importados por no residentes; registro si el GST turnover llega a **A$75.000** (ventana móvil de 12 meses); registro voluntario posible; si se vende a través de una plataforma de distribución electrónica, la obligación puede recaer en la plataforma. | Tasa 10% (conocimiento previo). | Fuente oficial ATO [T7]; resto [T8] |
| **Canadá** | GST/HST: no residentes que venden productos digitales a consumidores deben registrarse al superar **CAD 30.000** en 12 meses, bajo el marco simplificado (desde julio 2021; sin créditos de insumos, declaraciones trimestrales). Quebec (QST): mismo umbral de CAD 30.000, desde 2019. | PST provinciales: no verificado. | EVIDENCIA [T18][T19][T20] |
| **EE. UU.** | Sin IVA federal. Tras *Wayfair* (2018), los 45 estados con sales tax y DC tienen nexo económico, mayoría con umbral de USD 100.000 de ventas (varios eliminan el conteo de transacciones). **La imposición de bienes digitales varía por estado**; Maine amplió en 2026; California (SB 122) y Colorado traen cambios desde 2027 (esto último no confirmado con fuente oficial). Reglas de "marketplace facilitator": no verificadas. | Un MoR actúa como facilitador y cobra donde corresponde. | EVIDENCIA [T9][T10][T11], fuentes en conflicto sobre 2026 |
| **India** | GST OIDAR: proveedor extranjero B2C debe registrarse (formulario REG-10), pagar **18% IGST** y presentar GSTR-5A mensual; sin umbral; B2B = reverse charge. Una fuente dice 5% para e-books (HSN 9984): no aplicar a moldes sin consultar. | Lugar de suministro por pares de pruebas (IP, tarjeta, dirección, SIM). | EVIDENCIA [T12][T13] |
| **Japón** | Consumption Tax (10%, conocimiento previo) sobre servicios digitales B2C de extranjeros; desde abril de 2025 las **plataformas designadas** (ventas > JPY 5.000 millones, según una fuente) pagan el impuesto por los vendedores. B2B = reverse charge. | Confirmar designación en la lista de la NTA. | EVIDENCIA [T14][T15] |
| **Corea del Sur** | VAT 10%; registro simplificado de proveedores extranjeros por Hometax, sin umbral; declaración trimestral (un tercero dice semestral: contradicción); exentos de e-invoicing doméstico. | Plazo de registro: 20 días vs. "desde la primera venta" (contradicción). | EVIDENCIA [T16][T17] |
| **Turquía** | Desde 2018 el proveedor extranjero de servicios electrónicos B2C debe registrarse en el IVA, sin umbral; tasa **20%** (desde 10-jul-2023); declaración mensual (fecha límite 24, 26 o 28 según fuente: contradicción); sin deducción de insumos. DST 7,5% solo para grandes grupos (EUR 750 M global). | | EVIDENCIA [T21][T39] |
| **Rusia** | Desde 1-oct-2022 (Ley 323-FZ) vuelve el modelo de agente tributario para B2B (el cliente ruso paga el IVA); proveedores extranjeros B2C se registran. La FTS reconoció que las sanciones dificultan los pagos; cobro vía intermediarios exime del registro. **No vender: ver sanciones.** | 20% (conocimiento previo). | EVIDENCIA [T22][T23][T24] |
| **Sudáfrica** | Proveedor extranjero de servicios electrónicos se registra si supera **R1 millón** en 12 meses (antes R50.000; cambio 1-abr-2019) y cumple 2 de 3 criterios (residente, banco sudafricano, dirección en SA); excepción desde 5-ene-2023 para exceso temporal y anormal. SARS persigue pagos no declarados. | IVA 15%. | Fuente oficial SARS [T25]; Bowmans [T26] |
| **Arabia Saudita** | Proveedor no residente B2C: IVA **15%**, sin umbral, registro desde la primera venta (o 30 días según otra fuente); ZATCA directo o representante; B2B = reverse charge. | | EVIDENCIA [T27][T28] |
| **EAU** | No encontré fuentes en la búsqueda. Conocimiento previo: IVA 5%, registro de no residentes. | | NO VERIFICADO·previo |
| **Indonesia** | Los operadores extranjeros se designan "PMSE VAT Collector" al superar IDR 600 M/año o IDR 50 M/mes, o 12.000 usuarios/año o 1.000/mes; pueden pedirlo voluntariamente. Tasa: **conflicto**: la página oficial lista 12%; una guía 2026 habla de tasa efectiva 11% (12% sobre base 11/12). En 2026 la DGT describe un mecanismo paralelo (SPP-TDLN). | | Fuente oficial [T29] + terceros [T30]; **tasa NO VERIFICADO** |
| **Brasil** | Reforma tributaria: CBS (federal) e IBS (estatal/municipal) alcanzan a proveedores extranjeros de contenido descargable, SaaS, etc. (Decreto 12.955/2026 según fuentes de terceros). Registro con CNPJ, sin umbral; representante local opcional; plataformas pueden ser responsables por sustitución. **Fechas en conflicto:** 1-ago-2026 (registros, e-factura), 1-dic-2026 (NFS-e para plataformas e intangibles), 2027 (cobro efectivo; en 2026 sería informativo). Comarch informa un aplazamiento para personas físicas a 2027. ISS/PIS/COFINS: no verificado. | | EVIDENCIA, fechas **NO VERIFICADO** [T35][T36][T37][T38] |
| **México** | IVA 16%; los proveedores extranjeros de servicios digitales se registran en el RFC y cobran el IVA; si no se registran, el receptor lo trata como importación. Retenciones a vendedores vía plataformas. Fuentes de 2019-2022. | | EVIDENCIA vieja [T32][T34] |
| **Chile** | IVA 19% a servicios digitales de extranjeros ("Solución IVA", régimen simplificado desde 1 de junio de un año que el resumen no precisa; entiendo que 2020). Retención en medios de pago si no se registran. | | Fuente oficial Hacienda [T33]; CIAT [T32] |
| **Colombia** | Prestadores no residentes se inscriben en el IVA; pueden optar por retención en medios de pago. Tasa 19% (conocimiento previo; CIAT habla de 18-22% para la región). | | EVIDENCIA [T32]; tasa NO VERIFICADO |
| **Uruguay** | No investigado. | | NO VERIFICADO·previo |

**Observación sobre la fiscalización [EVIDENCIA]:** SARS (Sudáfrica) cruza pagos al exterior con registros; ARCA (Argentina) reforzó cruces de facturación y liquidación de divisas [S26]. La ventaja de no tener umbral en muchos países implica que "ser chico" no te exime de la obligación, aunque la fiscalización real sobre micro-vendedores sea baja. No te recomiendo apostar a eso; ver sección 9.

## 5. Legal y cumplimiento

**Toda esta sección es [NO VERIFICADO·previo].** No pude buscar durante la sesión. Usarla como checklist para el abogado, no como referencia.

### 5.1 Privacidad, cookies y datos

| Marco | Qué implica para moldey |
|---|---|
| **GDPR / UK GDPR** | Aplican si ofrecés a personas en UE/UK (art. 3.2). Necesitás política de privacidad, base legal por tratamiento, derechos de acceso/borrado, y evaluar si hace falta representante en la UE/UK (art. 27). El MoR es controlador de los datos de pago; vos de tu analítica y newsletter. |
| **Cookies / ePrivacy** | UE/UK: consentimiento previo para cookies no esenciales (analítica, publicidad). Usar CMP con bloqueo de scripts y Google Consent Mode v2 si usás productos de Google. EE. UU.: opt-out y respeto de Global Privacy Control. Brasil (LGPD) y Quebec (Ley 25) también exigen transparencia. |
| **CCPA/CPRA y leyes estatales de EE. UU.** | Umbrales (ingresos > ~USD 25 M, 100.000 consumidores, o 50% de ingresos por venta/compartición de datos) probablemente no se alcanzan; igual conviene enlazar "Do Not Sell/Share" si usás publicidad. |
| **LGPD (Brasil)** | Aplica a quien trata datos de personas en Brasil; requiere base legal, DPO/contacto y política en portugués. |
| **PIPL (China) / ICP** | Aplica extraterritorialmente si ofrecés a personas en China. Alojar en China continental exige licencia **ICP** y entidad local; servir desde afuera evita ICP pero con velocidad degradada y posibles bloqueos; Baidu favorece sitios con ICP. Para moldey: **no priorizar China**. |
| **India DPDP** | Ley 2023, reglas publicadas a fines de 2025 con implementación escalonada (verificar estado); consentimiento y avisos. |
| **Rusia (152-FZ)** | Localización de datos de ciudadanos rusos. Otra razón para no operar ahí. |
| **Turquía KVKK** | Ley 6698; registro de responsables (VERBİS) y reglas de transferencia internacional. Bajo riesgo para un comercio chico, pero revisar. |
| **Newsletter** | UE: consentimiento (doble opt-in recomendado); Canadá: CASL; EE. UU.: CAN-SPAM. |

### 5.2 Términos, reembolsos y consumidor

- **Derecho de desistimiento UE:** para contenido digital descargable, el derecho de 14 días se pierde si el consumidor consiente expresamente que la ejecución comience y reconoce que pierde ese derecho (Directiva 2011/83/UE, art. 16 m); el UK tiene una regla equivalente. En un MoR esto lo implementa la plataforma; si vendés directo, necesitás casilla de aceptación y confirmación duradera por email. [NO VERIFICADO·previo]
- **Política de reembolso:** entre "sin reembolsos por ser producto digital" (típico) y reembolso condicionado (archivo defectuoso, doble compra). Publicarla en cada idioma. Evitar promesas que no cumplas: la política visible es señal de confianza (sección 6).
- **Textos legales traducidos:** no usar traducción automática sin revisión; cláusula de prevalencia del idioma (ES/EN).

### 5.3 Accesibilidad y menores

- **European Accessibility Act (EAA):** aplica desde el 28-jun-2025 a servicios de comercio electrónico dirigidos a consumidores de la UE; hay exención para microempresas de servicios (menos de 10 personas y facturación ≤ EUR 2 M), pero depende de la interpretación nacional y de si un proveedor extranjero entra. Referencia técnica: EN 301 549 (basada en WCAG 2.1 AA); la versión vigente de WCAG es 2.2. **Apuntar a WCAG 2.2 AA** en tienda, checkout y PDFs de instrucciones (texto real, no solo imágenes). [NO VERIFICADO·previo]
- **Menores:** no dirigir marketing a menores de 13 (COPPA); GDPR art. 8 (13-16 según país). Aunque coser sea afición juvenil, el sitio es para compradores adultos; no recopilar datos de menores a sabiendas.

### 5.4 Propiedad intelectual, licencias y piratería

- **Qué se protege (esquema general, varía por país; consultar abogado) [NO VERIFICADO·previo]:** el **documento del molde** (dibujos, textos de instrucciones, diagramas, fotos, artes gráficos, tipografías, diseño de página) suele ser protegible por copyright. En EE. UU., la forma funcional de una prenda ("útil article") generalmente **no** se protege, de modo que alguien puede hacer prendas parecidas; en la UE la originalidad y los derechos de diseño (registrados y no registrados) cambian el panorama. La protección práctica y más fuerte es **contractual:** términos de licencia del archivo.
- **Licencias:** definir "Personal" (uso propio, regalos), "Comercial pequeño" (prendas terminadas hasta N unidades/año, con atribución opcional) y "Comercial ampliado" (producción mayor). Cláusulas anti-reventa: prohibido redistribuir, subir a nubes públicas, revender el archivo o derivados editables, y entrenar modelos de IA con el material. Fotos y gráficos de terceros: licencia propia y por escrito.
- **DMCA / avisos de retirada:** moldey no hospeda contenido de terceros, así que el uso útil es **enviar** notificaciones a Google, hostings, Etsy, Telegram, etc. cuando aparezcan copias. Registrar un agente designado ante la U.S. Copyright Office solo importa si el sitio hospedara contenido de usuarios (reseñas con fotos, comunidad). En la UE existe el mecanismo de notificación y acción de la DSA.
- **Antipiratería (de más a menos efectivo) [OPINIÓN]:** (1) enlaces firmados con caducidad y límite de descargas; (2) marca de agua visible discreta y/o metadatos con ID del comprador (disuade filtraciones y permite rastrear); (3) monitoreo + notificaciones de retirada; (4) cuenta con historial de descargas. Los PDF con "capas bloqueadas" o permisos/contraseña se pueden eliminar con herramientas comunes; sirven de molestia, no de DRM.
- **Sanciones/embargos:** OFAC (EE. UU.) obliga a personas y bancos estadounidenses; un vendedor argentino no es persona estadounidense, pero **MoR, bancos y procesadores sí aplican** las listas. Países con restricciones totales o grandes (Cuba, Irán, Corea del Norte, Siria con cambios en 2025 a verificar, Crimea/DNR/LNR, Rusia/Bielorrusia por rieles de pago): Polar bloquea Cuba, Rusia, Irán, Corea del Norte y Siria [S15]; Paddle bloquea ciertos países y a junio 2026 solo menciona restricción regional de Ucrania [S13]. **No vender ni anunciar activamente en esos mercados.** Nota: hay hablantes de ruso en Kazajistán, Alemania, Israel, etc., que sí podrían comprarte; el SEO en ruso no equivale a vender "a Rusia".

## 6. Confianza y conversión global

Esta sección combina prácticas de la industria sin respaldo cuantitativo propio de esta sesión. **No cito cifras de conversión** porque no pude verificar ninguna. [OPINIÓN / NO VERIFICADO·previo]

**Señales a localizar por idioma/mercado:**

1. **Precio claro:** moneda local, impuestos incluidos (UE/UK/AU) o "impuestos al pagar" (EE. UU./CA), sin costos ocultos.
2. **Métodos de pago reales** visibles (solo íconos que de verdad funcionan en el checkout de ese país).
3. **Políticas visibles en footer y en la ficha:** reembolso, licencia, privacidad, términos, envío digital ("descarga inmediata") traducidas al idioma de la página.
4. **Contacto humano:** correo con respuesta prometida (ej. 24-48 h), WhatsApp Business (dominante en LatAm, India, Indonesia, parte de África/Europa), y en mercados específicos LINE (Japón/Tailandia/Taiwán), KakaoTalk (Corea), Telegram (Europa del Este). Formulario de contacto traducido y con selector de idioma.
5. **Reseñas reales** con foto de la prenda terminada, por idioma cuando sea posible. No inventar ni copiar reseñas: riesgo de penalización y de problemas con consumidor. Marcado `Product`/`AggregateRating` solo con datos reales y siguiendo las políticas de Google. [NO VERIFICADO·previo]
6. **Muestra gratuita** y hoja de prueba (sección 7).
7. **Sello de seguridad y marca del MoR/procesador** en el checkout; HTTPS siempre.
8. **Soporte multilingüe con IA:** un chatbot con base de conocimiento (talles, impresión, errores comunes) reduce tickets, pero hay que dejar una vía humana y no responder cuestiones legales/reembolsos sin revisión.

**Impacto SEO/AEO [OPINIÓN]:** E-E-A-T es un concepto de las guías para evaluadores de calidad de Google, no un factor de ranking medible directamente; las señales útiles son las que además mejoran experiencia: autoría y biografía visibles de la persona que diseña los moldes, fotos propias del proceso, página "Sobre nosotros" con datos reales (país, contacto), políticas claras, reseñas verificables. Para AEO, las respuestas de IA suelen preferir páginas con datos concretos (tabla de medidas, metraje de tela, nivel de dificultad) y reputación consistente. [NO VERIFICADO: sin estudio verificado en esta sesión]

**Tiempos de carga:** apuntar a los umbrales de Core Web Vitals de Google (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1) con CDN, imágenes optimizadas y poco JavaScript; importante para mercados con redes móviles lentas (India, Sudeste Asiático, África). [NO VERIFICADO·previo]

## 7. Entrega técnica de archivos [NO VERIFICADO·previo, práctica estándar]

| Tema | Recomendación |
|---|---|
| **Nombres de archivo** | ASCII, sin espacios ni acentos, con versión y tamaño: `moldey_blusa-lima_v1.2_A4.pdf`, `..._Letter.pdf`, `..._A0.pdf`. Evita problemas en descompresores y móviles. |
| **Estructura del ZIP** | `/LEEME-READ-ME.pdf` (índice), `/A4/`, `/Letter/`, `/A0/`, `/Instrucciones/<idioma>.pdf`, `/Editables/` (DXF/SVG con unidades declaradas). Un archivo `VERSION.txt` con historial. |
| **PDF** | Hoja de prueba al comienzo (cuadrado de 5 cm / 2 in para validar escala), "imprimir al 100%, no ajustar a página", mapa de ensamble de hojas, márgenes de pegado, fuentes incrustadas, texto real (accesible). |
| **Capas (OCG)** | Una capa por talle o rango para imprimir solo lo necesario. Las capas no funcionan igual en visores de navegador y móviles; **incluir también PDFs separados por rango de talles** como alternativa. |
| **Peso** | Priorizar vectores; comprimir imágenes; objetivo orientativo de ≤ 10-25 MB por PDF y ZIPs más ligeros para redes lentas; ofrecer versión "lite". |
| **Papel por país** | Letter en EE. UU., Canadá, México, Chile, Colombia, Filipinas y países de Centroamérica (verificar por país); A4 en el resto; A0 para copisterías/plotter. Detectar región y preseleccionar, pero siempre incluir ambas. |
| **Instrucciones multilingües** | Un PDF de instrucciones por idioma, no uno plurilingüe. Complementar con pictogramas y un QR a una página web con instrucciones localizadas (sirve a SEO y se actualiza sin reenviar archivos). |
| **Almacenamiento y CDN** | Cloudflare R2 (sin cargo de salida, según lo que sé) o S3 + CloudFront, con **URLs firmadas** (ej. 24-72 h) y límite de descargas (3-5), y un enlace "reenviar mi descarga" por email para evitar tickets. Si el MoR entrega los archivos, revisar su límite de tamaño y de descargas. |
| **Versionado** | Versión en nombre y metadatos; si corregís un error, notificar a compradores por email con enlace nuevo (retención y menos soporte). |
| **Vista previa sin regalar** | Imágenes de la prenda terminada, croquis técnico (dibujo plano), tabla de medidas y metraje en HTML (indexable y citable por IA), una página del PDF con marca de agua "MUESTRA", y un molde gratis de entrada. **No dejar PDFs completos accesibles por URL pública indexable**: bloquear con `noindex` y servirlos solo firmados. |

## 8. Qué hacer en moldey.com (priorizado, por olas)

**Escala:** Impacto A/M/B; Esfuerzo A/M/B.

### Ola 0 — Imprescindible para vender hoy (0-30 días)

| # | Acción | Impacto | Esfuerzo |
|---|---|---|---|
| 1 | **Elegir MoR y confirmar con la documentación oficial** si acepta a un vendedor argentino y moldes PDF (Polar y Lemon Squeezy primero; Paddle/Creem a confirmar; Gumroad como alternativa). Contratar al contador antes de recibir el primer pago. | A | M |
| 2 | **Checkout principal en el MoR** con tarjetas, Apple/Google Pay y PayPal; mostrar precios en monedas principales (USD, EUR, GBP, CAD, AUD) con impuestos manejados por el MoR. | A | M |
| 3 | **Venta doméstica Argentina** con Mercado Pago (pesos), con el contador definiendo facturación. | M | B-M |
| 4 | **Páginas legales mínimas** en ES + EN: términos, privacidad, reembolsos, licencia (personal/comercial/anti-reventa), contacto. Revisión de un abogado. | A | M |
| 5 | **Entrega inmediata** (email + área de descargas) con enlaces firmados, caducidad, límite de descargas y reenvío. | A | M |
| 6 | **Soporte básico:** correo y WhatsApp Business con tiempos prometidos; FAQ de impresión (escala 100%, ensamble). | A | B |
| 7 | **CMP de cookies** para UE/UK/BR y analítica en modo consentimiento. | M | B-M |
| 8 | **Bloqueo de países sancionados** en el checkout (lo hace el MoR) y no anunciar en ellos. | M | B |

### Ola 1 — Consolidar (1-3 meses)

| # | Acción | Impacto | Esfuerzo |
|---|---|---|---|
| 9 | **Hoja de prueba, A4/Letter automático, instrucciones en 3-5 idiomas** (EN, ES, PT, FR, DE) y QR a instrucciones web. | A | M |
| 10 | **Vista previa y muestra gratis;** tablas de medidas/metraje en HTML (SEO/AEO). | A | M |
| 11 | **Reseñas reales** (pedirlas por email post-compra) y marcado `Product`. | M-A | B |
| 12 | **Packs/bundles y precio mínimo** para absorber la comisión fija. | A | B |
| 13 | **Marca de agua con ID del comprador;** monitoreo básico de piratería y plantilla de notificación DMCA. | M | M |
| 14 | **Políticas traducidas y revisadas** en cada idioma que reciba tráfico significativo; selector de idioma en contacto. | M | M |
| 15 | **Medir** por país: sesiones, inicios de checkout, ventas y causas de abandono. Con eso decidir la ola 2. | A | B |

### Ola 2 — Expansión por evidencia (3-9 meses)

| # | Acción | Impacto | Esfuerzo |
|---|---|---|---|
| 16 | **Brasil:** Pix (vía MoR/PSP que lo ofrezca) si PT-BR rinde; vigilar la reforma CBS/IBS (fechas en conflicto). | A | M-A |
| 17 | **Europa:** métodos locales (iDEAL/Bancontact/BLIK/Klarna/Wero) según mercados de mayor tráfico. | M-A | B-M (depende del MoR) |
| 18 | **PPP piloto** en 3 tiers con verificación de país de tarjeta; A/B contra precio único. | M | M |
| 19 | **India/Indonesia/Filipinas:** UPI/QRIS/GCash solo si el MoR/PSP los ofrece y hay demanda. | M | M-A |
| 20 | **Accesibilidad WCAG 2.2 AA** y declaración de accesibilidad (EAA). | M | M |
| 21 | **Japón/Corea/Golfo:** métodos locales (konbini/PayPay, KakaoPay/Naver Pay, mada/Tabby/Tamara) si hay señal. | M | M |

### Ola 3 — Opciones de largo plazo (9+ meses)

| # | Acción | Impacto | Esfuerzo |
|---|---|---|---|
| 22 | **China** (ICP/PIPL/Alipay/WeChat) solo con evidencia clara y entidad/partner local. | B-M | A |
| 23 | **Sociedad en EE. UU./UK/UE** si el volumen y el contador lo justifican (no antes). | M | A |
| 24 | **Registro de marca** en mercados clave y política formal de licencias comerciales ampliadas. | M | M-A |

## 9. Qué NO hacer

1. **No vender B2C global directo con PayPal/Mercado Pago/WooCommerce sin MoR** creyendo que "soy chico, no pasa nada": varias jurisdicciones no tienen umbral para extranjeros (UE/OSS, UK, India, Turquía, Corea, KSA, Brasil) y las autoridades cruzan pagos. La falta de fiscalización actual no es un permiso.
2. **No abrir una sociedad en EE. UU./UK solo para usar Stripe** sin asesoramiento fiscal argentino previo.
3. **No usar PPP sin verificar el país de la tarjeta** ni sin entender las reglas de la UE sobre geobloqueo.
4. **No confiar en contraseñas o "bloqueos" de PDF como protección;** no publicar enlaces de descarga públicos e indexables.
5. **No vender ni promocionar a Rusia, Cuba, Irán, Corea del Norte, Siria ni regiones sancionadas;** no intentar eludir los bloqueos del MoR con VPN o intermediarios.
6. **No publicar políticas legales traducidas automáticamente sin revisión,** ni copiar términos de otra tienda (derechos de autor y riesgo de cláusulas inaplicables).
7. **No inventar reseñas, sellos ni cifras de "ventas".**
8. **No integrar 30 métodos de pago a la vez;** cada integración directa implica costos, conciliación y cumplimiento.
9. **No fijar precios convertidos a mano** cada vez que cambia el tipo de cambio: usar la conversión del MoR y revisar la lista de precios cada trimestre.
10. **No asumir que "100 idiomas" significa 100 mercados vendibles;** verificar por país si el MoR cobra, si hay método de pago relevante, y si hay obligación fiscal.
11. **No dar por cierto lo que dice una reseña de un competidor** (muchas fuentes de esta investigación son de empresas que compiten entre sí): verificar tarifas y países en la página oficial.
12. **No mezclar cuentas:** no recibir pagos del negocio en la cuenta personal sin consultarlo con el contador.

## 10. Qué debe validar un contador y un abogado

**Contador (Argentina):**
- Encuadre (monotributo vs. régimen general), topes y cómo computan los ingresos por exportación de servicios/licencias digitales; la afirmación de una sola fuente de que la factura E no suma al tope de monotributo [S26].
- Cómo facturar a un MoR extranjero (factura E, concepto, tipo de cambio, ¿a quién?) y qué ocurre con pagos de PayPal/Payoneer/Wise.
- Régimen cambiario vigente (Comunicación A 8330 y siguientes): obligación de liquidar según seas persona humana o jurídica, cuenta bancaria en USD en entidad local vs. billeteras, plazos de ingreso de divisas (20 días hábiles vs. 30 corridos vs. 5: contradicciones).
- Derechos de exportación o retenciones aplicables a servicios/licencias digitales (pregunta abierta, no la pude verificar).
- Implicancias de tener una sociedad en EE. UU./UK controlada desde Argentina.
- Venta doméstica: IVA y facturación de productos digitales a consumidores argentinos.
- Qué se sigue debiendo localmente aunque el MoR remita los impuestos del consumidor.

**Abogado:**
- Textos de términos, privacidad, reembolsos y licencias en ES/EN y su adaptación a UE/UK/BR.
- Necesidad de representante GDPR/UK GDPR; cumplimiento de ePrivacy/CPRA/LGPD.
- Derecho de desistimiento en contenido digital (UE/UK) y flujo de aceptación en el checkout.
- Alcance del EAA para un proveedor argentino y el tamaño de la empresa.
- Protección de los moldes (qué se protege por país), licencias comerciales y DMCA/DSA.
- Sanciones y países bloqueados; geobloqueo UE y PPP.

## 11. Contradicciones, vacíos y cosas que quedaron sin verificar

- **Verificar en páginas oficiales:** Argentina como país de payout en Paddle y Creem; lista completa de Lemon Squeezy (snapshot viejo) y Polar (no vi BR/MX); tarifa vigente de Polar (4%+0,40 vs. 5%+0,50); remisión de IVA UE en Payhip; si cada MoR acepta moldes digitales.
- **Pendiente de búsqueda:** métodos de pago que activa cada MoR por país; legal (GDPR/EAA/LGPD/PIPL/DPDP/KVKK); DMCA/OFAC; entrega técnica y almacenamiento; confianza y cifras de conversión; UAE, Uruguay, Noruega, Suiza, Nueva Zelanda; Digistore24, FastSpring, Hotmart, Kiwify, Shopify y WooCommerce; marketplaces como Etsy como canal complementario.
- **Contradicciones:** fecha de la adquisición de Lemon Squeezy; comisión de Gumroad (procesamiento incluido o no); plazo de registro/declaración en Corea; fecha de declaración mensual en Turquía; tasa de Indonesia (11% vs. 12%); fechas de CBS/IBS en Brasil; plazos cambiarios en Argentina.
- **Calidad:** la mayoría de las fuentes son de terceros con interés comercial; las oficiales (ATO, SARS, pajak.go.id, Hacienda Chile, docs de Polar, Creem, Paddle, Gumroad y Lemon Squeezy) son las que conviene releer antes de decidir.

## 12. Fuentes (las que aparecieron en los resultados; fecha cuando fue visible)

**Plataformas y pagos [S]**
- [S1] https://dodopayments.com/blogs/stripe-supported-countries-alternatives (2026; 46 países; competidor MoR)
- [S2] https://www.cs-cart.com/blog/stripe-supported-countries/ (2026)
- [S3] https://payatlas.com/countries/argentina-ar
- [S4] https://www.guiadesoftware.com/blog/mejor-pasarela-pago-argentina
- [S5] https://osome.com/uk/blog/stripe-argentina-verified-account
- [S6] https://get.bandcamp.help/hc/en-us/articles/32854280223511 ; https://talent.docs.mercor.com/policies/supported-countries
- [S7] https://docs.lemonsqueezy.com/help/getting-started/supported-countries (snapshot antiguo)
- [S8] https://docs.lemonsqueezy.com/help/payments/currencies ; https://docs.lemonsqueezy.com/help/checkout/payment-methods (no leída)
- [S9] https://www.lemonsqueezy.com/blog/new-bank-payouts (2021: 79 países por banco, 200+ por PayPal)
- [S10] https://dodopayments.com/blogs/lemonsqueezy-review (2026)
- [S11] https://alternativeto.net/news/2024/7/stripe-acquires-payment-processing-platform-lemon-squeezy (jul-2024)
- [S12] https://dodopayments.com/blogs/paddle-fees-explained (referencia jul-2026) ; https://paynow.gg/compare/paddle ; https://learnwithhasan.com/payment-gateways/paddle/
- [S13] https://developer.paddle.com/partners/embed-billing/get-started/supported-sellers ("a junio de 2026")
- [S14] https://developer.paddle.com/partners/embed-billing/seller-go-live/payout-accounts
- [S15] https://polar.sh/docs/merchant-of-record/supported-countries
- [S16] https://x.com/polar_sh/status/1915379610809782428 (fecha no visible)
- [S17] https://polar.sh/docs/features/finance/payouts
- [S18] https://dodopayments.com/blogs/polar-sh-review (2026)
- [S19] https://gumroad.com/pricing
- [S20] https://checkoutpage.com/blog/gumroad-fees (2026)
- [S21] https://dodopayments.com/blogs/payhip-review (jul-2026)
- [S22] https://fungies.io/payhip-review-2026
- [S23] https://docs.creem.io/merchant-of-record/supported-countries
- [S24] https://docs.creem.io/merchant-of-record/finance/payouts
- [S25] https://docs.creem.io/faq/supported-countries
- [S26] https://contablix.ar/blog/factura-e-exportacion-servicios-2026 (2026)
- [S27] https://www.global66.com/blog/?p=23586 (2026)
- [S28] https://www.iprofesional.com/impuestos/426384-la-salida-progresiva-del-cepo (20-jun-2026)
- [S29] https://servidos.ar/calculadora-exportacion (baja confiabilidad) ; https://blogdelcontador.com.ar/news-45392-freelancers-flexibilizan-cepo-habilitan-mas-dolares-sin-liquidar ; https://www.iproup.com/finanzas/48882-freelancers-monotributistas-nuevo-regimen-del-gobierno
- [S30] https://www.iprofesional.com/finanzas/403093-pay-pal-argentina-como-cobrar-en-dolares (19-jun-2026)
- [S31] https://www.global66.com/blog/recibir-dolares-paypal-argentina/ ; https://www.jonatanalmeira.com/?p=70809 (2026)
- [S32] https://www.payoneer.com/es/resources/estrategias-para-usar-y-mover-tus-fondos-en-argentina/
- [S33] https://www.iprofesional.com/finanzas/444811-conviene-payoneer-comisiones-actualizadas-para-pasar-dolares-a-un-banco-local
- [S34] https://wise.com/ar/blog/retirar-dinero-de-payoneer-en-argentina (verificado sep-2025)
- [S35] https://www.jonatanalmeira.com/?p=65154 (2026)
- [S36] https://gironews.com/varejo-digital/pix-responde-por-42-do-e-commerce-e-vira-referencia-global/ ; https://www.infomoney.com.br/?p=2358170 (Ebanx)
- [S37] https://paymentexpert.com/2026/04/01/digital-wallets-worldpay-gpr-2026/ (1-abr-2026)
- [S38] https://eco.com/support/en/articles/15083174-stripe-stablecoin-payments-2026 (2026)

**Impuestos [T]**
- [T1] https://www.avalara.com/us/en/blog/ioss-moss-oss-what-does-it-all-mean.html
- [T2] https://support.taxually.com/support/solutions/articles/80001155457
- [T3] https://helpdesk.hellotax.com/hc/en-150/articles/49817186344209-Non-Union-OSS-for-Non-EU-Digital-Service-Providers
- [T4] https://beancount.io/blog/2026/07/08/eu-vat-one-stop-shop-us-freelancers-saas-founders (8-jul-2026)
- [T5] https://www.fonoa.com/countries/united-kingdom
- [T6] https://quaderno.io/guides/united-kingdom/vat/registration/
- [T7] https://www.ato.gov.au/api/public/content/0-f0676a52-df3e-4d50-a25e-940c2103c562 (oficial)
- [T8] https://www.vatcalc.com/australia/australia-gst-on-digital-services-by-non-residents/
- [T9] https://dodopayments.com/blogs/sales-tax-digital-goods-by-state (2026)
- [T10] https://taxcloud.com/blog/sales-tax-changes-2026/
- [T11] https://trykintsugi.com/sales-tax-guides/usa/economic-nexus (2026)
- [T12] https://treelife.in/legal/oidar-registration-in-india/
- [T13] https://www.xflowpay.com/blog/oidar-services
- [T14] https://www.fonoa.com/resources/blog/japan-designates-digital-platforms-as-deemed-suppliers-for-consumption-tax
- [T15] https://trykintsugi.com/sales-tax-guides/apac/japan (2026)
- [T16] https://trykintsugi.com/sales-tax-guides/apac/south-korea (2026)
- [T17] https://dodopayments.com/tax/vat-south-korea
- [T18] https://stripe.com/resources/more/canada-vat
- [T19] https://rsmcanada.com/our-insights/tax-alerts/qst-registration-may-be-required-as-of-september-1-2019.html (2019)
- [T20] https://beancount.io/blog/2026/07/13/canada-gst-hst-cross-border-online-sellers-guide (13-jul-2026)
- [T21] https://www.fonoa.com/resources/country-tax-guides/turkiye/tax-on-digital-services
- [T22] https://www.noerr.com/en/insights/russia-vat-on-electronic-services
- [T23] https://www.pgplaw.com/analytics-and-brochures/alerts/electronic-services/
- [T24] https://schneider-group.com/en/news/countries/changes-concerning-vat-payment-on-e-services/
- [T25] https://www.sars.gov.za/latest-news/vat-registration-supply-of-electronic-services-by-foreign-suppliers-and-foreign-intermediaries/ (oficial)
- [T26] https://bowmanslaw.com/insights/vat-on-electronic-services-amended-regulations-and-guidance-from-sars/
- [T27] https://www.fonoa.com/resources/country-tax-guides/saudi-arabia/tax-on-digital-services
- [T28] https://www.dariba.co/non-resident-suppliers-and-vat-obligations/
- [T29] https://pajak.go.id/index.php/en/digitaltax (oficial)
- [T30] https://trykintsugi.com/sales-tax-guides/apac/indonesia (2026) ; documento DGT 2026 SPP-TDLN: https://www.pajak.go.id/sites/default/files/2026-09/Indonesia%27s%20VAT%20Collection%20Mechanism%20for%20Cross-Border%20Digital%20Transactions%20%28SPP-TDLN%29.pdf
- [T32] https://www.ciat.org/Biblioteca/DocumentosdeTrabajo/2025/DT_05_2025.pdf (2025)
- [T33] https://www.hacienda.cl/noticias-y-eventos/noticias/ministerio-de-hacienda-informa-sobre-iva-a-plataformas-digitales (oficial)
- [T34] https://www.elcontribuyente.mx/2022/03/12-plataformas-digitales-extranjeras-se-dan-de-alta-ante-el-sat/ (mar-2022)
- [T35] https://www.vatcalc.com/brazil/brazil-vat-non-resident-digital-services-providers-marketplaces-2026/ (2026)
- [T36] https://www.fonoa.com/resources/blog/brazil-cbs-ibs-tax-rules-digital-platforms-2026 (2026)
- [T37] https://www.comarch.com/trade-and-services/data-management/legal-regulation-changes/brazil-postpones-cbs-registration-and-invoicing-duties-for-individuals-to-2027/
- [T38] https://www.fiscal-requirements.com/news/5854-brazil-moves-toward-e-invoicing-requirements-for-foreign-suppliers-from-december-2026
- [T39] https://dodopayments.com/tax/vat-turkey

**Legal (sección 5), confianza (6) y entrega (7):** sin fuentes de esta sesión; todo es conocimiento previo marcado [NO VERIFICADO·previo].
