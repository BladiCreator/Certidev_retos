# En este reto se evalúa el conocimiento sobre la creación y uso de funciones, un elemento sintáctico que permite reutilizar bloques de código en un programa.


# Instrucciones
# Definir una función: Crea una función llamada multiplicar que tome dos números como argumentos y devuelva su producto.
# Llamada a la función: Utiliza la función multiplicar para multiplicar los números 5 y 3, y guarda el resultado en una variable llamada resultado.
# Argumentos y parámetros: Modifica la función multiplicar para que también pueda aceptar un tercer argumento opcional que determina si el resultado debe ser impreso en pantalla.
def multiplicar(n1, n2, isPrint = False):
    """Retorna el resultado de la multiplicación de n1 y n2 pasados por parámetros respectivamente, si se introduce True al tercer argumento, imprime el resultado por pantalla.

    Args:
        n1 (any): 1rst factor de la multiplicación
        n2 (any): 2nd factor de la multiplicación
        isPrint (bool, optional): Indica si imprimir por pantalla el resultado o retornarlo. Defaults to False.

    Returns:
        int or float or void: Producto de la multiplicación
    """
    if not isPrint:
        return n1 * n2
    print(n1 * n2)

resultado = multiplicar(5, 3)

# Valores predeterminados: Crea una función llamada saludar que tome un nombre como argumento y tenga un valor predeterminado de "Amigo". La función debe imprimir un saludo.

def saludar(nombre: str = "Amigo"):
    """Imprime por pantalla un saludo a (nombre pasado por parámetro)

    Args:
        nombre (str, optional): Nombre a saludar. Defaults to "Amigo".
    """
    print("Hola, " + nombre)

# Retorno de valores: Crea una función llamada es_par que tome un número como argumento y devuelva True si el número es par y False si no lo es.

def es_par(numero: int) -> bool:
    """Verifica si el valor pasado por parámetro es par.

    Args:
        numero (int): Números tanto enteros usado para verificar si es par

    Returns:
        _type_: bool
    """
    return numero % 2 == 0


# Documentación: Añade un docstring a cada función que has creado.
