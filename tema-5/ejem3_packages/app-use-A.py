import package_A as p

print(p.module_x.hola())

import package_A.module_x

print (package_A.module_x.hola())

from package_A import module_x

print (module_x.hola())

from package_A.module_x import hola

print (hola())
