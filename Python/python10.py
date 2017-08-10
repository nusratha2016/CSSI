def alternate():
    S= raw_input("please enter a word:")
    n= ""
    for x in range(0,len(S)):
        if x % 2 == 0:
         n=n+S[x].upper()
        else:
         n=n+S[x].lower()
    print(n)


def alternate2():
    S=raw_input("please enter a word:")
    n2=[]
    for x in range(0,len(S),2):
        n2.append(S[x].upper())
        if x+1 < len(S):
             n2.append(S[x+1].lower())

  print("".join(n2))

alternate()
alternate2()
