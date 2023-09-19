import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()

window.geometry("800x500")
window.title("BURCUNU ÖĞREN")

label = tk.Label(window, text="SEN HANGİ BURÇSUN?", font="Times 20", fg="black")
label.place(x=300, y=10)

labelgun = tk.Label(window, text="Doğum Gününüz: ", font="Times 14", fg="black")
labelgun.place(x=25, y=50)

labelay = tk.Label(window, text="Doğum Ayınız: ", font="Times 14", fg="black")
labelay.place(x=25, y=80)

entry_gun = tk.Entry(window, width=50)
entry_gun.place(x=160, y=50)

entry_ay = tk.Entry(window, width=50)
entry_ay.insert(string="", index=0)
entry_ay.place(x=160, y=80)

result_label = tk.Label(window, text="", font="Times 14", fg="black")
result_label.place(x=25, y=140)

def buton():
    burclar = {
    "Ocak": {
        "Oğlak": list(range(1, 21)),
        "Kova": list(range(21, 32)) }, 
    "Şubat": { 
        "Kova": list(range(1, 19)),
        "Balık": list(range(21, 30)),},
    "Mart": {
        "Balık": list(range(1, 21)),
        "Koç": list(range(21, 32))}, 
    "Nisan": {
        "Koç": list(range(1, 21)),
        "Boğa": list(range(21, 32))},
    "Mayıs": {
        "Boğa": list(range(1, 21)),
        "İkizler": list(range(21, 32))}, 
    "Haziran": {
        "İkizler": list(range(1, 22)),
        "Yengeç": list(range(21, 32))},
    "Temmuz": {
        "Yengeç": list(range(1, 23)),
        "Aslan": list(range(21, 32))}, 
    "Ağustos": {
        "Aslan": list(range(1, 23)),
        "Başak": list(range(21, 32))},
    "Eylül": {
        "Başak": list(range(1, 23)),
        "Terazi": list(range(21, 32))}, 
    "Ekim": {
        "Terazi": list(range(1, 24)),
        "Akrep": list(range(21, 32))},
    "Kasım": {
        "Akrep": list(range(1, 23)),
        "Yay": list(range(21, 32))}, 
    "Aralık": {
        "Yay": list(range(1, 22)),
        "Oğlak": list(range(21, 32))}                
}

    gun = int(entry_gun.get())
    ay = entry_ay.get().title()

    if ay in burclar:
        cs = burclar[ay]
        for burc, gunler in cs.items():
            if gun in gunler:
                result_label.config(text=f"{gun} günü {ay} ayı {burc} burcudur.")
                break
        else:
            result_label.config(text=f"{ay} ayında {gun}. gün için burç bulunamadı.")
    else:
        result_label.config(text=f"{ay} geçerli bir ay değil.")

labelb = tk.Label(window, text="Burcunuz: ", font="Times 14", fg="black")
labelb.place(x=25, y=110)

burcbuton = tk.Button(window, text="Burç Hesapla", fg="black", command=buton)
burcbuton.place(x=70, y=190)

window.mainloop()

