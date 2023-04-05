# importing time, Fore (from colrama) and functions(from functions.py)
import time
import functions
from colorama import Fore , Style

# storing colors and reset value in variables
c1 = Fore.RED
c2 = Fore.GREEN
c3 = Fore.YELLOW
rst = Style.RESET_ALL

print(),functions.homeMenu() # calling homeMenu from functions
while True:
    # exception handling for choose
    try:
        print(),print('_'*59)
        # asking user for input
        choose = int(input('Choose the number of the action you want to perform \n \n -> '+c3))
        print(rst,'_'*10)
        if choose == 1:
            functions.displayItems() # calling displayItems from functions
            functions.askQstn() # calling askQstn from functions
        elif choose == 2:
            
            functions.rentCostumes() # calling rentCostumes from functioms
        elif choose == 3:
            
            functions.returnCostumes() # calling returnCostumes from functions
            
        elif choose == 4 :
            time.sleep(0.5),print(),print()
            print(c2 + '_'*15, '>' , 'Thank you for visiting us' , '<' , '_'*14 )
            print('_'*60 + rst)
            break
        else :
            print( c1,'Please choose a valid action !',rst)

    except:
        time.sleep(0.2)
        print(c1,'please assign a valid task  !',rst )
        
            
 
