from cmd import Cmd


class MyPrompt(Cmd):2
prompt = 'TWonky>'
intro = 'Welcome to the TwonkOS test terminal', 'Twonk = content'
#wat doet dit?
def do_exit(self, inp):
        """Exit the whole app"""
        print("Bye")
        return True
#het werkt, maar je moet ff uitleggen hoe die true hier werkt want ik snap hem nie
def do_add(self, inp):
        print("Adding '{}'".format(inp))

        '''if format(''):
            print('kaas is ook erg lekker')'''

def help_add(self):
        print('''This will add a new thing''')
# waarom gebruik je ''''''?
#voor print gebruik je ""

MyPrompt().cmdloop()
print("Programma gestopt")
