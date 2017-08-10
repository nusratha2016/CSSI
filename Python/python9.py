names = "NUSRATH"
name = "uSrAtH"
for letter in names:
    print (letter + name)
range (0,len(name),2)


names = "NUSRATH"
name = names.lower()
print(names)
print(name)
solution=""
for x in range(0,len(name)):
  if x % 2 == 1:
    solution =solution+name[x]
  else:
    solution=solution+name[x].upper()
print(solution)
