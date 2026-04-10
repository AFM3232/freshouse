---
name: Estructura interna de cotizaciones Excel Freshouse
description: Patrones de hojas, columnas y organización detectados en los archivos xlsx de cotizaciones de CLAUDE_SEX. Base para automatización y análisis comparativo.
type: project
---

Relevamiento realizado el 2026-03-24 sobre 6 archivos representativos.

## TIPO 1 — Cotización con APU integrado (más completo)
Archivos: COTIZACIÓN Y APU - ATLANTIS.xlsx, APU COTIZACIÓN - LOS CEDROS (ACTUALIZADO).xlsx, COTIZACIÓN - EDIFICIO EL MIRADOR.xlsx

Hojas típicas:
- Hoja de medidas / cantidades de obra (matriz dimensional: CARAS, PISOS, ML, H, M2)
- CUADRO GENERAL DE ACTIVIDADES o COTIZACIÓN (resumen por capítulos e ítems)
- APU por actividad (una hoja por actividad o todas agrupadas)
- RESUMEN APU (tabla consolidada de precios unitarios)

Columnas en hoja de cotización:
| Capitulo | Item | Descripcion/Actividad | Unidad | Cantidad | Vr Unitario | Vr Total/Valor Directo Actividad |

Columnas en hoja APU (estructura fija por bloque):
- I. EQUIPOS: DESCRIPCIÓN / UNIDAD / RENDIMIENTO / TARIFA / VALOR-PARCIAL
- II. MATERIALES: DESCRIPCIÓN / UNIDAD / CANTIDAD / PRECIO-UNIT / VALOR-PARCIAL
- III. TRANSPORTE: DESCRIPCIÓN / UNIDAD / RENDIMIENTO / TARIFA / VALOR-PARCIAL
- IV. MANO DE OBRA: DESCRIPCIÓN / UNIDAD / RENDIMIENTO / JORNAL / VALOR-PARCIAL
- Subtotales por sección + TOTAL APU + Desperdicio %

## TIPO 2 — Cotización simple por bloques/torres (sin APU detallado)
Archivos: COTIZACIÓN RESERVA DE LA COLINA 2025.xlsx, COTIZACIÓN BELMONTE.xlsx

Hojas: Una por bloque/torre (BLOQUE B, BLOQUE C, BLOQUE D)

Columnas:
| CAPT | ITEMS | ACTIVIDAD/DESCRIPCION | UNIDAD | CANTIDAD | VR UNITARIO | VALOR DIRECTO ACTIVIDAD |

Estructura de costos al pie:
- COSTO DIRECTO
- ADMON (% sobre costo directo — tipicamente 8%)
- UTILIDAD (% variable)
- IVA (sobre utilidad)
- VALOR TOTAL OFERTA

## TIPO 3 — APU con hoja de cantidades detallada (medición dimensional)
Archivos: APU FACHADA PRINCIPAL PORTAL DEL QUINDÍO.xlsx

Hojas: RESUMEN CANTIDADES / RESUMEN APU / CANTIDAD DE OBRA (con columnas: TORRE, FACHADA, SECCIÓN, DESCRIPCIÓN, ALTO, ANCHO, CANT, TOTAL M2, DESCUENTOS) / APU / hoja adicional ARCU

## PATRONES COMUNES DETECTADOS

Capítulos recurrentes en todas las cotizaciones:
1. PRELIMINARES (señalización, campamento, asesoría técnica)
2. DEMOLICIÓN Y PREPARACIÓN DE SUPERFICIE (lavado, remoción de texturas, mortero, acronal)
3. ACABADO DE PINTURA (Koraza Pro 550, Graniplast, elastomérica)
4. IMPERMEABILIZACIÓN (zonas húmedas, cubiertas, losas)
5. SELLADO (ventanería, dilataciones)
6. TERMINADO/LIMPIEZA

Actividades más frecuentes con sus unidades:
- Lavado General: M2, precio típico $1.500–$4.200/m2 (varía mucho entre versiones)
- Pintura Koraza Pro 550: M2, precio típico $15.000–$18.500/m2
- Reposición de Mortero: M2, precio ~$52.000/m2
- Sellado ventanería: ML, precio ~$5.200/ml
- Impermeabilización zonas anteriores: M2, precio ~$186.300/m2
- Graniplast (restitución): M2, precio ~$13.000–$37.000/m2 (rango amplio)

Materiales que aparecen con frecuencia en APUs:
- Koraza Pro 550 (CÑ de 19L): $450.000
- Hipoclorito: $35.000/GL
- Acronal: $32.500/GL
- Sikasit: $180.000/Kg
- Soudaflex: $21.000/Kg
- Mortero 1:3: $650.000/M3

Mano de obra:
- Oficial: jornal $130.000/día (dato 2025)
- Rendimiento lavado: 66 M2/día (aprox)
- Rendimiento pintura: 46 M2/día (aprox)

Errores/Inconsistencias detectadas:
- Archivo BELMONTE.xlsx: una hoja tiene encabezado "EDIFICIO ATLANTIS" en lugar de Belmonte (reuso de plantilla sin corregir nombre)
- Precios de lavado varían 1.500 vs 4.200 entre versiones del mismo proyecto (posible error de versión)
- Items duplicados (ej: ítem 1.1 aparece 3 veces en Belmonte con diferentes descripciones)

**Why:** Relevamiento solicitado por usuario el 2026-03-24.
**How to apply:** Usar estos patrones para validar coherencia de nuevas cotizaciones, automatizar extracción de datos y detectar errores en plantillas reutilizadas.
