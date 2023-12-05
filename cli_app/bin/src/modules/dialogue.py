from prettytable import PrettyTable

class Dialogues:
    # Class variable for version number
    version_number = '00.00.02'

    def __init__(self) -> None:
        # Instance variable to store dialogues
        self.dialogues = {}

    def welcome(self):
        return f'''
Welcome to Scrapealicious CLI Tool!
-------------------------------------------------------------
To see list of available commands type help and press enter. 
Other wise select from the menu options below...

1. API Scanner: type scan and press enter...
2. Settings: type settings and press enter...
3. Credits: type credits and press enter...
4. Exit: type exit and press enter...

Thank You for using our technology!
-------------------------------------------------------------

        '''

    def version(self):
        return f'Version {self.version_number}'

    def info(self):
        return 'Command line application that searches for API endpoints in web content. Copyright: 2023 Samuel Cooper'

    def warnings(self):
        # Placeholder for warning messages
        pass

    def display_help(self):
        table = PrettyTable()
        table.field_names = ['Command Name', 'Function']
        table.add_row(['help [name]', 'display specific information about a command name.'])
        table.add_row(['info', 'display information about app'])
        table.add_row(['version', 'display current version of cli'])
        print(table)

    def scanner_message(self):
        return f'''
API SCANNER TOOL 
-------------------------------------------------------------
Enter full URL below and press enter...
'''
    
    def blacklist(self):
        return 'Retrieving black list...'
    
    def whitelist(self):
        return 'Retrieving white list...'
    
    def settings(self):
        return 'Settings menu ... todo'
    
    def credits(self):
        return 'Created by Samuel Cooper'








#todo Implement a read along feature that uses text to speech to read out loud. 