import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os


main_screen_window = tk.Tk()
main_screen_window.geometry('1200x800')
main_screen_window.title('Notepad')
main_screen_window.wm_iconbitmap('notepad.ICO')

head_menu = tk.Menu()

new_logo = tk.PhotoImage(file='resources/new.png')
open_logo = tk.PhotoImage(file='resources/open.png')
save_logo = tk.PhotoImage(file='resources/save.png')
save_as_logo = tk.PhotoImage(file='resources/saves_as.png')
exit_logo = tk.PhotoImage(file='resources/exit.png')

file = tk.Menu(head_menu,tearoff=False)

copy_logo = tk.PhotoImage(file='resources/copy.png')
paste_logo = tk.PhotoImage(file='resources/paste.png')
cut_logo = tk.PhotoImage(file='resources/cut.png')
clear_logo = tk.PhotoImage(file='resources/clear.png')
search_logo = tk.PhotoImage(file='resources/search.png')

edit= tk.Menu(head_menu, tearoff=False)


tool_bar_logo = tk.PhotoImage(file='resources/tool_bar.png')
status_bar_logo = tk.PhotoImage(file='resources/status_bar.png')

view = tk.Menu(head_menu, tearoff=False)

light_blue_logo = tk.PhotoImage(file='resources/lightblue.png')
light_green_logo = tk.PhotoImage(file='resources/lightgreen.png')
blue_logo = tk.PhotoImage(file='resources/blue.png')
red_logo = tk.PhotoImage(file='resources/red.png')
green_logo = tk.PhotoImage(file='resources/green.png')
violet_logo = tk.PhotoImage(file='resources/violet.png')
yellowgreen_logo = tk.PhotoImage(file='resources/yellowgreen.png')

color_theme = tk.Menu(head_menu, tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_blue_logo, light_green_logo, blue_logo, red_logo, green_logo, violet_logo, yellowgreen_logo)


color_dict = {
    'Light Blue': ('#2d2d2d', '#add8e6'),
    'Light green': ('#ccffcc', '#99ff99'),
    'blue': ('#ccffcc', '#0000ff'),
    'Red': ('#2d2d2d', '#ff0000'),
    'green': ('#2d2d2d', '#008000'),
    'violet': ('#ccffcc', '#ee82ee'),
    'yellow green': ('#ccffcc', '#9acd32')
}


head_menu.add_cascade(label='File', menu=file)
head_menu.add_cascade(label='Edit', menu=edit)
head_menu.add_cascade(label='View', menu=view)
head_menu.add_cascade(label='Color Theme', menu=color_theme)



tool_bar = ttk.Label(main_screen_window)
tool_bar.pack(side=tk.TOP,fill=tk.X)


font_tuple = tk.font.families()
font_family = tk.StringVar()
font_group = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly' )
font_group['values'] = font_tuple
font_group.current(font_tuple.index('Arial'))
font_group.grid(row=0, column=0, padx=5)


size_variable = tk.IntVar()
font_size=ttk.Combobox(tool_bar, width=14, textvariable = size_variable,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)



bold_logo = tk.PhotoImage(file='resources/bold.png')
bold_button = ttk.Button(tool_bar, image=bold_logo)
bold_button.grid(row=0, column=2, padx=5)



italized_logo = tk.PhotoImage(file='resources/italized.jpg')
italized_button = ttk.Button(tool_bar,image=italized_logo)
italized_button.grid(row=0, column=3,padx=5)



underline_logo = tk.PhotoImage(file='resources/underline.png')
underline_button=ttk.Button(tool_bar,image=underline_logo)
underline_button.grid(row=0, column=4,padx=5)



font_logo = tk.PhotoImage(file='resources/fontcolor.png')
font_color_button = ttk.Button(tool_bar, image=font_logo)
font_color_button.grid(row=0, column=5, padx=5)



left_align_logo = tk.PhotoImage(file='resources/left_align.png')
left_align_button = ttk.Button(tool_bar, image=left_align_logo)
left_align_button.grid(row=0, column=6, padx=5)


center_align_logo = tk.PhotoImage(file='resources/center_align.png')
center_align_button = ttk.Button(tool_bar, image=center_align_logo)
center_align_button.grid(row=0, column=7, padx=5)


right_align_logo = tk.PhotoImage(file='resources/right_align.png')
right_align_button = ttk.Button(tool_bar, image=right_align_logo)
right_align_button.grid(row=0, column=8, padx=5)



text_editor = tk.Text(main_screen_window)
text_editor.config(wrap='word', relief=tk.FLAT)


scroll_bar = tk.Scrollbar(main_screen_window)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


present_font_family = 'Arial'
present_font_size = 12

def palitan_font(event=None):
    global present_font_family
    present_font_family = font_family.get()
    text_editor.config(font=(present_font_family, present_font_size))


def palitan_size(event=None):
    global present_font_size
    present_font_size = size_variable.get()
    text_editor.config(font=(present_font_family, present_font_size))

font_group.bind("<<ComboboxSelected>>", palitan_font)
font_size.bind("<<ComboboxSelected>>", palitan_size)


def palitan_bold():
    text_property = tk.font.Font(font=text_editor['font'])

    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(present_font_family,present_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(present_font_family,present_font_size,'normal'))

bold_button.configure(command=palitan_bold)


def palitan_italized():
    text_property=tk.font.Font(font=text_editor['font'])

    if text_property.actual()['slant']=='roman' :
        text_editor.configure(font=(present_font_family, present_font_size,'italic'))
    if text_property.actual()['slant']=='italic' :
        text_editor.configure(font=(present_font_family, present_font_size,'normal'))

italized_button.configure(command=palitan_italized)


def underline():
    text_property=tk.font.Font(font=text_editor['font'])
