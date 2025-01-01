print("Bem vindo ao programa de validação de triângulo! veja se os três números podem formar um triângulo.")
lado_1 =input("Por favor,insira o primeiro lado do triângulo:\n")
lado_1 = int(lado_1)
lado_2 = input("Insira o segundo lado do triângulo:\n")
lado_2 = int (lado_2)
lado_3 = input ("Agora,insira o terceiro lado do triângulo:\n")
lado_3 = int (lado_3)
if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1) :
        print("os três lados são possíveis formar 1 triângulo!")
else :
        print("não é possível formar um triângulo,pois os dois lados são sempre menores que o terceiro")
    