from colorama import init, Fore, Back, Style

init(autoreset=True)

"""
Para cambiar el color de las letras en la terminal con Python, la forma más sencilla y multiplataforma 
es  usar la librería colorama. 
Instálala con pip install colorama, luego usa 
    
    Fore para colores de texto, 
    Back para fondo y 
    Style para intensidad (ej. Fore.RED para rojo). 
    
    nhbbb uyyyyyyhhnb j jh667777777777t67m76mmmmmmmmmmmmmmmmm           trt54v 45b 7 6m m m m n nRecuerda inicializarla con init()

"""

COLORES={
    "negro":    Fore.BLACK,
    "rojo":     Fore.RED,
    "verde":    Fore.GREEN,
    "amarillo": Fore.YELLOW,
    "azul":     Fore.BLUE,
    "magenta":  Fore.MAGENTA,
    "cyan":     Fore.CYAN,
    "blanco":   Fore.WHITE,
    # Versiones brillantes
    "negro_brillante":    Fore.LIGHTBLACK_EX,
    "rojo_brillante":     Fore.LIGHTRED_EX,
    "verde_brillante":    Fore.LIGHTGREEN_EX,
    "amarillo_brillante": Fore.LIGHTYELLOW_EX,
    "azul_brillante":     Fore.LIGHTBLUE_EX,
    "magenta_brillante":  Fore.LIGHTMAGENTA_EX,
    "cyan_brillante":     Fore.LIGHTCYAN_EX,
    "blanco_brillante":   Fore.LIGHTWHITE_EX,
    }

def colorear_texto(texto: str, color: str) -> str:
    

    if color not in COLORES:
        opciones = ", ".join(COLORES.keys())
        raise ValueError(
            f"Color '{color}' no válido.\n"
            f"Colores disponibles: {opciones}"
        )

    return f"{COLORES[color]}{texto}{Style.RESET_ALL}"
