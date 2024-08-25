import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Muat data yang sudah dibersihkan
df_day = pd.read_csv('D:\projekdicoding\DataHasil\cleaned_day.csv')
df_hour = pd.read_csv('D:\projekdicoding\DataHasil\cleaned_hour.csv')

# Judul aplikasi
st.title('Analisis Penggunaan Sepeda')

# Bagian Latar Belakang
st.header('Latar Belakang')
st.write("""
Sistem berbagi sepeda adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses, 
mulai dari keanggotaan, penyewaan, hingga pengembalian, telah menjadi otomatis. Pengguna dapat dengan mudah 
menyewa sepeda dari satu lokasi dan mengembalikannya ke lokasi lain. Sistem ini berperan penting dalam 
pengelolaan lalu lintas, masalah lingkungan, dan kesehatan masyarakat.
""")

st.write("""
Dataset yang digunakan dalam analisis ini berdasarkan log historis selama dua tahun dari sistem Capital Bikeshare 
di Washington, D.C., untuk tahun 2011 dan 2012. Data ini telah diakumulasikan baik secara harian maupun per jam, 
dan informasi cuaca tambahan telah disertakan untuk memahami dampak faktor lingkungan terhadap perilaku penyewaan sepeda.
""")

# Kesimpulan 1: Musim yang Paling Populer
st.header('Kesimpulan 1: Musim dengan Penggunaan Sepeda Terbanyak')

# Menghitung penggunaan sepeda berdasarkan musim
season_usage = df_day.groupby('season')['cnt'].mean().reset_index()

# Mapping untuk mengganti nilai season menjadi nama musim yang lebih jelas
season_mapping = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
season_usage['Musim'] = season_usage['season'].map(season_mapping)

# Plot grafik penggunaan sepeda berdasarkan musim
fig, ax = plt.subplots()
sns.barplot(data=season_usage, x='Musim', y='cnt', ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Penggunaan Sepeda')
ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Musim')

st.pyplot(fig)

st.write("""
Musim Panas dan Gugur: Musim panas lebih populer karena cuaca yang hangat dan cerah, yang menarik banyak orang untuk bersepeda. Musim gugur juga tinggi karena cuaca masih mendukung meski tidak sehangat musim panas.
Musim Semi: Penggunaan lebih rendah karena cuaca yang masih tidak menentu dan suhu yang relatif lebih dingin.
Musim Dingin: Penggunaan terendah karena faktor cuaca dingin dan kondisi yang kurang bersahabat untuk bersepeda.
""")

# Kesimpulan 2: Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan
st.header('Kesimpulan 2: Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan')

# Menghitung penggunaan sepeda berdasarkan hari
day_of_week_usage = df_day.groupby('weekday')['cnt'].mean().reset_index()

# Plot grafik penggunaan sepeda berdasarkan hari
fig, ax = plt.subplots()
sns.barplot(data=day_of_week_usage, x='weekday', y='cnt', ax=ax)
ax.set_xlabel('Hari dalam Minggu')
ax.set_ylabel('Rata-rata Penggunaan Sepeda')
ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Hari dalam Minggu')

st.pyplot(fig)

st.write("""
Penggunaan sepeda cukup konsisten antara hari kerja dan akhir pekan/hari libur, 
yang menunjukkan bahwa sepeda digunakan baik untuk keperluan transportasi sehari-hari 
maupun rekreasi. Perusahaan dapat mengalokasikan sumber daya secara merata sepanjang minggu 
karena tidak ada perbedaan signifikan antara hari kerja dan akhir pekan dalam hal penggunaan sepeda.
""")

# Informasi Tambahan tentang Dataset
st.header('Informasi Dataset')
st.write("""
Dataset ini berisi data penggunaan sepeda dari Capital Bikeshare di Washington D.C. selama tahun 2011 dan 2012. 
Data mencakup informasi mengenai kondisi cuaca, musim, dan faktor lainnya yang mempengaruhi penggunaan sepeda.
""")

st.write("""
Untuk detail lebih lanjut tentang dataset ini, berikut adalah beberapa poin penting:
- Data dikumpulkan dari sistem Capital Bikeshare.
- Periode data meliputi tahun 2011 dan 2012.
- Informasi cuaca ditambahkan dari sumber eksternal untuk analisis lebih lanjut.
""")

st.write("""
Dataset ini dapat digunakan untuk berbagai tujuan penelitian, termasuk regresi untuk memprediksi jumlah sepeda yang disewa 
dan deteksi anomali berdasarkan peristiwa tertentu yang terjadi di kota, seperti Badai Sandy pada 30 Oktober 2012.
""")
