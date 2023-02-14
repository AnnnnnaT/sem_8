import model

def what_class():
    return input('Choose any class: ').upper()

def subject ():
    return input('What subject: ').lower()

def answering():
    return input('Who is answering: ')

def new_mark():
    return input('Your mark: ' )

def list_pupils(journal: dict):
    for k, pupil in enumerate(journal, 1):
        print(f'{k}. {pupil:20} {journal.get(pupil)}')