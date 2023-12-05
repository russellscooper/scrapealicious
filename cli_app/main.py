import json
from bin.src.modules.dialogue import Dialogues
from bin.src.core.tools import Security, Scanner
from lib.utils import FileWriter

#global variables 

while True:
    menus = Dialogues()
    secure_menu_input = Security(secure=True)
    
    #Welcome 
    print(menus.welcome())
    user_input = secure_menu_input.secure_string(input('Enter Selection: '))

    #Switches and cases
    if user_input == 'scan':
        print(menus.scanner_message())
        
        target_url = input('Target URL: ')
        tls_string = 'https://' + target_url
        scan = Scanner(tls_string)
        extracted_urls = scan.extractor()
        validated = scan.validate_endpoint(extracted_urls)
        print(validated)
        
        #Consider finding a better solution than a nested while loop. 
        user_write = input("Would you like to write results to file(y/n)?")
        while True:
            if user_write == 'y':
                file_writer = FileWriter("scan_results.txt")
                
                for entry in validated:
                    file_writer.write(json.dumps(entry) + "\n")
                break
            elif user_write == 'n':
                break
            
            else:
                print('Please enter y or n...')

    elif user_input == 'settings':
        pass
    elif user_input == 'credits':
        pass
    elif user_input == 'exit':
        break
    else:
        print('Please enter a valid selection...')

