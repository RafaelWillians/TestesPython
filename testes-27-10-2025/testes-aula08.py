def soma(a,b):
    resultado = a+b
    return resultado

def subtracao(a,b):
    resultado = a-b
    return resultado

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
calcular_subtracao = subtracao(valor1, valor2)

print(f"SUBTRAÇÃO = {calcular_subtracao}")