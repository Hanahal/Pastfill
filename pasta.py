import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import math
import io
import datetime
 
st.set_page_config(
    page_title="Relleno en Pasta (PF)",
    page_icon="🪨",
    layout="wide",
    initial_sidebar_state="collapsed"
)
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Serif:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');
 
section[data-testid="stSidebar"] {display: none !important;}
div[data-testid="stSidebarNav"]  {display: none !important;}
 
html, body, [class*="css"], .stApp {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 14px !important;
    color: #1a1a2e !important;
    background-color: #f0f4f8 !important;
}
 
.stApp { background: #f0f4f8 !important; }
 
h1 { font-family: 'IBM Plex Serif', serif !important; font-size: 24px !important; color: #1a365d !important; }
h2 { font-family: 'IBM Plex Serif', serif !important; font-size: 19px !important; color: #1a365d !important; }
h3 { font-family: 'IBM Plex Sans', sans-serif !important; font-weight: 600 !important; font-size: 15px !important; color: #2c5282 !important; }
 
.stTabs [data-baseweb="tab-list"] { background: #e2ecf7; border-radius: 10px; padding: 4px; gap: 4px; }
.stTabs [data-baseweb="tab"] {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 13px !important; font-weight: 600 !important;
    color: #2b6cb0 !important; border-radius: 8px !important;
    padding: 8px 16px !important;
}
.stTabs [aria-selected="true"] {
    background: #2b6cb0 !important; color: #fff !important;
    font-weight: 700 !important;
}
 
.hero-banner {
    background: linear-gradient(135deg, #1a365d 0%, #2c5282 50%, #2b6cb0 100%);
    border-radius: 14px; padding: 22px 30px; margin-bottom: 22px;
    box-shadow: 0 6px 24px rgba(26,54,93,0.25);
}
.hero-banner h1 { color: #fff !important; font-size: 23px !important; margin: 0; }
.hero-banner p  { color: #bee3f8 !important; font-size: 13px !important; margin: 5px 0 0 0; }
 
.metric-card {
    background: #fff; border: 1px solid #bee3f8; border-radius: 12px;
    padding: 14px 18px; margin-bottom: 10px;
    box-shadow: 0 2px 8px rgba(43,108,176,0.08);
}
.metric-label { color: #2b6cb0; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; }
.metric-value { color: #1a365d; font-size: 22px; font-weight: 700; font-family: 'IBM Plex Serif', serif; }
.metric-unit  { color: #4a90c4; font-size: 12px; }
 
.result-highlight {
    background: linear-gradient(135deg, #ebf8ff, #bee3f8);
    border: 2px solid #2b6cb0; border-radius: 10px;
    padding: 12px 18px; margin: 10px 0;
    box-shadow: 0 2px 10px rgba(43,108,176,0.15);
}
.result-highlight .label { color: #1a365d; font-weight: 700; font-size: 13px; }
.result-highlight .value { color: #2b6cb0; font-size: 20px; font-weight: 700; font-family: 'IBM Plex Mono', monospace; }
 
.section-header {
    background: #ebf8ff; border-left: 4px solid #2b6cb0;
    padding: 8px 14px; border-radius: 0 8px 8px 0;
    margin: 16px 0 10px 0;
    font-weight: 700; color: #1a365d; font-size: 15px;
}
 
.info-box {
    background: #f0f7ff; border: 1px solid #90cdf4;
    border-radius: 8px; padding: 10px 14px;
    color: #2c5282; font-size: 13px; line-height: 1.6;
}
 
.formula-box {
    background: #1a365d; border-radius: 8px;
    padding: 12px 18px; margin: 8px 0;
    color: #bee3f8; font-family: 'IBM Plex Mono', monospace;
    font-size: 13px; line-height: 1.8;
}
 
.styled-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.styled-table th {
    background: #2b6cb0; color: #fff; padding: 8px 12px;
    text-align: left; font-weight: 600; font-size: 12px;
    text-transform: uppercase; letter-spacing: 0.04em;
}
.styled-table td {
    padding: 7px 12px; border-bottom: 1px solid #bee3f8;
    color: #1a1a2e;
}
.styled-table tr:nth-child(even) td { background: #f0f7ff; }
.styled-table tr:hover td { background: #ebf8ff; }
 
.stButton > button {
    background: linear-gradient(135deg, #2b6cb0, #1a365d) !important;
    color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 700 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    padding: 10px 20px !important;
}
.stButton > button:hover { opacity: 0.88 !important; }
 
div[data-testid="stInfo"]    { background: #ebf8ff !important; color: #1a365d !important; border-color: #90cdf4 !important; }
div[data-testid="stSuccess"] { background: #f0fff4 !important; color: #1a472a !important; border-color: #9ae6b4 !important; }
div[data-testid="stWarning"] { background: #fffbeb !important; color: #744210 !important; border-color: #f6e05e !important; }
 
.cumple-si  { color: #276749; font-weight: 700; }
.cumple-no  { color: #c53030; font-weight: 700; }
 
.badge {
    display: inline-block; padding: 3px 10px; border-radius: 20px;
    font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
}
.badge-blue { background: #bee3f8; color: #1a365d; }
.badge-green { background: #c6f6d5; color: #1a472a; }
.badge-red   { background: #fed7d7; color: #742a2a; }
</style>
""", unsafe_allow_html=True)
 
PLOTLY_LAYOUT = dict(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#f8fbff",
    font=dict(family="IBM Plex Sans, sans-serif", color="#1a1a2e", size=13),
    xaxis=dict(gridcolor="#bee3f8", linecolor="#90cdf4", tickfont=dict(size=12)),
    yaxis=dict(gridcolor="#bee3f8", linecolor="#90cdf4", tickfont=dict(size=12)),
    legend=dict(font=dict(size=12), bgcolor="rgba(235,248,255,0.95)", bordercolor="#90cdf4", borderwidth=1),
    margin=dict(l=60, r=40, t=60, b=60),
)
BLUE_PALETTE = ["#2b6cb0", "#1a365d", "#3182ce", "#63b3ed", "#4299e1", "#2c5282", "#76e4f7", "#0bc5ea"]
 
def render_table(df):
    rows = "".join(
        f"<tr>{''.join(f'<td>{v}</td>' for v in row)}</tr>"
        for _, row in df.iterrows()
    )
    headers = "".join(f"<th>{c}</th>" for c in df.columns)
    return f'<table class="styled-table"><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>'
 
def metric_card(label, value, unit=""):
    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value} <span class="metric-unit">{unit}</span></div>
    </div>"""
 
def result_highlight(label, value):
    return f"""
    <div class="result-highlight">
        <div class="label">📌 {label}</div>
        <div class="value">{value}</div>
    </div>"""
 
def section_hdr(txt):
    st.markdown(f'<div class="section-header">◈ {txt}</div>', unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
#  PLANTILLA CSV
# ─────────────────────────────────────────────
def generate_template_csv() -> bytes:
    out = io.StringIO()
    out.write("# CSV MAESTRO - RELLENO EN PASTA (PASTE FILL)\n")
    out.write("# Instrucciones: complete los valores y suba este archivo.\n#\n")
 
    out.write("SECCION,TAJEO\nParametro,Valor\n")
    for r in [("altura_H_m", 30), ("ancho_W_m", 12), ("largo_L_m", 20),
              ("densidad_gamma_kNm3", 20), ("densidad_pasta_kgm3", 2080),
              ("factor_seguridad_FS", 1.5)]:
        out.write(f"{r[0]},{r[1]}\n")
 
    out.write("#\nSECCION,MEZCLA\nParametro,Valor\n")
    for r in [("contenido_solidos_pct", 78), ("cemento_pct_solidos", 4),
              ("densidad_relave_kgm3", 2800), ("densidad_cemento_kgm3", 3150),
              ("relacion_ac", 0.8), ("k_abrams", 10), ("n_abrams", 1.2)]:
        out.write(f"{r[0]},{r[1]}\n")
 
    out.write("#\nSECCION,BARRICADA\nParametro,Valor\n")
    for r in [("altura_pasta_m", 30), ("densidad_pasta_kgm3", 2080),
              ("limite_elastico_tau_Pa", 200), ("radio_tubo_R_m", 2),
              ("espesor_barricada_m", 0.3), ("ancho_barricada_m", 7),
              ("alto_barricada_m", 5), ("densidad_barricada_kgm3", 2400)]:
        out.write(f"{r[0]},{r[1]}\n")
 
    out.write("#\nSECCION,UCS_DIAS\nEspecimen,Dia7_MPa,Dia14_MPa,Dia28_MPa\n")
    for r in [["PF-A", 0.12, 0.18, 0.25], ["PF-B", 0.20, 0.30, 0.42],
              ["PF-C", 0.35, 0.52, 0.68], ["PF-D", 0.50, 0.72, 0.90],
              ["PF-E", 0.18, 0.28, 0.38]]:
        out.write(",".join(str(v) for v in r) + "\n")
 
    return out.getvalue().encode("utf-8")
 
# ─────────────────────────────────────────────
#  PARSER CSV
# ─────────────────────────────────────────────
def parse_master_csv(uploaded_file) -> dict:
    content = uploaded_file.read().decode("utf-8")
    sections, current_section, current_rows, header = {}, None, [], None
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.upper().startswith("SECCION,"):
            if current_section and header and current_rows:
                sections[current_section] = pd.DataFrame(current_rows, columns=header)
            current_section = line.split(",", 1)[1].strip().upper()
            current_rows, header = [], None
            continue
        parts = line.split(",")
        if header is None:
            header = parts
        else:
            parsed = []
            for v in parts:
                try:
                    parsed.append(float(v) if "." in v else int(v))
                except ValueError:
                    parsed.append(v.strip())
            current_rows.append(parsed)
    if current_section and header and current_rows:
        sections[current_section] = pd.DataFrame(current_rows, columns=header)
    return sections
 
# ─────────────────────────────────────────────
#  DEFAULTS
# ─────────────────────────────────────────────
DEFAULT_TAJEO = {
    "altura_H_m": 30.0, "ancho_W_m": 12.0, "largo_L_m": 20.0,
    "densidad_gamma_kNm3": 20.0, "densidad_pasta_kgm3": 2080.0,
    "factor_seguridad_FS": 1.5,
}
DEFAULT_MEZCLA = {
    "contenido_solidos_pct": 78.0, "cemento_pct_solidos": 4.0,
    "densidad_relave_kgm3": 2800.0, "densidad_cemento_kgm3": 3150.0,
    "relacion_ac": 0.8, "k_abrams": 10.0, "n_abrams": 1.2,
}
DEFAULT_BARRICADA = {
    "altura_pasta_m": 30.0, "densidad_pasta_kgm3": 2080.0,
    "limite_elastico_tau_Pa": 200.0, "radio_tubo_R_m": 2.0,
    "espesor_barricada_m": 0.3, "ancho_barricada_m": 7.0,
    "alto_barricada_m": 5.0, "densidad_barricada_kgm3": 2400.0,
}
DEFAULT_UCS = pd.DataFrame({
    "Especimen": ["PF-A", "PF-B", "PF-C", "PF-D", "PF-E"],
    "Dia7_MPa":  [0.12, 0.20, 0.35, 0.50, 0.18],
    "Dia14_MPa": [0.18, 0.30, 0.52, 0.72, 0.28],
    "Dia28_MPa": [0.25, 0.42, 0.68, 0.90, 0.38],
})
 
for k, v in [("csv_activo", False), ("tajeo", DEFAULT_TAJEO.copy()),
             ("mezcla", DEFAULT_MEZCLA.copy()), ("barricada", DEFAULT_BARRICADA.copy()),
             ("ucs_df", DEFAULT_UCS.copy())]:
    if k not in st.session_state:
        st.session_state[k] = v
 
# ─────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <h1>🪨 Relleno en Pasta (Paste Fill)</h1>
  <p>Diseño de mezcla · Resistencia UCS · Presión sobre barricada · Reporte técnico</p>
</div>
""", unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
#  CARGA CSV
# ─────────────────────────────────────────────
st.markdown("### 📂 Carga de Datos del Proyecto")
col_info, col_dl = st.columns([3, 1])
with col_info:
    st.info("**Paso 1:** Descargue la plantilla CSV → **Paso 2:** Complete con sus datos → **Paso 3:** Suba el archivo.")
with col_dl:
    st.download_button("⬇️ Descargar Plantilla", data=generate_template_csv(),
                       file_name="plantilla_PasteFill_maestro.csv", mime="text/csv",
                       use_container_width=True)
 
uploaded_csv = st.file_uploader("Seleccionar archivo CSV maestro (.csv)", type=["csv"], key="master_csv")
if uploaded_csv is not None:
    try:
        sections = parse_master_csv(uploaded_csv)
 
        def load_kv(sec, default):
            if sec not in sections:
                return default.copy()
            df_ = sections[sec].copy()
            df_.columns = ["Parametro", "Valor"]
            d = default.copy()
            for _, r in df_.iterrows():
                k = str(r["Parametro"]).strip()
                if k in d:
                    d[k] = float(r["Valor"])
            return d
 
        st.session_state.tajeo     = load_kv("TAJEO",     DEFAULT_TAJEO)
        st.session_state.mezcla    = load_kv("MEZCLA",    DEFAULT_MEZCLA)
        st.session_state.barricada = load_kv("BARRICADA", DEFAULT_BARRICADA)
 
        if "UCS_DIAS" in sections:
            du = sections["UCS_DIAS"].copy()
            du.columns = ["Especimen", "Dia7_MPa", "Dia14_MPa", "Dia28_MPa"]
            for col in du.columns[1:]:
                du[col] = pd.to_numeric(du[col], errors="coerce")
            st.session_state.ucs_df = du.reset_index(drop=True)
 
        st.session_state.csv_activo = True
        st.success(f"✔ CSV cargado correctamente — secciones: {', '.join(sections.keys())}")
    except Exception as e:
        st.error(f"❌ Error al procesar el CSV: {e}")
 
if st.session_state.csv_activo:
    if st.button("🔄 Restaurar datos por defecto"):
        for k in ["csv_activo", "tajeo", "mezcla", "barricada", "ucs_df"]:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()
 
st.markdown("---")
 
# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────
tabs = st.tabs([
    "📐 Datos del Tajeo",
    "⚗️ Dosificación de Mezcla",
    "💪 Resistencia UCS",
    "🧱 Presión sobre Barricada",
    "📊 Reporte Final",
])
 
# ══════════════════════════════
#  TAB 0 — DATOS DEL TAJEO
# ══════════════════════════════
with tabs[0]:
    st.markdown("## Datos Geométricos y Propiedades del Tajeo")
    tajeo = st.session_state.tajeo
 
    H     = float(tajeo["altura_H_m"])
    W     = float(tajeo["ancho_W_m"])
    L     = float(tajeo["largo_L_m"])
    gamma = float(tajeo["densidad_gamma_kNm3"])
    rho_p = float(tajeo["densidad_pasta_kgm3"])
    FS    = float(tajeo["factor_seguridad_FS"])
 
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown(metric_card("Altura H", f"{H:.1f}", "m"), unsafe_allow_html=True)
    with m2: st.markdown(metric_card("Ancho W", f"{W:.1f}", "m"), unsafe_allow_html=True)
    with m3: st.markdown(metric_card("Largo L", f"{L:.1f}", "m"), unsafe_allow_html=True)
    with m4: st.markdown(metric_card("γ pasta", f"{gamma:.0f}", "kN/m³"), unsafe_allow_html=True)
 
    section_hdr("Paso 1 — UCS Requerida (Fórmula Simplificada)")
    ca, cb = st.columns(2)
    with ca:
        UCS_req_kPa = (gamma * H) / (H / L + 1)
        UCS_req_MPa = UCS_req_kPa / 1000
        UCS_diseno  = UCS_req_MPa * FS
 
        df_paso1 = pd.DataFrame({
            "Parámetro": ["γ (kN/m³)", "H (m)", "L (m)", "H/L", "H/L + 1",
                          "UCS_req (kPa)", "UCS_req (MPa)", f"UCS_diseño (×FS={FS})", "UCS adoptada (MPa)"],
            "Valor": [
                f"{gamma:.1f}", f"{H:.1f}", f"{L:.1f}", f"{H/L:.3f}", f"{H/L+1:.3f}",
                f"{UCS_req_kPa:.1f}", f"{UCS_req_MPa:.4f}",
                f"{UCS_diseno:.4f}", "0.8 (norma interna)",
            ],
        })
        st.markdown(render_table(df_paso1), unsafe_allow_html=True)
        st.markdown(result_highlight("UCS requerida (simplificada)", f"{UCS_req_MPa:.4f} MPa"), unsafe_allow_html=True)
        st.markdown(result_highlight(f"UCS diseño (×FS={FS})", f"{UCS_diseno:.4f} MPa → adopt. 0.80 MPa"), unsafe_allow_html=True)
 
    with cb:
        st.markdown("""
        <div class="formula-box">
        Fórmula simplificada:<br><br>
        UCS_req = (γ × H) / (H/L + 1)<br><br>
        Donde:<br>
        γ = densidad del relleno endurecido (kN/m³)<br>
        H = altura del tajeo (m)<br>
        L = longitud del tajeo (m)<br><br>
        Factor seguridad: UCS_diseño = UCS_req × FS<br>
        → Por norma interna se adopta mínimo 0.8 MPa
        </div>
        """, unsafe_allow_html=True)
 
    section_hdr("Paso 2 — UCS Requerida (Fórmula de Mitchell 1982 adaptada a PF)")
    ca2, cb2 = st.columns(2)
    with ca2:
        sigma_req = (gamma * H**2 / (2 * L)) * FS
        sigma_req_MPa = sigma_req / 1000
 
        df_mitchell = pd.DataFrame({
            "Parámetro": ["γ (kN/m³)", "H² (m²)", "2×L (m)", "γH²/(2L) (kPa)", "FS", "σ_req (kPa)", "σ_req (MPa)"],
            "Valor": [
                f"{gamma:.1f}", f"{H**2:.1f}", f"{2*L:.1f}",
                f"{gamma*H**2/(2*L):.1f}", f"{FS:.2f}",
                f"{sigma_req:.1f}", f"{sigma_req_MPa:.4f}",
            ],
        })
        st.markdown(render_table(df_mitchell), unsafe_allow_html=True)
        ok = "✅ Por debajo de 0.8 MPa — seguro" if sigma_req_MPa < 0.8 else "⚠️ Supera 0.8 MPa — revisar diseño"
        st.markdown(result_highlight("σ_req Mitchell (MPa)", f"{sigma_req_MPa:.4f} MPa  —  {ok}"), unsafe_allow_html=True)
 
    with cb2:
        st.markdown("""
        <div class="formula-box">
        Fórmula de Mitchell (1982) para PF:<br><br>
        σ_req = (γ × H²) / (2 × L) × FS<br><br>
        Donde:<br>
        γ = densidad relleno (kN/m³)<br>
        H = altura pared autoestable (m)<br>
        L = longitud arco de esfuerzo (m)<br>
        FS = factor de seguridad<br><br>
        Asume φ = 0 (relleno cohesivo)
        </div>
        """, unsafe_allow_html=True)
 
    section_hdr("Volumen del Tajeo")
    vol = H * W * L
    df_vol = pd.DataFrame({
        "Dimensión": ["Altura H (m)", "Ancho W (m)", "Largo L (m)", "Volumen total (m³)"],
        "Valor": [f"{H:.1f}", f"{W:.1f}", f"{L:.1f}", f"{vol:.1f}"],
    })
    ca3, cb3 = st.columns(2)
    with ca3:
        st.markdown(render_table(df_vol), unsafe_allow_html=True)
        st.markdown(result_highlight("Volumen del tajeo", f"{vol:.1f} m³"), unsafe_allow_html=True)
    with cb3:
        z_arr = np.linspace(0, H, 60)
        pv    = gamma * z_arr
        fig_pv = go.Figure()
        fig_pv.add_trace(go.Scatter(
            x=pv, y=z_arr, mode="lines", fill="tozerox",
            fillcolor="rgba(43,108,176,0.15)",
            line=dict(color="#2b6cb0", width=3),
            name="Presión vertical γ·z"
        ))
        fig_pv.add_vline(x=UCS_req_kPa, line_dash="dash", line_color="#3182ce",
                         annotation_text=f"UCS_req={UCS_req_kPa:.0f} kPa",
                         annotation_font_color="#1a365d")
        fig_pv.update_layout(**PLOTLY_LAYOUT, height=300,
            title=dict(text="Distribución de Presión Vertical", font=dict(size=14)),
            xaxis_title="Presión (kPa)", yaxis_title="Profundidad z (m)")
        st.plotly_chart(fig_pv, use_container_width=True)
 
# ══════════════════════════════
#  TAB 1 — DOSIFICACIÓN
# ══════════════════════════════
with tabs[1]:
    st.markdown("## Dosificación de la Mezcla de Relleno en Pasta")
    mezcla = st.session_state.mezcla
    tajeo  = st.session_state.tajeo
 
    Cw_pct   = float(mezcla["contenido_solidos_pct"]) / 100
    cem_pct  = float(mezcla["cemento_pct_solidos"]) / 100
    rho_r    = float(mezcla["densidad_relave_kgm3"])
    rho_c_m  = float(mezcla["densidad_cemento_kgm3"])
    a_c_rel  = float(mezcla["relacion_ac"])
    k_ab     = float(mezcla["k_abrams"])
    n_ab     = float(mezcla["n_abrams"])
    rho_pasta= float(tajeo["densidad_pasta_kgm3"])
 
    section_hdr("Paso 3 — Dosificación por m³ de Pasta (base seca)")
 
    # Densidad de la mezcla sólida (promedio ponderado)
    rho_s_inv = cem_pct / rho_c_m + (1 - cem_pct) / rho_r
    rho_s     = 1 / rho_s_inv if rho_s_inv > 0 else 2800
 
    # Densidad pasta fresca
    rho_p_calc = 100 / (Cw_pct * 100 / rho_s + (100 - Cw_pct * 100) / 1000)
 
    masa_sol   = Cw_pct * rho_p_calc
    masa_cem   = cem_pct * masa_sol
    masa_rel   = masa_sol - masa_cem
    masa_agua  = rho_p_calc - masa_sol
 
    ca, cb = st.columns(2)
    with ca:
        df_dosif = pd.DataFrame({
            "Componente": ["Cemento", "Relave", "Sólidos totales", "Agua", "TOTAL pasta"],
            "Masa (kg/m³)": [f"{masa_cem:.1f}", f"{masa_rel:.1f}",
                             f"{masa_sol:.1f}", f"{masa_agua:.1f}", f"{rho_p_calc:.1f}"],
            "% en masa": [f"{masa_cem/rho_p_calc*100:.2f}%",
                          f"{masa_rel/rho_p_calc*100:.2f}%",
                          f"{Cw_pct*100:.1f}%",
                          f"{masa_agua/rho_p_calc*100:.2f}%", "100.0%"],
        })
        st.markdown(render_table(df_dosif), unsafe_allow_html=True)
        ac_calc = masa_agua / masa_cem if masa_cem > 0 else 0
        st.markdown(result_highlight("Relación agua/cemento (a/c)", f"{ac_calc:.2f}"), unsafe_allow_html=True)
        st.markdown(result_highlight("Densidad pasta fresca estimada", f"{rho_p_calc:.1f} kg/m³"), unsafe_allow_html=True)
    with cb:
        st.markdown(f"""
        <div class="formula-box">
        Densidad media sólidos:<br>
        1/ρ_s = Cem%/ρ_c + (1-Cem%)/ρ_r<br><br>
        Densidad pasta fresca:<br>
        ρ_pasta = 100 / (Cw/ρ_s + (1-Cw)/1000)<br><br>
        Masa sólidos = Cw × ρ_pasta<br>
        Masa cemento = cem% × masa_sólidos<br>
        Masa agua = ρ_pasta − masa_sólidos<br><br>
        ρ_s estimada  = {rho_s:.0f} kg/m³<br>
        Cw (% peso)   = {Cw_pct*100:.1f}%<br>
        Cem (% sóli.) = {cem_pct*100:.1f}%
        </div>
        """, unsafe_allow_html=True)
 
    section_hdr("Paso 4 — Estimación UCS con Ley de Abrams Modificada")
    CS_ratio = cem_pct
    UCS_abrams = k_ab * (CS_ratio ** n_ab)
 
    ca2, cb2 = st.columns(2)
    with ca2:
        df_abrams = pd.DataFrame({
            "Parámetro": ["C/S (cemento/sólidos)", "k (MPa)", "n", "UCS = k × (C/S)^n"],
            "Valor": [f"{CS_ratio:.4f}", f"{k_ab:.1f}", f"{n_ab:.2f}", f"{UCS_abrams:.4f} MPa"],
        })
        st.markdown(render_table(df_abrams), unsafe_allow_html=True)
        UCS_objetivo = 0.8
        CS_objetivo  = (UCS_objetivo / k_ab) ** (1 / n_ab)
        cem_objetivo = CS_objetivo * 100
        df_inv = pd.DataFrame({
            "Para UCS objetivo (0.8 MPa)": ["C/S necesario", "% cemento necesario"],
            "Valor": [f"{CS_objetivo:.4f}", f"{cem_objetivo:.2f}%"],
        })
        st.markdown(render_table(df_inv), unsafe_allow_html=True)
        st.markdown(result_highlight("UCS estimada 28d (Abrams)", f"{UCS_abrams:.4f} MPa"), unsafe_allow_html=True)
        if UCS_abrams < 0.8:
            st.warning(f"⚠ UCS estimada {UCS_abrams:.3f} MPa < 0.8 MPa → se recomienda incrementar cemento a ≥{cem_objetivo:.1f}%")
 
    with cb2:
        cs_arr = np.linspace(0.02, 0.12, 80)
        ucs_arr = k_ab * (cs_arr ** n_ab)
        fig_abr = go.Figure()
        fig_abr.add_trace(go.Scatter(
            x=cs_arr * 100, y=ucs_arr,
            mode="lines", line=dict(color="#2b6cb0", width=3), name="UCS (MPa)"
        ))
        fig_abr.add_vline(x=CS_ratio * 100, line_dash="dash", line_color="#3182ce",
                          annotation_text=f"C/S={CS_ratio*100:.1f}%",
                          annotation_font_color="#1a365d")
        fig_abr.add_hline(y=0.8, line_dash="dot", line_color="#e53e3e",
                          annotation_text="UCS mín 0.8 MPa", annotation_font_color="#c53030")
        fig_abr.update_layout(**PLOTLY_LAYOUT, height=300,
            title=dict(text="UCS 28d vs % Cemento/Sólidos (Abrams mod.)", font=dict(size=14)),
            xaxis_title="C/S (%)", yaxis_title="UCS (MPa)")
        st.plotly_chart(fig_abr, use_container_width=True)
 
    section_hdr("Proporciones por m³ — Gráfico de Composición")
    fig_comp = go.Figure(go.Pie(
        labels=["Cemento", "Relave", "Agua"],
        values=[masa_cem, masa_rel, masa_agua],
        marker=dict(colors=["#1a365d", "#4299e1", "#90cdf4"]),
        hole=0.45,
        textfont=dict(size=13, color="white"),
        textinfo="label+percent",
    ))
    fig_comp.update_layout(**PLOTLY_LAYOUT, height=340,
        title=dict(text=f"Composición de la Pasta ({rho_p_calc:.0f} kg/m³)", font=dict(size=14)))
    st.plotly_chart(fig_comp, use_container_width=True)
 
# ══════════════════════════════
#  TAB 2 — UCS
# ══════════════════════════════
with tabs[2]:
    st.markdown("## Curvas de Resistencia a la Compresión Simple (UCS)")
    ucs_df = st.session_state.ucs_df.copy()
    tajeo  = st.session_state.tajeo
    mezcla = st.session_state.mezcla
 
    H_t   = float(tajeo["altura_H_m"])
    L_t   = float(tajeo["largo_L_m"])
    g_t   = float(tajeo["densidad_gamma_kNm3"])
    FS_t  = float(tajeo["factor_seguridad_FS"])
    UCS_req_kPa2 = (g_t * H_t) / (H_t / L_t + 1)
    UCS_req2     = UCS_req_kPa2 / 1000 * FS_t
    UCS_adoptado = max(UCS_req2, 0.8)
 
    section_hdr("Tabla de Resultados UCS")
    df_show = ucs_df.copy()
    df_show.columns = ["Especimen", "Día 7 (MPa)", "Día 14 (MPa)", "Día 28 (MPa)"]
    st.markdown(render_table(df_show), unsafe_allow_html=True)
 
    section_hdr("Curva de Resistencia — Evolución con el Curado")
    fig_ucs = go.Figure()
    dias = [7, 14, 28]
    for i, (_, row) in enumerate(ucs_df.iterrows()):
        vals  = [row["Dia7_MPa"], row["Dia14_MPa"], row["Dia28_MPa"]]
        color = BLUE_PALETTE[i % len(BLUE_PALETTE)]
        fig_ucs.add_trace(go.Scatter(
            x=dias, y=vals, mode="lines+markers",
            name=row["Especimen"],
            line=dict(color=color, width=2.5),
            marker=dict(size=9, color=color, line=dict(color="white", width=1.5)),
        ))
    fig_ucs.add_hline(y=UCS_adoptado, line_dash="dash", line_color="#e53e3e", line_width=2,
                      annotation_text=f"UCS req = {UCS_adoptado:.3f} MPa",
                      annotation_font_color="#c53030")
    fig_ucs.update_layout(**PLOTLY_LAYOUT, height=400,
        title=dict(text="Curva de Resistencia UCS vs Días de Curado", font=dict(size=14)))
    st.plotly_chart(fig_ucs, use_container_width=True)
 
    section_hdr("Verificación a 28 días")
    ucs_max  = float(ucs_df["Dia28_MPa"].max())
    ucs_min  = float(ucs_df["Dia28_MPa"].min())
    ucs_mean = float(ucs_df["Dia28_MPa"].mean())
 
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown(metric_card("UCS requerida", f"{UCS_adoptado:.3f}", "MPa"), unsafe_allow_html=True)
    with m2: st.markdown(metric_card("UCS máx. 28d", f"{ucs_max:.3f}", "MPa"), unsafe_allow_html=True)
    with m3: st.markdown(metric_card("UCS prom. 28d", f"{ucs_mean:.3f}", "MPa"), unsafe_allow_html=True)
    with m4:
        factor = ucs_mean / UCS_adoptado if UCS_adoptado > 0 else 0
        icono  = "✅" if factor >= 1.0 else "⚠️"
        st.markdown(metric_card(f"{icono} Factor ensayado/req", f"{factor:.2f}", "—"), unsafe_allow_html=True)
 
    fig_28 = go.Figure()
    colores28 = ["#2b6cb0" if v >= UCS_adoptado else "#e53e3e" for v in ucs_df["Dia28_MPa"]]
    fig_28.add_trace(go.Bar(
        x=ucs_df["Especimen"], y=ucs_df["Dia28_MPa"],
        marker_color=colores28,
        text=[f"{v:.3f}" for v in ucs_df["Dia28_MPa"]],
        textposition="outside", textfont=dict(size=12),
        name="UCS 28d"
    ))
    fig_28.add_hline(y=UCS_adoptado, line_dash="dash", line_color="#e53e3e", line_width=2,
                     annotation_text=f"UCS req = {UCS_adoptado:.3f} MPa",
                     annotation_font_color="#c53030")
    fig_28.update_layout(**PLOTLY_LAYOUT, height=360,
        title=dict(text="UCS a 28 días — Azul: cumple, Rojo: no cumple", font=dict(size=14)))
    st.plotly_chart(fig_28, use_container_width=True)
 
# ══════════════════════════════
#  TAB 3 — BARRICADA
# ══════════════════════════════
with tabs[3]:
    st.markdown("## Paso 5 — Presión Lateral sobre la Barricada")
    barr = st.session_state.barricada
 
    h_b   = float(barr["altura_pasta_m"])
    rho_b = float(barr["densidad_pasta_kgm3"])
    tau0  = float(barr["limite_elastico_tau_Pa"])
    R_t   = float(barr["radio_tubo_R_m"])
    esp   = float(barr["espesor_barricada_m"])
    ancho = float(barr["ancho_barricada_m"])
    alto  = float(barr["alto_barricada_m"])
    rho_b2= float(barr["densidad_barricada_kgm3"])
 
    g = 9.81
    P_hidrost = rho_b * g * h_b / 1000   # kPa
    delta_P   = (2 * tau0 * h_b / R_t) / 1000  # kPa
    P_total   = P_hidrost + delta_P
 
    peso_barr_kN = esp * ancho * alto * rho_b2 * g / 1000
 
    section_hdr("Cálculo de Presión")
    ca, cb = st.columns(2)
    with ca:
        df_barr = pd.DataFrame({
            "Parámetro": [
                "Altura pasta (m)", "Densidad pasta (kg/m³)", "Presión hidrostática",
                "τ₀ límite elástico (Pa)", "Radio tubería R (m)", "ΔP límite elástico",
                "PRESIÓN TOTAL",
            ],
            "Valor": [
                f"{h_b:.1f} m", f"{rho_b:.0f} kg/m³",
                f"{P_hidrost:.1f} kPa",
                f"{tau0:.0f} Pa", f"{R_t:.1f} m",
                f"{delta_P:.2f} kPa",
                f"{P_total:.2f} kPa",
            ],
        })
        st.markdown(render_table(df_barr), unsafe_allow_html=True)
        st.markdown(result_highlight("Presión hidrostática", f"{P_hidrost:.2f} kPa"), unsafe_allow_html=True)
        st.markdown(result_highlight("ΔP por límite elástico", f"{delta_P:.3f} kPa"), unsafe_allow_html=True)
        st.markdown(result_highlight("Presión TOTAL sobre barricada", f"{P_total:.2f} kPa"), unsafe_allow_html=True)
 
    with cb:
        st.markdown(f"""
        <div class="formula-box">
        Presión hidrostática:<br>
        P_hid = ρ_pasta × g × H / 1000  (kPa)<br><br>
        Adición por límite elástico de Bingham:<br>
        ΔP = 2 × τ₀ × H / R  (Pa → kPa)<br><br>
        Presión total:<br>
        P_total = P_hid + ΔP<br><br>
        Valores:<br>
        P_hid = {rho_b:.0f}×{g}×{h_b:.1f}/1000 = {P_hidrost:.2f} kPa<br>
        ΔP = 2×{tau0:.0f}×{h_b:.1f}/{R_t:.1f}/1000 = {delta_P:.3f} kPa<br>
        P_total = {P_total:.2f} kPa
        </div>
        """, unsafe_allow_html=True)
 
    section_hdr("Diseño de la Barricada (Concreto Lanzado)")
    ca2, cb2 = st.columns(2)
    with ca2:
        df_barre2 = pd.DataFrame({
            "Parámetro": ["Espesor (m)", "Ancho (m)", "Alto (m)",
                          "Densidad concreto (kg/m³)", "Peso barricada (kN)", "Presión total (kPa)"],
            "Valor": [f"{esp:.2f}", f"{ancho:.1f}", f"{alto:.1f}",
                      f"{rho_b2:.0f}", f"{peso_barr_kN:.1f}", f"{P_total:.2f}"],
        })
        st.markdown(render_table(df_barre2), unsafe_allow_html=True)
        st.markdown(result_highlight("Peso barricada", f"{peso_barr_kN:.1f} kN"), unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box" style="margin-top:10px;">
        <b>Nota:</b> El momento resistente de la barricada se calcula considerando los anclajes
        perimetrales según normas específicas del proyecto (ACI 318 o normativa minera vigente).
        La verificación a flexión y punzonamiento queda fuera del alcance de esta herramienta.
        </div>
        """, unsafe_allow_html=True)
 
    with cb2:
        h_arr = np.linspace(0, h_b, 60)
        p_arr = rho_b * g * h_arr / 1000
        fig_pbarr = go.Figure()
        fig_pbarr.add_trace(go.Scatter(
            x=p_arr, y=h_arr, mode="lines", fill="tozerox",
            fillcolor="rgba(43,108,176,0.15)",
            line=dict(color="#2b6cb0", width=3),
            name="P hidrostática (kPa)"
        ))
        fig_pbarr.add_vline(x=P_total, line_dash="dash", line_color="#3182ce",
                            annotation_text=f"P_total={P_total:.1f} kPa",
                            annotation_font_color="#1a365d")
        fig_pbarr.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Distribución de Presión sobre Barricada", font=dict(size=14)),
            xaxis_title="Presión (kPa)", yaxis_title="Altura h (m)")
        st.plotly_chart(fig_pbarr, use_container_width=True)
 
    section_hdr("Tabla de Consistencia (Slump) vs Límite Elástico")
    df_slump = pd.DataFrame({
        "Slump (pulg)": ["6 – 7", "8 – 10", "> 10"],
        "Consistencia": ["Muy seca", "Media", "Fluida"],
        "τ₀ aprox. (Pa)": ["400 – 700", "150 – 400", "< 150"],
        "Bombeabilidad": ["Difícil", "Óptima", "Posible segregación"],
    })
    st.markdown(render_table(df_slump), unsafe_allow_html=True)
 
# ══════════════════════════════
#  TAB 4 — REPORTE FINAL
# ══════════════════════════════
with tabs[4]:
    st.markdown("## Resumen Técnico — Relleno en Pasta")
 
    tajeo  = st.session_state.tajeo
    mezcla = st.session_state.mezcla
    barr   = st.session_state.barricada
    ucs_df = st.session_state.ucs_df.copy()
 
    H     = float(tajeo["altura_H_m"])
    W     = float(tajeo["ancho_W_m"])
    L     = float(tajeo["largo_L_m"])
    gamma = float(tajeo["densidad_gamma_kNm3"])
    FS    = float(tajeo["factor_seguridad_FS"])
 
    UCS_simp = (gamma * H) / (H / L + 1) / 1000
    UCS_dis  = max(UCS_simp * FS, 0.8)
    sigma_mit = (gamma * H**2 / (2 * L)) * FS / 1000
 
    Cw_pct2   = float(mezcla["contenido_solidos_pct"]) / 100
    cem_pct2  = float(mezcla["cemento_pct_solidos"]) / 100
    rho_r2    = float(mezcla["densidad_relave_kgm3"])
    rho_c2    = float(mezcla["densidad_cemento_kgm3"])
    k_ab2     = float(mezcla["k_abrams"])
    n_ab2     = float(mezcla["n_abrams"])
    rho_p2    = float(tajeo["densidad_pasta_kgm3"])
 
    rho_s_inv2 = cem_pct2 / rho_c2 + (1 - cem_pct2) / rho_r2
    rho_s2     = 1 / rho_s_inv2
    rho_p_c2   = 100 / (Cw_pct2 * 100 / rho_s2 + (100 - Cw_pct2 * 100) / 1000)
    masa_sol2  = Cw_pct2 * rho_p_c2
    masa_cem2  = cem_pct2 * masa_sol2
    masa_rel2  = masa_sol2 - masa_cem2
    masa_agua2 = rho_p_c2 - masa_sol2
    UCS_abrams2 = k_ab2 * (cem_pct2 ** n_ab2)
 
    h_b2  = float(barr["altura_pasta_m"])
    rho_b2b = float(barr["densidad_pasta_kgm3"])
    tau02 = float(barr["limite_elastico_tau_Pa"])
    R_t2  = float(barr["radio_tubo_R_m"])
    esp2  = float(barr["espesor_barricada_m"])
    ancho2= float(barr["ancho_barricada_m"])
    alto2 = float(barr["alto_barricada_m"])
    rho_barr2 = float(barr["densidad_barricada_kgm3"])
    P_hid2 = rho_b2b * 9.81 * h_b2 / 1000
    dP2    = (2 * tau02 * h_b2 / R_t2) / 1000
    P_tot2 = P_hid2 + dP2
    peso_b2= esp2 * ancho2 * alto2 * rho_barr2 * 9.81 / 1000
    ucs_mean2 = float(ucs_df["Dia28_MPa"].mean())
    factor2   = ucs_mean2 / UCS_dis if UCS_dis > 0 else 0
 
    section_hdr("Indicadores Clave del Diseño")
    r1, r2, r3, r4 = st.columns(4)
    with r1: st.markdown(metric_card("UCS requerida", f"{UCS_dis:.3f}", "MPa"), unsafe_allow_html=True)
    with r2: st.markdown(metric_card("UCS estimada (Abrams)", f"{UCS_abrams2:.3f}", "MPa"), unsafe_allow_html=True)
    with r3: st.markdown(metric_card("Presión total barricada", f"{P_tot2:.1f}", "kPa"), unsafe_allow_html=True)
    with r4:
        ico = "✅" if factor2 >= 1.0 else "⚠️"
        st.markdown(metric_card(f"{ico} Factor UCS ens./req.", f"{factor2:.2f}", "—"), unsafe_allow_html=True)
 
    section_hdr("📄 Exportar Reporte PDF")
    st.markdown("""
    <div class="info-box">
    Genera un reporte PDF completo con todos los parámetros, tablas de resultados
    y gráficos del diseño (distribución de presión, dosificación, UCS vs días, comparativa 28 días).
    </div>
    """, unsafe_allow_html=True)
 
    if st.button("📥 Generar Reporte PDF — Relleno en Pasta", use_container_width=True):
        import io as _io
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.units import cm
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                        Table, TableStyle, Image as RLImage,
                                        HRFlowable)
        from reportlab.lib.enums import TA_CENTER, TA_RIGHT
 
        def fig_to_rli(fig, w_cm=15.5, h_cm=8.0):
            buf = _io.BytesIO()
            fig.write_image(buf, format="png", width=950, height=500, scale=2)
            buf.seek(0)
            return RLImage(buf, width=w_cm * cm, height=h_cm * cm)
 
        LP_pdf = dict(
            paper_bgcolor="white", plot_bgcolor="#f5f9ff",
            font=dict(family="Arial, sans-serif", color="#1a1a2e", size=13),
            margin=dict(l=60, r=40, t=65, b=60),
        )
 
        # Gráfico 1 — Presión tajeo
        z_p = np.linspace(0, H, 60)
        pv_p = gamma * z_p
        UCS_req_kPa_pdf = (gamma * H) / (H / L + 1)
        fig_p1 = go.Figure()
        fig_p1.add_trace(go.Scatter(x=pv_p, y=z_p, mode="lines", fill="tozerox",
            fillcolor="rgba(43,108,176,0.2)", line=dict(color="#2b6cb0", width=3),
            name="Presión vertical γ·z"))
        fig_p1.add_vline(x=UCS_req_kPa_pdf, line_dash="dash", line_color="#3182ce",
            annotation_text=f"UCS_req={UCS_req_kPa_pdf:.0f} kPa", annotation_font_color="#1a365d")
        fig_p1.update_layout(**LP_pdf, height=500,
            title=dict(text="Distribución de Presión Vertical en el Tajeo", font=dict(size=15)),
            xaxis_title="Presión vertical γ·z (kPa)", yaxis_title="Profundidad z (m)",
            xaxis=dict(gridcolor="#bee3f8"), yaxis=dict(gridcolor="#bee3f8"))
 
        # Gráfico 2 — UCS vs días
        fig_p2 = go.Figure()
        dias = [7, 14, 28]
        for i, (_, row) in enumerate(ucs_df.iterrows()):
            vals = [row["Dia7_MPa"], row["Dia14_MPa"], row["Dia28_MPa"]]
            fig_p2.add_trace(go.Scatter(x=dias, y=vals, mode="lines+markers",
                name=row["Especimen"], line=dict(color=BLUE_PALETTE[i % len(BLUE_PALETTE)], width=2.5),
                marker=dict(size=9)))
        fig_p2.add_hline(y=UCS_dis, line_dash="dash", line_color="#e53e3e", line_width=2,
            annotation_text=f"UCS req = {UCS_dis:.3f} MPa", annotation_font_color="#c53030")
        fig_p2.update_layout(**LP_pdf, height=500,
            title=dict(text="Curva UCS vs Días de Curado", font=dict(size=15)),
            xaxis=dict(tickvals=[7, 14, 28], gridcolor="#bee3f8"),
            yaxis=dict(title="UCS (MPa)", gridcolor="#bee3f8"))
 
        # Gráfico 3 — Barras UCS 28d
        colores_pdf = ["#2b6cb0" if v >= UCS_dis else "#e53e3e" for v in ucs_df["Dia28_MPa"]]
        fig_p3 = go.Figure()
        fig_p3.add_trace(go.Bar(x=ucs_df["Especimen"], y=ucs_df["Dia28_MPa"],
            marker_color=colores_pdf, text=[f"{v:.3f}" for v in ucs_df["Dia28_MPa"]],
            textposition="outside", name="UCS 28d (MPa)"))
        fig_p3.add_hline(y=UCS_dis, line_dash="dash", line_color="#e53e3e", line_width=2,
            annotation_text=f"UCS req = {UCS_dis:.3f} MPa", annotation_font_color="#c53030")
        fig_p3.update_layout(**LP_pdf, height=500,
            title=dict(text="UCS a 28 días vs Requerimiento — Azul: cumple, Rojo: no cumple", font=dict(size=15)),
            yaxis=dict(title="UCS (MPa)", gridcolor="#bee3f8"),
            xaxis=dict(gridcolor="#bee3f8"))
 
        # ── Estilos PDF ─────────────────────────────────
        styles = getSampleStyleSheet()
        def ps(name, base="Normal", **kw):
            return ParagraphStyle(name, parent=styles[base], **kw)
 
        S_TITLE = ps("t", "Title", fontSize=20, textColor=colors.HexColor("#1a365d"),
                     fontName="Helvetica-Bold", spaceAfter=2)
        S_SUB   = ps("s", fontSize=10, textColor=colors.HexColor("#4a90c4"),
                     fontName="Helvetica-Oblique", spaceAfter=10)
        S_H2    = ps("h2", fontSize=12, textColor=colors.HexColor("#1a365d"),
                     fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=5)
        S_BODY  = ps("b", fontSize=9.5, textColor=colors.HexColor("#1a1a2e"),
                     fontName="Helvetica", leading=14)
        S_NOTE  = ps("n", fontSize=8.5, textColor=colors.HexColor("#2c5282"),
                     fontName="Helvetica-Oblique", leading=12)
        S_RIGHT = ps("r", fontSize=8, textColor=colors.HexColor("#4a90c4"),
                     fontName="Helvetica", alignment=TA_RIGHT)
 
        TS_pdf = TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0), colors.HexColor("#2b6cb0")),
            ("TEXTCOLOR",     (0, 0), (-1, 0), colors.white),
            ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE",      (0, 0), (-1, 0), 9),
            ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
            ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.HexColor("#ebf8ff"), colors.white]),
            ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE",      (0, 1), (-1, -1), 9),
            ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#90cdf4")),
            ("TOPPADDING",    (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ])
 
        def make_tbl(rows, col_w=None):
            t = Table(rows, colWidths=col_w)
            t.setStyle(TS_pdf)
            return t
 
        def hr():
            return HRFlowable(width="100%", thickness=1.5,
                              color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2)
 
        # ── Construir historia ──────────────────────────
        buf_pdf = _io.BytesIO()
        doc = SimpleDocTemplate(buf_pdf, pagesize=A4,
                                leftMargin=2.2 * cm, rightMargin=2.2 * cm,
                                topMargin=2 * cm, bottomMargin=2 * cm)
        story = []
        hoy_str = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M")
 
        story.append(Paragraph("Relleno en Pasta (Paste Fill)", S_TITLE))
        story.append(Paragraph("Reporte Tecnico — Diseno de Mezcla, UCS y Barricada", S_SUB))
        story.append(hr())
        story.append(Paragraph(f"Fecha: {hoy_str}", S_NOTE))
        story.append(Spacer(1, 0.5 * cm))
 
        # Sección 1 — Tajeo
        story.append(Paragraph("1. Datos del Tajeo y UCS Requerida", S_H2))
        story.append(hr())
        data1 = [["Parametro", "Valor"],
                 ["Altura H (m)", f"{H:.1f}"],
                 ["Ancho W (m)",  f"{W:.1f}"],
                 ["Largo L (m)",  f"{L:.1f}"],
                 ["Densidad γ (kN/m³)", f"{gamma:.1f}"],
                 ["Factor seguridad FS", f"{FS:.2f}"],
                 ["UCS_req simplificada (MPa)", f"{UCS_simp:.4f}"],
                 ["UCS diseno adoptada (MPa)",  f"{UCS_dis:.4f}"],
                 ["σ_req Mitchell (MPa)",       f"{sigma_mit:.4f}"],
                 ]
        story.append(make_tbl(data1, col_w=[9.5 * cm, 6.5 * cm]))
 
        # Sección 2 — Dosificación
        story.append(Spacer(1, 0.4 * cm))
        story.append(Paragraph("2. Dosificacion por m3 de Pasta", S_H2))
        story.append(hr())
        data2 = [["Componente", "Masa (kg/m3)", "% en masa"],
                 ["Cemento", f"{masa_cem2:.1f}", f"{masa_cem2/rho_p_c2*100:.2f}%"],
                 ["Relave",  f"{masa_rel2:.1f}", f"{masa_rel2/rho_p_c2*100:.2f}%"],
                 ["Agua",    f"{masa_agua2:.1f}", f"{masa_agua2/rho_p_c2*100:.2f}%"],
                 ["TOTAL",   f"{rho_p_c2:.1f}", "100.0%"],
                 ]
        story.append(make_tbl(data2, col_w=[6 * cm, 5 * cm, 5 * cm]))
        ac_calc2 = masa_agua2 / masa_cem2 if masa_cem2 > 0 else 0
        story.append(Spacer(1, 0.2 * cm))
        story.append(Paragraph(
            f"Relacion a/c = {ac_calc2:.2f}  |  UCS estimada Abrams 28d = {UCS_abrams2:.4f} MPa",
            S_BODY))
 
        # Sección 3 — UCS
        story.append(Spacer(1, 0.4 * cm))
        story.append(Paragraph("3. Verificacion UCS Ensayada vs Requerimiento (28 dias)", S_H2))
        story.append(hr())
        header_u = [["Especimen", "Dia 7 (MPa)", "Dia 14 (MPa)", "Dia 28 (MPa)", "Cumple?"]]
        rows_u = [[r["Especimen"], f"{r['Dia7_MPa']:.3f}", f"{r['Dia14_MPa']:.3f}",
                   f"{r['Dia28_MPa']:.3f}",
                   "SI" if r["Dia28_MPa"] >= UCS_dis else "NO"]
                  for _, r in ucs_df.iterrows()]
        story.append(make_tbl(header_u + rows_u,
                              col_w=[4.5 * cm, 3 * cm, 3 * cm, 3.2 * cm, 2.3 * cm]))
        story.append(Spacer(1, 0.2 * cm))
        texto_factor = "CUMPLE" if factor2 >= 1.0 else "NO CUMPLE"
        story.append(Paragraph(
            f"UCS promedio 28d = {ucs_mean2:.3f} MPa  |  "
            f"Factor = {factor2:.2f}  |  {texto_factor}", S_BODY))
 
        # Sección 4 — Barricada
        story.append(Spacer(1, 0.4 * cm))
        story.append(Paragraph("4. Presion sobre Barricada", S_H2))
        story.append(hr())
        data4 = [["Parametro", "Valor"],
                 ["Altura pasta (m)",        f"{h_b2:.1f}"],
                 ["Densidad pasta (kg/m3)",   f"{rho_b2b:.0f}"],
                 ["Presion hidrostatica (kPa)", f"{P_hid2:.2f}"],
                 ["Limite elastico τ0 (Pa)",  f"{tau02:.0f}"],
                 ["Radio tuberia R (m)",       f"{R_t2:.1f}"],
                 ["ΔP limite elastico (kPa)",  f"{dP2:.3f}"],
                 ["PRESION TOTAL (kPa)",       f"{P_tot2:.2f}"],
                 ["Peso barricada (kN)",       f"{peso_b2:.1f}"],
                 ]
        story.append(make_tbl(data4, col_w=[9.5 * cm, 6.5 * cm]))
 
        # Sección 5 — Gráficos
        story.append(Spacer(1, 0.5 * cm))
        story.append(Paragraph("5. Graficos Tecnicos", S_H2))
        story.append(hr())
        try:
            story.append(Paragraph("5.1  Distribucion de Presion Vertical en el Tajeo", S_BODY))
            story.append(Spacer(1, 0.2 * cm))
            story.append(fig_to_rli(fig_p1))
            story.append(Spacer(1, 0.5 * cm))
            story.append(Paragraph("5.2  Curva de Resistencia UCS vs Dias de Curado", S_BODY))
            story.append(Spacer(1, 0.2 * cm))
            story.append(fig_to_rli(fig_p2))
            story.append(Spacer(1, 0.5 * cm))
            story.append(Paragraph("5.3  Comparativa UCS 28 dias vs Requerimiento", S_BODY))
            story.append(Spacer(1, 0.2 * cm))
            story.append(fig_to_rli(fig_p3))
        except Exception as e_img:
            story.append(Paragraph(
                f"Nota: graficos no disponibles ({e_img}). "
                "Instale kaleido con: pip install kaleido", S_NOTE))
 
        # Pie
        story.append(Spacer(1, 0.6 * cm))
        story.append(hr())
        story.append(Paragraph(
            f"Sistema PF v1.0  |  Generado: {hoy_str}",
            S_RIGHT))
 
        doc.build(story)
        buf_pdf.seek(0)
        fname = f"Reporte_PasteFill_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        st.download_button(
            label="⬇️ Descargar Reporte PDF",
            data=buf_pdf, file_name=fname,
            mime="application/pdf", use_container_width=True,
        )
        st.success(f"✔ Reporte generado: {fname} — haga clic arriba para descargar.")
 
# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
hoy = datetime.datetime.now().strftime("%d/%m/%Y")
st.markdown(f"""
<style>
.footer-box {{
    margin-top: 40px; padding: 18px 24px; width: 100%; text-align: center;
    background: #e2ecf7; border-top: 3px solid #2b6cb0;
    border-radius: 10px; font-size: 13px; color: #1a365d;
}}
.footer-title {{ font-family: 'IBM Plex Serif', serif; font-size: 16px;
    color: #1a365d; font-weight: 700; }}
</style>
<div class="footer-box">
    <div class="footer-title">🪨 Relleno en Pasta · Sistema PF</div>
    <div>Diseño de mezcla, análisis de resistencia UCS y presión sobre barricada</div>
    <br>
    <div>Versión 1.0 · {hoy} · Landriault et al., 1996 / Mitchell, 1982</div>
</div>
""", unsafe_allow_html=True)