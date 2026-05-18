#  RELLENO EN PASTA

Aplicación desarrollada en **Streamlit** para el diseño, análisis geomecánico y evaluación granulométrica de sistemas de **Relleno en Pasta (Paste Fill)** aplicados a minería subterránea.

La plataforma permite realizar cálculos geotécnicos desde la geometría del tajeo, diseño de mezcla cementada, análisis UCS, presión sobre barricadas y caracterización granulométrica del relave, además de generar reportes técnicos profesionales en PDF.

---

#  CARACTERÍSTICAS PRINCIPALES

##  ANÁLISIS DEL TAJEO

Cálculo automático de:

- Volumen del caserón
- UCS requerida
- Presión vertical del relleno
- Relación geométrica del tajeo
- Evaluación de estabilidad

### Métodos Implementados

- Método simplificado
- Método de Mitchell (1982)

### Funciones Adicionales

- Aplicación de factor de seguridad
- Visualización de presión vertical
- Interpretación geomecánica

---

#  DISEÑO DE MEZCLA

Dosificación de mezcla por metro cúbico:

- Cemento
- Relave
- Agua

### Cálculos Incluidos

- Densidad de pasta
- Relación agua/cemento
- Contenido de sólidos
- Relación cemento/sólidos (C/S)
- Estimación UCS mediante ley de Abrams modificada

### Visualizaciones

- UCS vs C/S
- Comparación de mezclas
- Evolución de resistencia

---

#  ANÁLISIS GRANULOMÉTRICO ASTM

Módulo técnico para caracterización granulométrica del relave utilizado en el relleno en pasta.

---

##  Normas Implementadas

- ASTM D6913 — Análisis granulométrico por tamices
- ASTM D2487 — Clasificación USCS
- ASTM D1140 — Determinación de finos pasante N°200

---

##  Parámetros Calculados

- % retenido parcial
- % retenido acumulado
- % que pasa
- D10
- D30
- D60
- Coeficiente de uniformidad (Cu)
- Coeficiente de curvatura (Cc)
- Módulo de fineza
- Clasificación USCS

---

##  Visualizaciones Granulométricas

- Curva granulométrica semilogarítmica
- Distribución grava–arena–finos
- Barras de retenido parcial
- Evaluación ASTM automática
- Indicadores de clasificación del material

---

##  Evaluaciones Técnicas

- Verificación de gradación
- Clasificación automática USCS
- Evaluación de contenido de finos
- Compatibilidad del relave para paste fill

---

#  RESISTENCIA UCS

Evaluación de resistencia a:

- 7 días
- 14 días
- 28 días

### Funciones

- Comparación entre probetas
- Validación contra UCS requerida
- Indicadores de cumplimiento
- Interpretación del desempeño mecánico

### Visualizaciones

- Curvas UCS vs tiempo
- Barras comparativas
- Líneas de referencia UCS requerida

---

#  PRESIÓN SOBRE BARRICADA

Cálculo de:

- Presión hidrostática del relleno
- Presión total sobre barricada
- Distribución de esfuerzos
- Evaluación estructural

### Modelos Aplicados

#### Modelo Hidrostático

Presión debido a columna de relleno.

#### Modelo Tipo Bingham

Considera comportamiento reológico del relleno en pasta.

---

##  Resultados

- Presión total
- Esfuerzo lateral
- Incremento de presión
- Carga sobre barricada

### Visualizaciones

- Distribución vertical de presión
- Diagramas de carga
- Comparación de escenarios

---

#  REPORTE TÉCNICO PDF

Generación automática de reporte profesional.

---

##  Incluye

- Datos del tajeo
- Diseño de mezcla
- Resultados UCS
- Evaluación de barricada
- Tablas granulométricas ASTM
- Clasificación USCS
- Cálculos geomecánicos
- Gráficos técnicos
- Interpretaciones ingenieriles

---

##  Características del Reporte

- Diseño profesional tipo ingeniería minera
- Tablas estructuradas
- Diagramas incrustados
- Exportación automática PDF
