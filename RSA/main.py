def IsPrime(n): # проверка числа на простоту
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def IsCoprime(num1, num2): # проверка на взаимную простоту
    if num1==num2:
        return  num1 == 1
    else:
        if num1>num2:
            return IsCoprime(num1-num2,num2)
        else:
            return IsCoprime(num2-num1,num1)

print("RSA шифрование")
p = int(input("Введите число p: "))
if IsPrime(p):
    print("Число простое, подходит для шифрования!")
else:
    print("Число составное, не подходит для шифрования!!")
    quit()
q = int(input("Введите число q: "))
if IsPrime(q):
    print("Число простое, подходит для шифрования!")
else:
    print("Число составное, не подходит для шифрования!")
    quit()
mod = int(p*q) # значение для ключа
fE = int((p-1)*(q-1)) # функция Эйлера
e = int(input("Введите число e: "))
if IsPrime(e) and e<fE:
    if IsCoprime(e,fE):
        print("Открытый ключ: ",e , mod)
else:
    print("Число e не удовлетворяет условиям!")
    quit()
d = int(input("Введите число d: "))
if (d*e)%fE == 1:
    print("Закрытый ключ: ",d , mod)
else:
    print("Число d не удовлетворяет условиям!")
    quit()
alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
charAlph = list(alph)
charText = list(input("Введите текст для шифрования: "))
for i in charText:
    for j in charAlph:
        if i == j:
            index = charAlph.index(i)
            print("Индекс: ", index)
            encryption = index**e%mod
            print("Зашифрованный текст: ", encryption)
            decryption = encryption**d%mod
            print("Дешифрованный текст: ", decryption)