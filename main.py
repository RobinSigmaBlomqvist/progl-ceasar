alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
run = True
while run == True:
    sak = ''
    meddelande = str(input("Vad vill du encrypta?:")).lower()
    nyckel = int(input("Hur stor shiffer?:"))
    for i in meddelande:
        if i in alfabet:
            position = alfabet.index(i)
            nyposition = (position + nyckel) % len(alfabet)
            sak += alfabet[nyposition]
        else:
            sak += i
    print(sak)

hej = [i for i in range(1, 100) if i % 3 == 0 and i % 5 == 0]
print(hej)