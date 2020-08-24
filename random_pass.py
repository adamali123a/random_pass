import random
import os
os.system("clear")
j = r"""
 __  __
|  \/  | ___  ___  ___ _____      __
| |\/| |/ _ \/ __|/ __/ _ \ \ /\ / /
| |  | | (_) \__ \ (_| (_) \ V  V /
|_|  |_|\___/|___/\___\___/ \_/\_/
"""
print("\033[0;31m",j)
print("Tool by Moscow\n")

print("\n\nzhmara 99 banwsa bo darchon\n\n")

a = "asdfghjklmnbvcxzqwertyuiop"

b = "ASDFGHJKLZXCVBNMQWERTYUIOP"

c = "0123456789"

qp = "!@#$%^&*()_+=/"

g = a + b + c + qp

h = g + a + b + qp + c

moscow = h + g + c + qp + b + a

for d in moscow:
    try:
        
        t = int(input("Lyera reazhy passwordkan daxl bka ==>  "))
        if (t == 99):
            break
        
        e = "".join(random.choices(moscow , k=t))
        print("\n\n","passwordkt ==> ",e,"\n\n")
        
    except:
        print("Aw shta bony nya")
        pass
