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

1. Run: type run and press enter...
2. Schedule Run: type sched and press enter...
3. Settings: type settings and press enter...
4. Credits: type credits and press enter...
5. Exit: type exit and press enter...

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
        table.add_row(['run', 'Enter a url and find api endpoints located at a url.'])
        print(table)

    def scanner_message(self):
        return f'''
API SCANNER TOOL 
-------------------------------------------------------------
Enter full URL below and press enter...
'''
    
    
    def settings(self):
        return 'Settings menu ... todo'
    
    def credits(self):
        return 'Created by Samuel Cooper'
    
    def schedule_dialogue(self):
        return '''
SCHEDULER MENU
-------------------------------------------------------------
Pass a run from the main thread to a time on the schedule.
Schedule is not persistent!
1. Set run : type set and press enter...
2. Cancel run : type cxc and press enter...
3. List scheduled runs : type lst and press enter...
4. Main menu : type return and press enter...



'''
    def schedule_warning(self):
        return '''
        Warning: You are about to clear all runs from schedule!
        '''







#todo Implement a read along feature that uses text to speech to read out loud. 