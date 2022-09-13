#iport de GUI files
import PySimpleGUI as sg

#De knop maken
layout = [[sg.Button('Kaas is erg lekker', size=(30,4))]]

#het schermpje zelf creeren
window = sg.Window('De pure waarheid', layout, size=(200,100))

event, values = window.read()