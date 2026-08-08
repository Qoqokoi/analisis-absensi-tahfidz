import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Laporan Naratif Tahfidz TI 2022",
    page_icon="📚",
    layout="wide"
)

# DATASET UTAMA (SESUAI NARRATIVE REPORT PDF)
data = {
    "Semester": ["Semester 1", "Semester 3", "Semester 5", "Semester 7", "Semester 9"],
    "Total Mahasiswa": [51, 24, 29, 29, 8],
    "Hadir": [46, 16, 2, 4, 1],
    "Tidak Hadir": [5, 8, 27, 25, 7],
    "% Hadir": [90.2, 66.7, 6.9, 13.8, 12.5],
    "Status Performa": ["Baik", "WARNING", "CRITICAL", "CRITICAL", "CRITICAL"]
}
df = pd.DataFrame(data)

# SKEMA WARNA DIAGRAM (SESUAI PDF KELOMPOK)
COLOR_HADIR = "#00FF00"        # Hijau Terang (Hadir / AMAN)
COLOR_TIDAK_HADIR = "#FF0000"  # Merah Terang (Tidak Hadir / KRITIS)
COLOR_LINE = "#0000FF"         # Biru (% Kehadiran)

# 2. HEADER & IDENTITAS KELOMPOK
st.markdown("<h4 style='text-align: center; color: #1E88E5;'>UNIVERSITAS DARUSSALAM GONTOR</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>Fakultas Sains dan Teknologi | Program Studi Teknik Informatika (2025/2026)</h5>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>LAPORAN NARATIF ANALISIS KEHADIRAN TAHFIDZ MAHASISWA TEKNIK INFORMATIKA 2022</h2>", unsafe_allow_html=True)
st.markdown("**Disusun Oleh (Kelompok):** Muhammad Hanan Annafi, Muhammad Raja Jibran, Akhogi Wafa, Sadam Husen, Muhammad Dafi al haq")

st.divider()

# 3. RINGKASAN EKSEKUTIF
st.header("1. Ringkasan Eksekutif")
st.info("""
Analisis ini mengevaluasi data kehadiran program Tahfidz mahasiswa Teknik Informatika angkatan 2022. Dari total 141 catatan kehadiran, hanya 69 kali (48.9%) mahasiswa hadir, sementara 72 kali (51.1%) tidak hadir. Penurunan paling drastis terjadi pada Semester 5, dari 90.2% (Semester 1) menjadi 6.9%. Temuan utama menunjukkan bahwa masalah bersifat sistemik, bukan sekadar penurunan komitmen individu, melainkan ketidakmampuan program mengakomodasi benturan jadwal magang dan kegiatan kampus mahasiswa senior.

**Rekomendasi utama:** Transformasi digital (absensi online) dan fleksibilitas jadwal pendampingan merupakan langkah kritis untuk mengembalikan partisipasi mahasiswa senior.
""")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Catatan Kehadiran", "141 Data")
m2.metric("Total Hadir", "69 (48.9%)")
m3.metric("Total Tidak Hadir", "72 (51.1%)")
m4.metric("Nadir Semester 5", "6.9% Hadir")

st.divider()

# 4. PENDAHULUAN & METODOLOGI
col_intro1, col_intro2 = st.columns(2)

with col_intro1:
    st.header("2. Pendahuluan")
    st.subheader("2.1 Konteks Operasional")
    st.write("Program Tahfidz merupakan instrumen strategis dalam membentuk karakter dan integritas akademik mahasiswa Teknik Informatika (TI) angkatan 2022. Dalam perspektif penjaminan mutu, pemantauan kehadiran bukan sekadar rutinitas administratif, melainkan indikator fundamental bagi keberhasilan internalisasi nilai-nilai program dan efektivitas investasi sumber daya institusi.")
    
    st.subheader("2.2 Tujuan Analisis")
    st.markdown("""
    1. Mendeskripsikan kondisi aktual kehadiran tahfidz per semester.
    2. Mengidentifikasi akar penyebab penurunan kehadiran.
    3. Memproyeksikan dampak jika tren dibiarkan.
    4. Merumuskan rekomendasi strategis perbaikan program.
    """)

