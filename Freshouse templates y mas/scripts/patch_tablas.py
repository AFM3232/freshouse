#!/usr/bin/env python3
"""Patch estético completo de las tablas de cotización."""
import re

PATH = "/Users/andresmontoyaosorio/Documents/TRABAJO/CLAUDE_SEX/CLAUDE/cotizacion Torre Providencia II.html"
with open(PATH, encoding="utf-8") as f:
    html = f.read()

# ─── 1. OCULTAR MAPA DE OBRAS ──────────────────────────────────────────────
html = html.replace(
    '<div class="obras-map-wrap" id="obras-map-wrap">',
    '<div class="obras-map-wrap" id="obras-map-wrap" style="display:none">'
)

# ─── 2. CSS TABLAS — reemplazar bloque completo ────────────────────────────
OLD_CSS = """/* === TABLES === */
.table-wrap{border-radius:12px;overflow:hidden;border:1px solid var(--border-subtle);box-shadow:0 1px 4px rgba(13,27,46,0.05)}
table{width:100%;border-collapse:collapse;font-size:.82rem}
thead tr{background:var(--fh-blue-100)}
th{padding:.85rem 1rem;text-align:left;font-family:'JetBrains Mono',monospace;font-size:.58rem;font-weight:500;text-transform:uppercase;letter-spacing:.1em;color:var(--fh-blue-500);border-bottom:1px solid var(--border-blue)}
td{padding:.85rem 1rem;border-bottom:1px solid var(--border-subtle);color:var(--text-secondary);font-family:'Inter',sans-serif;transition:background .15s;background:#FFFFFF}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:var(--bg-base)}
td:first-child{color:var(--text-primary);font-weight:500}
td.num{font-family:'JetBrains Mono',monospace;text-align:right;color:var(--text-primary)}
td.unit{font-family:'JetBrains Mono',monospace;font-size:.75rem;color:var(--text-muted);text-align:center}
th.right{text-align:right}
th.center{text-align:center}
/* grupo header dentro de tabla unificada */
tr.grp-header td{background:var(--bg-elevated);font-family:'Space Grotesk',sans-serif;font-size:.78rem;font-weight:600;color:var(--text-primary);padding:.55rem 1rem;border-top:2px solid var(--border-blue);border-bottom:1px solid var(--border-blue)}
tr.grp-header td.grp-total{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--fh-orange);font-weight:600}
.grp-tag{font-family:'JetBrains Mono',monospace;font-size:.55rem;color:var(--fh-orange);background:var(--fh-orange-muted);border:1px solid var(--fh-orange-border);padding:.1rem .45rem;border-radius:4px;margin-right:.6rem;letter-spacing:.08em;vertical-align:middle}"""

