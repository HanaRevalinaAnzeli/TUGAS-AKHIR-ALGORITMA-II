import os
import json

FILE_DATA = "data_mahasiswa.json"
daftar_mahasiswa = []


def muat_data():
    global daftar_mahasiswa
    if os.path.exists(FILE_DATA):
        file = open(FILE_DATA, "r")
        daftar_mahasiswa = json.load(file)
        file.close()


def simpan_data():
    file = open(FILE_DATA, "w")
    json.dump(daftar_mahasiswa, file, indent=4)
    file.close()

def cek_huruf(teks):
    return teks.replace(" ", "").isalpha()

def cetak_tabel(sumber_data):
    print("┌" + "─"*16 + "┬" + "─"*62 + "┬" + "─"*24 + "┐")
    print(f"│ {'NIM':^14} │ {'NAMA MAHASISWA':^60} │ {'PROGRAM STUDI':^22} │")
    print("├" + "─"*16 + "┼" + "─"*62 + "┼" + "─"*24 + "┤")
    
    if len(sumber_data) == 0:
        print(f"│ {'(Belum ada data mahasiswa)':^102} │")
    else:
        for mhs in sumber_data:
            print(f"│ {mhs['nim']:^14} │ {mhs['nama']:^60} │ {mhs['jurusan']:^22} │")        
    print("└" + "─"*16 + "┴" + "─"*62 + "┴" + "─"*24 + "┘")

def menu_tambah():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================================================================")
    print(f"{'TAMBAH DATA MAHASISWA':^106}")
    print("======================================================================================================")
    
    # Input NIM 12 Digit Angka
    while True:
        nim = input("Masukkan NIM (12 digit angka): ").strip()
        if not nim.isdigit():
            print("ERROR: NIM harus berupa angka!\n")
        elif len(nim) != 12:
            print(f"ERROR: NIM harus 12 digit! (Input Anda: {len(nim)} digit)\n")
        else:
            # Cek apakah NIM sudah ada
            sudah_ada = False
            for mhs in daftar_mahasiswa:
                if mhs["nim"] == nim:
                    sudah_ada = True
            
            if sudah_ada:
                print("ERROR: NIM sudah terdaftar!\n")
            else:
                break
                
    # Input Nama 
    while True:
        nama = input("Masukkan Nama Lengkap: ").strip()
        if not cek_huruf(nama):
            print("ERROR: Nama hanya boleh huruf dan spasi!\n")
        else:
            break
            
    # Input Prodi 
    while True:
        prodi = input("Masukkan Program Studi: ").strip()
        if not cek_huruf(prodi):
            print("ERROR: Prodi hanya boleh huruf dan spasi!\n")
        else:
            break
            
    mahasiswa_baru = {"nim": nim, "nama": nama, "jurusan": prodi}
    daftar_mahasiswa.append(mahasiswa_baru)
    simpan_data()
    input("\n[Sukses] Data berhasil ditambah! Tekan Enter...")


def menu_edit():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================================================================")
    print(f"{'EDIT DATA MAHASISWA':^106}")
    print("======================================================================================================")
    cetak_tabel(daftar_mahasiswa)
    
    target = input("\nMasukkan NIM mahasiswa yang mau diedit: ").strip()
    ketemu = False
    
    for mhs in daftar_mahasiswa:
        if mhs["nim"] == target:
            ketemu = True
            print(f"\nData lama -> Nama: {mhs['nama']} | Prodi: {mhs['jurusan']}")
            
            nama_baru = input("Nama baru (Kosongkan jika tidak diubah): ").strip()
            if nama_baru and cek_huruf(nama_baru):
                mhs["nama"] = nama_baru
                
            prodi_baru = input("Prodi baru (Kosongkan jika tidak diubah): ").strip()
            if prodi_baru and cek_huruf(prodi_baru):
                mhs["jurusan"] = prodi_baru
                
            simpan_data()
            input("\n[Sukses] Data berhasil diperbarui! Tekan Enter...")
            break
            
    if not ketemu:
        input("\n[Gagal] NIM tidak ditemukan! Tekan Enter...")


