# -*- coding: utf-8 -*-
"""Tugas Day 4 - Hands on Programming in Python (Kel 3).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eb8A-_Rhc2FYrTZOQAbWmt0cUpye6L1U

# Membuat Parent Class dan Child Class

Membuat parent class
"""


class BangunDatar:
    def luas_bgndatar():  # untuk menghitung luas
        pass


"""Membuat child class"""


class Persegi(BangunDatar):
    def luas_bgndatar(self, sisi):
        self.luas = sisi**2
        return self.luas


class PersegiPanjang(BangunDatar):
    def luas_bgndatar(self, panjang, lebar):
        self.luas = panjang * lebar
        return self.luas


class Segitiga(BangunDatar):
    def luas_bgndatar(self, alas, tinggi):
        self.luas = 0.5 * alas * tinggi
        return self.luas


class Lingkaran(BangunDatar):
    def luas_bgndatar(self, jari):
        self.luas = 3.14 * jari**2
        return self.luas


class Trapesium(BangunDatar):
    def luas_bgndatar(self, sisi1, sisi2, tinggi):
        self.luas = 0.5 * sisi1 * sisi2 * tinggi
        return self.luas


"""# Menghitung luas masing - masing bangun datar


"""

persegi1 = Persegi()
persegi1.luas_bgndatar(10)

persegi_panjang1 = PersegiPanjang()
persegi_panjang1.luas_bgndatar(10, 20)

segitiga1 = Segitiga()
segitiga1.luas_bgndatar(10, 25)

lingkaran1 = Lingkaran()
lingkaran1.luas_bgndatar(10)

trapesium1 = Trapesium()
trapesium1.luas_bgndatar(10, 12, 8)

"""# Mengurutkan luas bangun datar

Mengurutkan luas bangun datar menggunakan method sort
"""

bangun_datar = [
    persegi1.luas,
    persegi_panjang1.luas,
    segitiga1.luas,
    lingkaran1.luas,
    trapesium1.luas,
]
print(bangun_datar)

bangun_datar.sort()
print(bangun_datar)

"""# Menjumlah semua luas bangun datar"""

total_luas = sum(bangun_datar)
print(total_luas)
