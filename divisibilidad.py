import math

def suma_digitos(num):
    suma_local = 0
    while num > 0:
        suma_local += num % 10
        num //= 10  # División entera
    return suma_local

def ejecutar_directo():
    """Función para ejecución directa desde tkinter"""
    print("=== ANÁLISIS DE DIVISIBILIDAD ===")
    print("Este programa analiza los criterios de divisibilidad de un número.")
    print()
    
    while True:
        try:
            n = int(input("Ingrese un número a analizar: "))
            print(f"\nAnálisis del número {n}:")
            print("-" * 40)
            
            resultado = []
            
            # Criterios de divisibilidad
            resultado.append("✓ Es divisible por 1 (todos los números son divisibles por 1)")
            
            if n % 2 == 0:
                resultado.append("✓ Es divisible por 2 (último dígito par)")
            else:
                resultado.append("✗ NO es divisible por 2")
                
            if suma_digitos(n) % 3 == 0:
                resultado.append("✓ Es divisible por 3 (suma de dígitos divisible por 3)")
            else:
                resultado.append("✗ NO es divisible por 3")
                
            if (n % 100) % 4 == 0:
                resultado.append("✓ Es divisible por 4 (últimos dos dígitos divisible por 4)")
            else:
                resultado.append("✗ NO es divisible por 4")
                
            if n % 5 == 0:
                resultado.append("✓ Es divisible por 5 (termina en 0 o 5)")
            else:
                resultado.append("✗ NO es divisible por 5")
                
            if n % 7 == 0:
                resultado.append("✓ Es divisible por 7 (división exacta)")
            else:
                resultado.append("✗ NO es divisible por 7")
                
            if (n % 1000) % 8 == 0:
                resultado.append("✓ Es divisible por 8 (últimos tres dígitos divisible por 8)")
            else:
                resultado.append("✗ NO es divisible por 8")
                
            if suma_digitos(n) % 9 == 0:
                resultado.append("✓ Es divisible por 9 (suma de dígitos divisible por 9)")
            else:
                resultado.append("✗ NO es divisible por 9")
                
            if n % 10 == 0:
                resultado.append("✓ Es divisible por 10 (termina en 0)")
            else:
                resultado.append("✗ NO es divisible por 10")
            
            # Mostrar resultados
            for item in resultado:
                print(item)
                
            print("-" * 40)
            print(f"Análisis completado para el número {n}")
            
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea probar con otro número? (s=sí, n=no): ").lower()
        if continuar != 's':
            print("¡Gracias por usar el programa de divisibilidad!")
            break
        print("\n" + "="*50 + "\n")

def divisibilidad():
    """Función simplificada - ejecuta directamente"""
    ejecutar_directo()

# Cuando se ejecute directamente (no desde tkinter), ejecutar el programa
if __name__ == "__main__":
    ejecutar_directo()