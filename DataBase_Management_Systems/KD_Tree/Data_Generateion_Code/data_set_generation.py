import random					
import re	
d = int(input("Enter the dimension: "))
n = int(input("Enter no. of points: "))
temp11=str(d)+".txt"
f = open(temp11,'w+')
f.write(str(d)+" "+str(n)+"\n")																	#DO ENTRY IN ROW WISE
for i in range(0,n):
        for j in range(0,d-1):
                f.write(str(random.uniform(0, 1))+" ")
        f.write(str(random.uniform(0, 1))+"\n")        
f.close()        
