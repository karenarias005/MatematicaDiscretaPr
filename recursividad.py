def calcular_factorial(n):
    """Calcula el factorial de un número usando recursividad"""
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def ejecutar_directo():
    """Función para ejecución directa desde tkinter"""
    print("=== CÁLCULO DE FACTORIAL ===")
    print()
    
    while True:
        try:
            n = int(input("Ingrese un número para calcular su factorial: "))
            
            if n < 0:
                print("Error: No existe factorial de números negativos.")
                continue
            
            resultado = calcular_factorial(n)
            print(f"\nEl factorial de {n} es: {resultado}")
            
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
        except RecursionError:
            print("Error: Número demasiado grande para recursión. Use un número menor.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea calcular otro factorial? (s=sí, n=no): ").lower()
        if continuar != 's':
            print("¡Gracias por usar la calculadora de factoriales!")
            break
        print("\n" + "="*50 + "\n")

def recursividad():
    """Función simplificada - ejecuta directamente"""
    ejecutar_directo()

# Cuando se ejecute directamente (no desde tkinter), ejecutar el programa
if __name__ == "__main__":
    ejecutar_directo()