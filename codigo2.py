# ================================
# Programa: Suma de dos números
# Autor: Ricardo Flores (ejemplo)
# Descripción: Realiza la suma de dos números ingresados por el usuario
# ================================

def pedir_numero(mensaje):
    """
    Pide al usuario un número válido.
    Si el usuario ingresa algo incorrecto, vuelve a pedirlo.
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número válido.")

def sumar(a, b):
    """
    Retorna la suma de dos números.
    """
    return a + b

def main():
    """
    Función principal: controla el flujo del programa.
    """
    print("=== 🧮 Calculadora de Suma Optimizada ===")
    num1 = pedir_numero("Ingresa el primer número: ")
    num2 = pedir_numero("Ingresa el segundo número: ")

    resultado = sumar(num1, num2)
    print(f"✅ La suma de {num1} + {num2} es: {resultado}")

# ================================
# Punto de entrada del programa
# ================================
if __name__ == "__main__":
    main()
