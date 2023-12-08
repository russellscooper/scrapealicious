import argparse
from bin.src.modules.dialogue import Dialogues
from bin.src.core.tools import Security, Scanner, Crawler

# Main Loop

def main():
    while True:
        # Set up - argparse
        parser = argparse.ArgumentParser(description='Scrape a website for potential api endpoints!')
        parser.add_argument('command',choices=['run','settings','credits',], help='help')
    
        args = parser.parse_args()
    
        # Set up - run function 
        def Run(target_url):
            tls_check = Security(secure=True)
            checked_url = tls_check.ensure_tls(target_url)
        
            cralwer = Crawler(checked_url)
            scanner = Scanner(checked_url)
        
            urls = scanner.extractor()
            validated_url = scanner.validate_endpoint(urls)
            api_endpoints = cralwer.crawl(validated_url)

            print(api_endpoints)
    
        #Set up - main menu and security
        menus = Dialogues()
        secure_menu_input = Security(secure=True)
    
        #Welcome 
        print(menus.welcome())
        user_input = secure_menu_input.secure_string(input('Enter Selection: '))

        #Switches and cases
        if user_input == 'run':
            target_url = input('Enter URL: ')
            Run(target_url)

        elif user_input == 'settings':
            print(menus.settings())

        elif user_input == 'credits':
            print(menus.credits())

        elif user_input == 'help':
            print('to do')

        elif user_input == 'exit':
            break
        else:
            print('Please enter a valid selection...')

if __name__ == "__main__":
    main()