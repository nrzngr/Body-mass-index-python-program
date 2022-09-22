# Import modul yang diperlukan. Untuk menggunakan library python PyWebIO kita harus mengimpor
# beberapa modul penting dari library ini
from pywebio.input import *
from pywebio.output import *
from pyflowchart import *

"""Buat class "calculation" dan di mana didalamnya kita membuat atau mendefinisikan fungsi
   baru bernama "kalkulatorBMI" untuk mengklasifikasikan kondisi seseorang berdasarkan BMI nya
   yang diteruskan sebagai parameter
"""
# membuat class 
class calculation:

	# mendefinisikan fungsi baru
	def kalkulatorBMI(self, Tinggi, Massa):
		
		# menghitung BMI (Body Mass Index)
		BMI = (Massa)/(Tinggi*Tinggi)
		
		# klasifikasi
		for y1, y2 in [(16, 'sangat kurus'),
					(18.5, 'kekurangan berat badan'),
					(25, 'normal'), (30, 'kegemukan'),
					(35, 'obesitas sedang'),
					(float('inf'), 'OBESITAS PARAH, KAMI SARANKAN ANDA DIET SEKARANG JUGA!')]:
		
			if BMI <= y1:
				put_text('Body Mass Index Anda adalah: ', BMI, 'dan Anda termasuk ke kategori :', y2)
				break

# membuat input entry
Tinggi = float(input("Tinggi badan anda (dalam Meter)"))
Massa = float(input("Massa badan anda (dalam Kilogram)"))

# memasukan class calculation ke dalam variable bernama obj lalu melalui variable tersebut
# lakukan pemanggilan fungsi kalkulatorBMI beserta dengan parameter nya
obj = calculation()
obj.kalkulatorBMI(Tinggi, Massa)