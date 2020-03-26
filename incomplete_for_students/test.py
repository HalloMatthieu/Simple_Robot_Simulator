import model
import constants
import math

m = model.Model()
m.m1.speed = 10
m.m2.speed = 10
print("Premier model : {}".format(m))

linear_speed, rotation_speed = m.dk()
print("Model : {}".format(m))
if linear_speed == 10 and rotation_speed == 0:
    print("Test1 OK")
else:
    print("Test1 FAILED")

m.m1.speed = 10
m.m2.speed = 0
linear_speed, rotation_speed = m.dk(m1_speed=None, m2_speed=None)
print("Model : {}".format(m))
if linear_speed == 5 and rotation_speed == (10 / 0.120):
    print("Test2 OK")
else:
    print("Test2 FAILED")

m.m1.speed, m.m2.speed = m.ik(10, 0)
print("Model : {}".format(m))
if m.m1.speed == 10 and m.m2.speed == 10:
    print("Test3 OK")
else:
    print("Test3 Failed")

m.m1.speed, m.m2.speed = m.ik(10, 10)
print("Model : {}".format(m))
if m.m1.speed == 9.4 and m.m2.speed == 10.6:
    print("Test4 OK")
else:
    print("Test4 Failed")

m.m1.speed = m.m2.speed = 10
test_update = m.update(1)
print("Test5 : {}".format(test_update))
