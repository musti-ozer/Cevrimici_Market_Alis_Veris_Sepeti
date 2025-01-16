# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:13:39 2025

@author: pc
"""

import os

# Market sınıfı
class Market:
    def __init__(self, file_name="product.txt"):
        """Yapıcı metot: Dosya kontrolü yapar ve ürünü yükler."""
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()  # Dosya yoksa oluşturuyoruz

    def __del__(self):
        """Yıkıcı metot: Dosya kapatılır."""
        print(f"{self.file_name} dosyası kapatıldı.")
        
    def list_product(self):
        """Tüm ürünleri listele."""
        with open(self.file_name, 'r') as file:
            lines = file.read().splitlines()  # Dosya içeriğini satırlara ayırıyoruz

            if not lines:
                print("Dosya boş.")
                return

            print("Ürünler Listesi:")
            for index, line in enumerate(lines, start=1):
                urun_bilgileri = line.strip().split(',')
                if len(urun_bilgileri) == 4:
                    print(f"{index}. {urun_bilgileri[0]}, {urun_bilgileri[1]}, {urun_bilgileri[2]} TL, Stok: {urun_bilgileri[3]}")

    def add_product(self):
        """Yeni bir ürün ekler."""
        ad = input("Ürün Adı: ")
        kategori = input("Kategori: ")
        fiyat = input("Fiyat: ")
        stok = input("Stok Miktarı: ")

        yeni_urun = f"{ad},{kategori},{fiyat},{stok}\n"

        with open(self.file_name, 'a') as file:
            file.write(yeni_urun)
        print(f"{ad} adlı ürün başarıyla eklendi.")

    def delete_product(self):
        """Ürün silme işlemi."""
        self.list_product()

        silinecek_urun = input("Silmek istediğiniz ürünün adını veya numarasını girin: ")

        with open(self.file_name, 'r') as file:
            lines = file.readlines()

        urunler = []
        for line in lines:
            urun_bilgileri = line.strip().split(',')
            if len(urun_bilgileri) == 4:
                urunler.append(urun_bilgileri)

        silinen_urun = None
        if silinecek_urun.isdigit():
            index = int(silinecek_urun) - 1
            if 0 <= index < len(urunler):
                silinen_urun = urunler.pop(index)
        else:
            for urun in urunler:
                if urun[0].lower() == silinecek_urun.lower():
                    silinen_urun = urun
                    urunler.remove(urun)
                    break

        if silinen_urun:
            print(f"{silinen_urun[0]} adlı ürün başarıyla silindi.")
            with open(self.file_name, 'w') as file:
                for urun in urunler:
                    file.write(','.join(urun) + '\n')
        else:
            print("Silmek istediğiniz ürün bulunamadı.")

# Menü ve etkileşim
def menu():
    market = Market()  # Market nesnesi oluşturuluyor
    
    while True:
        print("\nÇevrimiçi Market Menü")
        print("1. Ürünleri Listele")
        print("2. Ürün Ekle")
        print("3. Ürün Sil")
        print("4. Çıkış")
        
        secim = input("Seçiminizi yapın: ")
        
        if secim == "1":
            market.list_product()  # Ürünleri listele
        elif secim == "2":
            market.add_product()  # Ürün ekle
        elif secim == "3":
            market.delete_product()  # Ürün sil
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break  # Programdan çık
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Menü fonksiyonu çağrılır
menu()
