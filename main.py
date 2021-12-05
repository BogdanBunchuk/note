import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
app = QApplication([])

win = QWidget()
win.setWindowTitle('Smart notes')
win.resize(900, 700)
win.move(100, 100)

create_note_btn = QPushButton('Create note')
delete_note_btn = QPushButton('Delete note')
save_note_btn = QPushButton('Save note')

attach_tag_btn = QPushButton('Attach tag')
unatach_tag_btn = QPushButton('Create tag')
search_by_tag_btn = QPushButton('Search by tag')

note_text = QTextEdit()

note_lbl = QLabel('Notes list')
tags_lbl = QLabel('Tags list')

notes_list = QListWidget()
tags_list = QListWidget()

tagline = QLineEdit('')
tagline.setPlaceholderText('Enter tag')

row1 = QHBoxLayout()
row1.addWidget(create_note_btn)
row1.addWidget(delete_note_btn)

row2 = QHBoxLayout()
row2.addWidget(attach_tag_btn)
row2.addWidget(unatach_tag_btn)

col1 = QVBoxLayout()
col1.addWidget(note_text)

col2 = QVBoxLayout()
col2.addWidget(note_lbl)
col2.addWidget(notes_list)
col2.addLayout(row1)
col2.addWidget(save_note_btn)
col2.addWidget(tags_lbl)
col2.addWidget(tags_list)
col2.addWidget(tagline)
col2.addLayout(row2)
col2.addWidget(search_by_tag_btn)

main_layout = QHBoxLayout()
main_layout.addLayout(col1)
main_layout.addLayout(col2)
win.setLayout(main_layout)

with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)
print(notes)


win.show()
app.exec_()