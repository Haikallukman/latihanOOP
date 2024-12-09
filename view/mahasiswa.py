class MahasiswaView:
    @staticmethod
    def tampilkan_list(mahasiswa_list):
        print("\nDaftar Mahasiswa:")
        for m in mahasiswa_list:
            print(m)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("\nDetail Mahasiswa:")
            print(mahasiswa)
        else:
            print("\nMahasiswa tidak ditemukan.")
