def hola():
    return "Hola"

import package_B.module_y

print(package_B.module_y.adios())

from package_B import module_y

print(module_y.adios())

from package_B.module_y import adios

print(adios())

print(__name__)