# Cisco Database
# Michael Gennery
# July 2021
     
from csv import reader
from MJG_Functions import *



###

### FUNCTIONS

###



#001
# Display list of routers

    

def display_routers(display_router_table):

    text0 = '    '
    tabtext1 = ''
    tabtext2 = ''
    tabtext3 = ''
    tabtext4 = ''
    tabtext5 = ''
    tabtext6 = ''
    tabtext7 = ''
    tabtext8 = ''
    tabtext9 = ''
    
    print('\nROUTERS\n\n')

    print('      SKU','\t\t    Make','\t\t Series','\t Model','\t\t IOS','\t\t BASE','\t\t\t POE(W)',' RAM','\t Flash','\t PRICE $')
    print('________________________________________________________________________________________________________________________________________________________\n')

    if len(display_router_table) < 1:
        print('\n\tNo routers to display')

    tabtext = ['',
               ' ',
               '  ',
               '   ',
               '    ',
               '     ',
               '      ',
               '       ',
               '        ',
               '         ',
               '          ',
               '           ',
               '            ',
               '             ',
               '              ',
               '               ',
               '                ',
               '                 ',
               '                  ',
               '                   ',
               '                    ',
               '                     '
               ]
    
    select_number = 1
    
    for router in display_router_table:

        # [0]   SKU
        # [1]   Make e.g. Cisco
        # [2]   Series
        # [3]   Model
        # [7]   IOS
        # [8]   Base
        # [12]  POE Wattage
        # [30]  RAM Max
        # [32]  Flash Max
        # [51]  Price

        # AFTER SKU - router[0] - tabtext1
        tabtext1_num = 20 - len(router[0])
        tabtext1 = tabtext[tabtext1_num]
        
        # AFTER MAKE router[1] - tabtext2
        if len(router[1]) <= 5:
            tabtext2 = '\t\t'
        elif len(router[1]) > 5 and len(router[1]) <= 10:
           tabtext2 = '\t\t'
        else:
           tabtext2 = '\t'
 
        # AFTER SERIES router[2] - tabtext3
        if len(router[2]) <= 5:
            tabtext3 = '\t\t'
        elif len(router[2]) > 5 and len(router[7]) <= 10:
           tabtext3 = '\t'
        else:
           tabtext3 = '\t'

        # AFTER MODEL router[3] - tabtext4
        if len(router[3]) <= 5:
            tabtext4 = '\t\t'
        else:
            tabtext4 = '\t'
        
        # AFTER IOS router[7] - tabtext5
        if len(router[7]) <= 3:
            tabtext5 = '\t\t'
        elif len(router[7]) > 3 and len(router[7]) <= 11:
            tabtext5 = '\t'
        else:
            tabtext5 = '\t'
            temptext = router[7] # The text is truncated to allow it to fit onto the screen
            router[7] = temptext[:7]
        if router[7] == 'Linux':
            tabtext5 += '\t'

        # AFTER BASE router[8] - tabtext6
        if len(router[8]) < 3:
            tabtext6 = '\t\t\t'
        elif len(router[8]) >= 3 and len(router[8]) <= 12:
            tabtext6 = '\t\t'
        elif len(router[8]) > 12 and len(router[8]) <= 20:
            tabtext6 = '\t'
        else:
            tabtext6 = '\t\t'
            temptext = router[8] # The text is truncated to allow it to fit onto the screen
            router[8] = temptext[:10]

        # AFTER POE router[12] - tabtext7
        tabtext7 = '\t'
        
        # AFTER FLASH router[7] - tabtext9
        tabtext9 = '\t'
        
        # AFTER RAM router[30] - tabtext8
        if len(router[30]) < 3:
            tabtext8 = '\t'
        elif len(router[30]) >= 3 and len(router[30]) <= 12:
            tabtext8 = '\t'
        else:
            tabtext8 = '\t'

        # [0]   SKU
        # [1]   Make e.g. Cisco
        # [2]   Series
        # [3]   Model
        # [7]   IOS
        # [8]   Base
        # [12]  POE Wattage
        # [30]  RAM Max
        # [32]  Flash Max
        # [51]  Price

        if select_number < 10:
            text0 = '00' + str(select_number) + ' -'
        elif select_number >= 10 and select_number < 100:
            text0 = '0' + str(select_number) + ' -'
        else:
            text0 = '' + str(select_number) + ' -'
            
        print(text0,router[0],tabtext1,router[1],tabtext2,router[2],tabtext3,router[3],tabtext4,router[7],tabtext5,router[8],tabtext6,router[12],tabtext7,router[30],tabtext8,router[32],tabtext9,router[51])

        select_number += 1

#002
# Select Router from a list



def select_router(display_router_table):

    print('\nSelect device for more information: -\n')
    select_number = 0
    tabtext = '\t\t\t'

    for router in display_router_table:

        # [0]   SKU
        # [1]   Make e.g. Cisco
        # [2]   Series
        # [3]   Model
        # [7]   IOS
        # [8]   Base
        # [12]  POE Wattage
        # [30]  RAM Max
        # [32]  Flash Max
        # [51]  Price
        # [53]  Router Number

        select_number += 1
        
    display_number = 0
    valid_input = False
    max_number = select_number
    
    while not valid_input:
        try:
            display_number = int(input('\n\nWhich router would you like to select? (ENTER 0 to exit) : '))
            valid_input = True
        except ValueError:
                valid_input = False
                print('Invalid Input!')
                display_number = -1 # This ensures that if an invalid input is entered the user must make the selection again - see IF statement below
        except TypeError:
                valid_input = False
                print('Invalid Input!')
                display_number = -1 # This ensures that if an invalid input is entered the user must make the selection again - see IF statement below

        if (display_number < 0 or display_number > max_number):
                valid_input = False
                print('You must select between 0 and ',max_number)
        else:
                valid_input = True
                
    if display_number == 0:
        return(-1)
    else:
        return display_router_table[display_number-1][53] # Return the correct index number for the router



#003
# Display selected router



def display_selected_router(router_number):
  
    print('\n\nROUTER DETAILS\n______________\n')
     
    print('SKU:\t',device_table[router_number][0])      # [0]   SKU

    # Router
    print('\nROUTER\n')
    
    print('Make:\t',device_table[router_number][1])     # [1]   Make e.g. Cisco
    print('Series:\t',device_table[router_number][2])   # [2]   Series
    print('Model:\t',device_table[router_number][3])    # [3]   Model

    # Type
    print('\nTYPE\n')
                                                        # [4]   Type A
                                                        # [5]   Type B
                                                        # [6]   Type C
    
    print('Type:\t',device_table[router_number][4],' \ ',device_table[router_number][5],' \ ',device_table[router_number][6])

    # Specs
    print('\nSPECS\n')
    
    print('IOS:\t',device_table[router_number][7], end='')         # [7]   IOS
    print('\t\tBASE:\t',device_table[router_number][8], end='')     # [8]   Base
    print('\t\tUSERS:\t',device_table[router_number][9], end='')    # [9]   Users
    print('\t\tSLOTS:\t',device_table[router_number][10])           # [10]  Slots
    print('RU:\t',device_table[router_number][11], end='')      # [11]  Rack Units
    print('\t\tPOE (W):\t',device_table[router_number][12])         # [12]  POE Wattage

    # Ports / Channels / Slots
    print('\nPORTS - CHANNELS - SLOTS\n')
      
    print('LAN ports:\t',device_table[router_number][13], end='')       # [13]  LAN ports
    print('\t\tLAN/TP:\t',device_table[router_number][14], end='')       # [14]  LAN/TP
    print('\t\tWAN Ports:\t',device_table[router_number][15], end='')    # [15]  WAN Ports
    print('\t\tWAN/TP:\t',device_table[router_number][16])               # [16]  WAN/TP
    print('LAN/LAN:\t',device_table[router_number][17], end='')      # [17]  LAN/LAN
    print('\t\tRJ/45:\t',device_table[router_number][18], end='')        # [18]  RJ/45
    print('\t\tSFP:\t',device_table[router_number][19], end='')          # [19]  SFP
    print('\t\tPVDM:\t',device_table[router_number][20])         # [20]  PVDM
    print('\t\tVPN:\t',device_table[router_number][21], end='')          # [21]  VPN
    print('\t\tUSB:\t',device_table[router_number][22], end='')          # [22]  USB
    print('\t\tBRI VOICE:\t',device_table[router_number][23])    # [23]  BRI Voice
    print('FXS:\t',device_table[router_number][24], end='')          # [24]  FXS
    print('\t\tFXO:\t',device_table[router_number][25], end='')          # [25]  FXO
    print('\t\tDSP:\t',device_table[router_number][26])                  # [26]  DSP

    # Performance
    print('\nPERFORMANCE\n')
    
    print('KPPS:\t',device_table[router_number][27], end='')             # [27]  KPPS
    print('\t\tMPPS:\t',device_table[router_number][28])             # [28]  MPPS

    # Memory
    print('\nMEMORY - MB\n')
    
    print('RAM:\t(MIN) ',device_table[router_number][29],' (MAX) ',device_table[router_number][30])   # [29]  RAM Min # [30]  RAM Max
    print('FLASH:\t(MIN) ',device_table[router_number][31],' (MAX) ',device_table[router_number][32]) # [31]  Flash Min # [32]  Flash Max

    # Throughput
    print('Throughput (MBPS):\t(MIN) ',device_table[router_number][33],' (MAX) ',device_table[router_number][34])     # [33]  TP Min # [34]  TP Max
    
    # Maximum Streams / Channels
    print('\nMaximum Streams - Channels\n')
    print('SRST:\t',device_table[router_number][35], end='')        # [35]  SRST
    print('\t\tCUCM:\t',device_table[router_number][36], end='')        # [36]  CUCM
    print('\t\tCCME:\t',device_table[router_number][37], end='')        # [37]  CCME
    print('\t\tCUBE:\t',device_table[router_number][38])        # [38]  CUBE
    print('CUE:\t',device_table[router_number][39], end='')         # [39]  CUE
    print('\t\tTCP:\t',device_table[router_number][40], end='')         # [40]  TCP
    print('\t\tIPSEC:\t',device_table[router_number][41], end='')       # [41]  IPSEC
    print('\t\tT1/E1:\t',device_table[router_number][42])       # [42]  T1/E1

    # Features
    print('\nSecurity:\t',device_table[router_number][43], end='')    # [43]  Security
    print('\t\tVoice:\t',device_table[router_number][44], end='')       # [44]  Voice
    print('\t\tQoS:\t',device_table[router_number][45], end='')         # [45]  QoS
    print('\t\t3G/4G:\t',device_table[router_number][46])       # [46]  3G/4G
    print('GPS:\t',device_table[router_number][47], end='')         # [47]  GPS
    print('\t\tRPS:\t',device_table[router_number][48], end='')         # [48]  RPS
    print('\t\tEXTERNAL:\t',device_table[router_number][49], end='')    # [49]  External
    print('\t\tWIRELESS:\t',device_table[router_number][50])    # [50]  Wireless

    # Price
    print('\n\nPRICE ($):\t',device_table[router_number][51])   # [51]  Price
    print('\nNOTES:\t',device_table[router_number][52])     # [52]  Notes

    # Index
    # [53]  Router Number
   
    option = ''
    valid_input = False

    while not valid_input:
        option = input('\nDo you wish to add this item to your BoM? (Y/N) : ')
        if option == 'Y' or option == 'y' or option == 'YES' or option == 'yes':
            option = 'y'
            valid_input = True
        elif option == 'N' or option == 'n' or option == 'NO' or option == 'no':
            option = 'n'
            valid_input = True
        else:
            print('You must reply Y - YES or N - NO!')

    quantity = 0
    valid_input = False

    if option == 'y':
        while not valid_input:
            try:
                quantity = int(input('How many do you need? : ')) # If the customer wants to add this item to the BoM, enter quantity required
            except ValueError:
                valid_input = False
                print('Invalid Input!')
            except TypeError:
                valid_input = False
                print('Invalid Input!')
            if quantity < 1 or quantity > 100:
                print('You must enter a valid number between 1 - 100')
                valid_input = False
            else:
                valid_input = True

            # Add item to the BoM

            item = []
            item.append(device_table[router_number][1]) # Make
            item.append(device_table[router_number][4]) # Type
            item.append(device_table[router_number][0]) # Product
            item.append(quantity)                         # Quantity
            item.append(device_table[router_number][51]) # Price $
            BoM.append(item)