with col_intro2:
    st.header("3. Metodologi")
    st.subheader("3.1 Sumber Data & 3.2 Pendekatan Analisis")
    st.write("Data dikumpulkan dari sistem pencatatan kehadiran program Tahfidz mahasiswa TI 2022 pada pertemuan ke-13 kelas A2 mencakup 5 kelompok semester (1, 3, 5, 7, dan 9) dengan total 141 catatan kehadiran.")
    st.markdown("""
    * **Analisis Deskriptif**: Evaluasi statistik kehadiran per semester.
    * **Analisis Diagnostik**: Identifikasi faktor penyebab (hambatan struktural & psikologis).
    * **Analisis Prediktif**: Proyeksi risiko berdasarkan tren penurunan.
    * **Analisis Preskriptif**: Perumusan framework solusi berbasis data.
    """)
    
    st.subheader("3.3 Visualisasi Data")
    st.write("Mengintegrasikan 5 jenis visualisasi data pendukung (Bar Chart, Pie Chart, Line Chart, Stacked Bar Chart, dan Diagram Rata-rata/Combo).")

st.divider()

# 5. PAPARAN TEMUAN & TABEL 1
st.header("4. Paparan Temuan")
st.subheader("4.1 Analisis Deskriptif: Evaluasi Kritis Kinerja Kehadiran")
st.write("Dalam evaluasi program pendidikan, stabilitas kehadiran adalah metrik utama keterlibatan mahasiswa. Penurunan angka kehadiran yang drastis merupakan sinyal kegagalan ekosistem pembelajaran dalam mengakomodasi dinamika peserta didik.")

st.write("#### Tabel 1: Ringkasan Data Kehadiran Tahfidz")
st.dataframe(df, use_container_width=True, hide_index=True)

st.caption("Penurunan kinerja dimulai jauh sebelum fase kritis (turun 23.5 poin persentase dari Sem 1 ke Sem 3). Titik keruntuhan (tipping point) terjadi pada Semester 5 di mana kehadiran jatuh hingga 6.9%. Secara agregat, partisipasi keseluruhan hanya menyentuh angka 48.9%.")

# FIGURE 1 & FIGURE 2
c_fig1, c_fig2 = st.columns(2)

