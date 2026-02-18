import package_A.package_B.module_y

print(package_A.package_B.module_y.adios())

from package_A import package_B

print(package_B.module_y.adios())

from package_A.package_B import module_y

print(module_y.adios())

from package_A.package_B.module_y import adios

print(adios())