#004 
# Display list of switches and other devices

    

def display_switches(display_switches_table):

    text0 = '     '
    tabtext1 = ''
    tabtext2 = ''
    tabtext3 = ''
    tabtext4 = ''
    tabtext5 = ''
    tabtext6 = ''
    tabtext7 = ''
    tabtext8 = ''
    tabtext9 = ''
    tabtext10 = ''
    tabtext11 = ''
    tabtext12 = ''
    tabtext13 = ''

    tabtext = ['',
               ' ',
               '  ',
               '   ',
               '    ',
               '     ',
               '      ',
               '       ',
               '        ',
               '         ',
               '          ',
               '           ',
               '            ',
               '             ',
               '              ',
               '               ',
               '                ',
               '                 ',
               '                  ',
               '                   ',
               '                    ',
               '                     '
               ]
    
    # [0] Make
    # [1] Type
    # [2] Layer
    # [3] Base
    # [4] Uplinks
    # [5] Series
    # [6] Product
    # [7] Ports
    # [8] PoE - Usage
    # [9] MBPS - Usage
    # [10] PoE (W) - Capacity
    # [11] MBPS - Capacity
    # [12] Part Code
    # [13] Price $
  
    print('\nSWITCHES\n\n')

    print('\n\n      Make','   Type','      Layer','\t  Base','\t\t Uplinks','\t Series','   Product','\t\t Ports','\t PoE(W)\t MBPS','\t    Part Code','\t\t  Price ($)')
    print('___________________________________________________________________________________________________________________________________________________________\n')

    if len(display_switches_table) < 1:
        print('\n\tNo switches to display')

    select_number = 1
    
    for device in display_switches_table:

        # AFTER MAKE device[0] - tabtext1
        if len(device[0]) < 6:
            tabtext1 = ' '
        elif len(device[0]) >= 6 and len(device[0]) <= 10:
           tabtext1 = '\t'            
        else:
           tabtext1 = ''
        if device[0] == 'MERAKI':
            tabtext1 = ''
            
        # AFTER TYPE device[1] - tabtext2
        if device[1] == 'IP Phone':
            tabtext2 = ' '
        elif len(device[1]) < 4:
            tabtext2 = '\t'
        elif len(device[1]) > 4 and len(device[1]) < 7:
            tabtext2 = '   '
        else:
           tabtext2 = '  '            

        # AFTER LAYER device[2] - tabtext3
        tabtext3_num = 7 - len(device[2])
        tabtext3 = tabtext[tabtext3_num]
        
        # AFTER BASE device[3] - tabtext4
        if len(device[3]) < 7:
            tabtext4 = '\t\t'
        elif len(device[3]) >= 7 and len(device[3]) <= 12:
           tabtext4 = '\t'            
        else:
           tabtext4 = ''
           temptext = device[3]
           device[3] = temptext[:14]

        # AFTER UPLINKS device[4] - tabtext5
        if len(device[4]) < 5:
            tabtext5 = '\t\t'
        elif len(device[4]) >= 5 and len(device[4]) <= 15:
           tabtext5 = '\t'            
        else:
           tabtext5 = '\t'

        # AFTER SERIES device[5] - tabtext6
        if len(device[5]) < 6:
            tabtext6 = '\t  '
        elif len(device[5]) >= 6 and len(device[5]) <= 7:
           tabtext6 = '  '            
        else:
           tabtext6 = ''

        # AFTER PRODUCT device[6] - tabtext7
        if len(device[6]) < 6:
            tabtext7 = '\t\t'
        elif len(device[6]) >= 6 and len(device[6]) < 13:
           tabtext7 = '\t\t'            
        elif len(device[6]) >= 13 and len(device[6]) <= 20:
           tabtext7 = '\t'            
        else:
           tabtext7 = '\t\t'

        # AFTER PORTS device[7] - tabtext8
        if len(str(device[7])) < 5:
            tabtext8 = ' \t'
        elif len(device[7]) >= 5 and len(device[7]) <= 10:
           tabtext8 = ' \t'            
        else:
           tabtext8 = ''

        # POE USAGE OR CAPACITY - device[8] & device[10] - display_poe
        if device[8] == '':
            display_poe = device[10]
        else:
            display_poe = device[8]
            
        # AFTER POE - display_poe - tabtext9
        if len(str(display_poe)) <= 1:
            tabtext9 = '\t'
        elif len(str(display_poe)) > 1 and len(str(display_poe)) < 5:
            tabtext9 = ' \t'
        elif len(str(display_poe)) >= 5 and len(str(display_poe)) <= 10:
           tabtext9 = ' '            
        else:
           tabtext9 = ''

        # MBPS USAGE OR CAPACITY - device[9] & device[11] - display_mbps
        if device[9] == '':
            display_mbps = device[11]
        else:
            display_mbps = device[9]

        # AFTER MBPS - display_mbps - tabtext10
        if len(str(display_mbps)) <= 1:
            tabtext10 = '\t\t\t   '
        elif len(str(display_mbps)) > 1 and len(str(display_mbps)) < 5:
            tabtext10 = '\t   '
        elif len(str(display_mbps)) == 5:
           tabtext10 = '    '
        elif len(str(display_mbps)) == 6:
           tabtext10 = '   '            
        elif len(str(display_mbps)) == 7:
           tabtext10 = '  '            
        else:
           tabtext10 = ''

        # AFTER POE CAPACITY - device[10] - tabtext11
        if len(device[10]) < 5:
            tabtext11 = '10: \t'
        elif len(device[10]) >= 5 and len(device[10]) <= 10:
           tabtext11 = '10: \t\t'            
        else:
           tabtext11 = '10: \t\t\t'

        # AFTER MBPS CAPACITY - device[11] - tabtext12
        if len(device[11]) < 8:
            tabtext12 = '\t'
        elif len(device[11]) >= 8 and len(device[11]) <= 10:
           tabtext12 = '  '            
        else:
           tabtext12 = ''

        # AFTER PART CODE - device[12] - tabtext13
        if len(device[12]) < 3:
           tabtext13 = '\t\t\t '            
        elif len(device[12]) >= 3 and len(device[12]) < 11:
            tabtext13 = '\t\t '
        elif len(device[12]) >= 11 and len(device[12]) <= 18:
           tabtext13 = '\t '            
        else:
           tabtext13 = ' '

        # [0] Make
        # [1] Type
        # [2] Layer
        # [3] Base
        # [4] Uplinks
        # [5] Series
        # [6] Product
        # [7] Ports
        # [8] PoE - Usage
        # [9] MBPS - Usage
        # [10] PoE (W) - Capacity
        # [11] MBPS - Capacity
        # [12] Part Code
        # [13] Price $

        if select_number < 10:
            text0 = '00' + str(select_number) + ' -'
        elif select_number >= 10 and select_number < 100:
            text0 = '0' + str(select_number) + ' -'
        else:
            text0 = '' + str(select_number) + ' -'

        print(text0,device[0],tabtext1,device[1],tabtext2,device[2],tabtext3,device[3],tabtext4,device[4],tabtext5,device[5],tabtext6,device[6],tabtext7,device[7],tabtext8,display_poe,tabtext9,display_mbps,tabtext10,device[12],tabtext13,device[13])

        select_number += 1


#005
# Select switch or other device from a list



