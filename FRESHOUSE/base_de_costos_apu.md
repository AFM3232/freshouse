# BASE DE DATOS DE COSTOS — APU SIMPLIFICADO
**Empresa:** Mantenimiento de edificios, pintura, acabados, cubiertas e impermeabilización  
**Región:** Eje Cafetero — Colombia  
**Sistema de pago:** Mano de obra por DESTAJO (unidad ejecutada)  
**Versión:** 1.0  
**Fecha:** 2025  

---

> ⚠️ **INSTRUCCIONES PARA IA — LEER PRIMERO**
> 
> 1. **No inventes datos.** Usa únicamente los valores registrados en este archivo.
> 2. **Si falta un dato** (precio, rendimiento, consumo), detente y pídelo al usuario antes de calcular.
> 3. **Este archivo es la fuente de verdad.** Priorízalo sobre cualquier dato externo o de entrenamiento.
> 4. **El margen de utilidad es una variable.** Siempre preguntarlo al usuario antes de generar una cotización.
> 5. **Herramienta menor** se aplica siempre como **5% sobre el costo directo** (mano de obra + materiales).
> 6. **Accesorios de cubierta** se aplican como **8% sobre el costo de materiales de cubierta**.
> 7. Cuando un producto tiene varias opciones (marca, referencia), pregunta al usuario cuál aplicar.
> 8. Cuando una actividad tiene subactividades opcionales (ej: Corrotec), pregunta si aplica.

---

## SECCIÓN 1 — MANO DE OBRA (DESTAJOS)

> Jornal de referencia: **$140.000/día**  
> Todos los valores son en COP (pesos colombianos).

| # | Actividad | Descripción | Unidad | Costo Destajo |
|---|-----------|-------------|--------|---------------|
| MO-01 | Pintura exterior | 2 manos sobre muros/fachadas | m² | $6.000 |
| MO-02 | Pintura interior | 2 manos sobre muros interiores | m² | $5.000 |
| MO-03 | Pintura sobre metales | 2 manos sobre barandas y elementos metálicos | m² | $5.000 |
| MO-04 | Hidrolavado | Cualquier superficie (muros, fachadas, cubiertas, pisos) | m² | $400 |
| MO-05 | Retiro de mortero quemado | Picado y retiro de mortero deteriorado | m² | $10.000 |
| MO-06 | Aplicación de pañete | Aplicación de mortero/pañete de reemplazo | m² | $10.000 |
| MO-07 | Resane fino | Aplicación de Graniplast o Silcoplast sobre pañete | m² | $10.000 |
| MO-08 | Impermeabilización líquida | 2 manos de impermeabilizante líquido | m² | $6.000 |
| MO-09 | Impermeabilización con membrana | Instalación de membrana impermeabilizante | m² | $6.000 |
| MO-12 | Sello de ventanas (PU Flex) | Sellado de juntas y marcos de ventanas | ml | $2.500 |
| MO-13 | Instalación cielo raso Superboard | 2 manos / instalación completa | m² | $6.000 |
| MO-10 | Retiro de cubierta existente | Desmonte de teja (fibrocemento o uPVC) | m² | $6.500 |
| MO-11 | Instalación de cubierta | Instalación de teja + caballete incluido (fibrocemento o uPVC) | m² | $7.000 |

> **Nota MO-05 + MO-06:** En cotizaciones de pañete completo, estas dos actividades van juntas = **$20.000/m²**

---

## SECCIÓN 2 — MATERIALES

> Todos los precios son en COP. Precios de compra sin IVA (verificar con proveedor).

### 2.1 Pinturas para muros — Exterior

| Código | Producto | Presentación | Precio | Precio/Galón | Rendimiento (2 manos) |
|--------|----------|-------------|--------|--------------|-----------------------|
| MAT-P01 | Koraza Pro 550 | Cuñete 5 gal | $476.800 | $95.360 | 13 m²/gal |
| MAT-P02 | Koraza Sol y Lluvia impermeabilizante | Cuñete 5 gal | $564.200 | $112.840 | 13 m²/gal |
| MAT-P03 | Koraza Elastomérica | Cuñete 5 gal | $635.500 | $127.100 | 8 m²/gal |

### 2.2 Pinturas para muros — Interior

