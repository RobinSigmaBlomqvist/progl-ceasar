alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
run = True
while run == True:
    sak = ''
    meddelande = str(input("Vad vill du encrypta?:"))
    nyckel = int(input("Hur stor shiffer?:"))
    for i in meddelande:
        if i in alfabet:
            position = alfabet.index(i)
            nyposition = (position + nyckel) % len(alfabet)
            sak += alfabet[nyposition]
        else:
            print("kys")
            sak += i
    print(sak)