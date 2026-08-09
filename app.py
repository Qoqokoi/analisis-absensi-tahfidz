import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Dashboard Dinamis Tahfidz TI 2022", page_icon="⚡", layout="wide")

COLOR_HADIR = "#00FF00"        # Hijau (Hadir / AMAN)
COLOR_TIDAK_HADIR = "#FF0000"  # Merah (Tidak Hadir / KRITIS)
COLOR_LINE = "#0000FF"         # Biru (% Kehadiran)

# 2. SIDEBAR: FITUR DINAMIS (UPLOAD FILE & FILTER)
st.sidebar.header("⚙️ Panel Data")
uploaded_file = st.sidebar.file_uploader("Upload File Excel/CSV Absensi", type=["xlsx", "csv"])

# DATASET DEFAULT (JIKA TIDAK UPLOAD FILE)
default_data = {
    "Semester": ["Semester 1", "Semester 3", "Semester 5", "Semester 7", "Semester 9"],
    "Total Mahasiswa": [51, 24, 29, 29, 8],
    "Hadir": [46, 16, 2, 4, 1],
    "Tidak Hadir": [5, 8, 27, 25, 7],
    "% Hadir": [90.2, 66.7, 6.9, 13.8, 12.5],
    "Status Performa": ["Baik", "WARNING", "CRITICAL", "CRITICAL", "CRITICAL"]
}

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df_raw = pd.read_csv(uploaded_file)
        else:
            df_raw = pd.read_excel(uploaded_file)
        st.sidebar.success("File Berhasil Dimuat!")
        df = df_raw
    except Exception as e:
        st.sidebar.error("Format file tidak sesuai. Gunakan data default.")
        df = pd.DataFrame(default_data)
else:
    df = pd.DataFrame(default_data)

# FILTER DINAMIS SEMESTER
selected_semester = st.sidebar.multiselect(
    "Filter Semester:",
    options=df["Semester"].unique(),
    default=df["Semester"].unique()
)

# KELOLA DATA TERFILTER
df_filtered = df[df["Semester"].isin(selected_semester)]

# 3. HEADER & METRICS DINAMIS
st.markdown("<h3 style='text-align: center; color: #1E88E5;'>UNIVERSITAS DARUSSALAM GONTOR</h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>DASHBOARD ANALISIS KEHADIRAN TAHFIDZ</h2>", unsafe_allow_html=True)
st.markdown("**Disusun Oleh:** Muhammad Hanan Annafi, Muhammad Raja Jibran, Akhogi Wafa, Sadam Husen, Muhammad Dafi al haq")

st.divider()

# REKALKULASI METRICS SECARA OTOMATIS
total_mhs = df_filtered["Total Mahasiswa"].sum()
total_hadir = df_filtered["Hadir"].sum()
total_absen = df_filtered["Tidak Hadir"].sum()
pct_hadir = (total_hadir / total_mhs * 100) if total_mhs > 0 else 0

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Data Terpilih", f"{total_mhs} Mahasiswa")
m2.metric("Total Hadir", f"{total_hadir} ({pct_hadir:.1f}%)")
m3.metric("Total Tidak Hadir", f"{total_absen} ({(100-pct_hadir):.1f}%)")
m4.metric("Status Sistem", "KRITIS" if pct_hadir < 75 else "AMAN")

st.divider()

# 4. TABEL DATA DINAMIS
st.subheader("📋 Tabel Data Absensi Terfilter")
st.dataframe(df_filtered, use_container_width=True, hide_index=True)

st.divider()

# 5. GRAFIK DINAMIS
st.header("📊 Visualisasi Data Interaktif")

c1, c2 = st.columns(2)

with c1:
    st.subheader("Figure 1: Bar Chart (Hadir vs Absen)")
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Hadir"], name="Hadir", marker_color=COLOR_HADIR))
    fig1.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR))
    fig1.update_layout(barmode="group", yaxis_title="Jumlah Mahasiswa")
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.subheader("Figure 2: Pie Chart Total Kehadiran")
    fig2 = px.pie(
        names=["Hadir", "Tidak Hadir"],
        values=[total_hadir, total_absen],
        color=["Hadir", "Tidak Hadir"],
        color_discrete_map={"Hadir": COLOR_HADIR, "Tidak Hadir": COLOR_TIDAK_HADIR}
    )
    st.plotly_chart(fig2, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    st.subheader("Figure 3: Line Chart Tren Kehadiran")
    fig3 = px.line(
        df_filtered, x="Semester", y="% Hadir", markers=True,
        text=[f"{v}%" for v in df_filtered["% Hadir"]]
    )
    fig3.update_traces(textposition="top center", line_color=COLOR_LINE, line_width=3)
    fig3.update_layout(yaxis_range=[0, 110])
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    st.subheader("Figure 4: Stacked Bar Chart")
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Hadir"], name="Hadir", marker_color=COLOR_HADIR))
    fig4.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR))
    fig4.update_layout(barmode="stack", yaxis_title="Jumlah Mahasiswa")
    st.plotly_chart(fig4, use_container_width=True)

# Figure 5: Combo Chart
st.subheader("Figure 5: Combo Chart dengan Sumbu Sekunder")
fig5 = go.Figure()
fig5.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Hadir"], name="Hadir", marker_color=COLOR_HADIR, yaxis="y"))
fig5.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR, yaxis="y"))
fig5.add_trace(go.Scatter(
    x=df_filtered["Semester"], y=df_filtered["% Hadir"], name="% Kehadiran",
    yaxis="y2", mode="lines+markers", line=dict(color=COLOR_LINE, width=3)
))
fig5.update_layout(
    yaxis=dict(title="Jumlah Mahasiswa"),
    yaxis2=dict(title="% Kehadiran", overlaying="y", side="right", range=[0, 110]),
    barmode="group"
)
st.plotly_chart(fig5, use_container_width=True)
