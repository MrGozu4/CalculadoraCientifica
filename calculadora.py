# Version 2 - Operaciones cientificas completas

# ============================================
#   CALCULADORA CIENTÍFICA - Python
#   Autor: Adrian
#   Version 2.0 - Operaciones científicas
# ============================================

def mostrar_menu():
    print("\n" + "="*45)
    print("       CALCULADORA CIENTÍFICA v2.0")
    print("="*45)
    print("  OPERACIONES BÁSICAS")
    print("  1. Suma             2. Resta")
    print("  3. Multiplicación   4. División")
    print("  5. Potencia         6. Raíz cuadrada")
    print("-"*45)
    print("  OPERACIONES CIENTÍFICAS")
    print("  7. Seno             8. Coseno")
    print("  9. Tangente        10. Logaritmo (log10)")
    print(" 11. Logaritmo natural (ln)")
    print(" 12. Factorial")
    print(" 13. Valor absoluto")
    print("-"*45)
    print("  0. Salir")
    print("="*45)

# ---- Operaciones básicas ----
def suma(a, b):          return a + b
def resta(a, b):         return a - b
def multiplicacion(a, b):return a * b

def division(a, b):
    if b == 0:
        return None, "Error: No se puede dividir entre cero"
    return a / b, None

def potencia(a, b):      return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return None, "Error: No se puede calcular raíz de número negativo"
    return math.sqrt(a), None

# ---- Operaciones trigonométricas (en grados) ----
def seno(angulo):        return math.sin(math.radians(angulo))
def coseno(angulo):      return math.cos(math.radians(angulo))
def tangente(angulo):
    if angulo % 180 == 90:
        return None, "Error: Tangente no definida para ese ángulo"
    return math.tan(math.radians(angulo)), None

# ---- Operaciones logarítmicas ----
def logaritmo(a):
    if a <= 0:
        return None, "Error: El logaritmo solo se define para números positivos"
    return math.log10(a), None

def logaritmo_natural(a):
    if a <= 0:
        return None, "Error: El logaritmo solo se define para números positivos"
    return math.log(a), None

# ---- Otras ----
def factorial(n):
    if n < 0 or n != int(n):
        return None, "Error: El factorial solo aplica a enteros no negativos"
    return math.factorial(int(n)), None

def valor_absoluto(a):   return abs(a), None

# ---- Utilidades ----
def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

def mostrar_resultado(resultado, error=None):
    if error:
        print(f"\n  ⚠ {error}")
    else:
        # Redondear si el resultado es casi entero
        if isinstance(resultado, float) and abs(resultado - round(resultado)) < 1e-10:
            resultado = round(resultado)
        print(f"\n  ✔ Resultado: {resultado}")

def main():
    print("\n  Bienvenido a la Calculadora Científica")
    print("  (Los ángulos trigonométricos se ingresan en GRADOS)")

    while True:
        mostrar_menu()
        opcion = input("\n  Seleccione una opción: ").strip()

        if opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break

        # Operaciones con DOS números
        elif opcion in ["1", "2", "3", "4", "5"]:
            a = obtener_numero("  Ingrese el primer número:  ")
            b = obtener_numero("  Ingrese el segundo número: ")

            if opcion == "1":
                mostrar_resultado(suma(a, b))
                print(f"  ({a} + {b})")
            elif opcion == "2":
                mostrar_resultado(resta(a, b))
                print(f"  ({a} - {b})")
            elif opcion == "3":
                mostrar_resultado(multiplicacion(a, b))
                print(f"  ({a} × {b})")
            elif opcion == "4":
                res, err = division(a, b)
                mostrar_resultado(res, err)
                if not err: print(f"  ({a} ÷ {b})")
            elif opcion == "5":
                mostrar_resultado(potencia(a, b))
                print(f"  ({a} ^ {b})")

        # Operaciones con UN número
        elif opcion in ["6", "7", "8", "9", "10", "11", "12", "13"]:
            a = obtener_numero("  Ingrese el número: ")

            if opcion == "6":
                res, err = raiz_cuadrada(a)
                mostrar_resultado(res, err)
                if not err: print(f"  (√{a})")
            elif opcion == "7":
                mostrar_resultado(seno(a))
                print(f"  (sen({a}°))")
            elif opcion == "8":
                mostrar_resultado(coseno(a))
                print(f"  (cos({a}°))")
            elif opcion == "9":
                res, err = tangente(a)
                mostrar_resultado(res, err)
                if not err: print(f"  (tan({a}°))")
            elif opcion == "10":
                res, err = logaritmo(a)
                mostrar_resultado(res, err)
                if not err: print(f"  (log₁₀({a}))")
            elif opcion == "11":
                res, err = logaritmo_natural(a)
                mostrar_resultado(res, err)
                if not err: print(f"  (ln({a}))")
            elif opcion == "12":
                res, err = factorial(a)
                mostrar_resultado(res, err)
                if not err: print(f"  ({int(a)}!)")
            elif opcion == "13":
                res, err = valor_absoluto(a)
                mostrar_resultado(res, err)
                if not err: print(f"  (|{a}|)")
        else:
            print("\n  ⚠ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
