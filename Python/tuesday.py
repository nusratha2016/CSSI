letters = ('A1 A2 A3 A4 A5 A6 A7 A8 ')
print(letters)
letters = ('B1 B2 B3 B4 B5 B6 B7 B8 ')
print(letters)
letters = ('C1 C2 C3 C4 C5 C6 C7 C8 ')
print(letters)
letters = ('D1 D2 D3 D4 D5 D6 D7 D8 ')
print(letters)
letters = ('E1 E2 E3 E4 E5 E6 E7 E8 ')
print(letters)
letters = ('F1 F2 F3 F4 F5 F6 F7 F8 ')
print(letters)
letters = ('G1 G2 G3 G4 G5 G6 G7 G8 ')
print(letters)
letters = ('H1 H2 H3 H4 H5 H6 H7 H8 ')
print(letters)

info = ""
info = ("#" * 27)+ '\n'
for j in range(8):
  info = info + '# '
  for i in range(1,9):
    info = info + chr(65 + j) + str(i)
    if i!= 8:
      info = info + ' '
  info = info + ' #\n'
info = info + ("#" * 27)
print(info)
