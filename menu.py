from PyInquirer import prompt
from examples import custom_style_2
from change_main_pw import change_main_password_input, get_seed, change_main_password
from select_service import select_service
from add_account import add_new_account
from password_generator import password_generator
from search_username import search_username
from get_accounts import get_all_accounts
from modify import modify
from delete import delete
from connect_database import connect_database
from authentication import user_exists, confirmation
from login import login
from signup import sign_up

def menu():
    collection = connect_database()

    options = [
        'Select service',
        'Add new account',
        'Password Generator',
        'Search for a username',
        'List of all accounts',
        'Modify an account',
        'Delete an account'
        ]
    questions = [
        {
            'type': 'list',
            'name': 'theme',
            'message': 'What do you want to do?',
            'choices': options
        }
    ]
    answers = prompt(questions, style=custom_style_2)
    if answers['theme'] == 'Select service':
        select_service(collection)
    elif answers['theme'] == 'Add new account':
        add_new_account(collection)
    elif answers['theme'] == 'Password Generator':
        password_generator()
    elif answers['theme'] == 'Search for a username':
        search_username(collection)
    elif answers['theme'] == 'List of all accounts':
        get_all_accounts(collection)
    elif answers['theme'] == 'Modify an account':
        modify(collection)
    elif answers['theme'] == 'Delete an account':
        delete(collection)
