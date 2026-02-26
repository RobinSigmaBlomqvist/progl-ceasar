alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
krypterat = str(input("Vad vill du decrypta?:")).lower()
for nyckel in range(0, len(alfabet)):
    dekrypterat = ""
    for i in krypterat:
        if i in alfabet:
            dekrypterat += alfabet[alfabet.index(i) - nyckel % 29]
        else:
            dekrypterat += i
    print(dekrypterat)