NEW_CSS = """/* === TABLES === */
.table-wrap{border-radius:14px;overflow:hidden;border:1px solid var(--border-subtle);box-shadow:0 4px 24px rgba(13,27,46,.09),0 1px 4px rgba(13,27,46,.05)}
table{width:100%;border-collapse:collapse;font-size:.82rem}
thead tr{background:#0F2D5C}
th{padding:.8rem 1rem;text-align:left;font-family:'JetBrains Mono',monospace;font-size:.56rem;font-weight:500;text-transform:uppercase;letter-spacing:.1em;color:#93C5FD;border-bottom:none}
th.col-total{color:#FED7AA}
td{padding:.82rem 1rem;border-bottom:1px solid var(--border-subtle);color:var(--text-secondary);font-family:'Inter',sans-serif;transition:background .15s;background:#FFFFFF}
tr:last-child td{border-bottom:none}
tbody tr:not(.grp-header):hover td{background:#F5F8FF}
tbody tr:not(.grp-header):nth-child(even) td{background:#FAFBFF}
tbody tr:not(.grp-header):nth-child(even):hover td{background:#F0F4FF}
td:first-child{color:var(--text-primary);font-weight:500}
td.num{font-family:'JetBrains Mono',monospace;text-align:right;color:var(--text-primary);font-size:.8rem}
td.unit{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--text-muted);text-align:center;background:transparent!important}
th.right{text-align:right}
th.center{text-align:center}
/* grupo header */
tr.grp-header td{font-family:'Space Grotesk',sans-serif;font-size:.76rem;font-weight:600;color:var(--text-primary);padding:.6rem 1rem;border-top:none;border-bottom:1px solid var(--border-subtle)}
tr.grp-header td.grp-total{font-family:'JetBrains Mono',monospace;font-size:.72rem;font-weight:700;text-align:right}
.grp-tag{font-family:'JetBrains Mono',monospace;font-size:.52rem;font-weight:700;padding:.12rem .5rem;border-radius:4px;margin-right:.65rem;letter-spacing:.08em;vertical-align:middle;border:1px solid transparent}
/* cotizacion header */
.cot-header{display:flex;align-items:center;justify-content:space-between;padding:1rem 1.5rem;background:#FFFFFF;border-bottom:3px solid var(--fh-orange)}
.cot-header-logo{height:52px;display:block}
.cot-header-mid{flex:1;padding:0 2rem;text-align:center}
.cot-header-project{font-family:'Space Grotesk',sans-serif;font-size:.95rem;font-weight:700;color:var(--fh-blue-900)}
.cot-header-ref{font-family:'JetBrains Mono',monospace;font-size:.48rem;color:var(--text-muted);letter-spacing:.1em;text-transform:uppercase;margin-top:3px}
.cot-badge{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:.52rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.25rem .8rem;border-radius:999px;color:#fff}
.cot-badge--blue{background:var(--fh-blue-400)}
.cot-badge--orange{background:var(--fh-orange)}
.cot-badge--purple{background:#4338CA}"""

html = html.replace(OLD_CSS, NEW_CSS)

# ─── 3. CABECERA TABLA 1 ──────────────────────────────────────────────────
OLD_H1 = """    <!-- CABECERA BICOLOR -->
    <div style="display:flex;align-items:stretch;border-bottom:3px solid #F97316;overflow:hidden">
      <div style="background:#FFFFFF;padding:.9rem 1.4rem;display:flex;align-items:center;border-right:2px solid #E4EDF8;flex-shrink:0">
        <img id="fh-logo-tabla" class="fh-logo-copy" src="" style="height:50px;display:block" onerror="this.style.display='none'">
      </div>
      <div style="background:linear-gradient(135deg,#0A1628,#0F2D5C);flex:1;padding:.9rem 1.4rem;display:flex;align-items:center;justify-content:space-between">
        <div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.38);letter-spacing:.1em;text-transform:uppercase">Armenia · Quindío</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.38);letter-spacing:.1em;text-transform:uppercase;margin-top:3px">NIT 901.234.567-0</div>
        </div>
        <div style="text-align:right">
          <div style="font-family:'Space Grotesk',sans-serif;font-size:.95rem;font-weight:600;color:#FFFFFF">Torre Providencia II</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.45);letter-spacing:.1em;text-transform:uppercase;margin-top:3px">Ref. FH-F-02 · Válido 13/04/2026</div>
          <div style="display:inline-block;margin-top:.45rem;background:#F97316;color:#fff;font-family:'JetBrains Mono',monospace;font-size:.52rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.22rem .7rem;border-radius:999px">Cotización 1</div>
        </div>
      </div>
    </div>"""

NEW_H1 = """    <!-- CABECERA COTIZACIÓN 1 -->
    <div class="cot-header">
      <img id="fh-logo-tabla" class="fh-logo-copy cot-header-logo" src="" onerror="this.style.display='none'">
      <div class="cot-header-mid">
        <div class="cot-header-project">Torre Providencia II</div>
        <div class="cot-header-ref">Armenia · Quindío &nbsp;·&nbsp; NIT 901.234.567-0 &nbsp;·&nbsp; Ref. FH-F-02</div>
      </div>
      <div style="text-align:right">
        <div style="font-family:'JetBrains Mono',monospace;font-size:.48rem;color:var(--text-muted);letter-spacing:.1em;text-transform:uppercase;margin-bottom:.4rem">Válido 13/04/2026</div>
        <span class="cot-badge cot-badge--orange">Cotización 1</span>
      </div>
    </div>"""

