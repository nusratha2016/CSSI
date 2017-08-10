def swap(name1, name2):
  empty=name1[0]
  name1[0]=name2[0]
  name2[0]=empty


name1 = ["Reid"]
name2 = ["Zavala"]
swap(name1, name2)
print(name1)
print(name2)
