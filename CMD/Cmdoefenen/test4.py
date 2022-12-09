from cmd import Cmd
import os
from time import sleep

class TwonkOS(Cmd):
    prompt = 'Twonky> '
    intro = "Welcome to the TwonkOS terminal", "Twonk = content", 'Typ \'help\' of \'?\' voor hulp bij alle commands.'

    def do_exit(self, inp):
        'Hiermee eindigd u het programma'
        print("Bedankt voor het gebruiken van de TwonkOS terminal, ")
        return True

    def do_prompt(self, inp):
        'Hiermee veranderd u de prompt'
        if inp == '' :
            print('Dit kan niet, probeer opnieuw: ')
        else:
            self.prompt = inp + '> '

    def do_kazen(self, kazen):
        'Typ dit voor de waarheid'
        kaas = 'kaas is gewoon echt flink superieur en daar kan je niks aan doen!'
        for letter in kaas:
                print(letter)

    def do_cwd(self, cwd):
        'Hiermee krijgt u de directory waar je nu inzit'
        cwd = os.getcwd()
        print(cwd)

    def do_lwd(self, lwd):
        'De lijst van mogelijke directory\'s'
        lwd = os.listdir()
        print(lwd)

    def do_bwd(self, bwd):
        'Hierbij gaat u een directory terug'
        bwd = os.chdir('../')
        print('Cwd is veranderd naar:', os.getcwd())

    def do_fwd(self, fwd):
        'Typ \'fwd\', en daaronder naar welke directory je toe wilt'
        inp = input()
        if os.path.exists(inp):
            os.chdir(inp)
            print('Cwd is veranderd naar:', os.getcwd())
        else:
            print('Werkte niet, typ lwd om de mogelijke directory\'s te bekijken.')

    def do_mnd(self, mnd):
        'Hiermee maak je een directory, gebruik \'/\' met de naam van de directory erachter die u wilt maken'
        inp = input()
        os.mkdir(inp)
        print("De directory", inp, "is toegevoegd")

    def do_red(self, red):
        'Hiermee verwijderd u een directory'
        inp = input()
        os.rmdir(os.getcwd() + inp)

    def do_pyt(self, pyt):
        'Typ \'pyt\', en dan eronder een simpel python command om die te laten uitvoeren.'
        inp = input()
        print(type(inp))
        exec(inp)

    #!Belangrijk!: zorg dat 'Emulate terminal in output console' aanstaat om de clear command te laten werken.
    #Hier ga je heen door: run -> edit configurations... -> het goede bestand kiezen -> onder het kopje 'execution' -> click het vinkje bij ' Emulate terminal in output console' aan.
    def do_clear(self, clear):
        'Typ \'clear\' om de terminal leeg te maken.'
        print('clearing...')
        sleep(1)
        os.system('clear')
        print("(\'Welcome to the TwonkOS terminal\',", "\'Twonk = content,\'", '\"Typ \'help\' of \'?\' voor hulp bij alle commands.\")')

    def do_rpf(self, rpf):
        'Hopelijk gaat dit wat doen. (python file openen)'
        rpf = input()
        if os.path.exists(rpf):
            exec(open(rpf).read())
            print("Programma gerund")
        else:
            print("Probeer opnieuw")

    def do_cat(self, gir):
        'Typ \'cat\' en dan daaronder \'sleepy cat\' of \'cat\' voor iets leuks.'
        inp = input()
        if inp == 'sleepy cat':
            print(r"""
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) 
                    """)
        elif inp == 'cat':
            print(r"""
                                                .--.
                                               `.  \
                                                 \  \
                                                  .  \
                                                  :   .
                                                  |    .
                                                  |    :
                                                  |    |
  ..._  ___                                       |    |
 `."".`''''""--..___                              |    |
 ,-\  \             ""-...__         _____________/    |
 / ` " '                    `""""""""                  .
 \                                                      L
 (>                                                      \_
/                                                         \_
\_    ___..---.                                            L
  `--'         '.                                           \_
                 .                                           \_
                _/`.                                           `.._
             .'     -.                                             `.
            /     __.-Y     /''''''-...___,...--------.._            |
           /   _."    |    /                ' .      \   '---..._    |
          /   /      /    /                _,. '    ,/           |   |
          \_,'     _.'   /              /''     _,-'            _|   |
                  '     /               `-----''               /     |
                  `...-'                                       `...-'
            """)

    def do_add(self, add):
        'Dit voegt iets toe, (tenmiste dat zegt ie)'
        if add == 'kaas' or add == 'kaasjes' or add == 'kazen':
            print('Kaas is ook erg lekker!')
        else:
            print('Geen kaas helaas.')
            print(add, 'is toegevoegd.')

TwonkOS().cmdloop()
print("Het programma is ten einde gekomen")
