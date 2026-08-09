import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Dashboard Navigasi Bab - Tahfidz TI 2022", page_icon="📖", layout="wide")

COLOR_HADIR = "#00FF00"        # Hijau Terang (Hadir / AMAN)
COLOR_TIDAK_HADIR = "#FF0000"  # Merah Terang (Tidak Hadir / KRITIS)
COLOR_LINE = "#0000FF"         # Biru (% Kehadiran)

# 2. SIDEBAR: UPLOAD FILE & FILTER SEMESTER
st.sidebar.header("⚙️ Data Dinamis")
uploaded_file = st.sidebar.file_uploader("Upload File Excel/CSV Absensi", type=["xlsx", "csv"])

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
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.sidebar.success("File Berhasil Dimuat!")
    except Exception:
        st.sidebar.error("Format file gagal dimuat. Menggunakan data default.")
        df = pd.DataFrame(default_data)
else:
    df = pd.DataFrame(default_data)

selected_semester = st.sidebar.multiselect(
    "Filter Semester:",
    options=df["Semester"].unique(),
    default=df["Semester"].unique()
)
df_filtered = df[df["Semester"].isin(selected_semester)]

# REKALKULASI METRICS
total_mhs = df_filtered["Total Mahasiswa"].sum()
total_hadir = df_filtered["Hadir"].sum()
total_absen = df_filtered["Tidak Hadir"].sum()
pct_hadir = (total_hadir / total_mhs * 100) if total_mhs > 0 else 0

# 3. SIDEBAR: NAVIGASI BAB (TANPA SCROLL)
st.sidebar.divider()
st.sidebar.header("📌 Navigasi Bab")
nav_menu = st.sidebar.radio(
    "Pilih Tampilan Bab:",
    [
        "Semua Bab (Full Dashboard)",
        "1. Ringkasan Eksekutif",
        "2. Pendahuluan & 3. Metodologi",
        "4. Paparan Temuan & Tabel Data",
        "📊 Visualisasi Data (5 Diagram)",
        "📑 Analisis 4 Sudut Pandang",
        "5. Kesimpulan & 6. Rekomendasi"
    ]
)

# HEADER UTAMA DASHBOARD
st.markdown("<h4 style='text-align: center; color: #1E88E5;'>UNIVERSITAS DARUSSALAM GONTOR</h4>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>LAPORAN ANALISIS KEHADIRAN TAHFIDZ (NAVIGASI MODULAR)</h3>", unsafe_allow_html=True)
st.markdown("**Disusun Oleh:** Muhammad Hanan Annafi, Muhammad Raja Jibran, Akhogi Wafa, Sadam Husen, Muhammad Dafi al haq")
st.divider()

# ==================== MODUL / BAB CONTENT ====================

# BAB 1: RINGKASAN EKSEKUTIF
if nav_menu in ["Semua Bab (Full Dashboard)", "1. Ringkasan Eksekutif"]:
    st.header("1. Ringkasan Eksekutif")
    st.info("""
    Analisis ini mengevaluasi data kehadiran program Tahfidz mahasiswa Teknik Informatika angkatan 2022. Dari total 141 catatan kehadiran, hanya 69 kali (48.9%) mahasiswa hadir, sementara 72 kali (51.1%) tidak hadir. Penurunan paling drastis terjadi pada Semester 5, dari 90.2% (Semester 1) menjadi 6.9%.
    """)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Data Terfilter", f"{total_mhs} Mahasiswa")
    m2.metric("Total Hadir", f"{total_hadir} ({pct_hadir:.1f}%)")
    m3.metric("Total Tidak Hadir", f"{total_absen} ({(100-pct_hadir):.1f}%)")
    m4.metric("Status Sistem", "KRITIS" if pct_hadir < 75 else "AMAN")
    st.divider()

# BAB 2 & 3: PENDAHULUAN & METODOLOGI
if nav_menu in ["Semua Bab (Full Dashboard)", "2. Pendahuluan & 3. Metodologi"]:
    c_p1, c_p2 = st.columns(2)
    with c_p1:
        st.header("2. Pendahuluan")
        st.write("**2.1 Konteks Operasional:** Program Tahfidz merupakan instrumen strategis pembentuk karakter mahasiswa TI 2022. Pemantauan kehadiran mencerminkan tingkat student engagement.")
        st.write("**2.2 Tujuan Analisis:** Mendeskripsikan kondisi aktual, mengidentifikasi akar penyebab, memproyeksikan dampak, dan merumuskan solusi.")
    with c_p2:
        st.header("3. Metodologi")
        st.write("**3.1 Sumber Data:** Pertemuan ke-13 kelas A2 mencakup 5 semester (141 catatan).")
        st.write("**3.2 Pendekatan Analisis:** Deskriptif, Diagnostik, Prediktif, dan Preskriptif.")
        st.write("**3.3 Visualisasi Data:** Menggunakan 5 jenis diagram interaktif.")
    st.divider()

