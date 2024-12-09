from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, prodi = InputForm.input_data()
            data_mahasiswa.tambah_mahasiswa(Mahasiswa(nim, nama, prodi))
        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
            prodi = input("Masukkan Prodi baru (kosongkan jika tidak diubah): ")
            data_mahasiswa.ubah_mahasiswa(nim, nama, prodi)
        elif pilihan == "4":
            nim = input("Masukkan NIM: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            MahasiswaView.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            MahasiswaView.tampilkan_list(data_mahasiswa.daftar_mahasiswa)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
