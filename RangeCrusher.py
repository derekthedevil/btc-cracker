from time import sleep
import bit
import re
import random
print ("Range Crusher V1.0.2")
print ("================")
A=str(input("Target Addr or Pattern: "))
b=int(input("Min Range: "))
c=int(input("Max Range: "))
d=int(input("Magnitude: "))
x=2**b
y=2**c
m0=int((y+x)/2)
m1=int((y+x)/2)
print ("================")
while True:
	   x=x+d
	   y=y-d
	   m0=m0+d
	   m1=m1-d
	   r0=random.randint(x+1,m1-1)
	   r1=random.randint(m0+1,y-1)
	   privx = bit.Key.from_int(x)
	   privy = bit.Key.from_int(y)
	   privm0 = bit.Key.from_int(m0)
	   privm1 = bit.Key.from_int(m1)
	   privr0=bit.Key.from_int(r0)
	   privr1=bit.Key.from_int(r1)
	   addr = str(privx.address+privy.address+privm0.address+privm1.address+privr0.address+privr1.address)
	   if re.search (A,addr):
	       print("")
	       print ("================")
	       print("INT: ",x)
	       print ("(PrivateKey)")
	       print (privx.to_wif())
	       print ("BTC Address: " + privx.address)
	       print ("================")
	       print("INT: ",y)
	       print ("(PrivateKey)")
	       print (privy.to_wif())
	       print ("BTC Address: " + privy.address)
	       print ("================")
	       print("INT: ",m0)
	       print ("(PrivateKey)")
	       print (privm0.to_wif())
	       print ("BTC Address: " + privm0.address)
	       print ("================")
	       print("INT: ",m1)
	       print ("(PrivateKey)")
	       print (privm1.to_wif())
	       print ("BTC Address: " + privm1.address)
	       print ("================")
	       print("INT: ",r0)
	       print ("(PrivateKey)")
	       print (privr0.to_wif())
	       print ("BTC Address: " + privr0.address)
	       print ("================")
	       print("INT: ",r1)
	       print ("(PrivateKey)")
	       print (privr1.to_wif())
	       print ("BTC Address: " + privr1.address)
	       print ("================")
	       break
	   else:
	   	print("x: ",x, " r0: ",r0," m1: ",m1)
	   	print("m0: ",m0, " r1: ",r1," y: ",y)