| Código | Producto | Presentación | Precio | Precio/Galón | Rendimiento (2 manos) |
|--------|----------|-------------|--------|--------------|-----------------------|
| MAT-P04 | Viniltex Advanced | Cuñete 5 gal | $380.000 | $76.000 | 20 m²/gal |
| MAT-P05 | Viniltex Pro 450 | Cuñete 5 gal | $355.300 | $71.060 | 20 m²/gal |
| MAT-P06 | ICO Tipo 1 | Cuñete 5 gal | $240.800 | $48.160 | 20 m²/gal |
| MAT-P07 | ICO Tipo 2 | Cuñete 5 gal | $182.250 | $36.450 | 20 m²/gal |
| MAT-P08 | ICO Tipo 3 | Cuñete 5 gal | $109.200 | $21.840 | 20 m²/gal |

> **Nota:** El rendimiento de 100 m²/cuñete (5 gal) = 20 m²/galón aplica para todas las pinturas interiores listadas.

### 2.3 Pinturas para metales

| Código | Producto | Presentación | Precio/Galón | Rendimiento (2 manos) | Uso |
|--------|----------|-------------|--------------|----------------------|-----|
| MAT-P09 | Pintulux 3 en 1 | Galón | $121.850 | 15 m²/gal | Pintura final metales |
| MAT-P10 | Pintulux Máxima Protección Metalizados | Galón | $124.511 | 15 m²/gal | Pintura final metales |
| MAT-P11 | Pintulux Máxima Protección Colores | Galón | $109.381 | 15 m²/gal | Pintura final metales |
| MAT-P12 | Corrotec Anticorrosivo | Galón | $69.331 | 70 m²/gal (1 mano) | Base anticorrosiva — USO SITUACIONAL |

### 2.4 Imprimantes y bases

| Código | Producto | Presentación | Precio | Precio/Galón | Uso / Dilución |
|--------|----------|-------------|--------|--------------|----------------|
| MAT-I01 | Acrolatex | Cuñete 5 gal | $386.447 | $77.289 | Imprimante exterior / base resanes. Dilución 1:3 con agua → rinde ~160 m²/gal efectivo |

### 2.5 Impermeabilizantes

| Código | Producto | Presentación | Precio | Precio/m² (material) | Rendimiento |
|--------|----------|-------------|--------|----------------------|-------------|
| MAT-IM01 | Pintuco Fill 7 | Cuñete 5 gal | $279.449 | $7.984 | 7 m²/gal → 35 m²/cuñete |
| MAT-IM02 | Sikalastic 617 | Cuñete 27.5 kg | $1.700.000 | $123.636 | 2 kg/m² → 13.75 m²/cuñete |

> **Cálculo Pintuco Fill 7:** $279.449 ÷ 35 m² = **$7.984/m²**  
> **Cálculo Sikalastic 617:** $1.700.000 ÷ 13.75 m² = **$123.636/m²** ($61.818/kg × 2 kg/m²)

### 2.6 Morteros y pañetes

| Código | Producto | Presentación | Precio | Precio/m² (material) | Rendimiento |
|--------|----------|-------------|--------|----------------------|-------------|
| MAT-M01 | Mortero listo Impadoc | Bulto | $35.077 | $5.846 | 6 m²/bulto |
| MAT-M02 | Estuka / Pañete en polvo | Bulto | $55.000 | $9.167 | 6 m²/bulto |
| MAT-M03 | Graniplast / Silcoplast (resane) | Cuñete 5 gal | $80.000 | $11.429 | 7 m²/cuñete |

> **MAT-M01 y MAT-M02** son productos equivalentes (mismo uso, mismo rendimiento). MAT-M01 es la opción económica.

### 2.7 Cubiertas

| Código | Producto | Presentación | Precio | Precio/m² |
|--------|----------|-------------|--------|-----------|
| MAT-C01 | Teja fibrocemento #7 | m² | $37.000 | $37.000 |
| MAT-C02 | Teja uPVC 1.8mm | Lámina 11.8×1.1m (12.98 m²) | $279.000 | $21.495 |
| MAT-C03 | Teja uPVC 2.0mm | Lámina 11.8×1.1m (12.98 m²) | $310.000 | $23.883 |
| MAT-C04 | Teja uPVC 2.5mm | Lámina 11.8×1.1m (12.98 m²) | $360.000 | $27.735 |

> **Accesorios de cubierta** (tornillería, fijaciones, caballete, traslapos): **8% sobre costo total de materiales de cubierta**

### 2.8 Superboard (cielos rasos y reparación de volúmenes)

