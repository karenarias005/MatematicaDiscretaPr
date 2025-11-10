import streamlit as st
import math

# Configuración de la página
st.set_page_config(
    page_title="Programas Matemáticos",
    page_icon="🔢",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
    .main {
        background-color: #DFBBCA;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
        background-color: #8674C9;
        color: white;
        border-radius: 10px;
        border: none;
        margin: 5px 0;
    }
    .stButton>button:hover {
        background-color: #774972;
    }
    h1 {
        color: #710755;
        text-align: center;
    }
    .definition-box {
        background-color: #F5E6E8;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Definiciones
DEFINICIONES = {
    "Divisibilidad": """
    La divisibilidad estudia las condiciones bajo las cuales un número puede ser dividido exactamente por otro. 
    Un número 'a' es divisible por 'b' si existe un número entero 'c' tal que a = b × c.
    
    **Criterios de divisibilidad:**
    - Por 2: Último dígito par
    - Por 3: Suma de dígitos divisible por 3
    - Por 4: Últimos dos dígitos divisible por 4
    - Por 5: Termina en 0 o 5
    - Por 9: Suma de dígitos divisible por 9
    - Por 10: Termina en 0
    """,
    
    "TFA": """
    El Teorema Fundamental de la Aritmética establece que todo número entero mayor que 1 puede ser 
    representado de manera única como producto de números primos, ignorando el orden de los factores.
    
    **Este teorema garantiza que:**
    - Cada número tiene una descomposición única en factores primos
    - Los números primos son los 'bloques de construcción' de todos los números
    - No importa el orden en que se multipliquen los factores primos
    """,
    
    "Números Primos": """
    Los números primos son aquellos números naturales mayores que 1 que solo son divisibles por sí mismos y por 1. 
    Son los 'bloques de construcción' de todos los números enteros.
    
    **Propiedades importantes:**
    - El 2 es el único número primo par
    - Hay infinitos números primos (Euclides)
    - Los números mayores que 1 que no son primos se llaman compuestos
    - La distribución de primos sigue patrones complejos
    """,
    
    "Recursividad": """
    La recursividad es un concepto en programación y matemáticas donde una función se define en términos de sí misma. 
    Es especialmente útil para resolver problemas que pueden ser divididos en subproblemas similares.
    
    **Características:**
    - Caso base: Condición de terminación
    - Caso recursivo: La función se llama a sí misma
    - Ejemplos clásicos: Factorial, Fibonacci
    - Ventaja: Código más elegante para problemas recursivos naturales
    """,
    
    "MCD y MCM": """
    El Máximo Común Divisor (MCD) es el número más grande que divide exactamente a dos o más números. 
    El Mínimo Común Múltiplo (MCM) es el número más pequeño que es múltiplo de dos o más números.
    
    **Propiedades:**
    - MCD(a,b) × MCM(a,b) = a × b
    - Algoritmo de Euclides: Método eficiente para calcular MCD
    - El MCD se usa para simplificar fracciones
    - El MCM se usa para sumar fracciones con diferente denominador
    """
}

# Inicializar estado de sesión
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'menu'
if 'programa_actual' not in st.session_state:
    st.session_state.programa_actual = None

# Funciones auxiliares
def suma_digitos(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    return suma

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def calcular_factorial(n):
    if n == 0:
        return 1
    return n * calcular_factorial(n - 1)

def calcular_mcd(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

def calcular_mcm(num1, num2):
    return (num1 * num2) // calcular_mcd(num1, num2)

def descomposicion_primos(n):
    if n <= 1:
        return f"{n} no se puede descomponer"
    
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
    
    if not factores:
        return f"{n} es primo"
    
    partes = []
    for primo, exponente in sorted(factores.items()):
        if exponente == 1:
            partes.append(str(primo))
        else:
            partes.append(f"{primo}^{exponente}")
    
    return f"{n} = " + " × ".join(partes)

# Funciones de navegación
def ir_a_definicion(programa):
    st.session_state.pagina = 'definicion'
    st.session_state.programa_actual = programa

def ir_a_ejecutar():
    st.session_state.pagina = 'ejecutar'

def ir_a_codigo():
    st.session_state.pagina = 'codigo'

def volver_menu():
    st.session_state.pagina = 'menu'
    st.session_state.programa_actual = None

# PÁGINA: MENÚ PRINCIPAL
if st.session_state.pagina == 'menu':
    st.title("🔢 PROGRAMAS MATEMÁTICOS")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("📊 Divisibilidad"):
            ir_a_definicion("Divisibilidad")
        
        if st.button("🔢 Teorema Fundamental de la Aritmética"):
            ir_a_definicion("TFA")
        
        if st.button("⭐ Números Primos"):
            ir_a_definicion("Números Primos")
        
        if st.button("🔄 Recursividad"):
            ir_a_definicion("Recursividad")
        
        if st.button("➗ Cálculo de MCD y MCM"):
            ir_a_definicion("MCD y MCM")

# PÁGINA: DEFINICIÓN
elif st.session_state.pagina == 'definicion':
    programa = st.session_state.programa_actual
    
    st.title(programa)
    st.markdown("---")
    
    st.markdown(f'<div class="definition-box">{DEFINICIONES[programa]}</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("▶️ EJECUTAR", use_container_width=True):
            ir_a_ejecutar()
    
    with col2:
        if st.button("💻 VER CÓDIGO", use_container_width=True):
            ir_a_codigo()
    
    with col3:
        if st.button("🏠 VOLVER", use_container_width=True):
            volver_menu()

# PÁGINA: EJECUTAR
elif st.session_state.pagina == 'ejecutar':
    programa = st.session_state.programa_actual
    
    st.title(f"▶️ {programa}")
    
    if st.button("🏠 Volver al Menú"):
        volver_menu()
    
    st.markdown("---")
    
    # DIVISIBILIDAD
    if programa == "Divisibilidad":
        n = st.number_input("Ingrese un número:", min_value=1, value=12, step=1)
        
        if st.button("🔍 Analizar"):
            st.subheader(f"Análisis del número {n}:")
            st.write("✓ Es divisible por 1 (todos los números lo son)")
            
            if n % 2 == 0:
                st.write("✓ Es divisible por 2 (último dígito par)")
            else:
                st.write("✗ NO es divisible por 2")
            
            if suma_digitos(n) % 3 == 0:
                st.write("✓ Es divisible por 3 (suma de dígitos divisible por 3)")
            else:
                st.write("✗ NO es divisible por 3")
            
            if (n % 100) % 4 == 0:
                st.write("✓ Es divisible por 4 (últimos dos dígitos divisibles por 4)")
            else:
                st.write("✗ NO es divisible por 4")
            
            if n % 5 == 0:
                st.write("✓ Es divisible por 5 (termina en 0 o 5)")
            else:
                st.write("✗ NO es divisible por 5")
            
            if n % 7 == 0:
                st.write("✓ Es divisible por 7")
            else:
                st.write("✗ NO es divisible por 7")
            
            if (n % 1000) % 8 == 0:
                st.write("✓ Es divisible por 8 (últimos tres dígitos divisibles por 8)")
            else:
                st.write("✗ NO es divisible por 8")
            
            if suma_digitos(n) % 9 == 0:
                st.write("✓ Es divisible por 9 (suma de dígitos divisible por 9)")
            else:
                st.write("✗ NO es divisible por 9")
            
            if n % 10 == 0:
                st.write("✓ Es divisible por 10 (termina en 0)")
            else:
                st.write("✗ NO es divisible por 10")
    
    # TFA
    elif programa == "TFA":
        n = st.number_input("Ingrese un número mayor que 1:", min_value=2, value=24, step=1)
        
        if st.button("🔢 Descomponer"):
            resultado = descomposicion_primos(n)
            st.success(resultado)
    
    # NÚMEROS PRIMOS
    elif programa == "Números Primos":
        limite = st.number_input("Ingrese hasta qué número buscar primos:", min_value=1, value=50, step=1)
        
        if st.button("🔍 Buscar Primos"):
            primos = [1]  # Incluir 1 como en código original
            primos.extend([i for i in range(2, limite + 1) if es_primo(i)])
            
            st.subheader(f"Números primos hasta {limite}:")
            
            # Mostrar en columnas
            cols = st.columns(10)
            for idx, primo in enumerate(primos):
                with cols[idx % 10]:
                    st.write(primo)
            
            st.info(f"Total: {len(primos)} números primos")
    
    # RECURSIVIDAD
    elif programa == "Recursividad":
        n = st.number_input("Ingrese un número para calcular factorial:", min_value=0, max_value=20, value=5, step=1)
        
        if st.button("🔢 Calcular Factorial"):
            try:
                resultado = calcular_factorial(n)
                st.success(f"El factorial de {n} es: {resultado}")
            except RecursionError:
                st.error("Número demasiado grande para recursión")
    
    # MCD Y MCM
    elif programa == "MCD y MCM":
        operacion = st.radio("Seleccione operación:", ["MCD", "MCM"])
        
        cantidad = st.number_input("¿Cuántos números?", min_value=2, max_value=10, value=2, step=1)
        
        numeros = []
        cols = st.columns(cantidad)
        for i in range(cantidad):
            with cols[i]:
                num = st.number_input(f"Número {i+1}", min_value=1, value=12+i*6, step=1, key=f"num_{i}")
                numeros.append(num)
        
        if st.button(f"🔢 Calcular {operacion}"):
            resultado = numeros[0]
            for i in range(1, len(numeros)):
                if operacion == "MCD":
                    resultado = calcular_mcd(resultado, numeros[i])
                else:
                    resultado = calcular_mcm(resultado, numeros[i])
            
            st.success(f"Números: {numeros}")
            st.success(f"El {operacion} es: {resultado}")

# PÁGINA: VER CÓDIGO
elif st.session_state.pagina == 'codigo':
    programa = st.session_state.programa_actual
    
    st.title(f"💻 Código: {programa}")
    
    if st.button("🏠 Volver al Menú"):
        volver_menu()
    
    st.markdown("---")
    
    codigos = {
        "Divisibilidad": '''def suma_digitos(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    return suma

n = int(input("Ingrese un número: "))

if n % 2 == 0:
    print("Es divisible por 2")

if suma_digitos(n) % 3 == 0:
    print("Es divisible por 3")
# ... más criterios''',
        
        "TFA": '''def descomposicion_primos(n):
    temp = n
    factores = {}
    divisor = 2
    
    while divisor * divisor <= temp:
        while temp % divisor == 0:
            factores[divisor] = factores.get(divisor, 0) + 1
            temp //= divisor
        divisor += 1
    
    if temp > 1:
        factores[temp] = 1
    
    return factores''',
        
        "Números Primos": '''def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

limite = int(input("Hasta qué número: "))
primos = [i for i in range(2, limite+1) if es_primo(i)]
print(primos)''',
        
        "Recursividad": '''def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n - 1)

n = int(input("Número: "))
print(f"Factorial de {n} es: {calcular_factorial(n)}")''',
        
        "MCD y MCM": '''def calcular_mcd(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

def calcular_mcm(num1, num2):
    return (num1 * num2) // calcular_mcd(num1, num2)'''
    }
    
    st.code(codigos[programa], language='python')
