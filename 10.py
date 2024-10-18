#Exercicio 01: Verificar se um número é positivo, negativo ou zero

# numero = int(input('Digite um número'))
# print(f'O número digitado é:{numero} ')

# if numero > 0:
#   print(f'Esse número é positivo')

# elif numero == 0:
#     print(f'O número é zero')
# else:
#     print(f'O número é negativo')


# #Exercicio 02: Maioridade

# idade = int(input('Digite a idade :'))
# print(f' A idade é: {idade}')
# if idade >= 18:
#   print(f'Maioridade')
# else:
#   print(f' Menoridade')


  #Exercicio 03 : Número par ou impar 


# num = int(input('Digite um numero:'))
# if num % 2 == 0:
#     print(f'O numero {num} é par')
# else:
#     print(f'O numero {num} é impar')


#Exercicio 04: Número maior 

# numero1 = int(input('Digite um numero:'))
# numero2 = int(input('Digite outro numero:'))
# if numero1 > numero2:
#     print(f'O numero {numero1} é maior que {numero2}')
# else:
#     print(f'O numero {numero2} é maior que {numero1}')



#Exercicio 05:peça o valor da compra se o valor for maior que 100 aplique um desconto de 10% caso contrario exiba valor sem desconto

# compra = float(input('Qual o valor da compra?'))
# if compra > 100:
#     desconto = compra * 0.1
#     total = compra - desconto
# else:
#     total = compra
# print(f'O valor da compra com desconto é R${total:.2f}')



#Exercicio 06:peça ao usuario um numero e verifique se ele é multiplo de 5

# numero = int(input('Digite um numero:'))
# if numero % 5 == 0:
#     print(f'O numero {numero} é multiplo de 5')
# else:
#     print(f'O numero {numero} não é multiplo de 5')


#Exercicio 07: peça 3 notas ao usuario e calcule a media. Se a media for maior ou igual a 7 informe aprovado senao reprovado
 
# nota1 = float(input('Digite a primeira nota:'))
# nota2 = float(input('Digite a segunda nota:'))
# nota3 = float(input('Digite a terceira nota:'))
# media = (nota1 + nota2 + nota3) / 3
# if media >= 7:
#     print(f'Aprovado com media {media:.2f}')
# else:
#     print(f'Reprovado com media {media:.2f}')

#Exercicio 08: Digite a senha

# senha = input('Digite sua senha ')

# if senha == 'python123_EFG':
#    print(f'Acesso Permitido')
# else:
#    print(f'Senha Incorreta')


#Exercicio 09: 

# #Peça ao usuário sua idade e informe se ele tem entrada gratuita (idade menor que 5 anos ou maior que 60)

# idade = int(input("Digite sua idade:"))

# if (idade <= 5) or (idade >= 60):
#     print("Entrada Gratuita")
# else:
#     print("Compre seu ingresso")

#Exercicio 10: Peça uma nota ao usuário entre 0 e 10 se o valor for inválido mostre uma mensagem de erro

# nota = int(input("Digite uma nota entre 0 e 10:"))

# if nota < 0 or nota > 10:
#     print("Nota inválida")
#     nota = int(input("Digite uma nota entre 0 e 10:"))

#Exercicio 11: Peça a idade do usuário e informe se ele é criança (menor de 12 anos) adolescente (entre 12 e 17 anos) adulto (maior de 18)

# idade = int(input("Digite sua idade:")) 

# if (idade < 12):
#     print("Criança")
# elif (idade >= 12) and (idade <= 17):
#     print("Adolescente")
# else:   
#     print("Adulto")

#Exercicio 12:Peça três números ao usuário e informe qual deles é o maior

# num1 = int(input("Digite o primeiro número:"))

# num2 = int(input("Digite o segundo número:"))

# num3 = int(input("Digite o terceiro número:"))

# if (num1 > num2) and (num1 > num3):
#     print(f"{num1} é o maior")
# elif (num2 > num1) and (num2 > num3):
#     print(f"{num2} é o maior")
# else:
#     print(f"{num3} é o maior")

#Exercicio 13: Peça dois números ao usuário e divida o primeiro pelo segundo; se o segundo for zero mostre uma mensagem de erro

# num1 = int(input("Digite o primeiro número:"))

# num2 = int(input("Digite o segundo número:"))

# if num2 == 0:
#     print("Erro!")
# else:
#     divisão = num1 / num2
#     print(f"A divisão entre {num1} e {num2} é:",divisão)

#Exercicio 14: Peça ao usuário um número e verifique se ele está entre 10 e 50

# num = int(input("Digite um número:"))

# if (num >= 10) and (num <= 50):
#     print("Esta entre 10 e 50")
# else:
#     print("Não esta entre 10 e 50")

#Exercicio 15: Peça a média do aluno e informe se ele foi aprovado (média maior ou igual a 7), em recuperação (média maior ou igual a 5 e menor que 7) ou reprovado (média menor que 5)

# media = float(input("Digite a sua média:"))

# if (media >= 7):
#     print("Aprovado")
# elif (media >= 5) and (media < 7):
#     print("Em recuperação")
# else:
#     print("Reprovado")

#Exercicio 16: Peça ao usuário sua massa e altura, calcule o IMC, informe se ele está abaixo do peso(IMC menor que 18,5), no peso ideal(IMC entre 18,5 e 25) ou acima(IMC maior que 25)

# massa = float(input("Digite sua massa:"))

# altura = float(input("Digite sua altura:"))

# indice_massa_corporal = (massa) / ((altura)**2)

# if (indice_massa_corporal < 18.5):
#     print("Abaixo do peso")
# elif (indice_massa_corporal >= 18.5) and (indice_massa_corporal < 25):
#     print("Peso ideal")
# else:
#     print("Acima do peso")   

#Exercicio 17: Peça ao usuário três lados e verifique se eles podem formar um triângulo; se sim, informe qual tipo de triângulo ele é (equilátero, isósceles ou escaleno)

# lado1 = int(input("Digite o valor do primeiro lado:"))

# lado2 = int(input("Digite o valor do segundo lado:"))

# lado3 = int(input("Digite o valor do terceiro lado:"))

# if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
#     if (lado1 == lado2) and (lado2 == lado3):
#         print("Triângulo Equilátero")
#     elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
#         print("Triângulo Escaleno")
#     else:
#         print("Triângulo Isósceles")
# else:
#     print("Nao formam um triângulo")

#Exercicio 18: Peça ao usuário um nome de usuário e senha; verifique se o nome de usuário é admin e a senha é 1234; se sim mostre uma mensagem de Login bem sucedido, caso contrário mostre uma mensagem de acesso negado

# nome = input("Digite seu nome de usuário:")

# senha = int(input("Digite sua senha:"))

# if (nome == "admin") and (senha == 1234):
#     print("Login bem sucedido")
# else:
#     print("Acesso negado")

#Exercicio 19: Peça a idade do usuário e verifque se ele pode dirigir (idade maior ou igual a 18); se tiver menos de 18 anos, informe quantos anos faltam para ele poder dirigir

# idade = int(input("Digite sua idade:"))

# if (idade >= 18):   
#     print("Pode dirigir")
# else:
#     faltam = 18 - idade
#     print(f"Faltam {faltam} anos para ele poder dirigir")



    
    
    