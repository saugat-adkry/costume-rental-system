# importing all the necessary libraries
import os, string, time
from colorama import Fore , Style, Back
from random import  choices
from tabulate import tabulate
from datetime import date, timedelta



# storing foreground and background color in variables 
c1 = Fore.RED
c2 = Fore.GREEN
c3 = Fore.YELLOW
c4 = Fore.BLUE

# storing Style.reset_all in a variable
rst = Style.RESET_ALL


#  creating a function that displays items in the stock
def displayItems():
    readFile = open('Costumes.txt','r').readlines()
    lst = []
    for lines in readFile:
        list = lines.rstrip('\n').split(',')
        lst.append(list) # adding each line to lst
    
    print()
    print(f'List of items in our stock : \n { "_"*29} ' )
    print()
    finalData = []
    # using for loop to ascess the data in the file
    for i in range(len(lst)):
        # getting name, brand, price and total items using for loop
        name = lst[i] [0]
        brand = lst[i] [1]
        price = lst[i] [2]
        totalNoOfItems = lst[i] [3]

        data = [name,brand,price,totalNoOfItems]
        # adding data in finalData with each itiration
        finalData.append(data)
        # defining table header names
        header_names = [c4+"Name", "Brand", "Price per day", "Total items"+rst]

    #display table
    print(tabulate(finalData, headers=header_names, tablefmt="fancy_grid", showindex="always"))
    print()



#  creating a function to diplay list of actions to perform
def homeMenu():
    print('_'*76)
    print(c3+'-'*20,"WELCOME TO SAUGAT'S COSTUME RENTAL",'-'*20+rst)
    print('_'*76)
    print()
    print("""
1. Display items
2. Rent Costumes
3. Return Costumes
4. Exit  """)
    print()



#  creating a function to ask question to user weather they want to exit the program or return to home page
def askQstn():
            while True:
                ask = input('Enter [h] to return to home page \n \n -> ' + c3)
                print(rst,'_'*10)
                print()
                if ask == 'h' or ask == 'H':
                    homeMenu()
                    break
                else:
                    time.sleep(0.2)
                    print(c1,'please enter [ h or H ] ', rst)



# Defining a function to change quantity of our items after renting or returning
def qntyChange(CosId,totalNoOfItems):
    readFile = open('Costumes.txt','r').readlines() # reading our file
    lst = []
    for line in readFile:
        list = line.rstrip('\n').split(',')
        lst.append(list) # storing each line in lst
    for i in range(len(lst)):
        # changing quantity in orignal file
        readFile[CosId] = readFile[CosId].replace(lst[i][3],str(f' {totalNoOfItems}'))
        art = open('Costumes.txt','w')
        art.writelines(readFile)
        art.close()




