import git
import os
from git import Repo

for i in range(1000):
	print(str(i) + " st push")
	complete = os.path.join("/home/ec2-user/prueba/FoodApp","prueba.txt")
	file1 = open(complete, "w")
	file1.write("File information \n White Palmsssssssssss at the time: " + str(i))
	file1.close()
	repo = Repo("/home/ec2-user/prueba/FoodApp")
	repo.git.add(update=True)
	repo.index.commit("This is the " + str(i) + " commit test")
	origin = repo.remote(name='origin')
	origin.push()
print("Done")


