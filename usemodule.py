import os
import sys

modulepath = os.getcwd() + '\\module'
sys.path.append(modulepath)
print(sys.path)

import mymodule
mymodule.show()
print(mymodule.name)
mymodule.name = 'usemodule.py'
print(mymodule.name)