def select_switch(display_switches_table):

    print('\nSelect device for more information: -\n')
    select_number = 0
    
    for device in display_switches_table:

        # [0] Make
        # [1] Type
        # [2] Layer
        # [3] Base
        # [4] Uplinks
        # [5] Series
        # [6] Product
        # [7] Ports
        # [8] PoE - Usage
        # [9] MBPS - Usage
        # [10] PoE (W) - Capacity
        # [11] MBPS - Capacity
        # [12] Part Code
        # [13] Price $
        # [14] Device Number

        select_number += 1
        
    display_number = 0
    valid_input = False
    max_number = select_number
    
    while not valid_input:
        try:
            display_number = int(input('\n\nWhich device would you like to select? (ENTER 0 to exit) : '))
        except ValueError:
            valid_input = False
            print('Invalid Input!')
            display_number = -1 # This ensures that if an invalid input is entered the user must make the selection again - see IF statement below
        except TypeError:
            valid_input = False
            print('Invalid Input!')
            display_number = -1 # This ensures that if an invalid input is entered the user must make the selection again - see IF statement below
            
        if (display_number < 0 or display_number > max_number):
            valid_input = False
            print('You must select between 0 and ',max_number)
        else:
            valid_input = True

    if display_number == 0:
        return(-1)
    else:
        return display_switches_table[display_number-1][14]



#006
# Display selected switch or other device



def display_selected_switch(device_number):

        # [0] Make
        # [1] Type
        # [2] Layer
        # [3] Base
        # [4] Uplinks
        # [5] Series
        # [6] Product
        # [7] Ports
        # [8] PoE - Usage
        # [9] MBPS - Usage
        # [10] PoE (W) - Capacity
        # [11] MBPS - Capacity
        # [12] Part Code
        # [13] Price $
        # [14] Device Number

    print('\n\nSWITCH \ DEVICE DETAILS\n_______________________\n')

    # [0] Make
    print('MAKE:\t\t\t\t',device_table_2[device_number][0])
    # [1] Type
    print('TYPE:\t\t\t\t',device_table_2[device_number][1])
    # [2] Layer
    print('LAYER:\t\t\t\t',device_table_2[device_number][2])
    # [3] Base
    print('BASE:\t\t\t\t',device_table_2[device_number][3])
    # [4] Uplinks
    print('UPLINKS:\t\t\t',device_table_2[device_number][4])
    # [5] Series
    print('SERIES:\t\t\t\t',device_table_2[device_number][5])
    # [6] Product
    print('PRODUCT:\t\t\t',device_table_2[device_number][6])
    # [7] Ports
    print('PORTS:\t\t\t\t',device_table_2[device_number][7])
    # [8] PoE - Usage
    print('PoE - Usage:\t\t\t',device_table_2[device_number][8])
    # [9] MBPS - Usage
    print('MBPS - Usage:\t\t\t',device_table_2[device_number][9])
    # [10] PoE (W) - Capacity
    print('PoE (W) - Capacity:\t\t',device_table_2[device_number][10])
    # [11] MBPS - Capacity
    print('MBPS - Capacity:\t\t',device_table_2[device_number][11])
    # [12] Part Code
    print('Part Code:\t\t\t',device_table_2[device_number][12])
    # [13] Price $
    print('Price $:\t\t\t',device_table_2[device_number][13])

    option = ''
    valid_input = False

    while not valid_input:
        option = input('\nDo you wish to add this item to your BoM? (Y/N) : ')
        if option == 'Y' or option == 'y' or option == 'YES' or option == 'yes':
            option = 'y'
            valid_input = True
        elif option == 'N' or option == 'n' or option == 'NO' or option == 'no':
            option = 'n'
            valid_input = True
        else:
            print('You must reply Y - YES or N - NO!')

    quantity = 0
    valid_input = False

    if option == 'y':
        while not valid_input:
            try:
                quantity = int(input('How many do you need? : ')) # If the customer wants to add this item to the BoM, enter quantity required
            except ValueError:
                valid_input = False
                print('Invalid Input!')
            except TypeError:
                valid_input = False
                print('Invalid Input!')
            if quantity < 1 or quantity > 100:
                print('You must enter a valid number between 1 - 100')
                valid_input = False
            else:
                valid_input = True

            # Add item to the BoM

            item = []
            item.append(device_table_2[device_number][0]) # Make
            item.append(device_table_2[device_number][1]) # Type
            item.append(device_table_2[device_number][6]) # Product
            item.append(quantity)                         # Quantity
            item.append(device_table_2[device_number][13]) # Price $
            BoM.append(item)



#007
# (Numbers) - Obtain filter specifications and enter results in a dictionary



def filter_device_range(filter_specs, question_text_min, variable_min, question_text_max, variable_max):
    
        # Specs
            # [9]   Users <<
            # [10]  Slots <<
            # [11]  Rack Units <<
            # [12]  POE Wattage <<

        # Ports / Channels / Slots
            # [13]  LAN ports <<
            # [15]  WAN Ports <<
            # [17]  LAN/LAN <<
            # [18]  RJ/45 <<
            # [19]  SFP <<
            # [20]  PVDM <<
            # [21]  VPN <<
            # [22]  USB <<
            # [23]  BRI Voice <<
            # [24]  FXS <<
            # [25]  FXO <<
            # [26]  DSP <<

        # Performance
            # [27]  KPPS <<
            # [28]  MPPS <<

        # Memory
            # [29]  RAM Min (MB) <<
            # [30]  RAM Max (MB) <<
            # [31]  Flash Min (MB) <<
            # [32]  Flash Max (MB) <<

        # Throughput
            # [33]  TP Min (MBPS) <<
            # [34]  TP Max (MBPS) <<

        # Maximum Streams / Channels
            # [35]  SRST <<
            # [36]  CUCM <<
            # [37]  CCME <<
            # [38]  CUBE <<
            # [39]  CUE <<
            # [40]  TCP <<
            # [41]  IPSEC <<
            # [42]  T1/E1 <<

        # Features
            # [43]  Security <<
            # [44]  Voice <<
            # [45]  QoS <<
            # [46]  3G/4G <<
            # [47]  GPS <<
            # [48]  RPS <<
            # [49]  External <<
            # [50]  Wireless <<

        # [51]  Price $ <<

        # Index

        # [53]  Router Number

    # Enter Lower range

    valid_input = False

    while not valid_input:
        filter_min = input(question_text_min)
        if filter_min == '':
            filter_min = '0'
        valid_input = True
        try:
            filter_specs[variable_min] = int(filter_min)
        except ValueError:
            valid_input = False
            print('Invalid Input!')
            filter_min = 0
        except TypeError:
            valid_input = False
            print('Invalid Input!')
            filter_min = 0
        if (int(filter_min) < 0 or int(filter_min) > 9999999999):
            valid_input = False
            print('Number must be between 0 - 9999999999')
            

    valid_input = False

    # Enter Upper range
    
    while not valid_input:
        filter_max = input(question_text_max)
        if filter_max == '':
            filter_max = '9999999999'
        valid_input = True
        try:
            filter_specs[variable_max] = int(filter_max)
        except ValueError:
            filter_max = 9999999999
            valid_input = False
            print('Invalid Input!')
        except TypeError:
            filter_max = 9999999999
            valid_input = False
            print('Invalid Input!')
        if (int(filter_max) < 0 or int(filter_max) > 9999999999):
            valid_input = False
            print('Number must be between 0 - 9999999999')
        elif int(filter_max) < int(filter_min):
            valid_input = False
            print('The Minimum cannot be more than the maximum!')

    return(filter_specs)



#008
# (Yes/No) - Obtain filter specifications and enter results in a dictionary



def filter_device_YN(question_text, question_variable):

    valid_input = False
    filter_string = ''
    YN_reply = ''
    
    while not valid_input:
        filter_string = input(question_text)
        filter_string.lower() # Turn into lowercase
        if filter_string == '':
            YN_reply = 'n'
            valid_input = True
        elif filter_string == 'y' or filter_string == 'n':
            valid_input = True
            YN_reply = filter_string
        else:
            valid_input = False
            print('You must reply Y - YES or N - NO!')
    return(YN_reply)



#009
# (Numbers) Obtain filter specifications and enter results in a dictionary



def filter_device_range_2(filter_specs_2,question_text_min, variable_min, question_text_max, variable_max):
       
    # [0] Make
    # [1] Type
    # [2] Layer
    # [3] Base
    # [4] Uplinks
    # [5] Series
    # [6] Product
    # [7] Ports
    # [8] PoE Usage
    # [9] MBPS - Usage
    # [10] PoE (W) - Capacity
    # [11] MBPS - Capacity
    # [12] Part Code
    # [13] Price $

    valid_input = False

    while not valid_input:
        filter_min = input(question_text_min)
        if filter_min == '':
            filter_min = '0'
        valid_input = True
        try:
            filter_specs_2[variable_min] = int(filter_min)
        except ValueError:
            valid_input = False
            print('Invalid Input!')
            filter_min = 0
        except TypeError:
            valid_input = False
            print('Invalid Input!')
            filter_min = 0
        if (int(filter_min) < 0 or int(filter_min) > 9999999999):
            valid_input = False
            print('Number must be between 0 - 9999999999')

    valid_input = False
    enter_min = 0
    enter_max = 9999

    # Enter Upper range
    
    while not valid_input:
        filter_max = input(question_text_max)
        if filter_max == '':
            filter_max = '9999999999'
        valid_input = True
        try:
            filter_specs_2[variable_max] = int(filter_max)
        except ValueError:
            valid_input = False
            print('Invalid Input!')
            filter_max = 9999
        except TypeError:
            valid_input = False
            print('Invalid Input!')
            filter_max = 9999
        if (int(filter_max) < 0 or int(filter_max) > 9999999999):
            valid_input = False
            print('Number must be between 0 - 9999999999')
        elif int(filter_max) < int(filter_min):
            valid_input = False
            print('The Minimum cannot be more than the maximum!')

    return(filter_specs_2)



#010
# Select a filter option from a given list



def filter_device_selection(filter_text,option,filter_list):

    print(filter_text)
    print('Select an option from the following list')
    print(filter_list)

    valid_input = False
    
    while not valid_input:
        input_selection = input('ENTER SELECTION: ')
        input_selection = input_selection.upper() # Data needs to be converted into uppercase for effective comparison
        if input_selection == '':
            input_selection = 'ALL' # Default is ALL
        if input_selection in filter_list:
            valid_input = True
            return(input_selection)
        else:
            print('YOU MUST SELECT AN OPTION FROM THE LIST!!')



#011
# Filter the routers database
    


