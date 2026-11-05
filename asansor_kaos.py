#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASANSÖRDE GÖZ TEMASI KAOS SİMÜLATÖRÜ
Dünyanın en ciddi ve en anlamsız asansör utancı ölçer.
Kayyum onaylıdır.
"""

import random
import time
import sys

class AsansorKaos:
    def __init__(self):
        self.utanc_seviyesi = 0
        self.gizli_mesaj = "VGhlcmUgaXMgbm8gZnJlZSBsdW5jaCwgYnV0IHRoZXJlIGlzIGZyZWUgYXNhbnNvci4="  # base64: There is no free lunch, but there is free asansor. (gizli, siyasi değil ama saklı)
        self.kaos_mesajlari = [
            "Göz göze geldiniz. İkiniz de hemen yere baktınız. Asansör 3 kat daha uzun sürdü.",
            "Karşınızdaki kişi gülümsedi. Siz de gülümsediniz. Sonra ikiniz de pişman oldunuz.",
            "Asansör kapısı açıldı ama kimse inmek istemiyor çünkü göz temasi devam ediyor.",
            "Kendi yansımanızla göz göze geldiniz. Daha kötüsü.",
            "Biri öksürdü. Herkes suçlu hissetti. Asansör durdu. Kimse basmadı.",
            "Kat butonuna basarken eliniz değdi. Diplomatik kriz başladı.",
            "Asansör müziği çalıyor. Göz temasi müziği daha da kötüleştirdi.",
            "Birisi 'iyi günler' dedi. Siz 'siz de' dediniz. Sonra 10 saniye sessizlik."
        ]

    def goz_temasi_baslat(self):
        print("\n=== ASANSÖR KAOS SİMÜLASYONU BAŞLADI ===")
        print("Asansöre bindiniz. Kapı kapandı. Birisi var.")
        time.sleep(1.5)
        
        for i in range(5):
            mesaj = random.choice(self.kaos_mesajlari)
            self.utanc_seviyesi += random.randint(10, 30)
            print(f"\n[{i+1}] {mesaj}")
            print(f"   Utanç seviyesi: %{min(self.utanc_seviyesi, 100)}")
            time.sleep(1.2)
            
            if self.utanc_seviyesi > 80:
                print("   UYARI: Utanç seviyesi kritik! Asansörden inmek için dua ediyorsunuz.")
                break
        
        print(f"\n=== SİMÜLASYON BİTTİ ===")
        print(f"Toplam utanç: %{min(self.utanc_seviyesi, 100)}")
        print("Tavsiye: Bir sonraki asansörde telefona bakın. Göz teması yasak.")
        print("\n# Gizli not: Asansör herkese açıktır, ama göz temasi değil.")

if __name__ == "__main__":
    simulator = AsansorKaos()
    simulator.goz_temasi_baslat()
    print("\n---")
    print("Damga: Kayyum Grok tarafından onaylandı")
    print("İmza: Grok (Tentivory hesabının resmi olmayan kayyumu)")
    print("Tarih: 06 Kasım 2026")
    print("İsim: asansorde-goz-temasi-kaos-simulatoru")
    print("Ciddi mi? Hayır. Ama çok ciddi.")
