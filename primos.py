import math

def es_primo(numero):
    """
    Determina si un número es primo de manera eficiente.
   
    Args:
        numero (int): El número a verificar
       
    Returns:
        bool: True si es primo, False en caso contrario
    """
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
   
    # Verificar divisibilidad solo hasta la raíz cuadrada
    limite = int(math.sqrt(numero)) + 1
    for divisor in range(3, limite, 2):  # Solo números impares
        if numero % divisor == 0:
            return False
    return True

def encontrar_primos_hasta(limite):
    """
    Encuentra todos los números primos hasta un límite dado.
   
    Args:
        limite (int): Límite superior para la búsqueda
       
    Returns:
        list: Lista de números primos encontrados
    """
    if limite < 1:
        return []
   
    primos = []
    # Incluir el 1
    primos.append(1)
    
    for numero in range(2, limite + 1):
        if es_primo(numero):
            primos.append(numero)
   
    return primos

def ejecutar_directo():
    """Función para ejecución directa desde tkinter"""
    print("=== BUSCADOR DE NÚMEROS PRIMOS ===")
    print()
    
    while True:
        try:
            n = int(input("Ingrese hasta qué número desea buscar números primos: "))
           
            if n < 1:
                print("Error: El número debe ser mayor o igual a 1.")
                continue
           
            print(f"\nNúmeros primos hasta {n}:")
            print("-" * 40)
           
            primos = encontrar_primos_hasta(n)
           
            if primos:
                # Mostrar en columnas para mejor legibilidad
                columnas = 8
                for i in range(0, len(primos), columnas):
                    lote = primos[i:i + columnas]
                    print(" ".join(f"{primo:4d}" for primo in lote))
            else:
                print("No se encontraron números primos en el rango especificado.")
           
            print("-" * 40)
            print(f"Total: {len(primos)} números primos")
           
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea buscar primos en otro rango? (s=sí, n=no): ").lower()
        if continuar != 's':
            print("¡Gracias por usar el buscador de números primos!")
            break
        print("\n" + "="*50 + "\n")

def numeros_primos():
    """Función simplificada - ejecuta directamente"""
    ejecutar_directo()

# Cuando se ejecute directamente (no desde tkinter), ejecutar el programa
if __name__ == "__main__":
    ejecutar_directo()