def filter_routers_1():

    print('\nFILTER DATABASE - ROUTERS\n__________________________________________')

    print('\nJust press ENTER for all devices')

    filter_specs = {

        # Specs
        'o9_min' : 0,           # [9]   Users <<
        'o9_max' : 9999999999,
        'o10_min' : 0,          # [10]  Slots <<
        'o10_max' : 9999999999,
        'o11_min' : 0,          # [11]  Rack Units <<
        'o11_max' : 9999999999,
        'o12_min' : 0,
        'o12_max' : 9999999999, # [12]  POE Wattage <<
        
        # Ports / Channels / Slots
	'o13_min' : 0,          # [13]  LAN ports <<
        'o13_max' : 9999999999,
        'o15_min' : 0,          # [15]  WAN Ports <<
        'o15_max' : 9999999999,
        'o17_min' : 0,          # [17]  LAN/LAN <<
        'o17_max' : 9999999999,
        'o18_min' : 0,          # [18]  RJ/45 <<
        'o18_max' : 9999999999, 
        'o19_min' : 0,          # [19]  SFP <<
        'o19_max' : 9999999999,
        'o20_min' : 0,          # [20]  PVDM <<
        'o20_max' : 9999999999,
        'o21_min' : 0,          # [21]  VPN <<
        'o21_max' : 9999999999,
        'o22_min' : 0,          # [22]  USB <<
        'o22_max' : 9999999999,
        'o23_min' : 0,          # [23]  BRI Voice <<
        'o23_max' : 9999999999,
        'o24_min' : 0,          # [24]  FXS <<
        'o24_max' : 9999999999,
        'o25_min' : 0,          # [25]  FXO <<
        'o25_max' : 9999999999,
        'o26_min' : 0,          # [26]  DSP <<
        'o26_max' : 9999999999,
        
        # Performance
        'o27_min' : 0,          # [27]  KPPS <<
        'o27_max' : 9999999999,
        'o28_min' : 0,          # [28]  MPPS <<
        'o28_max' : 9999999999,
        
        # Memory
        'o29_min' : 0,          # [29]  RAM Min (MB) <<
        'o30_max' : 9999999999, # [30]  RAM Max (MB) <<
        'o31_min' : 0,          # [31]  Flash Min (MB) <<
        'o32_max' : 9999999999, # [32]  Flash Max (MB) <<
        
        # Throughput
        'o33_min' : 0,          # [33]  TP Min (MBPS) <<
        'o34_max' : 9999999999, # [34]  TP Max (MBPS) <<
        
        # Maximum Streams / Channels
        'o35_min' : 0,          # [35]  SRST <<
        'o35_max' : 9999999999,
        'o36_min' : 0,          # [36]  CUCM <<
        'o36_max' : 9999999999,
        'o37_min' : 0,          # [37]  CCME <<
        'o37_max' : 9999999999,
        'o38_min' : 0,          # [38]  CUBE <<
        'o38_max' : 9999999999,
        'o39_min' : 0,          # [39]  CUE <<
        'o39_max' : 9999999999,
        'o40_min' : 0,          # [40]  TCP <<
        'o40_max' : 9999999999,
        'o41_min' : 0,          # [41]  IPSEC <<
        'o41_max' : 9999999999,
        'o42_min' : 0,          # [42]  T1/E1 <<
        'o42_max' : 9999999999,
        
        # Features
        'o43' : 'y',    # [43]  Security <<
        'o44' : 'y',    # [44]  Voice <<
        'o45' : 'y',    # [45]  QoS <<
        'o46' : 'y',    # [46]  3G/4G <<
        'o47' : 'y',    # [47]  GPS <<
        'o48' : 'y',    # [48]  RPS <<
        'o49' : 'y',    # [49]  External <<
        'o50' : 'y',    # [50]  Wireless <<
        
         # [51]  Price $ <<
        'o51_min' : 0,
        'o51_max' : 9999999999
    }

        # filter_device[]

    print('\n\t - SPECIFICATIONS -\n')
        
        # Specs
            # [9]   Users <<
            # [10]  Slots <<
            # [11]  Rack Units <<
            # [12]  POE Wattage <<

    filter_specs = filter_device_range(filter_specs,'MINUMUM USERS: ', 'o9_min', 'MAXIMUM USERS: ', 'o9_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM SLOTS: ', 'o10_min', 'MAXIMUM SLOTS: ', 'o10_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM RACK UNITS: ', 'o11_min', 'MAXIMUM RACK UNITS: ', 'o11_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM POE(W): ', 'o12_min', 'MAXIMUM POE(W): ', 'o12_max')

    print('\n\t - PORTS - CHANNELS / SLOTS -\n')
        
        # Ports / Channels / Slots
            # [13]  LAN ports <<
            # [15]  WAN Ports <<
            # [17]  LAN/LAN <<
            # [18]  RJ/45 <<
            # [19]  SFP <<
            # [20]  PVDM <<
            # [21]  VPN <<
            # [22]  USB <<
            # [23]  BRI Voice <<
            # [24]  FXS <<
            # [25]  FXO <<
            # [26]  DSP <<

    filter_specs = filter_device_range(filter_specs,'MINUMUM LAN PORTS: ', 'o13_min', 'MAXIMUM LAN PORTS: ', 'o13_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM WAN PORTS: ', 'o15_min', 'MAXIMUM WAN PORTS: ', 'o15_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM LAN\\WAN: ', 'o17_min', 'MAXIMUM LAN\\WAN: ', 'o17_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM RJ45: ', 'o18_min', 'MAXIMUM RJ45: ', 'o18_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM SFP: ', 'o19_min', 'MAXIMUM SFP: ', 'o19_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM PVDM: ', 'o20_min', 'MAXIMUM PVDM: ', 'o20_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM VPN: ', 'o21_min', 'MAXIMUM VPN: ', 'o21_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM USB: ', 'o22_min', 'MAXIMUM USB: ', 'o22_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM BRI VOICE: ', 'o23_min', 'MAXIMUM BRI VOICE: ', 'o23_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM FXS: ', 'o24_min', 'MAXIMUM FXS: ', 'o24_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM FXO: ', 'o25_min', 'MAXIMUM FXO: ', 'o25_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM DSP: ', 'o26_min', 'MAXIMUM DSP: ', 'o26_max')

    print('\n\t - PERFORMANCE\n')
        
        # Performance
            # [27]  KPPS <<
            # [28]  MPPS <<

    filter_specs = filter_device_range(filter_specs,'MINUMUM KPPS: ', 'o27_min', 'MAXIMUM KPPS: ', 'o27_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM MPPS: ', 'o28_min', 'MAXIMUM MPPS: ', 'o28_max')

    print('\n\t - MEMORY - (MB)\n')
        
        # Memory
            # [29]  RAM Min <<
            # [30]  RAM Max <<
            # [31]  Flash Min <<
            # [32]  Flash Max <<

    filter_specs = filter_device_range(filter_specs,'MINUMUM RAM (MB): ', 'o29_min', 'MAXIMUM RAM (MB): ', 'o30_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM FLASH (MB): ', 'o31_min', 'MAXIMUM FLASH (MB): ', 'o32_max')

    print('\n\t - THROUGHPUT - MBPS\n')
        
        # Throughput
            # [33]  TP Min <<
            # [34]  TP Max <<

    filter_specs = filter_device_range(filter_specs,'MINUMUM THROUGHPUT (MBPS): ', 'o33_min', 'MAXIMUM THROUGHPUT (MBPS): ', 'o34_max')

    print('\n\tMAXIMUM STREAMS AND CHANNELS\n')
        
        # Maximum Streams / Channels
            # [35]  SRST <<
            # [36]  CUCM <<
            # [37]  CCME <<
            # [38]  CUBE <<
            # [39]  CUE <<
            # [40]  TCP <<
            # [41]  IPSEC <<
            # [42]  T1/E1 <<

    filter_specs = filter_device_range(filter_specs,'MINUMUM SRST: ', 'o35_min', 'MAXIMUM SRST: ', 'o35_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM CUCM: ', 'o36_min', 'MAXIMUM CUCM: ', 'o36_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM CCME: ', 'o37_min', 'MAXIMUM CCME: ', 'o37_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM CUBE: ', 'o38_min', 'MAXIMUM CUBE: ', 'o38_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM CUE: ', 'o39_min', 'MAXIMUM CUE: ', 'o39_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM TCP: ', 'o40_min', 'MAXIMUM TCP: ', 'o40_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM IPSEC: ', 'o41_min', 'MAXIMUM IPSEC: ', 'o41_max')
    filter_specs = filter_device_range(filter_specs,'MINUMUM T1/E1: ', 'o42_min', 'MAXIMUM T1/E1: ', 'o42_max')

    print('\n\t - FEATURES -\n')
        
        # Features
            # [43]  Security <<
            # [44]  Voice <<
            # [45]  QoS <<
            # [46]  3G/4G <<
            # [47]  GPS <<
            # [48]  RPS <<
            # [49]  External <<
            # [50]  Wireless <<

    filter_specs['o43'] = filter_device_YN('SECURITY (Y/N): ', 'o43')
    filter_specs['o44'] = filter_device_YN('VOICE (Y/N): ', 'o44')
    filter_specs['o45'] = filter_device_YN('QOS (Y/N): ', 'o45')
    filter_specs['o46'] = filter_device_YN('3G/4G (Y/N): ', 'o46')
    filter_specs['o47'] = filter_device_YN('GPS (Y/N): ', 'o47')
    filter_specs['o48'] = filter_device_YN('RPS (Y/N): ', 'o48')
    filter_specs['o49'] = filter_device_YN('EXTERNAL (Y/N): ', 'o49')
    filter_specs['o50'] = filter_device_YN('WIRELESS (Y/N): ', 'o50')

    print('\n\t - PRICE $ -\n')
        
         # [51]  Price <<

    filter_specs = filter_device_range(filter_specs,'MINUMUM PRICE $: ', 'o51_min', 'MAXIMUM PRICE $: ', 'o51_max')

        # Index
        
        # [53]  Router Number

    return(filter_specs)

        

#012
# After all the specifications have been entered, display a list of routers with the selected criteria: -



