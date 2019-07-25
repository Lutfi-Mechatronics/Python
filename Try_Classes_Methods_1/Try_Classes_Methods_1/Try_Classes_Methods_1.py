
from class1 import LocalVariableMatha as lv
from class1 import ObjectMatha as ob
from class1 import GlobalVariableMatha as gv

print("Local Variables : ")
lv.add(10,2)
lv.subtract(9,6)
lv.subtract(a=6,b=9)
lv.devide(100,5)

print("\n Objects : ")
c=ob(25,8)
d=ob(17,9)
c.add()
c.subtract()
c.devide()
d.add()
d.subtract()
d.devide()

print("\n Global Variables : ")
a=gv(25,8)
b=gv(17,9)
a.add()
a.subtract()
a.devide()
b.add()
b.subtract()
b.devide()
