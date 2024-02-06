from ast import Continue
from distutils.log import error
import movietk
import main_menu_copy
try:
    movietk.ply()
except error:
    Continue
main_menu_copy.start()