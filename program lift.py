import tkinter as bk  # fitur tidak akan diupdate lagi

layar = bk.Tk()
layar.geometry("300x400")
layar_2 = bk.Tk()
layar_2.geometry("500x200")
tulisan_ajaib = bk.StringVar()
format_posisi_ajaib = bk.StringVar()
input_lantai = bk.StringVar()
format_posisi_ajaib.set("Anda berada di ")
lantai_berapa = "Lantai Dasar"
tulisan_ajaib.set("Lantai Dasar")
format_lantai = "Sekarang kita berada di lantai "
tulisan_konfirmasi_ajaib = bk.StringVar()
tulisan_konfirmasi_ajaib.set("Anda telah Memencet tombol ini sebanyak 7 kali, apakah anda ingin membuat lantai baru?")
lantai, penanda_batasan = 4, 0
susunan_lantai = ["B3", "B2", "B1", "LG", "G", "UG", "1", "2", "3", "4", "5", "6", "7", "Rooftop"]  # total 14 lantai
# ground di lantai ke 4 pada awalnya


def lokasi_lantai(tempat):
    global lantai_berapa, lantai, penanda_batasan, susunan_lantai
    lokasi = "G"
    ukuran_list = len(susunan_lantai) - 1
    if tempat < 0:
        format_posisi_ajaib.set("Ini adalah lantai terendah!")
        penanda_batasan = penanda_batasan - 1
        tempat, lantai = 0, 0
        lokasi = susunan_lantai[0]
    elif tempat > ukuran_list:
        format_posisi_ajaib.set("Ini adalah lantai tertinggi!")
        penanda_batasan = penanda_batasan + 1
        tempat, lantai = ukuran_list, ukuran_list
        lokasi = susunan_lantai[ukuran_list]
    elif 0 <= tempat <= ukuran_list:
        format_posisi_ajaib.set("Anda berada di")
        penanda_batasan = 0
        lokasi = susunan_lantai[tempat]
    return lokasi


def naik_atau_turun(tujuan):
    global lantai_berapa, lantai

    if tujuan == "NAIK":
        lantai = lantai + 1
    elif tujuan == "TURUN":
        lantai = lantai - 1
    lantai_berapa = "Lantai " + lokasi_lantai(lantai)
    tulisan_ajaib.set(lantai_berapa)

    # utama()


def utama():
    global tulisan_ajaib, penanda_batasan
    tombol_naik = bk.Button(layar_2, text="Naik 1 lantai", command=lambda: naik_atau_turun("NAIK"))
    tombol_turun = bk.Button(layar_2, text="Turun 1 lantai", command=lambda: naik_atau_turun("TURUN"))
    tulisan = bk.Label(layar, textvariable=tulisan_ajaib, bg="#f7ff9c")
    format_posisi = bk.Label(layar, textvariable=format_posisi_ajaib, bg="#cdff6e")

    tombol_naik.grid(row=0, column=0)
    tombol_turun.grid(row=1, column=0)
    format_posisi.pack()
    tulisan.pack()

    layar.mainloop()

    layar_2.mainloop()


utama()

# batas
