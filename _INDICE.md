# FRESHOUSE — Índice Central

**Empresa:** Freshouse Ingeniería de Fachadas  
**Región:** Eje Cafetero — Colombia

---

## Repositorios

| Repo | Contenido | URL |
|---|---|---|
| `freshouse` | Documentos: cotizaciones, informes, obras, presentaciones | github.com/AFM3232/freshouse |
| `freshouse-web` | Página web: index.html, logos, media, vercel.json | github.com/AFM3232/freshouse-web |

---

## Estructura del repositorio

```
CLAUDE/
  cotizaciones/       — Cotizaciones generadas (HTML, xlsx)
  informes/           — Informes y presentaciones HTML
  informes/media/     — Fotos comprimidas para presentaciones (~26 MB)
  marketing/          — Brochure, mapa de obras
  media/              — Fotos ORIGINALES sin comprimir (~393 MB, solo local)
  scripts/            — Scripts Python para generar documentos
  templates/          — Templates base (HTML, xlsx)
FRESHOUSE/            — Base de conocimiento (costos, estructura, inventario)
OBRAS/                — Documentos por obra (cotizaciones, contratos, informes)
```

---

## Base de conocimiento

| Documento | Descripción |
|---|---|
| [[FRESHOUSE/base_de_costos_apu\|Base de Costos APU]] | Precios de mano de obra, materiales e insumos. Fuente de verdad para cotizaciones. |
| [[FRESHOUSE/estructura_cotizaciones_excel\|Estructura Cotizaciones Excel]] | Patrones de hojas y columnas detectados en los xlsx. Base para automatización. |
| [[FRESHOUSE/inventario_proyectos\|Inventario de Proyectos]] | Lista de 40+ obras con archivos xlsx disponibles. |

---

## Obras activas

| Obra                 | Carpeta                       |
| -------------------- | ----------------------------- |
| ATLANTIS             | `OBRAS/ATLANTIS/`             |
| LOS CEDROS           | `OBRAS/LOS CEDROS/`           |

---

## Templates y herramientas

| Archivo | Descripción |
|---|---|
| `CLAUDE/templates/TEMPLATE_COTIZACION.html` | Template HTML base para cotizaciones |
| `CLAUDE/templates/TEMPLATE_INFORME.html` | Template HTML base para informes |
| `CLAUDE/templates/FRESHOUSE_APU_BASE.xlsx` | APU base en Excel |

---

## Media

| Carpeta | Contenido | Tamaño |
|---|---|---|
| `CLAUDE/media/` | Fotos originales (alta calidad, solo local) | ~393 MB |
| `CLAUDE/informes/media/` | Fotos comprimidas (usadas en presentaciones HTML) | ~26 MB |

> Los originales NO se suben al repo git por su peso.
> Las comprimidas son las que referencian las presentaciones.

---

## Flujo de trabajo

```
Editar en Mac (CLAUDE_SEX)  →  git push  →  GitHub  →  git pull  →  PC (CLAUDE_SEXV2)
```

Obsidian lee los archivos directamente del repo local — al hacer `git pull` aparecen automaticamente los cambios.
