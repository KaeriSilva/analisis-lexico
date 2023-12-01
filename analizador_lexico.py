
import re

# Palabras reservadas
palabras_reservadas = [
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default',
    'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
    'if', 'int', 'long', 'register', 'return', 'short', 'signed',
    'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
    'unsigned', 'void', 'volatile', 'while', 'printf','scanf', 'True','False'
]

# Diccionario de caracteres especiales y sus etiquetas
especiales = {
    '(': 'AP', #abre parentesis
    ')': 'CP', #cierra parentesis
    '{': 'AL', #abre llave
    '}': 'CL', #cierra llave
    '[': 'AC', #abre corchete
    ']': 'CC' #cierra corchete
}

# Expresiones regulares
regex_letras = r'[a-zA-Z_]'
regex_numero = r'[0-9]'


def determinar_tipo(token):
    if token in palabras_reservadas:
        return "PR"
    elif re.match(regex_letras, token):
        return "ID"
    elif token in especiales:
        return especiales[token]  # Utiliza la etiqueta del diccionario
    elif re.match(regex_numero, token):
        return "NUM"
    else:
        return "CAR"

def tokenizador():
    with open("tokens.txt", "r") as archivo:
        lineas = archivo.readlines()


    for linea in lineas:
        tokens = re.findall(r'\b\w+\b|[^\w\s]', linea)
        print(tokens)
        for token in tokens:
            
            tipo = determinar_tipo(token)
            print(f"{tipo} ", end='')
        print()  
    
tokenizador()