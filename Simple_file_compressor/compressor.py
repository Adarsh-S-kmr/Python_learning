import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED

import make_archive

sor = sg.Text("Select files to compress")
dest = sg.Text("Select destination")
sou_t = sg.InputText()
dest_t = sg.InputText()
source_b = sg.FilesBrowse("choose files",key = 'files')
dest_b = sg.FolderBrowse("choose folder",key = 'folder')
comp = sg.Button('compress')
output = sg.Text('',key = 'result')
window = sg.Window('File_compressor',layout=[[sor,sou_t,source_b],
                                        [dest,dest_t,dest_b],[comp,output]])
while True:
    event , values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive.mak(filepaths,folder)
    window['result'].update(value = 'compression completed')
    if event == WIN_CLOSED:
        break
window.close()
