
def calculo(first, second, op):
    result = 0 # Variable que guardara el resultado final

    # Verifica si los numeros son de decimal cero
    if first.is_integer():
        first = (int)(first)

    if second.is_integer():
        second = (int)(second)


    # Chequea que operacion realizar
    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    elif op == '*':
        result = first * second
    elif op == '/':
        result = int(first / second) # Asegura que el resultado sera en formato Int
    else:
        print("Operacion Invalida, debe ser +, -, * o /") 
        return -1

    print(f"El resultado de {first} {op} {second} es {result}")