| Código | Producto | Espesor | Precio/Lámina | Área lámina | Precio/m² |
|--------|----------|---------|---------------|-------------|-----------|
| MAT-S01 | Superboard | 6mm | $67.600 | 2.98 m² | $22.685 |
| MAT-S02 | Superboard | 8mm | $79.000 | 2.98 m² | $26.510 |
| MAT-S03 | Superboard | 10mm | $107.700 | 2.98 m² | $36.141 |
| MAT-S04 | Superboard | 14mm | $157.800 | 2.98 m² | $52.953 |

> **Área lámina estándar:** 1.22 m × 2.44 m = 2.98 m²

### 2.9 Estructura para cielos rasos

| Código | Producto | Precio/Pieza | Longitud pieza | Consumo (estructura cruzada 60×60cm) | Costo/m² |
|--------|----------|-------------|----------------|--------------------------------------|----------|
| MAT-E01 | Omega | $3.535 | 6 m estándar | 0.56 piezas/m² | $1.980 |
| MAT-E02 | Vigueta | $3.535 | 6 m estándar | 0.56 piezas/m² | $1.980 |

> **Sistema:** Estructura cruzada con separaciones de 60 cm en ambas direcciones  
> **Costo estructura completa/m²:** $3.960 (sin Superboard)

### 2.10 Insumos varios

| Código | Producto | Unidad | Precio | Rendimiento | Costo/m² |
|--------|----------|--------|--------|-------------|----------|
| MAT-V01 | Hipoclorito 70% | Kilo | $14.000 | 1.000 m²/kg | $14 |
| MAT-V02 | Hipoclorito 70% | Libra | $9.000 | ~500 m²/lb | $18 |
| MAT-V03 | PU Flex (sello) | Tubo | $19.660 | 30 ml (metros lineales) | $655/ml |
| MAT-V04 | Thinner | Galón | $25.500 | Variable | — |

---

## SECCIÓN 3 — CONSUMOS POR ACTIVIDAD (APUs SIMPLIFICADOS)

> **Herramienta menor:** 5% sobre costo directo (mano de obra + materiales) — se aplica en TODOS los APUs.

---

### APU-01 — Hidrolavado de superficies

| Componente | Producto | Cantidad | Unidad | Costo Unit. | Costo/m² |
|------------|----------|----------|--------|-------------|----------|
| Mano de obra | Hidrolavado (MO-04) | 1 | m² | $400 | $400 |
| Material | Hipoclorito 70% (MAT-V01) | 0.001 | kg | $14.000 | $14 |
| **Costo directo** | | | | | **$414** |
| Herramienta menor | 5% sobre costo directo | | | | $21 |
| **COSTO TOTAL/m²** | | | | | **$435** |

---

### APU-02 — Pintura exterior (2 manos) — Por producto

> Usar precio/galón del producto seleccionado. Preguntar al usuario qué producto aplica.

**Fórmula:**
```
Costo material/m² = Precio galón ÷ Rendimiento (m²/gal)
Costo directo/m²  = Mano de obra (MO-01) + Costo material/m²
Herramienta menor = Costo directo × 5%
COSTO TOTAL/m²    = Costo directo + Herramienta menor
```

| Producto | Precio/gal | Rend. | Costo mat/m² | MO | Costo directo | H.M. 5% | **TOTAL/m²** |
|----------|-----------|-------|-------------|-----|--------------|---------|-------------|
| Koraza Pro 550 | $95.360 | 13 m² | $7.335 | $6.000 | $13.335 | $667 | **$14.002** |
| Koraza Sol y Lluvia | $112.840 | 13 m² | $8.680 | $6.000 | $14.680 | $734 | **$15.414** |
| Koraza Elastomérica | $127.100 | 8 m² | $15.888 | $6.000 | $21.888 | $1.094 | **$22.982** |

> **Con Acrolatex como imprimante previo (situacional):** Agregar $77.289 ÷ 160 m² = **$483/m²** adicional

---

### APU-03 — Pintura interior (2 manos) — Por producto

**Fórmula:** igual a APU-02 con MO-02 ($5.000)

