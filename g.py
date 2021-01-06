import os
import time
import glob

def yapımcı():
	return "kerem ata"
def alfabe():
	return "abcçdefgğhııjklmnoöprsştuüvyz"
class ekran:
		versiyon = "pre 3"
		
		def ver(self):
			return ekran.versiyon
		def yardım(self):
			return "ekran.sil() ekranını temizleme komutu"
			return "ekran.hat() ekran hatlarını yazar"
			return "ekran.sor sistem sorusu sormaya yarar"
			return "ekran.bas son soru değerini belirtir"
			return "yapımcı yapımcıyı yazar"
			return "ekran.versyon versiyonu yazar"
		
			
		def sor(self,x):
 			y=input(x)
 			return y
		soru=input("?")
		
		def bas(self):
			return("değer="+soru+" ")

     
class dos:
	def yarat(self):
		dos=input("dosya adı:")
		open(dos,"w")


 
 #tanımlama#
ekran = ekran()
dos = dos()