def filter_routers_2(filter_specs):

    filtered_routers = []

    for device in device_table:
        match = False

        # Go through each criteria in turn, and check if the router meets the desired specification
                
        # Specs

        if int(device[9]) < filter_specs['o9_min']: # [9]   Users
            # ('STEP 9 - ',device[9],filter_specs['o9_min'],filter_specs['o9_max'])
            match = False

        elif int(device[9]) > filter_specs['o9_max']: # [9]   Users
            # ('STEP 9 - ',device[9],filter_specs['o9_min'],filter_specs['o9_max'])
            match = False
            
        elif (int(device[10]) < filter_specs['o10_min']):  # [10]  Slots
            # ('STEP 10 - ',device[10],filter_specs['o10_min'],filter_specs['o10_max'])        
            match = False

        elif (int(device[10]) > filter_specs['o10_max']):  # [10]  Slots
            # ('STEP 10 - ',device[10],filter_specs['o10_min'],filter_specs['o10_max'])        
            match = False
                                
        elif (int(device[11]) < filter_specs['o11_min']):  # [11]  Rack Units <<
            # ('STEP 11 - ',device[11],filter_specs['o11_min'],filter_specs['o11_max'])
            match = False

        elif (int(device[11]) > filter_specs['o11_max']):  # [11]  Rack Units <<
            # ('STEP 11 - ',device[11],filter_specs['o11_min'],filter_specs['o11_max'])
            match = False

        elif (int(device[12]) < filter_specs['o12_min']):  # [12]  POE Wattage <<
            # ('STEP 12 - ',device[12],filter_specs['o12_min'],filter_specs['o12_max'])
            match = False

        elif (int(device[12]) > filter_specs['o12_max']): # [12]  POE Wattage <<
            # ('STEP 12 - ',device[12],filter_specs['o12_min'],filter_specs['o12_max'])
            match = False            

        # Ports / Channels / Slots

        elif (int(device[13]) < filter_specs['o13_min']): # [13]  LAN ports <<
            # ('STEP 13 - ',device[13],filter_specs['o13_min'],filter_specs['o13_max'])
            match = False

        elif (int(device[13]) > filter_specs['o13_max']): # [13]  LAN ports <<
            # ('STEP 13 - ',device[13],filter_specs['o13_min'],filter_specs['o13_max'])
            match = False
            
        elif (int(device[15]) < filter_specs['o15_min']): # [15]  WAN Ports <<
            # ('STEP 15 - ',device[15],filter_specs['o15_min'],filter_specs['o15_max'])
            match = False

        elif (int(device[15]) > filter_specs['o15_max']):  # [15]  WAN Ports <<
            # ('STEP 15 - ',device[15],filter_specs['o15_min'],filter_specs['o15_max'])
            match = False

        elif (int(device[17]) < filter_specs['o17_min']): # [17]  LAN/LAN <<
            # ('STEP 17 - ',device[17],filter_specs['o17_min'],filter_specs['o17_max'])
            match = False

        elif (int(device[17]) > filter_specs['o17_max']): # [17]  LAN/LAN <<
            # ('STEP 17 - ',device[17],filter_specs['o17_min'],filter_specs['o17_max'])
            match = False
    
        elif (int(device[18]) < filter_specs['o18_min']): # [18]  RJ/45 <<
            # ('STEP 18 - ',device[18],filter_specs['o18_min'],filter_specs['o18_max'])
            match = False
            
        elif (int(device[18]) > filter_specs['o18_max']): # [18]  RJ/45 <<
            # ('STEP 18 - ',device[18],filter_specs['o18_min'],filter_specs['o18_max'])
            match = False

        elif (int(device[19]) < filter_specs['o19_min']): # [19]  SFP <<
            # ('STEP 19 - ',device[19],filter_specs['o19_min'],filter_specs['o19_max'])
            match = False

        elif (int(device[19]) > filter_specs['o19_max']): # [19]  SFP <<
            # ('STEP 19 - ',device[19],filter_specs['o19_min'],filter_specs['o19_max'])
            match = False

        elif (int(device[20]) < filter_specs['o20_min']): # [20]  PVDM <<
            # ('STEP 20 - ',device[20],filter_specs['o20_min'],filter_specs['o20_max'])
            match = False    

        elif (int(device[20]) > filter_specs['o20_max']): # [20]  PVDM <<
            # ('STEP 20 - ',device[20],filter_specs['o20_min'],filter_specs['o20_max'])
            match = False    

        elif (int(device[21]) < filter_specs['o21_min']): # [21]  VPN <<
            # ('STEP 21 - ',device[21],filter_specs['o21_min'],filter_specs['o21_max'])
            match = False

        elif (int(device[21]) > filter_specs['o21_max']):  # [21]  VPN <<
            # ('STEP 21 - ',device[21],filter_specs['o21_min'],filter_specs['o21_max'])
            match = False
   
        elif (int(device[22]) < filter_specs['o22_min']):  # [22]  USB <<
            # ('STEP 22 - ',device[22],filter_specs['o22_min'],filter_specs['o22_max'])
            match = False

        elif (int(device[22]) > filter_specs['o22_max']):  # [22]  USB <<
            # ('STEP 22 - ',device[22],filter_specs['o22_min'],filter_specs['o22_max'])
            match = False
            
        elif (int(device[23]) < filter_specs['o23_min']):  # [23]  BRI Voice <<
            # ('STEP 23 - ',device[23],filter_specs['o23_min'],filter_specs['o23_max'])
            match = False

        elif (int(device[23]) > filter_specs['o23_max']):  # [23]  BRI Voice <<
            # ('STEP 23 - ',device[23],filter_specs['o23_min'],filter_specs['o23_max'])
            match = False

        elif (int(device[24]) < filter_specs['o24_min']): # [24]  FXS <<
            # ('STEP 24 - ',device[24],filter_specs['o24_min'],filter_specs['o24_max'])
            match = False

        elif (int(device[24]) > filter_specs['o24_max']):  # [24]  FXS <<
            # ('STEP 24 - ',device[24],filter_specs['o24_min'],filter_specs['o24_max'])
            match = False
        
        elif (int(device[25]) < filter_specs['o25_min']):  # [25]  FXO <<
            # ('STEP 25 - ',device[25],filter_specs['o25_min'],filter_specs['o25_max'])
            match = False

        elif (int(device[25]) > filter_specs['o25_max']):  # [25]  FXO <<
            # ('STEP 25 - ',device[25],filter_specs['o25_min'],filter_specs['o25_max'])
            match = False

        elif (int(device[26]) < int(filter_specs['o26_min'])):# [26]  DSP <<
            # ('STEP 26 - ',device[26],filter_specs['o26_min'],filter_specs['o26_max'])
            match = False

        elif (int(device[26]) > int(filter_specs['o26_max'])): # [26]  DSP <<
            # ('STEP 26 - ',device[26],filter_specs['o26_min'],filter_specs['o26_max'])
            match = False
    
        # Performance

        elif (int(device[27]) < int(filter_specs['o27_min'])):  # [27]  KPPS <<
            # ('STEP 27 - ',device[27],filter_specs['o27_min'],filter_specs['o27_max'])
            match = False

        elif (int(device[27]) > int(filter_specs['o27_max'])): # [27]  KPPS <<
            # ('STEP 27 - ',device[27],filter_specs['o27_min'],filter_specs['o27_max'])
            match = False
        
        # [28]  MPPS <<

        elif float(device[28]) < filter_specs['o28_min']:
            # ('STEP 28 - ',device[28],filter_specs['o28_min'],filter_specs['o28_max'])
            match = False

        elif float(device[28]) > filter_specs['o28_max']:
            # ('STEP 28 - ',device[28],filter_specs['o28_min'],filter_specs['o28_max'])
            match = False
                                                                    
        # Memory - MB

        # [29]  RAM Min & [30]  RAM Max <<

        elif (int(device[29]) < int(filter_specs['o29_min'])):
            # ('STEP 29 - ',device[29],filter_specs['o29_min'],filter_specs['o30_max'])
            match = False

        elif (int(device[30]) > int(filter_specs['o30_max'])):
            # ('STEP 30 - ',device[30],filter_specs['o29_min'],filter_specs['o30_max'])
            match = False

        # [31]  Flash Min & # [32]  Flash Max <<

        elif (int(device[31]) < int(filter_specs['o31_min'])):
            # ('STEP 31 - ',device[31],filter_specs['o31_min'],filter_specs['o32_max'])
            match = False

        elif (int(device[32]) > int(filter_specs['o32_max'])):
            # ('STEP 32 - ',device[32],filter_specs['o31_min'],filter_specs['o32_max'])
            match = False
                                                                                                                                                                                
        # Throughput - MBPS

        # [33]  TP Min <<
        # [34]  TP Max <<

        elif float(device[33]) < filter_specs['o33_min']:
            # ('STEP 33 & 34 - ',device[33],device[34],filter_specs['o33_min'],filter_specs['o34_max'])
            match = False
                                                                                                

        elif float(device[33]) > filter_specs['o34_max']:
            # ('STEP 33 & 34 - ',device[33],device[34],filter_specs['o33_min'],filter_specs['o34_max'])
            match = False
                                                                                                
        # Maximum Streams / Channels

        # [35]  SRST <<

        elif (int(device[35]) < int(filter_specs['o35_min'])):
            # ('STEP 35 - ',device[35],filter_specs['o35_min'],filter_specs['o35_max'])
            match = False

        elif (int(device[35]) > int(filter_specs['o35_max'])):
            # ('STEP 35 - ',device[35],filter_specs['o35_min'],filter_specs['o35_max'])
            match = False

        # [36]  CUCM <<

        elif (int(device[36]) < int(filter_specs['o36_min'])): 
            # ('STEP 36 - ',device[36],filter_specs['o36_min'],filter_specs['o36_max'])
            match = False

        elif (int(device[36]) > int(filter_specs['o36_max'])): 
            # ('STEP 36 - ',device[36],filter_specs['o36_min'],filter_specs['o36_max'])
            match = False
            
        # [37]  CCME <<

        elif (int(device[37]) < int(filter_specs['o37_min'])):
            # ('STEP 37 - ',device[37],filter_specs['o37_min'],filter_specs['o37_max'])
            match = False

        elif (int(device[37]) > int(filter_specs['o37_max'])):
            # ('STEP 37 - ',device[37],filter_specs['o37_min'],filter_specs['o37_max'])
            match = False
                                                                                                           
        # [38]  CUBE <<

        elif (int(device[38]) < int(filter_specs['o38_min'])): 
            # ('STEP 38 - ',device[38],filter_specs['o38_min'],filter_specs['o38_max'])
            match = False

        elif (int(device[38]) > int(filter_specs['o38_max'])):
            # ('STEP 38 - ',device[38],filter_specs['o38_min'],filter_specs['o38_max'])
            match = False

        # [39]  CUE <<

        elif (int(device[39]) < int(filter_specs['o39_min'])):
            # ('STEP 39 - ',device[39],filter_specs['o39_min'],filter_specs['o39_max'])
            match = False

        elif (int(device[39]) > int(filter_specs['o39_max'])):
            # ('STEP 39 - ',device[39],filter_specs['o39_min'],filter_specs['o39_max'])
            match = False
            
        # [40]  TCP <<

        elif (int(device[40]) < int(filter_specs['o40_min'])):
            # ('STEP 40 - ',device[40],filter_specs['o40_min'],filter_specs['o40_max'])
            match = False

        elif (int(device[40]) > int(filter_specs['o40_max'])):
            # ('STEP 40 - ',device[40],filter_specs['o40_min'],filter_specs['o40_max'])
            match = False
                                                                                                                        
        # [41]  IPSEC <<

        elif (int(device[41]) < int(filter_specs['o41_min'])):
            # ('STEP 41 - ',device[41],filter_specs['o41_min'],filter_specs['o41_max'])
            match = False


        elif (int(device[41]) > int(filter_specs['o41_max'])):
            # ('STEP 41 - ',device[41],filter_specs['o41_min'],filter_specs['o41_max'])
            match = False
                                                                                                                            
        # [42]  T1/E1 <<

        elif (int(device[42]) < int(filter_specs['o42_min'])):
            # ('STEP 42 - ',device[42],filter_specs['o42_min'],filter_specs['o42_max'])
            match = False

        elif (int(device[42]) > int(filter_specs['o42_max'])):
            # ('STEP 42 - ',device[42],filter_specs['o42_min'],filter_specs['o42_max'])
            match = False
                                                                                                                                
        # Features

        elif filter_specs['o43'] == 'y' and device[43] != 'YES': # [43]  Security <<
            # ('STEP 43 - ',device[43],filter_specs['o43'])
            match = False

        elif filter_specs['o44'] == 'y' and device[44] != 'YES': # [44]  Voice <<
            # ('STEP 44 - ',device[44],filter_specs['o44'])                                                                                                                            
            match = False

        elif filter_specs['o45'] == 'y' and device[45] != 'YES': # [45]  QoS <<
            # ('STEP 45 - ',device[45],filter_specs['o45'])
            match = False

        elif filter_specs['o46'] == 'y' and (device[46] != '3G' and device[46] != '4G'): # [46]  3G/4G <<
            # ('STEP 46 - ',device[46],filter_specs['o46'])
            match = False
                                                                                                                                                    
        elif filter_specs['o47'] == 'y' and device[47] != 'YES': # [47]  GPS <<
            # ('STEP 47 - ',device[47],filter_specs['o47'])
            match = False

        elif filter_specs['o48'] == 'y' and device[48] != 'YES': # [48]  RPS <<
            # ('STEP 48 - ',device[48],filter_specs['o48'])
            match = False

        elif filter_specs['o49'] == 'y' and device[49] != 'YES': # [49]  External <<
            # ('STEP 49 - ',device[49],filter_specs['o49'])
            match = False

        elif filter_specs['o50'] == 'y' and device[50] != 'YES': # [50]  Wireless <<
            # ('STEP 50 - ',device[50],filter_specs['o50'])
            match = False

        # [51]  Price <<
        
        elif (int(device[51]) < int(filter_specs['o51_min'])):
           # ('STEP 51 - ',device[51],filter_specs['o51_min'],filter_specs['o51_max'])
            match = False

        elif (int(device[51]) > int(filter_specs['o51_max'])):
            # ('STEP 51 - ',device[51],filter_specs['o51_min'],filter_specs['o51_max'])
            match = False

        else:
            match = True # If the data matches all of the criteria, the match flag is marked as True

        if match:
            filtered_routers.append(device) # # If the data matches all of the criteria and the match flag is marked as True, add to the filtered list
            
    return(filtered_routers)



