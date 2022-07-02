import pywhatkit

with open("ornek.txt", "r", encoding="utf-8") as elyazi:  #txt dosyasına kendi dosyanızın adını girin.
    el_yazisi = elyazi.read()

print("İşlem Başlatıldı...")

pywhatkit.text_to_handwriting(el_yazisi, "elyazisi.png")

print("İşlem tamamlandı")