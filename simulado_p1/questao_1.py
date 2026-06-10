x=-2.5
y=7.2
z=-5.1

import math

m= int(z/y) + round(x*y,1) - abs(z) >= math.ceil(z/y) - math.floor(x/2) + abs(x-y)

print (m)