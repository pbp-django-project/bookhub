**Anggota Kelompok:**   
Naufal Ichsan - 2206082013 - NI04Code  
Iqza Ardiansyah - 2206810042 - iqzaardiansyah  
Mariano Gerardus Senduk - 2206814236 - nano141004  
Shirin zarqaa rabbaanii arham - 2206081964 - shirinzarqaa  
Mario Michael Jeremy Sitanggang - 2206828626 - mariomichael  

**Nama Web App**: BookHub 
**Url PaaS**: bookhub-f06-tk.pbp.cs.ui.ac.id     

**Deskripsi Singkat**:
"BookHub" adalah sebuah platform inovatif yang bertujuan untuk menginspirasi dan meningkatkan minat dalam membaca buku. Platform ini menawarkan berbagai fitur interaktif yang dirancang untuk menghubungkan pengguna dengan buku-buku yang mereka gemarii, penulis yang mereka kagumi, dan komunitas literasi yang mereka hormati. Dengan fitur pencarian buku terperinci, pengguna dapat dengan mudah menemukan buku berdasarkan berbagai kriteria, sambil menjelajahi ulasan pengguna dan rekomendasi yang berguna. Pustaka Pribadi memungkinkan pengguna untuk mengatur daftar buku yang mereka baca, memberikan peringkat, dan berbagi ulasan dengan komunitas, sementara Buletin Literasi memberikan akses ke berita terkini dan artikel tentang dunia literasi. Dengan "BookHub," kami mengundang semua pecinta buku untuk menjelajahi, berinteraksi, dan berbagi kecintaan mereka pada literasi.
"BookHub" juga memberikan ruang bagi para penulis dan pembaca untuk terhubung, berinteraksi, dan mendiskusikan karya-karya sastra. Dengan akses ke dashboard admin, pengelola dapat dengan mudah mengelola konten dan mengawasi aktivitas pengguna.Oleh karena itu , "BookHub"  menjadi salah satu platform yang dapat berguna untuk menjelajahi dunia tak terbatas  melalui buku dan berkontribusi dalam memperkaya pengalaman literasi bersama komunitas yang bersemangat.
Fitur Utama:
1. Pencarian Buku Terperinci: Pengguna dapat mencari buku berdasarkan judul, penulis, genre, tahun terbit, atau kata kunci lainnya. Hasil pencarian akan menampilkan buku-buku dengan informasi terperinci, ulasan pengguna, dan rekomendasi terkait. (modul books)
2. Pustaka Pribadi: Setiap pengguna memiliki pustaka pribadi di mana mereka dapat menyimpan daftar buku yang telah mereka baca, sedang dibaca, atau ingin dibaca. Pengguna juga dapat memberikan peringkat dan menulis ulasan tentang buku-buku ini. (modul profile)
3. Buletin Literasi: Aplikasi akan memiliki bagian berita dan artikel tentang literasi, penulis terkenal, peristiwa literasi, dan tips membaca. Ini akan membantu meningkatkan kesadaran literasi pengguna.
4. Dashboard Admin: Sebuah dashboard admin akan memungkinkan pengelola untuk mengelola konten, mengawasi aktivitas pengguna, dan memodifikasi data buku. (django-admin)
5. Pengguna Terdaftar dan Anonim: Aplikasi akan mendukung pengguna terdaftar yang dapat membuat profil pribadi, serta pengguna anonim yang dapat menjelajahi buku dan artikel.
6. Fitur Ulasan: Setiap pengguna dapat mengulas buku yang sudah mereka baca dengan memberikan rating 0-5.
7. Fitur rekomendasi terkait: Ketika pengguna mengklik suatu judul buku, pada bagian web akan terdapat beberapa rekomendasi terkait berdasarkan genre atau penulis.
8. Fitur history baca: fitur ini akan menglist setiap buku yang telah dibuka oleh user.

Manfaat:
- Meningkatkan literasi di masyarakat dengan memfasilitasi akses ke berbagai buku dan literatur.
- Mendorong kolaborasi antara pembaca dan penulis.
- Membangun komunitas literasi yang aktif dan berbagi.
- Memberikan wawasan literasi melalui berita dan artikel berkualitas tinggi.
- Meningkatkan kesadaran literasi di tengah tema "Literasi dalam Kebinekaan untuk Kemajuan Bangsa" yang sedang berlangsung.

Dataset menggunakan antara,
Project Gutenberg: https://www.gutenberg.org/ebooks/offline_catalogs.html, https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv, dan https://drive.google.com/file/d/17jiAwHx_68zUrolbTl75IoLRFK_JLYrx/view
Atau Google API


**Modul**  
Modul Main: berisi homepage, login, signup, logout (pengelolaan user), contact, privacy policy, user terms. (Naufal)  

Modul Books: berisi segala pengolahan yang berkaitan dengan buku dan pemilahan baik berdasarkan genre, authors, tahun terbit, dll, terdapat fitur agar user bisa mengupload suatu buku atau delete buku yang telah diupload, terdapat pula detail buku seperti genre/authors/penerbit/sinopsis apabila buku diklik (Naufal)  

Modul Profile: berisi profil pengguna, menentukan role-role dari user dan hak-hak pengguna dalam menggunakan aplikasi profile pada umumnya. Modul ini juga rencananya akan memiliki fitur yang sering diimplementasi oleh aplikasi media sosial kebanyakan seperti mengganti username, menambahkan/mengganti foto profil, dsb. (Iqza)  

Modul Buletin literasi : berisi tentang berita literasi atau artikel literasi dan disertai dengan rekomendasi buku yang terkait. (Shirin)  

Modul Review : Berisi halaman untuk me-review buku yang telah dibaca, dengan pemberian komentar atau ulasan dan juga pemberian rating. Hasil review dapat dilihat oleh pengguna lain saat melihat informasi buku tersebut. (Nano)   

Modul Koleksi Pengguna: Modul yang memungkinkan pengguna berkontribusi dengan menambahkan buku mereka sendiri sebagai koleksi bersama, terdapat fitur untuk menghapus buku yang sudah ditambahkan (Mario)



**Role User**:  
- Admin User (full access)  
- Login User (bisa melakukan input berupa menambahkan/menghapus buku, melakukan review)  
- Anonymous user/tidak login (bisa membaca/mendownload buku, tidak bisa melakukan review maupun menambah/menghapus buku)