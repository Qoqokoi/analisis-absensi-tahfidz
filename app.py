import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Laporan Naratif Tahfidz TI 2022",
    page_icon="🎓",
    layout="wide"
)

# DATASET UTAMA
data = {
    "Semester": ["Semester 1", "Semester 3", "Semester 5", "Semester 7", "Semester 9"],
    "Total": [51, 24, 29, 29, 8],
    "Hadir": [46, 16, 2, 4, 1],
    "Tidak Hadir": [5, 8, 27, 25, 7],
    "% Hadir": [90.2, 66.7, 6.9, 13.8, 12.5],
    "Status": ["Baik", "WARNING", "CRITICAL", "CRITICAL", "CRITICAL"]
}
df = pd.DataFrame(data)

# 2. HEADER & IDENTITAS KELOMPOK
st.markdown("<h3 style='text-align: center;'>UNIVERSITAS DARUSSALAM GONTOR</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Fakultas Sains dan Teknologi | Program Studi Teknik Informatika</h4>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>LAPORAN NARATIF ANALISIS KEHADIRAN TAHFIDZ</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Mahasiswa TI Angkatan 2022 — Tahun Ajaran 2025/2026</h5>", unsafe_allow_html=True)

st.write("**Disusun Oleh Kelompok:** Muhammad Hanan Annafi, Muhammad Raja Jibran, Akhogi Wafa, Sadam Husen, Muhammad Dafi al haq")
st.divider()

# 3. RINGKASAN EKSEKUTIF & METRICS
st.header("1. Ringkasan Eksekutif")
st.info("""
Analisis ini mengevaluasi data kehadiran program Tahfidz mahasiswa Teknik Informatika angkatan 2022. 
Dari total 141 catatan kehadiran, hanya 69 kali (48.9%) mahasiswa hadir, sementara 72 kali (51.1%) tidak hadir. 
Penurunan paling drastis terjadi pada Semester 5, dari 90.2% (Semester 1) menjadi 6.9%.
""")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Catatan", "141 Data")
m2.metric("Total Hadir", "69 (48.9%)")
m3.metric("Total Tidak Hadir", "72 (51.1%)")
m4.metric("Titik Nadir (Sem 5)", "6.9% Hadir")

st.divider()

# 4. PENDAHULUAN & METODOLOGI
with st.expander("📌 2. Pendahuluan & 3. Metodologi (Klik untuk Membuka)", expanded=False):
    st.write("### 2.1 Konteks Operasional")
    st.write("Program Tahfidz merupakan instrumen strategis dalam membentuk karakter dan integritas akademik mahasiswa TI 2022. Pemantauan kehadiran mencerminkan tingkat student engagement dan komitmen terhadap standar mutu lulusan.")
    
    st.write("### 3. Metodologi & Sumber Data")
    st.write("Data dikumpulkan dari sistem pencatatan kehadiran program Tahfidz mahasiswa TI 2022 pada pertemuan ke-13 kelas A2, mencakup 5 kelompok semester (1, 3, 5, 7, dan 9). Pendekatan menggunakan 4 tingkat analisis (Deskriptif, Diagnostik, Prediktif, Preskriptif) dan 5 jenis visualisasi data.")

st.divider()

# 5. PAPARAN TEMUAN & TABEL DATA
st.header("4. Paparan Temuan & Data Kehadiran")

st.subheader("Table 1: Ringkasan Data Kehadiran Tahfidz")
st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

# 6. 5 VISUALISASI DIAGRAM (100% SAMA DENGAN LAPORAN)
st.header("📊 Visualisasi Data (5 Diagram Laporan)")

col1, col2 = st.columns(2)

# Figure 1: Bar Chart
with col1:
    st.subheader("Figure 1: Kehadiran vs Ketidakhadiran")
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df["Semester"], y=df["Hadir"], name="Hadir", marker_color="#1f77b4"))
    fig1.add_trace(go.Bar(x=df["Semester"], y=df["Tidak Hadir"], name="Tidak Hadir", marker_color="#d62728"))
    fig1.update_layout(barmode="group", yaxis_title="Jumlah Mahasiswa")
    st.plotly_chart(fig1, use_container_width=True)