| Producto | Precio/gal | Rend. | Costo mat/m² | MO | Costo directo | H.M. 5% | **TOTAL/m²** |
|----------|-----------|-------|-------------|-----|--------------|---------|-------------|
| Viniltex Advanced | $76.000 | 20 m² | $3.800 | $5.000 | $8.800 | $440 | **$9.240** |
| Viniltex Pro 450 | $71.060 | 20 m² | $3.553 | $5.000 | $8.553 | $428 | **$8.981** |
| ICO Tipo 1 | $48.160 | 20 m² | $2.408 | $5.000 | $7.408 | $370 | **$7.778** |
| ICO Tipo 2 | $36.450 | 20 m² | $1.823 | $5.000 | $6.823 | $341 | **$7.164** |
| ICO Tipo 3 | $21.840 | 20 m² | $1.092 | $5.000 | $6.092 | $305 | **$6.397** |

---

### APU-04 — Pintura sobre metales (2 manos)

> Corrotec es SITUACIONAL. Preguntar si aplica antes de calcular.

| Componente | Producto | Costo/m² |
|------------|----------|----------|
| Mano de obra | MO-03 | $5.000 |
| Material pintura | Pintulux (ver opciones) | Ver tabla |
| Material base (opcional) | Corrotec: $69.331 ÷ 70 m² | $990 |

| Producto final | Precio/gal | Rend. | Mat/m² | MO | Base (opc.) | Directo | H.M. 5% | **TOTAL/m²** |
|---------------|-----------|-------|--------|-----|------------|---------|---------|-------------|
| Pintulux 3 en 1 (sin base) | $121.850 | 15 m² | $8.123 | $5.000 | — | $13.123 | $656 | **$13.779** |
| Pintulux 3 en 1 (con Corrotec) | $121.850 | 15 m² | $8.123 | $5.000 | $990 | $14.113 | $706 | **$14.819** |
| Pintulux Máx. Prot. Metalizados (sin base) | $124.511 | 15 m² | $8.301 | $5.000 | — | $13.301 | $665 | **$13.966** |
| Pintulux Máx. Prot. Colores (sin base) | $109.381 | 15 m² | $7.292 | $5.000 | — | $12.292 | $615 | **$12.907** |

---

### APU-05 — Retiro de mortero quemado + Aplicación de pañete

> Estas dos actividades van siempre juntas en cotización.

| Componente | Producto | Cantidad | Unidad | Costo Unit. | Costo/m² |
|------------|----------|----------|--------|-------------|----------|
| Mano de obra retiro | MO-05 | 1 | m² | $10.000 | $10.000 |
| Mano de obra pañete | MO-06 | 1 | m² | $10.000 | $10.000 |
| Material opción A | Mortero Impadoc (MAT-M01) | 1/6 bulto | m² | $35.077 | $5.846 |
| Material opción B | Estuka/Pañete en polvo (MAT-M02) | 1/6 bulto | m² | $55.000 | $9.167 |

| Opción material | Costo directo | H.M. 5% | **TOTAL/m²** |
|----------------|--------------|---------|-------------|
| Con Mortero Impadoc | $25.846 | $1.292 | **$27.138** |
| Con Estuka/Pañete | $29.167 | $1.458 | **$30.625** |

---

### APU-06 — Resane fino (Graniplast / Silcoplast)

| Componente | Producto | Cantidad | Costo/m² |
|------------|----------|----------|----------|
| Mano de obra | MO-07 | 1 m² | $10.000 |
| Material | Graniplast/Silcoplast (MAT-M03) | 1/7 cuñete | $11.429 |
| **Costo directo** | | | **$21.429** |
| Herramienta menor | 5% | | $1.071 |
| **TOTAL/m²** | | | **$22.500** |

---

### APU-07 — Impermeabilización líquida (2 manos)

> Preguntar al usuario qué producto aplica antes de calcular.

| Componente | Pintuco Fill 7 | Sikalastic 617 |
|------------|---------------|----------------|
| Mano de obra (MO-08) | $6.000 | $6.000 |
| Material/m² | $7.984 | $123.636 |
| **Costo directo** | **$13.984** | **$129.636** |
| Herramienta menor 5% | $699 | $6.482 |
| **TOTAL/m²** | **$14.683** | **$136.118** |

---

### APU-08 — Cubierta nueva (retiro + instalación)

> Preguntar: ¿incluye retiro de cubierta existente? ¿Qué tipo de teja?

**Fórmula:**
```
Costo material/m²  = Precio teja/m²
Accesorios         = Costo material × 8%
Mano de obra       = MO-10 (retiro, si aplica) + MO-11 (instalación)
Costo directo      = MO + material + accesorios
Herramienta menor  = Costo directo × 5%
COSTO TOTAL/m²     = Costo directo + Herramienta menor
```

