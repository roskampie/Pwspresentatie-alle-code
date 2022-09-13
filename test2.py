from cmd import Cmd

class MyPrompt(Cmd):
    prompt = 'TWonky>'
    intro = 'Welcome to the TwonkOS test terminal', 'Twonk = content'

    def do_exit(self, inp):
        """Exit the whole app"""
        print("Bye")
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))
    def help_add(self):
        print('''This will add a new thing''')

MyPrompt().cmdloop()
print("after")

