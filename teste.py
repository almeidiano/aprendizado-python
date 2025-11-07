# operação de adição

# 1. pega no minimo 2 ou mais numeros 
# 2. faz o calculo
# 3. mostra

# int
def adicao(x, y):
    z = x + y
    return z

def subtracao(x, y):
    z = x - y
    return z

def multiplicaçao(x, y):
    z = x * y
    return z

def divisao(x, y):
    if y == 0:
        return "Cannot divide by zero"

    z = x / y
    return z


print(divisao(23,0))