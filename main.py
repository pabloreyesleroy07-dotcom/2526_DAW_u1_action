def saludo(nombre: str) -> str:
    """Genera un mensaje de bienvenida personalizado.

    Args:
        nombre (str): Nombre de la persona.

    Returns:
        str: Cadena formateada con el saludo.
    """
    return f"Hola, {nombre}!"


if __name__ == "__main__":
    print(saludo("Mundo"))
