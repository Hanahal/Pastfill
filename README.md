# RELLENO EN PASTA (PASTE FILL SYSTEM)

Aplicación desarrollada en Streamlit para el diseño y análisis de sistemas de relleno en pasta en minería subterránea. Permite realizar cálculos geomecánicos desde la geometría del tajeo, dosificación de mezcla, resistencia UCS y presión sobre barricadas, además de generar reportes técnicos en PDF.

# CARACTERÍSTICAS PRINCIPALES

## ANÁLISIS DEL TAJEO
Cálculo del volumen del caserón  
UCS requerida mediante:  
- Método simplificado  
- Método de Mitchell (1982)  
Aplicación de factor de seguridad  
Visualización de presión vertical  

## DISEÑO DE MEZCLA
Dosificación por metro cúbico de pasta:  
- Cemento  
- Relave  
- Agua  

Cálculo de densidad de pasta  
Relación agua/cemento  
Estimación de UCS mediante ley de Abrams modificada  
Gráficos de comportamiento UCS vs C/S  

## RESISTENCIA UCS
Evolución de resistencia a 7, 14 y 28 días  
Comparación entre probetas  
Verificación contra UCS requerida  
Indicadores de cumplimiento del diseño  

## PRESIÓN SOBRE BARRICADA
Cálculo de presión hidrostática del relleno  
Efecto del límite elástico (modelo tipo Bingham)  
Presión total sobre la estructura  
Evaluación de carga sobre la barricada  
Gráficos de distribución de presión  

## REPORTE TÉCNICO
Generación automática de PDF  
Incluye:  
- Tablas de resultados  
- Cálculos geomecánicos  
- Gráficos técnicos  

Exportable para informes de ingeniería  

# ENTRADA DE DATOS

La aplicación trabaja en dos modos:

## Modo automático
Usa valores por defecto precargados  

## Modo CSV
Permite cargar archivo maestro con datos de:  
- TAJEO  
- MEZCLA  
- BARRICADA  
- UCS por edades  

Incluye plantilla descargable desde la aplicación  

# MODELOS Y FÓRMULAS UTILIZADAS

UCS requerida (simplificada):  
UCS = (γ × H) / (H/L + 1) × FS  

Método de Mitchell (1982):  
σ = (γ × H²) / (2 × L) × FS  

Ley de Abrams modificada:  
UCS = k × (C/S)^n  

Presión hidrostática:  
P = ρ × g × H  

Modelo de esfuerzo tipo Bingham:  
ΔP = 2 × τ₀ × H / R  

# INSTALACIÓN

git clone https://github.com/tuusuario/paste-fill-system.git  
cd paste-fill-system  
pip install -r requirements.txt  
streamlit run app.py  

# DEPENDENCIAS

streamlit  
numpy  
pandas  
plotly  
reportlab  
kaleido  

# USO

Ejecutar la aplicación con Streamlit  
Cargar archivo CSV o usar datos por defecto  
Navegar por pestañas:  
- Tajeo  
- Mezcla  
- UCS  
- Barricada  
- Reporte final  

Generar reporte PDF  

# REFERENCIAS

Landriault et al. (1996) – Paste Fill Systems  
Mitchell (1982) – Modelos de estabilidad en rellenos  
ACI 318 – Diseño de concreto  