# Figure 2: Pie Chart
with col2:
    st.subheader("Figure 2: Distribusi Total Kehadiran")
    fig2 = px.pie(
        names=["Hadir", "Tidak Hadir"],
        values=[69, 72],
        color_discrete_sequence=["#1f77b4", "#d62728"],
        hole=0.3
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

# Figure 3: Line Chart
with col3:
    st.subheader("Figure 3: Tren Persentase Kehadiran")
    fig3 = px.line(
        df, x="Semester", y="% Hadir", markers=True,
        text=[f"{v}%" for v in df["% Hadir"]]
    )
    fig3.update_traces(textposition="top center", line_color="#1f77b4", line_width=3)
    fig3.update_layout(yaxis_range=[0, 110], yaxis_title="Persentase Kehadiran (%)")
    st.plotly_chart(fig3, use_container_width=True)

# Figure 4: Stacked Bar Chart
with col4:
    st.subheader("Figure 4: Komposisi Kehadiran (Stacked)")
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=df["Semester"], y=df["Hadir"], name="Hadir", marker_color="#1f77b4"))
    fig4.add_trace(go.Bar(x=df["Semester"], y=df["Tidak Hadir"], name="Tidak Hadir", marker_color="#d62728"))
    fig4.update_layout(barmode="stack", yaxis_title="Jumlah Mahasiswa")
    st.plotly_chart(fig4, use_container_width=True)

# Figure 5: Bar Chart + Average Line
st.subheader("Figure 5: Perbandingan Kehadiran dengan Rata-rata")
fig5 = go.Figure()
fig5.add_trace(go.Bar(x=df["Semester"], y=df["Hadir"], name="Hadir", marker_color="#1f77b4"))
fig5.add_trace(go.Bar(x=df["Semester"], y=df["Tidak Hadir"], name="Tidak Hadir", marker_color="#d62728"))
fig5.add_hline(
    y=13.8, line_dash="dash", line_color="green",
    annotation_text="Rata-rata Hadir (13.8)", annotation_position="top right"
)
fig5.update_layout(barmode="group", yaxis_title="Jumlah Mahasiswa")
st.plotly_chart(fig5, use_container_width=True)

st.divider()

# 7. ANALISIS 4 SUDUT PANDANG
st.header("📑 Analisis 4 Sudut Pandang")

t1, t2, t3, t4 = st.tabs(["Deskriptif", "Diagnostik", "Prediktif", "Preskriptif"])

with t1:
    st.write("### 4.1 Analisis Deskriptif")
    st.write("Penurunan kinerja dimulai jauh sebelum fase kritis. Terdapat penurunan 23.5 poin persentase dari Semester 1 (90.2%) ke Semester 3 (66.7%) sebagai *early warning sign*. Titik keruntuhan (*tipping point*) terjadi pada Semester 5 di angka 6.9%. Partisipasi agregat hanya 48.9%.")

with t2:
    st.write("### 4.2 Analisis Diagnostik")
    st.write("**A. Hambatan Struktural:** Benturan kegiatan Magang/KKP pada Semester 7+, disrupsi geografis lokasi magang luar kota, serta beban organisasi kepanitiaan besar kampus di Semester 5 (PKKMB, Wisuda, Seminar).")
    st.write("**B. Hambatan Psikologis:** Perhatian terserap untuk skripsi dan wisuda di semester tua, membuat program tahfidz dianggap beban tambahan.")

with t3:
    st.write("### 4.3 Analisis Prediktif")
    st.markdown("""
    1. **Inefisiensi Sumber Daya**: Utilisasi fasilitas/Murobbi di Semester 5 hanya 7% dari alokasi anggaran penuh.
    2. **Erosi Kualitas Lulusan**: Target hafalan diprediksi gagal dicapai oleh mayoritas mahasiswa senior.
    3. **Proyeksi Kehadiran**: Kehadiran diprediksi terus berada di bawah 10% untuk mahasiswa senior jika tanpa intervensi.
    """)

with t4:
    st.write("### 4.4 Analisis Preskriptif")
    st.markdown("""
    1. **Platform Digital**: Sistem absensi dan setoran *online* bagi mahasiswa magang luar kota.
    2. **Pendampingan Fleksibel**: Murobbi menggunakan sistem *milestone* berbasis progres waktu fleksibel.
    3. **Sistem Insentif**: Pemberian sertifikat/penghargaan atas pencapaian hafalan.
    4. **Early Warning System (EWS)**: Protokol intervensi dan konseling jika mahasiswa absen 2x berturut-turut.
    """)

st.divider()

# 8. KESIMPULAN & REKOMENDASI (TABLE 2)
st.header("5. Kesimpulan & 6. Rekomendasi")

st.write("### Kesimpulan")
st.write("Program Tahfidz TI 2022 menghadapi krisis partisipasi sistemik pada mahasiswa senior. Masalah utama bukan penurunan komitmen individu, melainkan ketidakmampuan sistem mengakomodasi benturan jadwal dan kendala geografis.")

st.write("### Table 2: Prioritas Rekomendasi")
rekom_data = {
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
}
st.dataframe(pd.DataFrame(rekom_data), use_container_width=True, hide_index=True)