#013
# Filter the switch and other Cisco devices database with the entered criteria



def filter_switches_1():

    filter_specs_2 = {

        'o0' : 'ALL', # [0] Make
        'o1' : 'ALL', # [1] Type
        'o2' : 'ALL', # [2] Layer
        'o3' : 'ALL', # [3] Base
        'o7_min' : 0,       # [7]   Ports <<
        'o7_max' : 9999999999,
        'o8_min' : 0,       # [8]   PoE Usage <<
        'o8_max' : 9999999999,
        'o9_min' : 0,       # [9]  MBPS <<
        'o9_max' : 9999999999,
        'o13_min' : 0,      # [13]  Price <<
        'o13_max' : 9999999999,
            
        }

    quit_prog = False

    while not quit_prog:
        
        option = ''
        valid_input = False
        
        while not valid_input:
            option = input('\nDo you wish to display all the switches in the database? (Y/N): ')
            option = option.lower()
            if option == 'y' or option == 'yes':
                option = 'y'
                valid_input = True
                quit_prog = True
            elif option == 'n' or option == 'no':
                option = 'n'
                valid_input = True
            else:
                print('You must reply Y - YES or N - NO!')

        if option == 'n':

            option = ''
            valid_input = False

            while not valid_input:
                option = input('\nDo you wish to filter the database? (Y/N) :' )
                option = option.lower()
                if option == 'y' or option == 'yes':
                    option = 'y'
                    valid_input = True
                elif option == 'n' or option == 'no':
                    option = 'n'
                    quit_prog = True
                    valid_input = True
                else:
                    print('You must reply Y - YES or N - NO!')

            if option == 'y':

                filter_make = ['AVAYA','CISCO','MERAKI','NEXUS','ALL','']
                filter_type = ['IP PHONE','SWITCH','WAP','ALL','']
                filter_layer = ['2','3','ALL','']
                filter_base = ['LAN BASE','IP BASE','IP SERVICES','ALL','']

                    # [0] Make
                    # [1] Type
                    # [2] Layer
                    # [3] Base
                    # [4] Uplinks
                    # [5] Series
                    # [6] Product
                    # [7] Ports
                    # [8] PoE Usage
                    # [9] MBPS - Usage
                    # [10] PoE (W) - Capacity
                    # [11] MBPS - Capacity
                    # [12] Part Code
                    # [13] Price $


                filter_specs_2['o0'] = filter_device_selection('\nDEVICE MAKE\n','o0',filter_make)
                filter_specs_2['o1'] = filter_device_selection('\nDEVICE TYPE\n','o1',filter_type)
                filter_specs_2['o2'] = filter_device_selection('\nDEVICE LAYER\n','o2',filter_layer)
                filter_specs_2['o3'] = filter_device_selection('\nDEVICE BASE\n','o3',filter_base)

                print('\nPress ENTER for all devices')

                filter_specs_2 = filter_device_range_2(filter_specs_2,'\nMINUMUM PORTS: ', 'o7_min', 'MAXIMUM PORTS: ', 'o7_max')
                filter_specs_2 = filter_device_range_2(filter_specs_2,'\nMINUMUM POE: ', 'o8_min', 'MAXIMUM POE: ', 'o8_max')
                filter_specs_2 = filter_device_range_2(filter_specs_2,'\nMINUMUM MBPS: ', 'o9_min', 'MAXIMUM MBPS: ', 'o9_max')
                filter_specs_2 = filter_device_range_2(filter_specs_2,'\nMINUMUM PRICE $: ', 'o13_min', 'MAXIMUM PRICE $: ', 'o13_max')

                quit_prog = True
                
    return(filter_specs_2)



#014
# After all the specifications have been entered, filter list of routers with the selected criteria: -

    

def filter_switches_2(switches_table,filter_specs_2):

    """

    filter_specs_2 = {

        'o0' : 'ALL', # [0] Make
        'o1' : 'ALL', # [1] Type
        'o2' : 'ALL', # [2] Layer
        'o3' : 'ALL', # [3] Base
        'o7_min' : 0,       # [7]   Ports <<
        'o7_max' : 9999999999,
        'o8_min' : 0,       # [8]   PoE Usage <<
        'o8_max' : 9999999999,
        'o9_min' : 0,       # [9]  MBPS <<
        'o9_max' : 9999999999,
        'o13_min' : 0,      # [13]  Price <<
        'o13_max' : 9999999999,
            
        }
    """
    
    filtered_switches = []
    
    for device in switches_table:

        device[0] = device[0].upper() # Data needs to be converted into uppercase for effective comparison
        device[1] = device[1].upper()
        device[2] = device[2].upper()
        device[3] = device[3].upper()
        
        if (filter_specs_2['o0'] == device[0]) or (filter_specs_2['o0'] == 'ALL'):
            if (filter_specs_2['o1'] == device[1]) or (filter_specs_2['o1'] == 'ALL'):
                if (filter_specs_2['o2'] == device[2]) or (filter_specs_2['o2'] == 'ALL'):
                    if (filter_specs_2['o3'] == device[3]) or (filter_specs_2['o3'] == 'ALL'):                 
                        if (float(text_to_num(device[7])) >= float(filter_specs_2['o7_min']) or filter_specs_2['o7_min'] == '') and (filter_specs_2['o7_max'] == '' or float(text_to_num(device[7])) <= float(filter_specs_2['o7_max'])):
                            if (float(text_to_num(device[8])) >= float(filter_specs_2['o8_min']) or filter_specs_2['o8_min'] == '') and (filter_specs_2['o8_max'] == '' or float(text_to_num(device[8])) <= float(filter_specs_2['o8_max'])):
                                if (float(text_to_num(device[9])) >= float(filter_specs_2['o9_min']) or filter_specs_2['o9_min'] == '') and (filter_specs_2['o9_max'] == '' or float(text_to_num(device[9])) <= float(filter_specs_2['o9_max'])):
                                    if (float(text_to_num(device[13])) >= float(filter_specs_2['o13_min']) or filter_specs_2['o13_min'] == '') and (filter_specs_2['o13_max'] == '' or float(text_to_num(device[13])) <= float(filter_specs_2['o13_max'])):
                                        
                                        filtered_switches.append(device)

    return(filtered_switches)



