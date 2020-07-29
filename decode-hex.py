# Decode the string.

import pyperclip

# Almacena el texto decodificado
salida = ''

# Guarda el texto a decodificar
texto = input('Introduce un texto: ')

# Decodifica el texto
salida = bytes.fromhex(texto).decode('utf-8')

# Imprime en pantalla el texto decodificado
print(salida)

# Copia el mensaje al portapapeles
pyperclip.copy(salida)
