def calcular_mcd(num1, num2):
    """Calcula el MCD usando el algoritmo de Euclides"""
    a, b = abs(num1), abs(num2)
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mcm(num1, num2):
    """Calcula el MCM usando la relación MCM(a,b) = |a*b| / MCD(a,b)"""
    if num1 == 0 or num2 == 0:
        return 0
    return abs(num1 * num2) // calcular_mcd(num1, num2)

def calcular_mcd_multiple(numeros):
    """Calcula el MCD para múltiples números"""
    if not numeros:
        return 0
    mcd = numeros[0]
    for num in numeros[1:]:
        mcd = calcular_mcd(mcd, num)
    return mcd

def calcular_mcm_multiple(numeros):
    """Calcula el MCM para múltiples números"""
    if not numeros:
        return 0
    mcm = numeros[0]
    for num in numeros[1:]:
        mcm = calcular_mcm(mcm, num)
    return mcm

def ejecutar_directo():
    """Función para ejecución directa desde tkinter"""
    print("=== CALCULADORA MCD Y MCM ===")
    print("Basado en el algoritmo de Euclides")
    print()
    
    while True:
        try:
            # Selección de operación
            print("Seleccione la operación:")
            print("1. Calcular MCD (Máximo Común Divisor)")
            print("2. Calcular MCM (Mínimo Común Múltiplo)")
            
            opcion = input("Ingrese su opción (1 o 2): ").strip()
            
            if opcion not in ['1', '2']:
                print("Opción no válida. Seleccionando MCD por defecto.")
                opcion = '1'
            
            # Cantidad de números
            cantidad = int(input("¿Cuántos números desea ingresar? (mínimo 2): "))
            if cantidad < 2:
                print("Error: Debe ingresar al menos 2 números.")
                continue
            
            # Ingreso de números
            numeros = []
            for i in range(cantidad):
                if i == 0:
                    num = int(input("Ingrese el primer número: "))
                else:
                    num = int(input("Ingrese el siguiente número: "))
                numeros.append(num)
            
            print("\n" + "="*50)
            
            # Realizar cálculo según opción
            if opcion == '1':
                resultado = calcular_mcd_multiple(numeros)
                print(f"Números ingresados: {numeros}")
                print(f"El MCD es: {resultado}")
                print(f"Explicación: El Máximo Común Divisor es el número más grande")
                print(f"que divide exactamente a todos los números de la lista.")
                
            else:  # opcion == '2'
                resultado = calcular_mcm_multiple(numeros)
                print(f"Números ingresados: {numeros}")
                print(f"El MCM es: {resultado}")
                print(f"Explicación: El Mínimo Común Múltiplo es el número más pequeño")
                print(f"que es múltiplo de todos los números de la lista.")
            
            print("="*50)
            print("Cálculo completado.")
            
        except ValueError:
            print("Error: Por favor ingrese números enteros válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea realizar otro cálculo? (s=sí, n=no): ").lower()
        if continuar != 's':
            print("¡Gracias por usar la calculadora MCD y MCM!")
            break
        print("\n" + "="*50 + "\n")

def euclides_func():
    """Función simplificada - ejecuta directamente"""
    ejecutar_directo()

# Cuando se ejecute directamente (no desde tkinter), ejecutar el programa
if __name__ == "__main__":
    ejecutar_directo()