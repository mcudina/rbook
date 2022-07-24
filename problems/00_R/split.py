import re
import os

with open("aux.txt", 'r') as file:
    tex = file.read()

divs = re.split("(</*div[^>]*>)",tex)

for i in range(10):
    prb = divs[8*i+1]+divs[8*i+2]+divs[8*i+3]+divs[5*8+4]
    sol = divs[8*i+5]+divs[8*i+6]+divs[8*i+7]+divs[5*8+8]
    with open("Sim-"+str(i)+".prb","w") as file:
        file.write(prb)
    with open("Sim-"+str(i)+".sol","w") as file:
        file.write(sol)

