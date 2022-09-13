from cmd import Cmd

class MyPrompt(Cmd):
    prompt = 'TWonky>'
    intro = 'Welcome to the TwonkOS test terminal', 'Twonk = content'
#wat doet dit?
    def do_exit(self, inp):
        """Exit the whole app"""
        print("Bye")
        return True
#dit werkt nice, lekker bezig
    def do_add(self, inp):
        print("Adding '{}'".format(inp))
#voeg een manier toe om de {} als nieuwe add te doen (code generation)
    def help_add(self):
        print('''This will add a new thing''')
#wat doet dit? vgm help zit vgm in de cmd package
MyPrompt().cmdloop()
print("after")
#het werkt, leg pls uit hoe