#015
# Display Bill of Materials



def display_bom(BoM):

    # [0] Make
    # [1] Type
    # [2] Product
    # [3] Quantity
    # [4] Price $

    tabtext = ['',
               ' ',
               '  ',
               '   ',
               '    ',
               '     ',
               '      ',
               '       ',
               '        ',
               '         ',
               '          ',
               '           ',
               '            ',
               '             ',
               '              ',
               '               ',
               '                ',
               '                 ',
               '                  ',
               '                   ',
               '                    ',
               '                     ',
               '                      ',
               '                       ',
               '                        ',
               '                         ',
               '                          '
               
               ]

    print('\nBill of Materials\n_________________')
    print('\nMake\t','Type',tabtext[21],'Product',tabtext[18],'Quantity\t','Price $')
    print('________________________________________________________________________________\n')

    BoM_total = 0
    for item in BoM:
        if item[3] == '':
            item[3] = '0'               
        if item[4] == '':
            item[4] = '0'
        print(item[0],'\t',item[1],tabtext[25-len(item[1])],item[2],tabtext[25-len(item[2])],item[3],'\t',item[4])
        try:
            BoM_total = int(BoM_total) + (int(item[4]) * int(item[3]))
        except ValueError:
            BoM_total = BoM_total
            # If there isn't a valid number in price, just leave it
            
    print('\nTOTAL $: \t\t\t\t\t\t\t\t',BoM_total)



## List of Functions



#001 - display_routers(display_router_table):                                   - Display list of routers 

#002 - select_router(display_router_table):                                     - Select Router from a list       
#002 - return display_router_table[display_number-1][53]                        - Return the correct index number for the router

#003 - display_selected_router(router_number):                                  - Display selected router

#004 - display_switches(display_switches_table):                                -  Display list of switches and other devices 

#005 - select_switch(display_switches_table):                                   - Select switch or other device from a list
#005 - return display_switches_table[display_number-1][14]

#006 - display_selected_switch(device_number):                                  - Display selected switch or other device

#007 - filter_device_range(filter_specs, question_text_min, variable_min, question_text_max, variable_max):
#007 - (Numbers) Obtain filter specifications and enter results in a dictionary
#007 - return(filter_specs)

#008 - filter_device_YN(question_text, question_variable):
#008 - (Yes/No) Obtain filter specifications and enter results in a dictionary
#008 - return(YN_reply)

#009 - filter_device_range_2(filter_specs_2,question_text_min, variable_min, question_text_max, variable_max):
#009 - (Numbers) Obtain filter specifications and enter results in a dictionary
#009 - return(filter_specs_2)
        
#010 - filter_device_selection(filter_text,option,filter_list):                 - Select a filter option from a given list

#011 - filter_routers_1():                                                      - Filter the routers database 
#011 - return(filter_specs)

#012 - filter_routers_2(filter_specs):                                          - After all the specifications have been entered,
#012                                                                            display a list of routers with the selected criteria:
#012 - return(filtered_routers)

#013 - filter_switches_1():                                                     - Filter the switch and other Cisco devices database with
#013                                                                            the entered criteria
#013 - return(filter_specs_2)

#014 - filter_switches_2(switches_table,filter_specs_2):                        - After all the specifications have been entered, filter
#014                                                                            list of switches with the selected criteria
#014 - return(filtered_switches)

#015 - display_bom(BoM):                                                        - Display Bill of Materials



##

## MAIN CODE

## >>



# Read data about routers into a table


routers_file = open('ROUTERS.csv')
routers_DB = reader(routers_file)
routers_table = routers_DB


# Read data about switches and other devices into a table


switches_file = open('SWITCHES.csv')
switches_DB = reader(switches_file)
switches_table = switches_DB


# VARIABLE LIST


option = ''
valid_input = False
quit_prog = False
select_option = ''
device_table = []   # Complete list of routers
device_table_2 = [] # Complete list of switches and other devices
device = []         # Each device on the device_table list
router_number = 0   # For selecting a router
BoM = []            # Bill of Materials (BoM)
BoM_total = 0       # BoM Total
item = []           # Item on BoM
selected_router = ''    # Router selected from list
selected_device = ''    # Device selected from list
filter_specs = {}    # Specs of filter options - Routers
filter_specs_2 = []  # Specs of filter options - Switches & Devices
enter_min = 0
enter_max = 0
enter_filter = False
maximum = 99999999

# This dictionary is used to filter the routers database

filter_specs = {

        # Specs
    'o9_min' : 0,    # [9]   Users <<
    'o9_max' : 9999999999,
    'o10_min' : 0,    # [10]  Slots <<
    'o10_max' : 9999999999,
    'o11_min' : 0,     # [11]  Rack Units <<
    'o11_max' : 9999999999,
    'o12_min' : 0,
    'o12_max' : 9999999999, # [12]  POE Wattage <<
        
        # Ports / Channels / Slots
    'o13_min' : 0,  # [13]  LAN ports <<
    'o13_max' : 9999999999,
    'o15_min' : 0, # [15]  WAN Ports <<
    'o15_max' : 9999999999,
    'o17_min' : 0, # [17]  LAN/LAN <<
    'o17_max' : 9999999999,
    'o18_min' : 0, # [18]  RJ/45 <<
    'o18_max' : 9999999999, 
    'o19_min' : 0, # [19]  SFP <<
    'o19_max' : 9999999999,
    'o20_min' : 0, # [20]  PVDM <<
    'o20_max' : 9999999999,
    'o21_min' : 0, # [21]  VPN <<
    'o21_max' : 9999999999,
    'o22_min' : 0, # [22]  USB <<
    'o22_max' : 9999999999,
    'o23_min' : 0, # [23]  BRI Voice <<
    'o23_max' : 9999999999,
    'o24_min' : 0, # [24]  FXS <<
    'o24_max' : 9999999999,
    'o25_min' : 0, # [25]  FXO <<
    'o25_max' : 9999999999,
    'o26_min' : 0, # [26]  DSP <<
    'o26_max' : 9999999999,
        
        # Performance
    'o27_min' : 0, # [27]  KPPS <<
    'o27_max' : 9999999999,
    'o28_min' : 0,# [28]  MPPS <<
    'o28_max' : 9999999999,


    # Memory
    'o29_min' : 0, # [29]  RAM Min (MB) <<
    'o30_max' : 9999999999, # [30]  RAM Max (MB) <<
    'o31_min' : 0,# [31]  Flash Min (MB) <<
    'o32_max' : 9999999999, # [32]  Flash Max (MB) <<

        # Throughput - MBPS
    'o33_min' : 0,# [33]  TP Min <<
    'o34_max' : 9999999999, # [34]  TP Max <<
        
        # Maximum Streams / Channels
    'o35_min' : 0, # [35]  SRST <<
    'o35_max' : 9999999999,
    'o36_min' : 0,# [36]  CUCM <<
    'o36_max' : 9999999999,
    'o37_min' : 0,# [37]  CCME <<
    'o37_max' : 9999999999,
    'o38_min' : 0,# [38]  CUBE <<
    'o38_max' : 9999999999,
    'o39_min' : 0,# [39]  CUE <<
    'o39_max' : 9999999999,
    'o40_min' : 0,# [40]  TCP <<
    'o40_max' : 9999999999,
    'o41_min' : 0,# [41]  IPSEC <<
    'o41_max' : 9999999999,
    'o42_min' : 0, # [42]  T1/E1 <<
    'o42_max' : 9999999999,

   
        # Features
    'o43' : 'n', # [43]  Security <<
    'o44' : 'n',# [44]  Voice <<
    'o45' : 'n',# [45]  QoS <<
    'o46' : 'n',# [46]  3G/4G <<
    'o47' : 'n',# [47]  GPS <<
    'o48' : 'n',# [48]  RPS <<
    'o49' : 'n',# [49]  External <<
    'o50' : 'n',# [50]  Wireless <<
        
         # [51]  Price $ <<
    'o51_min' : 0,
    'o51_max' : 9999999999
    
    }

    # This dictionary is used to filter the swicthes database

filter_specs_2 = {
        
    'o0' : 'ALL', # [0] Make
    'o1' : 'ALL', # [1] Type
    'o2' : 'ALL', # [2] Layer
    'o3' : 'ALL', # [3] Base
    'o7_min' : 0,       # [7]   Ports <<
    'o7_max' : 9999999999,
    'o8_min' : 0,       # [8]   PoE Usage <<
    'o8_max' : 9999999999,
    'o9_min' : 0,       # [9]  MBPS <<
    'o9_max' : 9999999999,
    'o13_min' : 0,      # [13]  Price <<
    'o13_max' : 9999999999,
        
    }


# Move data from routers_table into a simpler and tidier format in device_table

        # device[]
        
	# SKU [0]
	
        # Router
             # [1]   Make e.g. Cisco
             # [2]   Series
             # [3]   Model

        # Type
             # [4]   Type A
             # [5]   Type B
             # [6]   Type C

        # Specs
             # [7]   IOS
             # [8]   Base
             # [9]   Users
             # [10]  Slots
             # [11]  Rack Units
             # [12]  POE Wattage

        # Ports / Channels / Slots
             # [13]  LAN ports
             # [14]  LAN/TP
             # [15]  WAN Ports
             # [16]  WAN/TP
             # [17]  LAN/LAN
             # [18]  RJ/45
             # [19]  SFP
             # [20]  PVDM
             # [21]  VPN
             # [22]  USB
             # [23]  BRI Voice
             # [24]  FXS
             # [25]  FXO
             # [26]  DSP

        # Performance
             # [27]  KPPS
             # [28]  MPPS

        # Memory - MB
             # [29]  RAM Min
             # [30]  RAM Max
             # [31]  Flash Min
             # [32]  Flash Max

        # Throughput - MBPS
             # [33]  TP Min
             # [34]  TP Max

        # Maximum Streams / Channels
             # [35]  SRST
             # [36]  CUCM
             # [37]  CCME
             # [38]  CUBE
             # [39]  CUE
             # [40]  TCP
             # [41]  IPSEC
             # [42]  T1/E1

        # Features
             # [43]  Security
             # [44]  Voice
             # [45]  QoS
             # [46]  3G/4G
             # [47]  GPS
             # [48]  RPS
             # [49]  External
             # [50]  Wireless

        # [51]  Price - $

        # [52]  Notes

        # Index

        # [53]  Router Number


