# programmer : AmirHossein Naei
# website : amirhn.ir

import random
shomare = 0
while(1):
	print("emtiyaz : " +str(shomare))
	entekhab = input("1- sang \n2- kaghaz \n3- gheychi \n")
	entekhab = int(entekhab)
	if entekhab == 0 : 
		break
	if (entekhab != 1) and (entekhab != 2) and (entekhab != 3):
		print("خودت فهمیدی چی گفتی؟")
		break
	entekhabesystem = random.randint(1,3)
	entekhabesystemstring = ""
	if entekhabesystem == 1 : entekhabesystemstring = "سنگ"
	elif entekhabesystem == 2 : entekhabesystemstring = "کاغذ"
	elif entekhabesystem == 3 : entekhabesystemstring = "قیچی"
	print("entekhabe system : "+entekhabesystemstring)
	if(entekhabesystem == 1 and entekhab == 2) or (entekhabesystem == 2 and entekhab == 3) or (entekhabesystem == 3 and entekhab == 1):
		print("مساوی شدید !!!")
		shomare+=1
	elif entekhabesystem == entekhab :
		print("مساوی شدید !!")
	else :
		print("باختی !!!")
		shomare-=1
	print("\n\n")