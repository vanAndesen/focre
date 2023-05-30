import PySimpleGUI as psg
from os import makedirs


#Settings
padding = (5, 5)
current = ''


#Folder Creation Lists
newBody = ['Audio', 'Sprites']
newElement = ['Audio', 'Textures']
newLevel = ['Audio', 'Textures', 'Tilemaps']
newTheme = ['DynamicFonts', 'Fonts', 'Resources', 'Textures']


#PySimpleGUI Layouts
psg.theme('DarkGreen5')
project_selection = [
    [psg.Push(), psg.Text('Browse to select your projects root folder.'), psg.Push()],
    [psg.Push(), psg.Input(size=(50, 1), pad=(10, 20), key='-PROJECTFOLDER-'), psg.FolderBrowse(), psg.Push()],
    [psg.Push(), psg.Button('Start', size=(15, 1), key='-START-'),psg.Push()]
]

#Selection window
window = psg.Window('FOCRE - Folder creator for gamedevelopment.', project_selection, size=(550, 140))
while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break
    if event == '-START-':
        current = values['-PROJECTFOLDER-']
        window.close()


#Main layout
project =[
    [psg.Text(current)]
]
foldername_input = [    
    [psg.Push(), psg.Text('Folder name'),psg.Input(size=(20, 1), do_not_clear=False, pad=(1, 20), key='-FOLDER-'), psg.Push()]
]
component_buttons = [
    [psg.Push(), psg.Text('Game Objects'), psg.Push()],
    [psg.HSeparator()],
    [psg.Button('Character', size=(15 , 1), key='character'), 
    psg.Button('Component', size=(15 , 1), pad=padding, key='component')],
    [psg.Button('Item', size=(15 , 1), key='item'),
    psg.Button('Object', size=(15 , 1), pad=padding, key='object')]
]
level_buttons =[
    [psg.Push(), psg.Text('Level'), psg.Push()],
    [psg.HSeparator()],    
    [psg.Button('Level', size=(15 , 1), pad=padding, key='level')]
]
ui_buttons = [ 
    [psg.Push(), psg.Text('User Interface'), psg.Push()],
    [psg.HSeparator()],
    [psg.Button('HUD', size=(15 , 1), key='hud'), 
    psg.Button('HUD Element', size=(15 , 1), key='hud_element')],       
    [psg.Button('UI', size=(15 , 1), key='ui'), 
    psg.Button('UI Element', size=(15 , 1), pad=padding, key='ui_element')]
]
basic_buttons = [
    [psg.Push(), psg.Text('Basic Folders'), psg.Push()],
    [psg.HSeparator()],
    [psg.Button('Autoloads', size=(15 , 1), key='autoloads'),
    psg.Button('HUD', size=(15 , 1), key='hud_base')],
    [psg.Button('Theme', size=(15 , 1), pad=padding, key='theme'),
    psg.Button('UI', size=(15 , 1), key='ui_base')]
]
misc_buttons = [
    [psg.Push(), psg.Text('Micellaneous Folders'), psg.Push()],
    [psg.HSeparator()],
    [psg.Button('Assets', size=(15 , 1), key='_assets'), 
    psg.Button('Test', size=(15 , 1), key='_test'),
    psg.Button('Screenshots', size=(15 , 1), pad=padding, key='_screenshots')],    
    [psg.Button('Linux', size=(15 , 1), key='_linux'),
    psg.Button('Web', size=(15 , 1), key='_web'),
    psg.Button('Windows', size=(15 , 1), pad=padding, key='_windows')]
]
layout_main = [
    [psg.Push(), psg.Column(project), psg.Push()],
    [psg.Push(), psg.Column(foldername_input), psg.Push()],    
    [psg.Push(), psg.Column(component_buttons), psg.Push()],
    [psg.Push(), psg.Column(level_buttons), psg.Push()],
    [psg.Push(), psg.Column(ui_buttons), psg.Push()],    
    [psg.Push(), psg.Column(basic_buttons), psg.Push()],
    [psg.Push(), psg.Column(misc_buttons), psg.Push()],
    [psg.Push(), psg.Button('Quit', size=(12, 1), pad=(0, 50), key='-QUIT-'),psg.Push()]
]


#Folder hierarki
def folder_builder(folders, type):
    try:
        for folder in folders:
            makedirs(current + type + values['-FOLDER-'] + f'/{folder}')
    except:
        pass

def misc_folders(misc):
    try:
        makedirs(current + misc)
    except:
        pass

#Main program
window = psg.Window(f'FOCRE - {current}', layout_main, size=(550, 720))
while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED or event == '-QUIT-':
        break
    if event == 'autoloads':
        misc_folders('/Autoloads')
    if event == 'character':        
        folder_builder(newBody, '/Characters/')
    if event == 'component':            
        makedirs(current + '/Component/' + values['-FOLDER-'])
    if event == 'hud':
        folder_builder(newElement, '/HUD/')
    if event == 'hud_base':
        makedirs(current + '/HUD')
    if event == 'hud_element':        
        folder_builder(newElement, '/HUD/Element/')
    if event == 'item':
        folder_builder(newBody, '/Items/')
    if event == 'level':
        folder_builder(newLevel, '/Levels/')    
    if event == 'object':
        folder_builder(newBody, '/Objects/')
    if event == 'theme':
        try:
            for folder in newTheme:
                makedirs(current + f'/Theme/{folder}')
        except:
            pass
    if event == 'ui':
        folder_builder(newElement, '/UI/')
    if event == 'ui_base':
        makedirs(current + '/UI')
    if event == 'ui_element':        
        folder_builder(newElement, '/UI/Element/')
    if event == '_assets':
        misc_folders('/_Assets')
    if event == '_linux':
        misc_folders('/_Linux')
    if event == '_screenshots':
        misc_folders('/_Screenshots')
    if event == '_test':
        misc_folders('/_Test')
    if event == '_web':
        misc_folders('/_Web')
    if event == '_windows':
        misc_folders('/_Windows')