for router in routers_table:
    device = []
    
    if router[1] == 'OK': # Check device is not EOL
       
        device.append(router[0])    # [0]   SKU

        # Router
        device.append(router[3])         # [1]   Make e.g. Cisco
        device.append(str(router[4]))    # [2]   Series
        device.append(str(router[5]))    # [3]   Model

        # Type
        device.append(router[6])    # [4]   Type A
        device.append(router[7])    # [5]   Type B
        device.append(router[8])    # [6]   Type C

        # Specs
        device.append(router[9])    # [7]   IOS
        device.append(router[10])   # [8]   Base
        device.append(router[11])   # [9]   Users
        device.append(router[12])   # [10]  Slots
        device.append(router[13])   # [11]  Rack Units
        device.append(router[14])   # [12]  POE Wattage

        # Ports / Channels / Slots
        device.append(router[18])   # [13]  LAN ports
        device.append(router[19])   # [14]  LAN/TP
        device.append(router[20])   # [15]  WAN Ports
        device.append(router[21])   # [16]  WAN/TP
        device.append(router[22])   # [17]  LAN/LAN
        device.append(router[23])   # [18]  RJ/45
        device.append(router[24])   # [19]  SFP
        device.append(router[25])   # [20]  PVDM
        device.append(router[26])   # [21]  VPN
        device.append(router[27])   # [22]  USB
        device.append(router[28])   # [23]  BRI Voice
        device.append(router[29])   # [24]  FXS
        device.append(router[30])   # [25]  FXO
        device.append(router[31])   # [26]  DSP

        # Performance
        device.append(router[32])   # [27]  KPPS
        device.append(router[33])   # [28]  MPPS

        # Memory
        device.append(router[34])   # [29]  RAM Min (MB)
        device.append(router[35])   # [30]  RAM Max (MB)
        device.append(router[36])   # [31]  Flash Min (MB)
        device.append(router[37])   # [32]  Flash Max (MB)

        # Throughput
        device.append(router[38])   # [33]  TP Min - MBPS
        device.append(router[39])   # [34]  TP Max - MBPS

        # Maximum Streams / Channels
        device.append(router[40])   # [35]  SRST
        device.append(router[41])   # [36]  CUCM
        device.append(router[42])   # [37]  CCME
        device.append(router[43])   # [38]  CUBE
        device.append(router[44])   # [39]  CUE
        device.append(router[45])   # [40]  TCP
        device.append(router[46])   # [41]  IPSEC
        device.append(router[47])   # [42]  T1/E1

        # Features
        device.append(router[48])   # [43]  Security
        device.append(router[49])   # [44]  Voice
        device.append(router[50])   # [45]  QoS
        device.append(router[51])   # [46]  3G/4G
        device.append(router[52])   # [47]  GPS
        device.append(router[53])   # [48]  RPS
        device.append(router[54])   # [49]  External
        device.append(router[55])   # [50]  Wireless

        device.append(router[56])   # [51]  Price - $
        device.append(router[57])   # [52]  Notes

        # Index
        device.append(router_number)# [53]  Router Number

        # These if statements are necessary for successful filtering
        
        if device[9] == '':
            device[9] = '0'

        if device[10] == '':
            device[10] = '0'
    
        if device[11] == '':
            device[11] = '0'
    
        if device[12] == '':
            device[12] = '0'

        if device[12] == 'YES':
            device[12] = '100'

        if device[13] == '':
            device[13] = '0'

        if device[15] == '':
            device[15] = '0'
    
        if device[17] == '':
            device[17] = '0'
    
        if device[18] == '':
            device[18] = '0'

        if device[19] == '':
            device[19] = '0'

        if device[20] == '':
            device[20] = '0'

        if device[21] == '':
            device[21] = '0'
    
        if device[21] == '':
            device[21] = '0'
    
        if device[22] == '':
            device[22] = '0'

        if device[23] == '':
            device[23] = '0'

        if device[24] == '':
            device[24] = '0'
    
        if device[25] == '':
            device[25] = '0'
    
        if device[26] == '':
            device[26] = '0'

        if device[27] == '':
            device[27] = '0'

        if device[28] == '':
            device[28] = '0'

        if device[29] == '':
            device[29] = '0'
    
        if device[30] == '':
            device[30] = device[29]
    
        if device[31] == '':
            device[31] = '0'

        if device[32] == '':
            device[32] = device[31]
                
        if device[33] == '':
            device[33] = '0'

        if device[34] == '':
            device[34] = device[33]
    
        if device[35] == '':
            device[35] = '0'

        if device[36] == '':
            device[36] = '0'

        if device[37] == '':
            device[37] = '0'

        if device[38] == '':
            device[38] = '0'
                
        if device[39] == '':
            device[39] = '0'
    
        if device[40] == '':
            device[40] = '0'

        if device[41] == '':
            device[41] = '0'

        if device[42] == '':
            device[42] = '0'

        device[51] = text_to_num(device[51])

        device_table.append(device)
        
        router_number += 1
    

# Move data from switches_table into a simpler and tidier format in device_table_2

    # [0] Make
    # [1] Type
    # [2] Layer
    # [3] Base
    # [4] Uplinks
    # [5] Series
    # [6] Product
    # [7] Ports
    # [8] PoE Usage
    # [9] MBPS - Usage
    # [10] PoE (W) - Capacity
    # [11] MBPS - Capacity
    # [12] Part Code
    # [13] Price $


device_number = 0

for switch in switches_table:
    
    if switch[2] == 'OK': # Check device is not EOL
        device = []

        device.append(switch[0])    # [0] Make
        device.append(switch[1])    # [1] Type
        device.append(switch[4])    # [2] Layer
        device.append(switch[5])    # [3] Base
        device.append(switch[6])    # [4] Uplinks
        device.append(switch[7])    # [5] Series
        device.append(switch[8])    # [6] Product
        device.append(switch[9])    # [7] Ports
        
        device.append(switch[10])    # [8] PoE Usage
        device.append(switch[11])    # [9] MBPS - Usage
        device.append(switch[12])    # [10] PoE (W) - Capacity
        device.append(switch[13])    # [11] MBPS - Capacity
        device.append(switch[14])    # [12] Part Code
        device.append(switch[15])    # [13] Device

        # Index
        device.append(device_number) # [14]  Device Number

        device_table_2.append(device)

        device_number += 1



##

## MAIN CODE - Part 2

##



while not quit_prog:

    print('\nCISCO\nDEVICES, ROUTER, SWITCH DATABASE\n________________________________')


    ## ROUTERS

    while not quit_prog:

    ## ROUTERS
        
        valid_input = False # Reset the error flag

        # Ask the user if they would like to display all device

        while not valid_input:
            select_option = input('\nDo you wish to see all the routers? (Y = YES, N = NO): ')
            select_option = select_option.lower()
            if select_option == 'y' or select_option == 'n':
                valid_input = True
            else:
                valid_input = False
                print('You Must Enter Y or N!')

        if select_option == 'n':
            filter_specs = filter_routers_1()                   # Obtain the necessary specifications for filtering the routers data base
            filtered_routers = filter_routers_2(filter_specs)   # Create a table of filtered routers with the required specifications
            display_routers(filtered_routers)                   # Display the filtered database
            router_number = select_router(filtered_routers)     # Allow the user to select a router
        else:
            display_routers(device_table)                       # Display the whole database
            router_number = select_router(device_table)         # Allow the user to select a router

        if router_number >= 0:
            display_selected_router(router_number)              # Display the details of the selected router

        valid_input = False # Reset the error flag

        # Ask the user if they would like to use the routers database again

        while not valid_input:
            select_option = input('\nDo you wish to use the routers database again? (Y = YES, N = NO): ')
            select_option = select_option.lower()
            if select_option == 'y' or select_option == 'n':
                valid_input = True
            else:
                valid_input = False
                print('You Must Enter Y or N!')

        if select_option == 'n':
            quit_prog = True

   
    ## SWITCHES and other devices >>

    
    print('\nCISCO\nDEVICES, ROUTER, SWITCH DATABASE\n________________________________')

    quit_prog = False

    while not quit_prog:
        
        filter_specs_2 = filter_switches_1()                                    # Obtain the necessary specifications for filtering the switches database
        filtered_switches = filter_switches_2(device_table_2,filter_specs_2)    # Create a table of filtered switches with the required specifications
        display_switches(filtered_switches)                                     # Display list of selected switches
        selected_device = select_switch(filtered_switches)                      # Allow the user to select a switch
        if selected_device >= 0:
            display_selected_switch(selected_device)                                # Display the selected switch
        
        valid_input = False # Reset the error flag

        # Ask the user if they would like to use the switches database again

        while not valid_input:
            select_option = input('\nDo you wish to use the switches database again? (Y = YES, N = NO): ')
            select_option = select_option.lower()
            if select_option == 'y' or select_option == 'n':
                valid_input = True
            else:
                valid_input = False
                print('You Must Enter Y or N!')

        if select_option == 'n':
            quit_prog = True
        else:
            quit_prog = False
            
    # Display Bill of Materials

    display_bom(BoM)
            
    # Quit the program?

    option = ''
    valid_input = False
    quit_prog = False

    while not valid_input:
        option = input('\nDo you wish to quit the database? (Y/N): ')
        option = option.lower()
        if option == 'y' or option == 'yes':
            option = 'y'
            valid_input = True
            quit_prog = True
        elif option == 'n' or option == 'no':
            option = 'n'
            valid_input = True
        else:
            print('You must reply Y - YES or N - NO!')

    if option == 'y':
        quit_prog = True
