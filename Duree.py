import os

class Duree:

	def __init__(self,h,m,s):
		self.h=h
		self.m=m
		self.s=s

	def affiche_duree(self):
		print("la durée est de",self.h,"heures",self.m,"minutes et",self.s,"secondes")	


duree1 = Duree(11,12,3)
duree1.affiche_duree()



os.system("pause")