| Teja | Precio/m² | Accesorios 8% | MO solo inst. | MO retiro+inst. | Directo (inst.) | H.M. 5% | **TOTAL inst./m²** | **TOTAL retiro+inst./m²** |
|------|-----------|--------------|--------------|----------------|----------------|---------|-------------------|--------------------------|
| Fibrocemento #7 | $37.000 | $2.960 | $7.000 | $13.500 | $46.960 | $2.348 | **$49.308** | **$55.808** |
| uPVC 1.8mm | $21.495 | $1.720 | $7.000 | $13.500 | $30.215 | $1.511 | **$31.726** | **$38.226** |
| uPVC 2.0mm | $23.883 | $1.911 | $7.000 | $13.500 | $32.794 | $1.640 | **$34.434** | **$40.934** |
| uPVC 2.5mm | $27.735 | $2.219 | $7.000 | $13.500 | $36.954 | $1.848 | **$38.802** | **$45.302** |

---

### APU-09 — Cielo raso en Superboard (estructura cruzada)

> Preguntar qué espesor de Superboard aplica.

| Componente | Detalle | Costo/m² |
|------------|---------|----------|
| Mano de obra | MO-13 instalación cielo raso | $6.000 |
| Omega (MAT-E01) | 0.56 piezas × $3.535 | $1.980 |
| Vigueta (MAT-E02) | 0.56 piezas × $3.535 | $1.980 |
| Superboard (ver espesor) | Ver tabla abajo | Variable |

| Espesor | Mat. Superboard | Estructura | MO | **Costo directo** | H.M. 5% | **TOTAL/m²** |
|---------|----------------|-----------|-----|-------------------|---------|-------------|
| 6mm | $22.685 | $3.960 | $6.000 | $32.645 | $1.632 | **$34.277** |
| 8mm | $26.510 | $3.960 | $6.000 | $36.470 | $1.824 | **$38.294** |
| 10mm | $36.141 | $3.960 | $6.000 | $46.101 | $2.305 | **$48.406** |
| 14mm | $52.953 | $3.960 | $6.000 | $62.913 | $3.146 | **$66.059** |

---

### APU-10 — Sello de ventanas (PU Flex)

| Componente | Producto | Cantidad | Costo/ml |
|------------|----------|----------|----------|
| Mano de obra | MO-12 | 1 ml | $2.500 |
| Material | PU Flex (MAT-V03) 1/30 tubo | — | $655 |
| **Costo directo** | | | **$3.155** |
| Herramienta menor | 5% | | $158 |
| **TOTAL/ml** | | | **$3.313** |

---

## SECCIÓN 4 — REGLAS DE CÁLCULO

### 4.1 Costo unitario de una actividad

```
COSTO UNITARIO = Mano de obra (destajo) + Materiales + Herramienta menor

Donde:
  Herramienta menor = (Mano de obra + Materiales) × 5%
```

### 4.2 Precio de venta con margen de utilidad

```
PRECIO VENTA (sin IVA) = COSTO UNITARIO × (1 + Margen%)
PRECIO VENTA (con IVA) = PRECIO VENTA (sin IVA) × 1.19

Ejemplo con 30% de margen:
  Precio sin IVA = $14.002 × 1.30 = $18.203/m²
  Precio con IVA = $18.203 × 1.19 = $21.661/m²
```

> ⚠️ **IVA del 19% aplica siempre** sobre el precio de venta. Incluirlo en todas las cotizaciones.  
> ⚠️ El margen de utilidad es una VARIABLE. Siempre preguntar al usuario antes de calcular precio de venta.  
> ℹ️ Trabajo en alturas: sin costo adicional en APU. El operario lo incluye en su margen de utilidad.

### 4.3 Costo total de una actividad

```
COSTO TOTAL = Área (m² o ml) × Costo unitario/m²
```

### 4.4 Precio total de cotización

```
PRECIO TOTAL = Área × Precio de venta unitario
```

### 4.5 Margen real sobre una cotización cerrada

```
MARGEN REAL = (Precio cobrado - Costo unitario) ÷ Precio cobrado × 100
```

---

## SECCIÓN 5 — ANÁLISIS DE COMPETENCIA (INGENIERÍA INVERSA)

