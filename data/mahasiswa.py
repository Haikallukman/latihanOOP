class Mahasiswa:
    def __init__(self, nim, nama, prodi):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Prodi: {self.prodi}"


class DataMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.daftar_mahasiswa = [m for m in self.daftar_mahasiswa if m.nim != nim]

    def ubah_mahasiswa(self, nim, nama=None, prodi=None):
        for m in self.daftar_mahasiswa:
            if m.nim == nim:
                if nama:
                    m.nama = nama
                if prodi:
                    m.prodi = prodi
                break

    def cari_mahasiswa(self, nim):
        for m in self.daftar_mahasiswa:
            if m.nim == nim:
                return m
        return None
