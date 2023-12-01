from bin.src.modules.dialogue import Dialogues
from bin.src.core.tools import Security, Scanner
from bin.src.modules.api_scanner import api_scan
#Don't forget that some instances of the dialogue object require a user_input object. Set user_input using input() function. 

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

    elif user_input == 'wl':
        pass
    elif user_input == 'bl':
        pass
    elif user_input == 'settings':
        pass
    elif user_input == 'credits':
        pass
    elif user_input == 'exit':
        break
    else:
        print('Please enter a valid selection...')

