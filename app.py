import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Config Halaman
st.set_page_config(page_title="Dashboard Tahfidz TI 2022", layout="wide", page_icon="📊")

# Header & Informasi Kelompok
st.title("📊 Laporan Analisis Kehadiran Tahfidz TI 2022")
st.subheader("Universitas Darussalam Gontor - Pengantar Sains Data")
st.caption("Dibuat oleh Kelompok: Muhammad Hanan Annafi, Muhammad Raja Jibran, Akhogi Wafa, Sadam Husen, Muhammad Dafi al haq")

st.divider()

# Metric Cards (Ringkasan Angka Kunci)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Mahasiswa", "141 Orang")
col2.metric("Total Hadir", "69 (48.9%)")
col3.metric("Total Tidak Hadir", "72 (51.1%)", delta="-2.2%", delta_color="inverse")
col4.metric("Status Sistem", "KRITIS", delta="Di Bawah Standar 75%", delta_color="inverse")

st.divider()

# Layout 2 Kolom (Tabel Data & Visualisasi)
left_col, right_col = st.columns([1, 1.3])

with left_col:
    st.subheader("📋 Rekapitulasi Data Kehadiran")
    data = {
        "Semester": ["Semester 1", "Semester 3", "Semester 5", "Semester 7", "Semester 9"],
        "Total": [51, 24, 29, 29, 8],
        "Hadir": [46, 16, 2, 4, 1],
        "Tidak Hadir": [5, 8, 27, 25, 7],
        "% Kehadiran": [90.2, 66.7, 6.9, 13.8, 12.5],
        "Status": ["Baik", "WARNING", "CRITICAL", "CRITICAL", "CRITICAL"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)

with right_col:
    st.subheader("📈 Combo Chart Interaktif (Hadir vs Tidak Hadir)")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df["Semester"], y=df["Hadir"], name="Hadir", marker_color="#2ECC71"))
    fig.add_trace(go.Bar(x=df["Semester"], y=df["Tidak Hadir"], name="Tidak Hadir", marker_color="#E74C3C"))
    fig.add_trace(go.Scatter(
        x=df["Semester"], y=df["% Kehadiran"], name="% Kehadiran", 
        yaxis="y2", mode="lines+markers+text", 
        text=[f"{v}%" for v in df["% Kehadiran"]], textposition="top center",
        line=dict(color="#2980B9", width=3)
    ))
    fig.update_layout(
        yaxis=dict(title="Jumlah Mahasiswa"),
        yaxis2=dict(title="% Kehadiran", overlaying="y", side="right", range=[0, 110]),
        barmode="group",
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Laporan Naratif 4 Sudut Pandang (Sistem Tab)
st.subheader("📑 Laporan Naratif & Analisis 4 Sudut Pandang")
tab1, tab2, tab3, tab4 = st.tabs(["1. Descriptive", "2. Diagnostic", "3. Predictive", "4. Prescriptive"])

with tab1:
    st.write("### 🔍 Deskripsi Masalah")
    st.markdown("""
    * **Rata-Rata Kehadiran Total Gagal**: Hanya menyentuh **48.9%** (69 dari 141 mahasiswa hadir), jauh di bawah ambang batas kelulusan **75%**.
    * **System Collapse (Semester 5)**: Kehadiran anjlok drastis dari **90.2%** (Semester 1) menjadi **6.9%** (Semester 5).
    * **Akar Masalah**: Pembangkangan/alpa massal terstruktur pada mahasiswa tingkat atas (>85% alpa).
    """)

with tab2:
    st.write("### 💡 Diagnostik Akar Masalah")
    st.markdown("""
    * **Beban Kurikulum Teknis (S5+)**: Puncak pengerjaan Tugas Besar (Tubas), praktikum lab, sprint coding, dan skripsi.
    * **Disrupsi Magang & Geografis**: Bentrok jam kerja magang/KKP dan lokasi di luar kota.
    * **Erosi Pengawasan**: Ketiadaan *punishment matrix* memicu normalisasi pembolosan (*normalization of deviance*).
    """)

with tab3:
    st.write("### ⚠️ Proyeksi Risiko Masa Depan")
    st.markdown("""
    * **Inefisiensi Anggaran**: Utilisasi fasilitas/murobbi di Semester 5 hanya **7%**, memicu pemborosan sumber daya kampus.
    * **Bottleneck Kelulusan**: Penumpukan tunggakan tahfidz menahan sidang skripsi dan meningkatkan risiko *Drop Out* (DO).
    * **Penularan Budaya**: Pembolosan senior dicontoh oleh angkatan di bawahnya.
    """)

with tab4:
    st.write("### ✅ Solusi Strategis Berbasis Data")
    st.markdown("""
    * **Automated Early Warning System**: Notifikasi WA/Telegram otomatis jika alpa 2x + pemblokiran sementara KRS/Kartu Ujian.
    * **Format Flexi-Mentoring (S5+)**: Ubah karantina fisik menjadi setoran *Peer-Mentoring* kelompok kecil.
    * **Digitalisasi Absensi**: Platform setoran *online* khusus mahasiswa magang di luar kota.
    """)
