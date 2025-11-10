def es_primo(n):
    """Determina si un número es primo"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Verificar solo hasta la raíz cuadrada
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def descomposicion_en_primos(n):
    """Descompone un número en sus factores primos"""
    if n <= 1:
        return f"{n} no se puede descomponer en factores primos"
    
    temp = n
    factores = {}
    divisor = 2
    
    while divisor * divisor <= temp:
        while temp % divisor == 0:
            factores[divisor] = factores.get(divisor, 0) + 1
            temp //= divisor
        divisor += 1
    
    if temp > 1:
        factores[temp] = factores.get(temp, 0) + 1
    
    # Construir la representación
    if not factores:
        return f"{n} es primo"
    
    partes = []
    for primo, exponente in sorted(factores.items()):
        if exponente == 1:
            partes.append(str(primo))
        else:
            partes.append(f"{primo}^{exponente}")
    
    return f"{n} = " + " × ".join(partes)

def ejecutar_directo():
    """Función para ejecución directa desde tkinter"""
    print("=== TEOREMA FUNDAMENTAL DE LA ARITMÉTICA ===")
    print()
    
    while True:
        try:
            n = int(input("Ingrese un número entero mayor que 1 para descomponer: "))
            
            if n <= 1:
                print("Error: El número debe ser mayor que 1.")
                continue
            
            resultado = descomposicion_en_primos(n)
            print(f"\n{resultado}")
            
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea descomponer otro número? (s=sí, n=no): ").lower()
        if continuar != 's':
            print("¡Gracias por usar el programa de descomposición en primos!")
            break
        print("\n" + "="*50 + "\n")

def teorema_fundamental_aritmetica():
    """Función simplificada - ejecuta directamente"""
    ejecutar_directo()

# Cuando se ejecute directamente (no desde tkinter), ejecutar el programa
if __name__ == "__main__":
    ejecutar_directo()