# upper line gives a dictionary whose attributes we are changing
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(present_font_family, present_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(present_font_family, present_font_size,'normal'))

underline_button.configure(command=underline)



def palitan_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_button.configure(command=palitan_font_color)

def left_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

left_align_button.configure(command=left_align)



def center_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

center_align_button.configure(command=center_align)


def right_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

right_align_button.configure(command=right_align)



text_editor.configure(font=('Arial',12))

status_bar = ttk.Label(main_screen_window, text ='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False

def changed(event=None):
    global text_changed
    if text_editor.edit_modified():###checks if any character is added or not
        text_changed= True
        words = len(text_editor.get(1.0, 'end-1c').split()) ##it even counts new line character so end-1c subtracts one char
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f' Words: {words} Characters : {characters}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)


url = ''


def new_file_logo(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)
file.add_command(label='New', image=new_logo ,compound=tk.LEFT, accelerator ='Ctrl+N',command=new_file_logo)


def open_file_logo(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except :
        return
    main_screen_window.title(os.path.basename(url))


file.add_command(label='Open', image=open_logo ,compound=tk.LEFT, accelerator ='Ctrl+O',command =open_file_logo)

def save_file_logo(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else :
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'),('All files','*.*')))
            content = text_editor.get(1.0, tk.END)
            url.write(content)
            url.close()
    except :
        return


file.add_command(label='Save', image=save_logo, compound=tk.LEFT, accelerator ='Ctrl+S', command=save_file_logo)


def save_as_logo_file(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files','*.*')))
        url.write(content)
        url.close()
    except :
        return


file.add_command(label='Save As', image=save_as_logo,compound=tk.LEFT, accelerator='Ctrl+Alt+S',command=save_as_logo_file)



def exit_module(event=None):
    global url, text_changed
    try:
        if text_changed:
            boxmessage = messagebox.askyesnocancel('Warning','Do you want to save the file')
            if boxmessage is True :

                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_screen_window.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    main_screen_window.destroy()
            elif boxmessage is False:
                main_screen_window.destroy()
        else:
            main_screen_window.destroy()
    except:
        return



file.add_command(label='Exit', image=exit_logo, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_module)



def search_module(event=None):

    def find():
        word = entry_find.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if(not start_pos):
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='')


    def replace_module():
        word = entry_find.get()
        replace_module_text = entry_replace.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_module_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_dlg = tk.Toplevel()
    find_dlg.geometry('450x250+500+200')
    find_dlg.resizable(0,0)

    #  frame
    find_frm = ttk.LabelFrame(find_dlg, text ='Find/Replace')
    find_frm.pack(pady=20)

    # labels
    find_txt_lbl = ttk.Label(find_frm,text ='Find :')
    replace_txt_lbl = ttk.Label(find_frm,text ='Replace')

    # entry boxes
    entry_find = ttk.Entry(find_frm,width=30)
    entry_replace = ttk.Entry(find_frm,width=30)


    # Button
    btn_find = ttk.Button(find_frm,text ='Find',command=find)
    btn_replace = ttk.Button(find_frm,text ='Replace',command=replace_module)

    # label grid
    find_txt_lbl.grid(row=0,column=0,padx=4,pady=4)
    replace_txt_lbl.grid(row=1,column=0,padx=4,pady=4)

    #entry grid
    entry_find.grid(row=0, column=1,padx=4,pady=4)
    entry_replace.grid(row=1, column=1,padx=4,pady=4)

    ##button grid
    btn_find.grid(row=2 ,column=0 ,padx=8,pady=4)
    btn_replace.grid(row=2 ,column=1 ,padx=8,pady=4)

    find_dlg.mainloop()

edit.add_command(label='Copy',image=copy_logo,compound=tk.LEFT, accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_logo,compound=tk.LEFT, accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_logo,compound=tk.LEFT, accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear',image=clear_logo,compound=tk.LEFT, accelerator='Ctrl+ALt+X',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Search/Find',image=search_logo,compound=tk.LEFT, accelerator='Ctrl+F',command=search_module)

view_statusbar = tk.BooleanVar()
view_statusbar.set(True)
view_toolbar = tk.BooleanVar()
view_toolbar.set(True)

def conceal_toolbar():
    global view_toolbar
    if view_toolbar:
        tool_bar.pack_forget()
        view_toolbar =False

    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand =True)
        status_bar.pack(side=tk.BOTTOM)
        view_toolbar = True


def conceal_statusbar():
    global view_statusbar
    if view_statusbar:
        status_bar.pack_forget()
        view_statusbar =False
    else:
        status_bar.pack(side=tk.BOTTOM)
        view_statusbar=True




view.add_checkbutton(label='Tool Bar',onvalue =True,offvalue=0,variable =view_toolbar,image=tool_bar_logo, compound=tk.LEFT,command=conceal_toolbar)
view.add_checkbutton(label='Status Bar',onvalue =1,offvalue=False,variable =view_statusbar,image=status_bar_logo, compound=tk.LEFT,command=conceal_statusbar)

def palitan_theme():
    choose_theme = theme_choice.get()
    color_tuple =color_dict.get(choose_theme)
    fg_color, bg_color =color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)

count = 0
for i in color_dict :
    color_theme.add_radiobutton(label = i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command =palitan_theme)
    count+=1

main_screen_window.bind("<Control-n>", new_file_logo)
main_screen_window.bind("<Control-o>", open_file_logo)
main_screen_window.bind("<Control-s>", save_file_logo)
main_screen_window.bind("<Control-Alt-s>", save_as_logo_file)
main_screen_window.bind("<Control-q>", exit_module)
main_screen_window.bind("<Control-q>", exit_module)
main_screen_window.bind("<Control-f>", search_module)

main_screen_window.config(menu=head_menu)
main_screen_window.mainloop()