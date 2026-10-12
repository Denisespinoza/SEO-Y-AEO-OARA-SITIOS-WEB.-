# SEO y AEO para moldey.com — paquete de investigación y plan (oct. 2026)

Investigación y plan de ejecución para mejorar la **visibilidad global de moldey.com** (moldes digitales de costura: PDF para imprimir, archivos editables y plantillas de sublimación) en **buscadores (SEO)** y en **respuestas de IA (AEO/GEO)**, por oleadas, hasta cubrir los **100 idiomas más hablados**. Está pensado para dárselo a **Claude Code en tu PC**, dentro del proyecto del sitio.

## Cómo usarlo (3 pasos)

1. Copiá esta carpeta dentro del proyecto de moldey.com (por ejemplo `moldey.com/docs/seo-aeo/`) o clonala al lado.
2. Abrí Claude Code en la carpeta del sitio y pegá el prompt de **[`00-PROMPT-MAESTRO-CLAUDE-CODE.md`](00-PROMPT-MAESTRO-CLAUDE-CODE.md)**. Arranca solo por la **Fase 0 (auditoría, solo lectura)** y se detiene a esperar tu aprobación.
3. Revisá `AUDITORIA-INICIAL.md` y `PLAN-AJUSTADO.md`, respondé las decisiones que te pida (lista en el plan, §7) y aprobá fase por fase. Opcional: copiá `plantillas/CLAUDE.md.moldey` a la raíz del repo del sitio para que las reglas queden permanentes.

## Qué hay

| Archivo | Para qué |
|---|---|
| [`00-PROMPT-MAESTRO-CLAUDE-CODE.md`](00-PROMPT-MAESTRO-CLAUDE-CODE.md) | El prompt para pegar en Claude Code |
| [`06-PLAN-MOLDEY-COM.md`](06-PLAN-MOLDEY-COM.md) | **El plan completo para moldey.com**: fases, triage de los 11 idiomas, pagos/legal, medición, riesgos, decisiones tuyas |
| [`04-CHECKLIST-IMPLEMENTACION-TECNICA.md`](04-CHECKLIST-IMPLEMENTACION-TECNICA.md) | Tareas técnicas con criterio de aceptación (auditoría, base técnica, multilingüe, datos estructurados, medición, CI) |
| [`01-INFORME-INVESTIGACION-SEO-AEO.md`](01-INFORME-INVESTIGACION-SEO-AEO.md) | Síntesis de la investigación SEO/AEO global, con nivel de evidencia |
| [`02-ESTRATEGIA-100-IDIOMAS.md`](02-ESTRATEGIA-100-IDIOMAS.md) | Cómo llegar a los 100 idiomas: oleadas, modelo de priorización, puertas de salida, hub mínimo |
| [`03-TERMINOLOGIA-MOLDERIA-100-IDIOMAS.md`](03-TERMINOLOGIA-MOLDERIA-100-IDIOMAS.md) | Cómo se dice y se busca «molde de costura» en 113 idiomas (con nivel de confianza) |
| [`05-GUIA-AEO-OPERATIVA.md`](05-GUIA-AEO-OPERATIVA.md) | AEO operativo: contenido citable, bots, medición, protocolo mensual de auditoría de IA |
| [`CONTEXTO-NEGOCIO.md`](CONTEXTO-NEGOCIO.md) | Datos del negocio dados por la persona dueña |
| `data/` | `idiomas-master.csv` (113 idiomas), `oleadas.csv`, `terminologia-100-idiomas.csv/.json` (16 columnas por idioma, con URL de evidencia) |
| `plantillas/` | `robots.txt`, JSON-LD (`Product` digital, `Organization`), estructura de ficha, glosario base, prompts de auditoría de IA (11 idiomas), `CLAUDE.md.moldey` |
| `scripts/` | Python estándar: generar sitemaps con hreflang, validar hreflang, consolidar terminología, generar oleadas y el documento 03 |
| `research/raw/` | Informes crudos de los 7 temas (`T1`–`T7`), la 2.ª pasada de verificación (`V2-*`) y la terminología por grupo (`terminologia/`) |

## Léelo con estas advertencias (honestidad sobre la investigación)

- **No se auditó moldey.com.** Desde el entorno de investigación no hay acceso al sitio. Por eso el plan empieza con una auditoría real (Fase 0) y asume que hay que confirmar la plataforma, los 11 idiomas, la indexación y los pagos.
- **Método:** solo búsqueda web (sin poder abrir páginas, solo leer resúmenes de resultados) y con un tope de búsquedas por turno. Se hizo una **1.ª pasada** (16 agentes en paralelo, que agotaron el tope y dejaron casi toda la terminología sin verificar) y una **2.ª pasada de verificación** con presupuesto por agente (~160 búsquedas). Todo lo no verificado está marcado `[NO VERIFICADO]` o con confianza `baja`.
- **Terminología:** de 113 idiomas, **11 con confianza alta, 30 media y 72 baja** (inferidos por IA sin verificación web). **Nada de confianza baja/media debe publicarse sin revisión de un hablante nativo.**
- **La lista de «100 idiomas más hablados»** se reconstruyó de varias fuentes de Ethnologue (el orden exacto varía entre ediciones y no se pudo confirmar desde la posición ~20). Lo que importa es qué idiomas y en qué orden se atacan. Las 100 entradas son **72 idiomas con presencia web propia + 28 variedades** que se escriben con otro idioma; más 13 extras relevantes para moldería.
- **Los puntajes de priorización de idiomas son hipótesis**, no mediciones: reemplazarlos con Search Console, Keyword Planner, Trends, Wordstat y Naver.
- **Pagos, impuestos y legal:** no es asesoramiento legal ni fiscal. Validar con contador y abogado. Las disponibilidades de merchants of record para Argentina vienen de resúmenes de buscador: confirmar en la página oficial antes de abrir cuenta.
- **Privacidad del repositorio:** este repo puede ser **público**; el contenido describe tu estrategia de negocio (no contiene credenciales). Si preferís que no sea público, pasalo a privado en la configuración de GitHub.

## Verificar que los scripts funcionan

```bash
python3 scripts/generar_sitemaps_hreflang.py data/ejemplos/urls-ejemplo.csv /tmp/sm --base https://moldey.com
python3 scripts/validar_hreflang.py /tmp/sm/sitemap-*.xml
python3 scripts/consolidar_terminologia.py && python3 scripts/generar_oleadas.py && python3 scripts/generar_md_terminologia.py
```