# BAB 4: PAPARAN TEMUAN & TABEL DATA
if nav_menu in ["Semua Bab (Full Dashboard)", "4. Paparan Temuan & Tabel Data"]:
    st.header("4. Paparan Temuan")
    st.write("#### Tabel 1: Ringkasan Data Kehadiran Tahfidz")
    st.dataframe(df_filtered, use_container_width=True, hide_index=True)
    st.divider()

# VISUALISASI DATA (5 DIAGRAM)
if nav_menu in ["Semua Bab (Full Dashboard)", "📊 Visualisasi Data (5 Diagram)"]:
    st.header("📊 Visualisasi Data (5 Diagram Laporan)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Figure 1: Kehadiran vs Ketidakhadiran")
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Hadir"], name="Hadir", marker_color=COLOR_HADIR))
        fig1.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR))
        fig1.update_layout(barmode="group", yaxis_title="Jumlah Mahasiswa")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Figure 2: Distribusi Total Kehadiran")
        fig2 = px.pie(
            names=["Hadir", "Tidak Hadir"],
            values=[total_hadir, total_absen],
            color=["Hadir", "Tidak Hadir"],
            color_discrete_map={"Hadir": COLOR_HADIR, "Tidak Hadir": COLOR_TIDAK_HADIR}
        )
        st.plotly_chart(fig2, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Figure 3: Tren Persentase Kehadiran")
        fig3 = px.line(df_filtered, x="Semester", y="% Hadir", markers=True, text=[f"{v}%" for v in df_filtered["% Hadir"]])
        fig3.update_traces(textposition="top center", line_color=COLOR_LINE, line_width=3)
        fig3.update_layout(yaxis_range=[0, 110])
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("Figure 4: Komposisi Kehadiran (Stacked)")
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Hadir"], name="Hadir", marker_color=COLOR_HADIR))
        fig4.add_trace(go.Bar(x=df_filtered["Semester"], y=df_filtered["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR))
        fig4.update_layout(barmode="stack", yaxis_title="Jumlah Mahasiswa")
        st.plotly_chart(fig4, use_container_width=True)

    st.subheader("Figure 5: Diagram Kehadiran dengan Rata-rata")
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
    st.divider()

# ANALISIS 4 SUDUT PANDANG
if nav_menu in ["Semua Bab (Full Dashboard)", "📑 Analisis 4 Sudut Pandang"]:
    st.header("📑 Analisis 4 Sudut Pandang")
    t1, t2, t3, t4 = st.tabs(["Deskriptif", "Diagnostik", "Prediktif", "Preskriptif"])
    
    with t1:
        st.write("### 4.1 Deskriptif")
        st.write("Penurunan persentase dimulai dari Semester 3 (66.7%) dan collapse di Semester 5 (6.9%). Partisipasi rata-rata total hanya 48.9%.")
    with t2:
        st.write("### 4.2 Diagnostik")
        st.write("Benturan kegiatan Magang/KKP, disrupsi lokasi geografis luar kota, dan beban organisasi kepanitiaan besar (PKKMB, Wisuda, Seminar).")
    with t3:
        st.write("### 4.3 Prediktif")
        st.write("Inefisiensi pemborosan anggaran Murobbi/fasilitas hingga 93%, kegagalan target hafalan, dan risiko penundaan skripsi.")
    with t4:
        st.write("### 4.4 Preskriptif")
        st.write("Penerapan platform absensi online, pendampingan Murobbi fleksibel, sistem insentif, dan Early Warning System (EWS).")
    st.divider()

# BAB 5 & 6: KESIMPULAN & REKOMENDASI
if nav_menu in ["Semua Bab (Full Dashboard)", "5. Kesimpulan & 6. Rekomendasi"]:
    st.header("5. Kesimpulan")
    st.warning("Masalah utama bukan penurunan komitmen individu secara absolut, melainkan ketidakmampuan sistem dalam mengakomodasi benturan jadwal dan kendala geografis.")
    
    st.header("6. Rekomendasi")
    st.write("#### Tabel 2: Prioritas Rekomendasi")
    rekom_df = pd.DataFrame({
        "No": [1, 2, 3, 4, 5],
        "Rekomendasi": ["Absensi Online", "Jadwal Fleksibel", "Peringatan Dini", "Insentif", "Kerjasama Magang"],
        "Detail": [
            "Sistem digital untuk mahasiswa magang luar kota",
            "Slot pagi/sore/weekend untuk mahasiswa sibuk",
            "Protokol intervensi setelah 2x absen berturut-turut",
            "Sertifikat/penghargaan pencapaian hafalan",
            "MoU dengan perusahaan untuk izin tahfidz"
        ],
        "Prioritas": ["Tinggi", "Tinggi", "Sedang", "Sedang", "Normal"]
    })
    st.dataframe(rekom_df, use_container_width=True, hide_index=True)