def menu_hapus():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================================================================")
    print(f"{'HAPUS DATA MAHASISWA':^106}")
    print("======================================================================================================")
    cetak_tabel(daftar_mahasiswa)
    
    target = input("\nMasukkan NIM mahasiswa yang mau dihapus: ").strip()
    ketemu = False
    
    for i in range(len(daftar_mahasiswa)):
        if daftar_mahasiswa[i]["nim"] == target:
            ketemu = True
            yakin = input(f"Yakin hapus {daftar_mahasiswa[i]['nama']}? (y/n): ").lower()
            if yakin == "y":
                daftar_mahasiswa.pop(i)
                simpan_data()
                input("\n[Sukses] Data berhasil dihapus! Tekan Enter...")
            break
            
    if not ketemu:
        input("\n[Gagal] NIM tidak ditemukan! Tekan Enter...")


def menu_sorting():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================================================================")
    print(f"{'MENU PENGURUTAN (SORTING)':^106}")
    print("======================================================================================================")
    print("1. Urutkan berdasarkan NIM")
    print("2. Urutkan berdasarkan Nama")
    kunci = input("Pilih (1-2): ")
    
    print("\nMetode:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    metode = input("Pilih (1-2): ")
    
    n = len(daftar_mahasiswa)
    
    # Bubble Sort
    if metode == "1":
        for i in range(n):
            for j in range(0, n - i - 1):
                val1 = daftar_mahasiswa[j]["nim"] if kunci == "1" else daftar_mahasiswa[j]["nama"].lower()
                val2 = daftar_mahasiswa[j+1]["nim"] if kunci == "1" else daftar_mahasiswa[j+1]["nama"].lower()
                if val1 > val2:
                    daftar_mahasiswa[j], daftar_mahasiswa[j+1] = daftar_mahasiswa[j+1], daftar_mahasiswa[j]
                    
    # Selection sort
    elif metode == "2":
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                val1 = daftar_mahasiswa[j]["nim"] if kunci == "1" else daftar_mahasiswa[j]["nama"].lower()
                val2 = daftar_mahasiswa[min_idx]["nim"] if kunci == "1" else daftar_mahasiswa[min_idx]["nama"].lower()
                if val1 < val2:
                    min_idx = j
            daftar_mahasiswa[i], daftar_mahasiswa[min_idx] = daftar_mahasiswa[min_idx], daftar_mahasiswa[i]

    simpan_data()
    input("\n[Sukses] Data berhasil diurutkan! Tekan Enter...")


def menu_searching():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================================================================")
    print(f"{'MENU PENCARIAN (SEARCHING)':^106}")
    print("======================================================================================================")
    print("1. Sequential Search (Bisa cari potongan nama/NIM)")
    print("2. Binary Search (Harus NIM lengkap/pas)")
    metode = input("Pilih (1-2): ")
    
    kata_kunci = input("\nMasukkan kata kunci pencarian: ").strip().lower()
    hasil = []
    
    # 1. Sequential Search
    if metode == "1":
        for mhs in daftar_mahasiswa:
            if kata_kunci in mhs["nim"] or kata_kunci in mhs["nama"].lower():
                hasil.append(mhs)
                
    # 2. Binary Search
    elif metode == "2":
        daftar_mahasiswa.sort(key=lambda x: x["nim"])
        
        low = 0
        high = len(daftar_mahasiswa) - 1
        while low <= high:
            mid = (low + high) // 2
            if daftar_mahasiswa[mid]["nim"] == kata_kunci:
                hasil.append(daftar_mahasiswa[mid])
                break
            elif daftar_mahasiswa[mid]["nim"] < kata_kunci:
                low = mid + 1
            else:
                high = mid - 1
                
    print(f"\n[Hasil Pencarian untuk: '{kata_kunci}']")
    cetak_tabel(hasil)
    input("Tekan Enter untuk kembali ke Menu Utama...")


muat_data()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================================================================")
    print(f"{'SISTEM DATABASE MAHASISWA':^106}")
    print("======================================================================================================")
    cetak_tabel(daftar_mahasiswa)
    
    print(f" Total Data: {len(daftar_mahasiswa)} Mahasiswa")
    print("-" * 102)
    print(" [1] Tambah Data     [3] Hapus Data     [5] Cari Data")
    print(" [2] Edit Data       [4] Urutkan Data   [6] Keluar")
    print("-" * 102)
    
    pilihan = input("Pilih Menu (1-6): ").strip()
    
    if pilihan == "1": menu_tambah()
    elif pilihan == "2": menu_edit()
    elif pilihan == "3": menu_hapus()
    elif pilihan == "4": menu_sorting()
    elif pilihan == "5": menu_searching()
    elif pilihan == "6":
        print("\nProgram ditutup. Terima kasih!")
        break
    else:
        input("\nPilihan salah! Tekan Enter...")