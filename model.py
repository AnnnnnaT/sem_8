journal = {}
subject = ''
path = 'C:\Users\User\sem8\Classes'

def class_path (what_class: str):
    global path
    path = path + '\\' what_class.upper() + '.txt' 

def subjects (any_subject: str):
    global subject
    subject = any_subject

def open_file():
    with open (path, 'r', encoding = 'utf-8') as file:
        data = file.readlines()
    for line in data:
        if line.split('|')[0] == subject:
            for pupil_marks in line.split('|')[1].strip().split(', '):
                journal[pupil_marks.split(':')[0]] = list(map(int, pupil_marks.split(':')[1].split())) #словарь(ключ - ученик; значение - оценки)


def saving_file():
    new_file = []
    with open (path,'r', encoding = 'unf-8') as data:
        file = data.readlines()

    for item in file:
        if item.split('|')[0]!= subject:
            new_file.append(item.strip())

    elem = []
    for pupil, marks in journal.elem():
        elem.append(pupil+ ':'+" ".joint(list(map(str, marks))))
    elem = subject + '|'+ ', '.join(elem)
    new_file.append(elem)

    with open(path, 'w', encoding= 'utf-8') as data:
        data.write('\n'.join(new_file))

def mark (pupil: str, mark: int):
    marks = list(journal.get(pupil))
    marks.append(mark)
    journal[pupil] = marks

def journal():
    return journal