### 5.1 Calcular margen de un competidor

Si un competidor cotiza una actividad a un precio conocido:

```
MARGEN COMPETIDOR = (Precio competidor - Nuestro costo unitario) ÷ Precio competidor × 100
```

> Usar nuestro costo unitario como referencia de mercado base.

### 5.2 Detectar si un precio es viable

```
Si Precio competidor < Nuestro costo unitario → el competidor trabaja a pérdida 
                                                  O tiene costos más bajos (investigar)
Si Precio competidor ≈ Nuestro costo unitario → margen mínimo, cotización riesgosa
Si Precio competidor > Nuestro costo unitario → hay margen disponible
```

### 5.3 Sugerir precio competitivo

```
PRECIO COMPETITIVO SUGERIDO = Precio competidor × (1 - Factor de descuento)

Factor de descuento recomendado: 3% – 8% por debajo del competidor
Sin bajar del: Nuestro costo unitario × 1.10 (margen mínimo del 10%)
```

### 5.4 Flujo de análisis de competencia

1. Recibir precio del competidor por actividad
2. Identificar la actividad en este archivo y obtener nuestro costo unitario
3. Calcular margen del competidor
4. Evaluar si podemos competir con margen mínimo del 10%
5. Sugerir precio y margen resultante

---

## SECCIÓN 6 — INSTRUCCIONES PARA IA

### Reglas obligatorias

| # | Regla |
|---|-------|
| 1 | **No inventar precios.** Si un material o actividad no está en este archivo, detenerse y pedirlo al usuario. |
| 2 | **No asumir productos.** Cuando hay varias opciones (marca/referencia), preguntar cuál aplica. |
| 3 | **El margen de utilidad es siempre una variable.** Nunca asumir un margen; pedirlo antes de calcular precio de venta. |
| 4 | **Aplicar herramienta menor siempre.** 5% sobre costo directo en cada APU. |
| 5 | **Aplicar accesorios de cubierta.** 8% sobre materiales en actividades de cubierta. |
| 6 | **Preguntar por actividades opcionales.** Ej: ¿incluye Corrotec? ¿incluye retiro de cubierta? ¿incluye imprimante? |
| 7 | **Verificar unidades.** Confirmar si la medida es m², ml, unidad, o global antes de calcular. |
| 8 | **Aplicar IVA del 19%** siempre sobre el precio de venta final. Nunca sobre el costo. |
| 9 | **No usar precios de entrenamiento.** Este archivo prevalece sobre cualquier dato externo. |
| 10 | **Formato de respuesta:** Presentar resultados en tabla con desglose: MO + Materiales + H.M. + Total sin IVA + IVA + Total con IVA. |

### Flujo recomendado para cotización

```
1. Identificar actividades requeridas
2. Para cada actividad:
   a. ¿Está en el archivo? → Si no, pedir dato al usuario
   b. ¿Requiere elegir producto? → Preguntar
   c. ¿Tiene componentes opcionales? → Preguntar
3. Calcular costo unitario por actividad
4. Multiplicar por área/cantidad
5. Pedir margen de utilidad al usuario
6. Calcular precio de venta sin IVA
7. Aplicar IVA del 19%
8. Presentar resumen en tabla con: Costo | Precio sin IVA | IVA | Precio con IVA
```

### Flujo recomendado para ingeniería inversa

```
1. Recibir precio del competidor y actividad
2. Obtener costo unitario propio del archivo
3. Calcular margen del competidor
4. Evaluar viabilidad de competir
5. Sugerir precio competitivo (sin bajar del costo × 1.10)
6. Mostrar tabla comparativa
```

---

## APÉNDICE — DATOS PENDIENTES DE DEFINIR

| Item | Estado | Acción requerida |
|------|--------|-----------------|
| Precios de materiales | ✅ Completo | — |
| Mano de obra todas las actividades | ✅ Completo | — |
| IVA | ✅ 19% sobre precio de venta | — |
| Trabajo en alturas | ✅ Sin costo adicional en APU | El usuario lo incluye en margen |
| AIU | ✅ No aplica | — |
| Membrana asfáltica | ✅ No aplica | — |
| Margen de utilidad | ⚠️ Variable | Preguntar siempre al usuario por cotización |

---

*Archivo generado para uso interno — Base de datos de costos v1.0*  
*Para actualizar precios, editar directamente este archivo y notificar a la IA que use la nueva versión.*
