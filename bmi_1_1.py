# Import modul yang diperlukan. Untuk menggunakan library python PyWebIO kita harus mengimpor
# beberapa modul penting dari library ini
from wsgiref import validate
from pywebio.input import *
from pywebio.output import *



"""Buat class "calculation" dan di mana didalamnya kita membuat atau mendefinisikan fungsi/method
   baru bernama "kalkulatorBMI" untuk mengklasifikasikan kondisi seseorang berdasarkan BMI nya
   yang diteruskan sebagai parameter
"""
# membuat input entry
def check_age(p): #fungsi untuk memastikan user tidak memasukan nilai negatif pada entry usia
    if p < 1:
        return 'Harap masukan nilai yang sesuai, tidak boleh negatif!!!'
usia = input("Usia anda: ", type=NUMBER, validate=check_age)
Gender = radio("Gender anda: ", options=['Pria', 'Wanita']) #fungsi radio = fungsi input pilihan dan hanya bisa pilih salah satu
Tinggi = float(input("Tinggi badan anda (dalam Meter, INGAT DALAM SATUAN METER!!)"))
Massa = float(input("Massa badan anda (dalam Kilogram)"))

# membuat class 
class calculation:

	# mendefinisikan fungsi baru
	def kalkulatorBMI(self, Tinggi, Massa):
		
		# menghitung BMI (Body Mass Index)
		BMI = (Massa)/(Tinggi*Tinggi)
		
		# klasifikasi
		for y1, y2 in [(16, 'Anda termasuk ke dalam kategori SANGAT KURUS, kami sarankan anda menaikan berat badan anda'),
					(18.5, 'Anda termasuk ke dalam kategoi KEKURANGAN BERAT BADAN'),
					(25, 'Anda termasuk ke dalam kategori NORMAL'), (30, 'Anda termasuk ke dalam kategori KELEBIHAN BERAT BADAN'),
					(35, 'Anda termasuk ke dalam kategori OBESITAS'),
					(float('inf'), 'OBESITAS PARAH, KAMI SARANKAN ANDA DIET SEKARANG JUGA!')]:
		
			if BMI <= y1:
				put_text('Body Mass Index Anda adalah: ', BMI), put_text(y2).style('color: red; font-size: 15px; font-weight: bold;') #membuat output text yang dihiasi oleh css
				put_table([                         #membuat output tabel kategori
    			    ['BMI', 'Kategori'],
    			    ['<= 16', 'sangat kurus'],
    			    ['<= 18.5', 'kekurangan berat badan'],
					['<= 25', 'normal'],
					['<= 30', 'kelebihan berat badan'],
					['<= 35', 'obesitas'],
					['> 35++', 'obesitas parah'],
                ])
				break


# memasukan class calculation ke dalam variable bernama obj lalu melalui variable tersebut
# lakukan pemanggilan fungsi kalkulatorBMI beserta dengan parameter nya
obj = calculation()
obj.kalkulatorBMI(Tinggi, Massa)
