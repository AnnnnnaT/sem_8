import model
import view

def start():
    model.class_path(view.what_class())
    model.subjects(view.subject())
    model.open_file()
    pupil= ''
    while True:
        journal = model.journal()
        view.list_pupils(journal)
        pupil = view.answering()
        if pupil == 'stop':
            break
        mark = int(view.new_mark())
        model.mark(pupil,mark)
    model.saving_file
