from cmd import Cmd


class MyPrompt(Cmd):
    prompt = 'Twonky>'
    intro = 'Welcome to the TwonkOS test shell', 'Twonk = content'

    def do_exit(self, inp):
        """Exit the whole app"""
        print("joe joe, veel plezier met je dag")
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))
    def help_add(self):
        print('''This will add a new thing''')


MyPrompt().cmdloop()
print("de code is nu afgerond")