html = html.replace(OLD_H1, NEW_H1)

# ─── 4. CABECERA TABLA 2 ──────────────────────────────────────────────────
OLD_H2 = """    <!-- CABECERA BICOLOR -->
    <div style="display:flex;align-items:stretch;border-bottom:3px solid #F97316;overflow:hidden">
      <div style="background:#FFFFFF;padding:.9rem 1.4rem;display:flex;align-items:center;border-right:2px solid #E4EDF8;flex-shrink:0">
        <img id="fh-logo-alt2" class="fh-logo-copy" src="" style="height:50px;display:block" onerror="this.style.display='none'">
      </div>
      <div style="background:linear-gradient(135deg,#0A1628,#0F2D5C);flex:1;padding:.9rem 1.4rem;display:flex;align-items:center;justify-content:space-between">
        <div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.38);letter-spacing:.1em;text-transform:uppercase">Armenia · Quindío</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.38);letter-spacing:.1em;text-transform:uppercase;margin-top:3px">NIT 901.234.567-0</div>
        </div>
        <div style="text-align:right">
          <div style="font-family:'Space Grotesk',sans-serif;font-size:.95rem;font-weight:600;color:#FFFFFF">Torre Providencia II</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.45);letter-spacing:.1em;text-transform:uppercase;margin-top:3px">Ref. FH-F-02B · Válido 13/04/2026</div>
          <div style="display:inline-block;margin-top:.45rem;background:#F97316;color:#fff;font-family:'JetBrains Mono',monospace;font-size:.52rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.22rem .7rem;border-radius:999px">Cotización 2</div>
        </div>
      </div>
    </div>"""

NEW_H2 = """    <!-- CABECERA COTIZACIÓN 2 -->
    <div class="cot-header">
      <img id="fh-logo-alt2" class="fh-logo-copy cot-header-logo" src="" onerror="this.style.display='none'">
      <div class="cot-header-mid">
        <div class="cot-header-project">Torre Providencia II</div>
        <div class="cot-header-ref">Armenia · Quindío &nbsp;·&nbsp; NIT 901.234.567-0 &nbsp;·&nbsp; Ref. FH-F-02B</div>
      </div>
      <div style="text-align:right">
        <div style="font-family:'JetBrains Mono',monospace;font-size:.48rem;color:var(--text-muted);letter-spacing:.1em;text-transform:uppercase;margin-bottom:.4rem">Válido 13/04/2026</div>
        <span class="cot-badge cot-badge--blue">Cotización 2</span>
      </div>
    </div>"""

html = html.replace(OLD_H2, NEW_H2)

# ─── 5. CABECERA TABLA 3 ──────────────────────────────────────────────────
OLD_H3 = """    <!-- CABECERA BICOLOR -->
    <div style="display:flex;align-items:stretch;border-bottom:3px solid #F97316;overflow:hidden">
      <div style="background:#FFFFFF;padding:.9rem 1.4rem;display:flex;align-items:center;border-right:2px solid #E4EDF8;flex-shrink:0">
        <img id="fh-logo-cot3" class="fh-logo-copy" src="" style="height:50px;display:block" onerror="this.style.display='none'">
      </div>
      <div style="background:linear-gradient(135deg,#0A1628,#0F2D5C);flex:1;padding:.9rem 1.4rem;display:flex;align-items:center;justify-content:space-between">
        <div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.38);letter-spacing:.1em;text-transform:uppercase">Armenia · Quindío</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.38);letter-spacing:.1em;text-transform:uppercase;margin-top:3px">NIT 901.234.567-0</div>
        </div>
        <div style="text-align:right">
          <div style="font-family:'Space Grotesk',sans-serif;font-size:.95rem;font-weight:600;color:#FFFFFF">Torre Providencia II</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:.5rem;color:rgba(255,255,255,.45);letter-spacing:.1em;text-transform:uppercase;margin-top:3px">Ref. FH-F-02C · Válido 13/04/2026</div>
          <div style="display:inline-block;margin-top:.45rem;background:#4338CA;color:#fff;font-family:'JetBrains Mono',monospace;font-size:.52rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.22rem .7rem;border-radius:999px">Cotización 3</div>
        </div>
      </div>
    </div>"""