#  creating a function to rent costumes 
def rentCostumes():
    currentTime = time.strftime("%Y%m%d_%H%M%S") # variable that stores current time
    # reading file
    readFile = open('Costumes.txt','r').readlines()
    index = []
    lst = []
    for line in readFile:
        list = line.rstrip('\n').split(',')
        lst.append(list) # adding each line to lst 
    for ind in range(len(lst)):
        index.append(ind) # adding index of item to ind

    displayItems()
    loop1 = True
    while loop1: 
        # exception handling for costume ID
        try:
            
            loop2 = True
            while loop2:
                # asking user for input using while loop
                cosID = int(input('Enter ID of costume you want to rent : \n \n -> ' + c3))
                print(rst,'_'*10)
                print()
                if cosID not in index:
                    
                    print(c1,'Enter a valid ID !',rst)
                    print()
                else :
                    loop3 = True
                    # exception handling for total costumes
                    while loop3:
                        try:
                            negativity = True
                            while negativity:
                                    
                                totalCostumes = int(input('Enter total costumes you want to rent : \n \n -> ' + c3))
                                print(rst,'_'*10)
                                print()

                                if totalCostumes <= 0:
                                    print(c1,'please enter valid number of costumes to rent !',rst)
                                    print()
                                else:
                                    negativity = False
                            cusName = input('Enter your name : \n \n -> ' + c3)
                            print(rst,'_'*10)
                            print()
                            
                            cusNum = input('Enter your phone number : \n \n -> ' + c3)
                            print(rst,'_'*10)
                            print()

                            # getting data using for loop
                            for i in range(len(lst)): 
                                name = lst[i] [0]
                                brand = lst[i] [1]
                                cost = lst[i] [2]
                                price = str(cost)
                                price2 = float(price.strip('$ '))
                                totalNoOfItems = int(lst[i] [3])
                                if cosID == i :
                                    if totalNoOfItems < totalCostumes :
                                        if totalNoOfItems == 0:
                                            
                                            print('-'*10,'Sorry but currently this item is ',c1, 'out of stock',rst,'-'*10),print()
                                        else:
                                            
                                            print('-'*10,'Sorry but currently we only have',c3,f' {totalNoOfItems} ',rst,'pieces of this item','-'*10)
                                        looping = True
                                        while looping:
                                            ask3 = input('Do you want to continue renting? ( y/n ) \n \n -> ' + c3)
                                            print(rst,'_'*10)
                                            print()
                                            if ask3 == 'y' or ask3 == 'Y':
                                                
                                                return rentCostumes()

                                            elif ask3 == 'n' or ask3 == 'N':
                                                
                                                homeMenu()
                                                looping = False
                                            else:
                                                print(c1,'please answer in ( y/n ) ',rst)
                                    else:
                                        totalNoOfItems1 = totalNoOfItems-totalCostumes
                                        # generating invoice id 
                                        rentInvoiceId = ''.join(choices(string.ascii_lowercase + string.digits , k = 5))
                                        # defining a function to display rented item's invoice
                                        def rentInvoice(noOfCostumes):
                                            with open('rentInvoices\\'+cusName+'_Rent_Invoice_'+currentTime+'.txt','w') as rentInvoices:
                                                rentInvoices.write(f""" 
----------------------------->Your bill for {name}<-----------------------------


invoice id : {str(rentInvoiceId)}
issue date : {date.today()}

        Costumer's Name             : {cusName} 
        Phone number                : {cusNum}
        Costume                     : {name}
        Brand                       :{brand}
        Total no. of costume rented : {noOfCostumes}
        Total price                 : ${totalCostumes*price2}

        Note : You will be charged with extra service charge of 10% per day after 5th day.

------------------------------------>Thank you for choosing us<-----------------------------------
                                        """)
                                                rentInvoices.close()
                
                                            print()
                                            
                                            print(c2,f' {name} successfully rented')
                                            print('-'*10,f'Check invoice for details','-'*10,rst)
                                            print()
                                            os.system(f'notepad.exe rentInvoices\\{cusName}_Rent_Invoice_{currentTime}.txt')
                                        # calling rentInvoice
                                        rentInvoice(totalCostumes)
                                        qntyChange(cosID,totalNoOfItems1) # calling qntyChange
                                        
                                        isLooped = True
                                        while isLooped:
                                            # asking user if they want to rent more
                                            ask5 = input('Do you want to rent more ? ( y/n ) : \n \n -> ' + c3)
                                            print(rst,'_'*10),print()
                                            if ask5 == 'y' or ask5 == 'Y' :
                                                loop5 = True
                                                while loop5:
                                                    # exception handling for number of costumes
                                                    try:
                                                        loop6 = True
                                                        while loop6:
                                                            
                                                            totalCostumes2 = int(input('Enter number of costumes you want to rent : \n \n -> ' + c3))
                                                            print(rst,'_'*10)
                                                            print()
                                                            if totalCostumes2 > totalNoOfItems1:
                                                                if totalNoOfItems1 == 0:
                                                                    
                                                                    print('-'*10,'Sorry but currently this item is',c1,' out of stock',rst,'-'*10)
                                                                    
                                                                    # printing multiple empty lines
                                                                    print(),print(),print()
                                                                    # calling homeMenu
                                                                    homeMenu()
                                                                    loop6 = False
                                                                else:
                                                                    
                                                                    print('-'*10,'Sorry but currently we only have ' ,c3 , f'{totalNoOfItems1} ',rst, ' pieces of this item left','-'*10)
                                                            elif totalCostumes2 <= 0:
                                                                print(c1,'please enter valid number of costumes to rent !',rst)
                                                                print()
                                                            else:
                                                                print()
                                                                totalCostumes3 = totalCostumes + totalCostumes2
                                                                # calling rentInvoice function
                                                                rentInvoice(totalCostumes3)
                                                                totalNoOfItems2 = totalNoOfItems-totalCostumes3
                                                                qntyChange(cosID,totalNoOfItems2) # calling qntyChange
                                                                homeMenu()
                                                                loop6 = False
                                                                # GIDDI VAKO TAHU
                                                            loop5 = False
                                                    except:
                                                        print()
                                                        
                                                        print(c1,'please enter a INTEGER value for number of costumes !',rst)
                                                        print()
                                                isLooped = False
                                                    
                                            elif ask5 == 'n' or ask5 =='N':
                                                
                                                homeMenu()  
                                                isLooped = False
                                            else :
                                                
                                                print(c1,'please answer in ( y/n ) ',rst)

                                
                            loop3 = False

                        except:
                            print()
                            
                            print(c1,'please enter a INTEGER value for total costumes !',rst)
                            print()
                    loop2 = False
            loop1 = False 
        
        except:
            print()
            
            print(c1,'Please enter a INTEGER value for ID !',rst)
            print()





 
