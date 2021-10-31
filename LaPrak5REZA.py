# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:19:48 2021

@author: RezaKurniawan
"""
print("- - - H I T U N G  G A J I  H A R I A N - - -")

jam_masuk = input("Jam Masuk kerja: ")
jam = int(float(jam_masuk))
if 4 <= jam < 10:
	print("Selamat Pagi")
elif 10 <= jam < 14:
	print("Selamat Siang")
elif 14 <= jam < 18:
	print("Selamat Sore")
elif 18 <= jam <= 24:
	print("Selamat Malam")

jam_keluar = input("\nJam Keluar kerja: ")
jam = int(float(jam_keluar))
if 4 <= jam < 10:
	print("Selamat Pagi")
elif 10 <= jam < 14:
	print("Selamat Siang")
elif 14 <= jam < 18:
	print("Selamat Sore")
elif 18 <= jam <= 24:
	print("Selamat Malam")
	

totalmenit_masuk = (int((jam_masuk).split('.')[0]) * 60) + int((jam_masuk).split('.')[1])
totalmenit_keluar = (int((jam_keluar).split('.')[0]) * 60) + int((jam_keluar).split('.')[1])
waktu = (totalmenit_keluar - totalmenit_masuk) // 60

lembur = int(waktu) - 8
gaji_perhari = 175
gaji_lembur = lembur * 15

total_gaji = gaji_perhari + gaji_lembur
print(f"""\n- - - R I N C I A N  G A J I - - -
Waktu Kerja\t\t: {waktu} jam ( {jam_masuk} sd {jam_keluar} )
Gaji per Hari\t: Rp 175.000
Lembur\t\t\t: Rp {gaji_lembur}.000 ( {lembur} jam x @ Rp 15.000 )
Total Gaji\t\t: Rp {total_gaji}.000""")