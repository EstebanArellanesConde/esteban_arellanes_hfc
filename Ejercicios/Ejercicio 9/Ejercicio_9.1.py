#!/usr/bin/python3

import re

Nombre = "Esteban Arellanes"
Usuario = "@xB4NT3"
Cadena = "H3ll0 W0rld, WH04M1"

nombre_re = re.search(r"\b[A-Z]{1}[a-z]*\s[A-Z]{1}[a-z].+", Nombre)
usuario_re = re.search(r"[@]\w*", Usuario)
cadena_re = re.search(r"\W.*W.*W", Cadena)

print(f'{cadena_re.group()}')