#  return costumes function
def returnCostumes():
    currentTime = time.strftime("%Y%m%d_%H%M%S") # storing current time in a variable
    readFile = open('Costumes.txt','r').readlines() # reading our file
    lst = []
    for line in readFile:
        list = line.rstrip('\n').split(',')
        lst.append(list) # storing each line in lst

    displayItems() # calling display items
    #  asking user for input
    cusName = input('Enter your name : \n \n -> ' + c3)
    print(rst,'_'*10)
    print()
    
    loop7 = True
    while loop7:
        try:
            loop8 = True
            while loop8:
                    
                    ReturnCosID = int(input('Enter ID of the costume you want to return : \n \n -> ' + c3))
                    print( rst , '_'*10)
                    print()
                    index = []
                    for i in range(len(lst)):
                        index.append(i) # storing index of costumes in index

                    # checking if enterd costumer id is in index
                    if ReturnCosID not in index:
                        
                        print(c1,'Enter a vaild id',rst)
                        print()
                    else:
                        loop9 = True
                        while loop9:
                            try:
                                negativity2 = True
                                while negativity2:
   
                                    totalCostumes = int(input('Enter total number of costumes you want to return : \n \n -> ' + c3))
                                    print(rst , '_'*10)
                                    print()

                                    if totalCostumes <= 0:
                                        print(c1,'please enter valid number of cosutmes to rent !',rst)
                                    else:
                                        negativity2 = False

                                # defining a function that ask renting date from customer
                                def dateFun():
                                    dateLoop = True 
                                    while dateLoop:
                                        DOR = input('Enter Date of rent of Costume (Y-M-D) : \n \n -> ' + c3) # asking user for date
                                        print(rst,'_'*10)
                                        print()
                                        if '-' in DOR:
                                            DOR2 = DOR.split('-') 
                                            DateOfRent = date(int(DOR2[0]) , int(DOR2[1]) , int(DOR2[2]))# spliting date and changing it to data type of date
                                            dateLoop = False
                                        else:
                                            print(c1,'enter date in Y-M-D format !',rst)
                                    loopX = True
                                    while loopX:
                                        if DateOfRent > date.today():
                                            
                                            print(c3,'We dont give service to time travellers !',rst)
                                            print()
                                            print(c1,'please enter a valid date !',rst)
                                            print()
                                            dateFun() # calling dateFun
                            
                                        else:
                                            TodayDate = date.today() # storing today's date in a variable
                                            
                                
                                            # using for loop to ascess the data of file
                                            for i in range(len(lst)):
                                                name = lst[i] [0]
                                                brand = lst[i] [1]
                                                cost = lst[i] [2]
                                                price = str(cost)
                                                price2 = float(price.strip('$ ')) # converting string price to float
                                                totalNoOfItems = int(lst[i] [3])
                                                if ReturnCosID == i :
                                                    rentingDays = (TodayDate - DateOfRent).days # converting days to int
                                                    if rentingDays == 0 :
                                                        rentingDays = 1
                                                    if TodayDate - DateOfRent > timedelta(days=5) :
                                                        # increasing total no of items 
                                                        totalNoOfItems = totalCostumes + totalNoOfItems
                                                        # generating invoice id
                                                        returnInvoiceId = ''.join(choices(string.ascii_lowercase + string.digits , k = 5))
                                                        fine = (10/100)*price2
                                                        costWithFine = fine + price2 # calculating cost with fine
                                
                                                        # making a invoice for returned costumes if the return date is more than 5 days
                                                        fileName = cusName+'_Return_invoice_'+currentTime
                                                        with open('returnInvoices\\'+fileName+'.txt','w') as returnInvoices:
                                                                returnInvoices.write(f""" 
----------------------------->Your bill for {name}<-----------------------------

    invoice id : {str(returnInvoiceId)}
    issue date : {TodayDate}

            Costumer's Name             : {cusName} 
            Costume                     : {name}
            Brand                       :{brand}
            Date Of Rent                : {DateOfRent}
            Date Of Return              : {TodayDate}
            Total renting Days          : {rentingDays} days
            Total no. of costume rented : {totalCostumes}
            Total price                 : ${totalCostumes*costWithFine*rentingDays}

            Note : You have been charged with extra service charge of 10% per day for
                    {rentingDays-5} days for delayed return .

------------------------------------>Thank you for choosing us<-----------------------------------
                                                        """)
                                                                returnInvoices.close()
                                
                                                        print()
                                                        print(c2,f' {name} successfully returned.')
                                                        print('-'*10,f'Check invoice for details','-'*10,rst)
                                                        print()
                                                        os.system(F'notepad.exe returnInvoices\\{cusName}_Return_invoice_{currentTime}.txt')
                                                        homeMenu()
                                                        qntyChange(ReturnCosID,totalNoOfItems) # calling qntyChange 
                                                    else:
                                                        # increasing total no. of items
                                                        totalNoOfItems = totalCostumes + totalNoOfItems
                                                        # generating invoice id
                                                        returnInvoiceId = ''.join(choices(string.ascii_lowercase + string.digits , k = 5))
                                                        # making a invoice for returned costumes if return date is less than 5 days
                                                        fileName = cusName+'_Return_invoice_'+currentTime
                                                        with open('returnInvoices\\'+fileName+'.txt','w') as returnInvoices:
                                                            returnInvoices.write(f""" 
----------------------------->Your bill for {name}<-----------------------------

    invoice id : {str(returnInvoiceId)}
    issue date : {TodayDate}

            Costumer's Name             : {cusName} 
            Costume                     : {name}
            Brand                       :{brand}
            Date Of Rent                : {DateOfRent}
            Date Of Return              : {TodayDate}
            Total renting Days          : {rentingDays} days
            Total no. of costume rented : {totalCostumes}
            Total price                 : ${totalCostumes*price2*rentingDays}

            Thank you for returning {name } within five days.

------------------------------------>Thank you for choosing us<-----------------------------------
                                                            """)
                                                            returnInvoices.close()
                                
                                                        print(),
                                                        print(c2,f' {name} successfully returned.')
                                                        print('_'*10,f'Check invoice for details','_'*10,rst)
                                                        print()
                                                        
                                                        homeMenu() #calling homeMenu
                                                        os.system(F'notepad.exe returnInvoices\\{cusName}_Return_invoice_{currentTime}.txt')
                                                        qntyChange(ReturnCosID,totalNoOfItems) # calling qntyChange 

                                                    break # break for loop
                                        loopX = False
                                loop9 = False
                                
                                dateFun() # calling dateFun
                                loop8 = False
    
                            except:
                                
                                print(c1,'Please enter INTEGER value for total costumes !',rst)
            loop7 = False
        except:
            
            print(c1,'please enter a INTEGER value for ID !',rst)
            print()