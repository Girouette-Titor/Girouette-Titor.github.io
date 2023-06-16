import os
import sys

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

path = 'C:\\Users\\Benja\\Desktop\\Otras cosas (AO, wget, etc)\\Characters\\CORPSE PARTY URNA FORTUNAE\\characters\\Arcueid Brunestud (A Piece of Blue Glass Moon)\\emotions'


print(os.path.abspath(__file__))
os.chdir(os.path.abspath(path))

arg = 'C:\\Users\\Benja\\Desktop\\Otras cosas (AO, wget, etc)\\Characters\\CORPSE PARTY URNA FORTUNAE\\characters\\Arcueid Brunestud (A Piece of Blue Glass Moon)\\char.ini'
if len(sys.argv) > 1:
    arg = sys.argv[1]

if arg == "":
    arg: 'C:\\Users\\Benja\\Desktop\\Otras cosas (AO, wget, etc)\\Characters\\CORPSE PARTY URNA FORTUNAE\\characters\\Arcueid Brunestud (A Piece of Blue Glass Moon)\\char.ini'

droppedFile = open(arg, "r")

state = input('Input state (on or off): ').lower()

for line in droppedFile.readlines():
    try:
        lines = line.rstrip().split(' ')
        if lines[0] in ('[SoundN]', '[SoundT]'):
            break
        num = lines[0].split('=')[0]
        if not is_int(num):
            continue

        emote = line.split('#')[2]
        print(emote)
        for button in os.listdir():
            if button == emote + '.png':
                os.rename(button, 'button{}_{}.png'.format(num, state))
                print('Made a new button for {}'.format(emote))
                break
        print('Currently on {}'.format(line))
    except:
        print("Excepted on line {}".format(line))
        continue
input('Donezo')
# while F in os.listdir():
#     os.rename(F, 'button{}_{}.png'.format(i, state))
#     i+=1