with c_fig1:
    st.subheader("Figure 1: Kehadiran vs Ketidakhadiran per Semester")
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df["Semester"], y=df["Hadir"], name="Hadir", marker_color=COLOR_HADIR))
    fig1.add_trace(go.Bar(x=df["Semester"], y=df["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR))
    fig1.update_layout(barmode="group", yaxis_title="Jumlah Mahasiswa", title="Analisis Kehadiran Karantina Tahfidz TI 2022")
    st.plotly_chart(fig1, use_container_width=True)

with c_fig2:
    st.subheader("Figure 2: Distribusi Total Kehadiran")
    fig2 = px.pie(
        names=["AMAN", "KRITIS"],
        values=[16.7, 83.3],
        color=["AMAN", "KRITIS"],
        color_discrete_map={"AMAN": COLOR_HADIR, "KRITIS": COLOR_TIDAK_HADIR},
        title="Distribusi Total Kehadiran"
    )
    st.plotly_chart(fig2, use_container_width=True)

# FIGURE 3
st.subheader("Figure 3: Tren Persentase Kehadiran")
fig3 = px.line(
    df, x="Semester", y="% Hadir", markers=True,
    text=[f"{v}%" for v in df["% Hadir"]],
    title="Tren Persentase Kehadiran Tahfidz"
)
fig3.update_traces(textposition="top center", line_color=COLOR_LINE, line_width=3)
fig3.update_layout(yaxis_range=[0, 110], yaxis_title="Persentase Kehadiran (%)")
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# 6. ANALISIS DIAGNOSTIK & FIGURE 4
st.subheader("4.2 Analisis Diagnostik: Identifikasi Hambatan dan Disrupsi")

col_diag1, col_diag2 = st.columns([1.2, 1])

with col_diag1:
    st.markdown("""
    **A. Hambatan Struktural dan Operasional (Rigiditas Sistem)**
    * **Benturan Profesional (Magang/KKP)**: Mahasiswa Semester 7 ke atas menghadapi kewajiban magang yang tidak fleksibel.
    * **Disrupsi Geografis**: Lokasi magang yang jauh atau di luar kota menciptakan penghalang fisik total.
    * **Beban Organisasi Mahasiswa Senior**: Semester 5 merupakan "tulang punggung" kepanitiaan kampus (PKKMB, Wisuda, Seminar).

    **B. Hambatan Psikologis dan Prioritas Akademik**
    * **Fokus Penyelesaian Studi**: Pada Semester 7 dan 9, perhatian terserap pada skripsi dan wisuda. Program tahfidz dianggap beban tambahan.
    """)

with col_diag2:
    st.subheader("Figure 4: Komposisi Kehadiran per Semester")
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=df["Semester"], y=df["Hadir"], name="Hadir", marker_color=COLOR_HADIR))
    fig4.add_trace(go.Bar(x=df["Semester"], y=df["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR))
    fig4.update_layout(barmode="stack", yaxis_title="Jumlah Mahasiswa", title="Komposisi Kehadiran Per Semester")
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# 7. ANALISIS PREDIKTIF & FIGURE 5
st.subheader("4.3 Analisis Prediktif & Figure 5: Diagram Kehadiran dengan Rata-rata")

col_pred1, col_pred2 = st.columns([1, 1.2])

with col_pred1:
    st.markdown("""
    1. **Inefisiensi dan Pemborosan Sumber Daya**: Pada Semester 5, ketidakhadiran mencapai 93%. Utilisasi nyata hanya 7% padahal anggaran Murobbi & fasilitas dialokasikan penuh.
    2. **Erosi Kualitas dan Standar Lulusan**: Kehadiran di bawah 10% pada semester senior membuat target hafalan tidak tercapai.
    3. **Proyeksi Kehadiran Masa Depan**: Kehadiran diprediksi terus berada di bawah 10% jika tanpa intervensi.
    """)

with col_pred2:
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(x=df["Semester"], y=df["Hadir"], name="Hadir", marker_color=COLOR_HADIR, yaxis="y"))
    fig5.add_trace(go.Bar(x=df["Semester"], y=df["Tidak Hadir"], name="Tidak Hadir", marker_color=COLOR_TIDAK_HADIR, yaxis="y"))
    fig5.add_trace(go.Scatter(
        x=df["Semester"], y=df["% Hadir"], name="% Kehadiran",
        yaxis="y2", mode="lines+markers", line=dict(color=COLOR_LINE, width=3)
    ))
    fig5.update_layout(
        title="Analisis Rata-Rata Kehadiran Karantina Tahfidz TI 2022",
        yaxis=dict(title="Jumlah Mahasiswa"),
        yaxis2=dict(title="% Kehadiran", overlaying="y", side="right", range=[0, 110]),
        barmode="group"
    )
    st.plotly_chart(fig5, use_container_width=True)

st.divider()

# 8. ANALISIS PRESKRIPTIF, KESIMPULAN & REKOMENDASI (TABEL 2)
st.subheader("4.4 Analisis Preskriptif: Framework Solusi dan Mitigasi")
st.markdown("""
1. **Implementasi Segera Platform Digital**: Absensi dan setoran online bagi mahasiswa magang luar kota.
2. **Transformasi Peran Murobbi (Pendampingan Fleksibel)**: Pendampingan berbasis milestone waktu fleksibel.
3. **Reinforcement melalui Sistem Insentif**: Sertifikat/penghargaan formal atas pencapaian hafalan.
4. **Aktivasi Sistem Peringatan Dini (EWS)**: Intervensi dan konseling jika mahasiswa absen 2x berturut-turut.
""")

st.header("5. Kesimpulan")
st.warning("Program Tahfidz TI 2022 menghadapi krisis partisipasi sistemik pada level mahasiswa senior. Penurunan drastis dari 90.2% (Semester 1) ke 6.9% (Semester 5) membuktikan model pelaksanaan saat ini tidak kompatibel dengan dinamika mahasiswa. Solusi tunggal paling efektif adalah transformasi digital dan fleksibilitas kurikulum.")

st.header("6. Rekomendasi")
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
st.write("#### Tabel 2: Prioritas Rekomendasi")
st.dataframe(rekom_df, use_container_width=True, hide_index=True)