NEW_H3 = """    <!-- CABECERA COTIZACIÓN 3 -->
    <div class="cot-header">
      <img id="fh-logo-cot3" class="fh-logo-copy cot-header-logo" src="" onerror="this.style.display='none'">
      <div class="cot-header-mid">
        <div class="cot-header-project">Torre Providencia II</div>
        <div class="cot-header-ref">Armenia · Quindío &nbsp;·&nbsp; NIT 901.234.567-0 &nbsp;·&nbsp; Ref. FH-F-02C</div>
      </div>
      <div style="text-align:right">
        <div style="font-family:'JetBrains Mono',monospace;font-size:.48rem;color:var(--text-muted);letter-spacing:.1em;text-transform:uppercase;margin-bottom:.4rem">Válido 13/04/2026</div>
        <span class="cot-badge cot-badge--purple">Cotización 3</span>
      </div>
    </div>"""

html = html.replace(OLD_H3, NEW_H3)

# ─── 6. GRUPO HEADERS — reemplazar estilos inline por clases limpias ───────

# GRP-1 Preliminares (azul)
html = html.replace(
    '<tr class="grp-header" style="background:linear-gradient(90deg,#0F2D5C,#1A52A8)">\n          <td colspan="5" style="color:#FFFFFF"><span class="grp-tag">GRP-1</span>Preliminares</td>\n          <td class="num grp-total" style="color:#FCD34D">$1.600.000</td>',
    '<tr class="grp-header" style="background:#EEF3FD;border-left:4px solid #1A52A8">\n          <td colspan="5"><span class="grp-tag" style="background:#DBEAFE;border-color:#93C5FD;color:#1D4ED8">GRP-1</span>Preliminares</td>\n          <td class="num grp-total" style="color:#1A52A8">$1.600.000</td>'
)

# GRP-2 Limpieza (teal)
html = html.replace(
    '<tr class="grp-header" style="background:linear-gradient(90deg,#134E4A,#0D9488)">\n          <td colspan="5" style="color:#FFFFFF"><span class="grp-tag" style="background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#FFFFFF">GRP-2</span>Limpieza y Alistamiento de Superficies</td>\n          <td class="num grp-total" style="color:#FCD34D">$13.325.682</td>',
    '<tr class="grp-header" style="background:#F0F9F8;border-left:4px solid #0D9488">\n          <td colspan="5"><span class="grp-tag" style="background:#CCFBF1;border-color:#5EEAD4;color:#0F766E">GRP-2</span>Limpieza y Alistamiento de Superficies</td>\n          <td class="num grp-total" style="color:#0D9488">$13.325.682</td>'
)

# GRP-3 Pintura (naranja)
html = html.replace(
    '<tr class="grp-header" style="background:linear-gradient(90deg,#7C2D12,#EA580C)">\n          <td colspan="5" style="color:#FFFFFF"><span class="grp-tag" style="background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#FFFFFF">GRP-3</span>Obras de Pintura en Muros de Fachada e Impermeabilizaci&#243;n</td>\n          <td class="num grp-total" style="color:#FCD34D">$74.136.144</td>',
    '<tr class="grp-header" style="background:#FFF7ED;border-left:4px solid #EA580C">\n          <td colspan="5"><span class="grp-tag" style="background:#FED7AA;border-color:#FB923C;color:#C2410C">GRP-3</span>Obras de Pintura en Muros de Fachada e Impermeabilizaci&#243;n</td>\n          <td class="num grp-total" style="color:#EA580C">$74.136.144</td>'
)

# GRP-4 Terminado (índigo)
html = html.replace(
    '<tr class="grp-header" style="background:linear-gradient(90deg,#1E1B4B,#4338CA)">\n          <td colspan="5" style="color:#FFFFFF"><span class="grp-tag" style="background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#FFFFFF">GRP-4</span>Terminado y Limpieza</td>\n          <td class="num grp-total" style="color:#FCD34D">$2.500.000</td>',
    '<tr class="grp-header" style="background:#F0EFFE;border-left:4px solid #4338CA">\n          <td colspan="5"><span class="grp-tag" style="background:#E0E7FF;border-color:#A5B4FC;color:#3730A3">GRP-4</span>Terminado y Limpieza</td>\n          <td class="num grp-total" style="color:#4338CA">$2.500.000</td>'
)

