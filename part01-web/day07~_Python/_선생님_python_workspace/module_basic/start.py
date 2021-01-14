#import test_module as test #ModuleNotFoundError
# import test_package.test_module as test
# import test_package.test_module2 as test2
from test_package import *

radius = test_module.number_input()
print(test_module.get_circumferecne(radius))
print(test_module.get_circle_area(radius))

x,y=test_module2.number_input()
print(test_module2.get_circumferecne(x, y))
print(test_module2.get_rectangle_area(x,y))

print("#메인의 __name__ 출력#")
print(__name__)
print()


