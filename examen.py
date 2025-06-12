def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

def mostrar_menu():
    print("\nCalculadora en Terminal")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    if opcion in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == '1':
                resultado = sumar(num1, num2)
            elif opcion == '2':
                resultado = restar(num1, num2)
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
            elif opcion == '4':
                resultado = dividir(num1, num2)

            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Por favor ingresa números válidos.")
    else:
        print("Opción no válida. Intenta de nuevo.")
