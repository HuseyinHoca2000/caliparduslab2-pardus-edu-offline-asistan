#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus EDU Offline Asistan
ÇalıPardusLab2 / Pardus Hata Yakalama ve Öneri Yarışması 2026
"""

from datetime import datetime


def cevap_uret(soru):
    soru = soru.lower()

    if "merhaba" in soru:
        return "Merhaba, size nasıl yardımcı olabilirim?"

    elif "saat" in soru:
        return f"Şu an saat: {datetime.now().strftime('%H:%M:%S')}"

    elif "python" in soru:
        return "Python için terminalde: sudo apt install python3"

    elif "libreoffice" in soru:
        return "Uygulama menüsünden LibreOffice'i açabilirsiniz."

    elif "ayarlar" in soru:
        return "Ayarlar menüsü sistem yapılandırması için kullanılabilir."

    elif "çıkış" in soru:
        return "Görüşmek üzere!"

    else:
        return "Bu konuda henüz eğitimim yok, ama öğrenebilirim."


def main():
    print("=" * 60)
    print("PARDUS EDU OFFLINE ASISTAN")
    print("=" * 60)
    print("Çıkmak için 'çıkış' yazın.\n")

    while True:
        soru = input("Siz: ")

        cevap = cevap_uret(soru)
        print("Asistan:", cevap)

        if "çıkış" in soru.lower():
            break


if __name__ == "__main__":
    main() 
