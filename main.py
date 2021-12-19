import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])

win = QWidget()
win.setWindowTitle("Smart notes")
win.resize(900, 700)

# interface
create_note_btn = QPushButton("Create note")
delete_note_btn = QPushButton("Delete note")
save_note_btn = QPushButton("Save note")

attach_tag_btn = QPushButton("Attach tag")
unattach_tag_btn = QPushButton("Unattach tag")
search_by_tag_btn = QPushButton("Search by tag")

note_text = QTextEdit()

note_lbl = QLabel("Notes list")
tag_lbl = QLabel("Tags list")

notes_list = QListWidget()
tags_list = QListWidget()

tagLine = QLineEdit('')
tagLine.setPlaceholderText("Enter tag...")

row1 = QHBoxLayout()
row1.addWidget(create_note_btn)
row1.addWidget(delete_note_btn)

row2 = QHBoxLayout()
row2.addWidget(attach_tag_btn)
row2.addWidget(unattach_tag_btn)

col1 = QVBoxLayout()
col1.addWidget(note_text)

col2 = QVBoxLayout()
col2.addWidget(note_lbl)
col2.addWidget(notes_list)
col2.addLayout(row1)
col2.addWidget(save_note_btn)
col2.addWidget(tag_lbl)
col2.addWidget(tags_list)
col2.addWidget(tagLine)
col2.addLayout(row2)
col2.addWidget(search_by_tag_btn)

main_layout = QHBoxLayout()
main_layout.addLayout(col1)
main_layout.addLayout(col2)
win.setLayout(main_layout)

def show_note():
    note = notes_list.selectedItems()[0].text()
    note_text.setText(notes[note]['text'])
    tags_list.clear()
    tags_list.addItems(notes[note]['tags'])

def add_note():
    note_name, ok = QInputDialog.getText(win, 'Новая заметка', 'Введите имя заметки')
    if ok:
        notes[note_name] = {'text': '', 'tags': []}
        with open('notes.json', 'w') as file:
            json.dump(notes, file)
            notes_list.clear()
            notes_list.addItems(notes)

def delete_note():
    note = notes_list.selectedItems()[0].text()
    del (notes[note])
    notes_list.clear()
    notes_list.addItems(notes)
notes_list.itemClicked.connect(show_note)
delete_note_btn.clicked.connect(delete_note)
with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)

create_note_btn.clicked.connect(add_note)
notes_list.addItems(notes)
win.show()
app.exec_()
