import math
a=275.27254151900394
b=202.2102705966607
c=-638.8905239808554
dlt=(b**2)-(4*a*c)
if dlt > 0:
    print("k1= ",((-b-(dlt**0.5))/2*a))
    print("k1= ",((-b+(dlt**0.5))/2*a))
elif dlt ==0:
    print("racine double k = ",-b/2*a)
else :
    print("racines imaginaire")      