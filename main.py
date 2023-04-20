#algoritmo número primo

i = 2
num = 37

while i < num:
    print(f"{num}%{i}=+{num%i}")
    if num%i==0:
        print(f"{num} não é primo pois {num}%{i}= 0")
        break
    elif i>=num/2:
        print(f"{num} é primo")
    i+=1







