import git
import os
import shutil
for i in range(1):
	print("Empezando a clonar", i)
	if os.path.exists("/home/ec2-user/prueba/FoodApp"):
		shutil.rmtree('/home/ec2-user/prueba/FoodApp')
		git.Git("/home/ec2-user/prueba").clone("https://stevenbermudez@dev.azure.com/stevenbermudez/FoodApp/_git/FoodApp")
	else:
		git.Git("/home/ec2-user/prueba").clone("https://stevenbermudez@dev.azure.com/stevenbermudez/FoodApp/_git/FoodApp")
print("Finish it")