# GRP-1 Cot2 Preparación (teal)
html = html.replace(
    '<tr class="grp-header" style="background:linear-gradient(90deg,#134E4A,#0D9488)">\n          <td colspan="5" style="color:#FFFFFF"><span class="grp-tag" style="background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#FFFFFF">GRP-1</span>Preparación de Superficies</td>\n          <td class="num grp-total" style="color:#FCD34D">$1.323.000</td>',
    '<tr class="grp-header" style="background:#F0F9F8;border-left:4px solid #0D9488">\n          <td colspan="5"><span class="grp-tag" style="background:#CCFBF1;border-color:#5EEAD4;color:#0F766E">GRP-1</span>Preparación de Superficies</td>\n          <td class="num grp-total" style="color:#0D9488">$1.323.000</td>'
)

# GRP-2 Cot2 Sikalastic (naranja)
html = html.replace(
    '<tr class="grp-header" style="background:linear-gradient(90deg,#7C2D12,#EA580C)">\n          <td colspan="5" style="color:#FFFFFF"><span class="grp-tag" style="background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#FFFFFF">GRP-2</span>Impermeabilizaci&#243;n con Sikalastic 617</td>\n          <td class="num grp-total" style="color:#FCD34D">$17.370.000</td>',
    '<tr class="grp-header" style="background:#FFF7ED;border-left:4px solid #EA580C">\n          <td colspan="5"><span class="grp-tag" style="background:#FED7AA;border-color:#FB923C;color:#C2410C">GRP-2</span>Impermeabilizaci&#243;n con Sikalastic 617</td>\n          <td class="num grp-total" style="color:#EA580C">$17.370.000</td>'
)

# GRP-1 Cot3 Parqueadero (índigo)
html = html.replace(
    '<tr class="grp-header" style="background:linear-gradient(90deg,#1E1B4B,#4338CA)">\n          <td colspan="5" style="color:#FFFFFF"><span class="grp-tag" style="background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#FFFFFF">GRP-1</span>Pintura — Parqueadero</td>\n          <td class="num grp-total" style="color:#FCD34D">$4.582.648</td>',
    '<tr class="grp-header" style="background:#F0EFFE;border-left:4px solid #4338CA">\n          <td colspan="5"><span class="grp-tag" style="background:#E0E7FF;border-color:#A5B4FC;color:#3730A3">GRP-1</span>Pintura — Parqueadero</td>\n          <td class="num grp-total" style="color:#4338CA">$4.582.648</td>'
)

# ─── 7. THEAD — quitar inline styles que sobreescriben el nuevo CSS ────────
# Table 1, 2, 3 thead overrides
html = html.replace(
    '<tr style="background:linear-gradient(90deg,#0F2D5C,#1A52A8)">\n          <th style="width:3rem;color:#93C5FD">Ítem</th>\n          <th style="color:#93C5FD">Descripción</th>\n          <th class="center" style="width:4rem;color:#93C5FD">Und</th>\n          <th class="right" style="width:5rem;color:#93C5FD">Cant.</th>\n          <th class="right" style="width:7rem;color:#93C5FD">V. Unitario</th>\n          <th class="right" style="width:7rem;color:#F97316">V. Total</th>',
    '<tr>\n          <th style="width:3rem">Ítem</th>\n          <th>Descripción</th>\n          <th class="center" style="width:4rem">Und</th>\n          <th class="right" style="width:5rem">Cant.</th>\n          <th class="right" style="width:7rem">V. Unitario</th>\n          <th class="right col-total" style="width:7rem">V. Total</th>'
)

# ─── 8. TOTALS-WRAP — actualizar max-width inline ─────────────────────────
html = html.replace('style="max-width:500px"', 'style="max-width:480px"')

with open(PATH, "w", encoding="utf-8") as f:
    f.write(html)
print("OK — todos los parches aplicados")
