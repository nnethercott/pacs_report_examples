import BaseDerived as bd
b = bd.Base(1)
d = bd.Derived(1,2)

print(b.get_id()) #outputs 1
print(d.get_id()) #outputs 2

d.say_hi() #inheritance 
