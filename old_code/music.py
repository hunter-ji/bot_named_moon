import random
import os
L = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g'}
A = {}
num = 0
def music():
    num = random.randint(1,7)
    music = L['%s'%num] + '.mp3'
    os.system('mplayer music/"%s"'%music)


if __name__ == '__main__':
    music()
