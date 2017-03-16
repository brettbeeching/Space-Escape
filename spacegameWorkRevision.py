#Get from the Command Center to the Airlock with the Alien killing you
from time import sleep
from turtle import *
from turtle import Turtle

from random import choice, randint, shuffle, sample

##bgcolor('black')
##color('white')
##ht()
##write('''Your crew is dead and your spaceship is floating through space without power.\nYou are only alive because of your quick thinking.\nYou grabbed an Atomsphere-Suit before the system failure.\nHowever you helmet-mounted light only has enough charge for 5 minutes''')
###sleep(3)
##clear()
##write('\nMake your way to the airlock and exit in the escape pod back to Earth.\nGodspeed!')
##

title('Space Ship Escape')

setworldcoordinates(0,0,100,100)
screensize(400,400)



areas = ['Command Center', 'Hallway', 'Galley', 'Airlock', 'Earth']



enemyareas = areas[0:-1]

class Scene(object):

    uturt = Turtle()#add a shape in the future
    
    def __init__(self, name):
        self.name = name
        self.currentpos = 'Command Center'
        self.battery = 5
        self.health = 3


    def findbattery(self):
        self.battery += 1
        print('%s finds a spare battery pack but it is almost depleted. You gain an extra minute of battery life. %s minutes of battery left' % (self.name, self.battery))
        
    def losebattery(self):
        self.battery -= 1
        print('The light flickers and the battery drains. %s minutes of battery left' % (self.battery))

    def losehealth(self):
        self.health -= 1
        print('Ouch! Lose 1 health. %s health remaining' % (self.health))
    
    #Changes the user position from Command Center to Hallway. 
    def movescenecc(self):
        self.currentpos = 'Hallway'
    
    def movescenehw(self, move):
        self.move = move
        #self.currentpos = 'Hallway'
        
        if self.move == 'galley':
            self.currentpos = areas[2]
            
        elif self.move == 'airlock':
            self.currentpos = areas[3]

        elif self.move == 'command center':
            self.currentpos = areas[0]

    def movesceneairlock(self, move):
        self.move = move

        if self.move == 'hallway':
            self.currentpos = areas[1]

        elif self.move == 'earth':
            self.currentpos = areas[4]    
    def movescenegalley(self):
        
        print('%s barely made it out of the %s.' % (self.name, self.currentpos))
        self.currentpos = 'Hallway'
        losebattery()
        print('But now stands in the %s. The helmet-mounted light is dim and losing power quickly. %s can\'t see anything. Go left or right? ' % (user.currentpos, user.name))
        print('Battery level: %s.' % (self.battery))
    
class BadGuy(Scene):

    #initializes turtle for enemy and colors it red.
    bturt = Turtle()
    bturt.color('red')
    
    def __init__(self,name):
        super().__init__(name)
        self.currentpos = enemyareas[randint(0,len(enemyareas)-1)]

    def changepos(self):
        if self.currentpos == enemyareas[1]:
            self.currentpos = enemyareas[enemyareas.index(choice(enemyareas))]

        else: self.currentpos == enemyareas[1]
        

#dummy initialized players
user = Scene('Brett')
enemy = BadGuy('Bad Guy')

#Create objects of randomevent functions
losebattery = user.losebattery
losehealth = user.losehealth
findbattery = user.findbattery

#Create randomevent list
randomevent = [losebattery, losehealth, findbattery]

print('Something reflects light in the corner of the Command Center. ')
sleep(.5)

#Opening scene. User has choice to investigate or exit room
start = True
while start == True:
    action = input('Investigate (I) or go for the exit (E)? ').lower()
    sleep(.5)
    if action == 'i':
        choice(randomevent)() #random event happens to player. 2/3 chance it's bad.
        sleep(.5)       
        print('%s moves toward the exit...' % (user.name))
        user.movescenecc()
        start = False

    elif action == 'e':
        print('%s moves toward the exit...' % (user.name))
        user.movescenecc()
        start = False

    else:
        print('Make a valid choice.')
        start = True
    

#if user.currentpos == enemy.currentpos:
   # print('FIGHT!!!!')

##while user.currentpos != 'Earth':
##    position = input('You are in the Airlock. Go to Earth or the Hallway... ').lower()
##
##    print('Moving towards escape pod...')
##    sleep(.5)
##
##    user.movesceneairlock(position)
##    print('Your current position is %s' % (user.currentpos))



#Test code for checking scene movement 
##user.movescenehw('galley')
##print(user.currentpos)
##user.movescenehw('airlock')
##print(user.currentpos)
##user.movescenehw('command center')
##print(user.currentpos)
##

#movepos = user.movescenecc()
