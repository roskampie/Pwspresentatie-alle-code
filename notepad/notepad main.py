
def new_file_logo(event=None):
global url
url = ''
text_editor.delete(1.0,tk.END)
file.add_command(label='new', image=new_logo ,compound=tk.LEFT, accelerator ='Ctrl+N',command=new_file_logo)