import calculadora

def main():

    print("Bienvenido a mi calculdadora\n")
    print("Las operaciones son en formato +, -, * y / \n")

    # Inicialmente transforma el input a formato float
    f = float(input("Primer valor = \n"))
    op = input("Que operacion quieres realizar = \n")
    s = float(input("Segundo valor = \n"))

    
    

    calculadora.calculo(f, s, op)

if __name__ == "__main__":
    main()

