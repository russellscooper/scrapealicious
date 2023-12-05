import json
from bin.src.modules.dialogue import Dialogues
from bin.src.core.tools import Security, Scanner, Crawler
from lib.utils import FileWriter, Downloader

#global variables 

while True:
    menus = Dialogues()
    secure_menu_input = Security(secure=True)
    
    #Welcome 
    print(menus.welcome())
    user_input = secure_menu_input.secure_string(input('Enter Selection: '))

    #Switches and cases
    if user_input == 'run':
        print(menus.scanner_message())
        target_url = input('Enter URL: ')
        tls_check = Security(secure=True)
        checked_url = tls_check.ensure_tls(target_url)
        
        cralwer = Crawler(checked_url)
        scanner = Scanner(checked_url)
        
        urls = scanner.extractor()
        validated_url = scanner.validate_endpoint(urls)
        api_endpoints = cralwer.crawl(validated_url)

        print(api_endpoints)

    elif user_input == 'settings':
        print(menus.settings())

    elif user_input == 'credits':
        print(menus.credits())

    elif user_input == 'exit':
        break
    else:
        print('Please enter a valid selection...')

