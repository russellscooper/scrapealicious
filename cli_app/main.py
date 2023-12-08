import json
import schedule
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

    elif user_input == 'schedule':
        while True:
            print(menus.schedule_dialogue())

            schedule_choice = input('Enter Option: ')

            if schedule_choice == 'set':
                pass
        
            elif schedule_choice  == 'cxc':
                print(menus.schedule_warning())
            
                confirm_clear = input('Proceed? y/n')

                if confirm_clear == 'y' or 'Y':
                    schedule.clear()
                    print('Schedule cleared ... all runs removed')
                elif confirm_clear == 'n' or 'N':
                    print('Clear aborted ... returning to menu')
                    pass
                else:
                    print('Please enter y/n')

            elif schedule_choice  == 'lst':
                run_list = schedule.get_jobs()
            
                print(run_list)

            elif schedule_choice  == 'return':
                break

    elif user_input == 'settings':
        print(menus.settings())

    elif user_input == 'credits':
        print(menus.credits())

    elif user_input == 'exit':
        break
    else:
        print('Please enter a valid selection...')

