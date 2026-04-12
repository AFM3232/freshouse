# FRESHOUSE — Índice Central

**Empresa:** Freshouse Ingeniería de Fachadas  
**Región:** Eje Cafetero — Colombia  
**Repo:** CLAUDE_SEXV2

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
| `CLAUDE/TEMPLATE_COTIZACION.html` | Template HTML base para cotizaciones |
| `CLAUDE/TEMPLATE_INFORME.html` | Template HTML base para informes |
| `CLAUDE/FRESHOUSE_APU_BASE.xlsx` | APU base en Excel |

---

## Flujo de trabajo

```
Editar en Mac (CLAUDE_SEX)  →  git push  →  GitHub  →  git pull  →  PC (CLAUDE_SEXV2)
```

Obsidian lee los archivos directamente del repo local — al hacer `git pull` aparecen automaticamente los cambios.
