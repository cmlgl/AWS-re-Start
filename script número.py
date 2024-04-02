numero = 250


while numero <= 251:
    print("Escolha um número entre 1 e 250")
    numero2 = int(input("Verificar números primos: "))
    mult = 0
    
    for count in range(2,numero2):
        if (numero2 % count == 0):
            print("Múltiplo de",count)
            mult += 1

    if(mult==0):
         print("É primo")
         print("Caminho absoluto: /home/ec2-user/environment")
    else:
         print("Tem",mult,"múltiplos acima de 2 e abaixo de",numero2)
         print("Caminho absoluto: /home/ec2-user/environment")