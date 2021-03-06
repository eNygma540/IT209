#-------------------------------------------------------------------------+
#Program name: IT209_A9.py                                                |
#Author: Brendon Lugo and William Dugbly                                  |
#Date Written: 4/17/19                                                    |
#Purpose: Assignment 9                                                    |  
#-------------------------------------------------------------------------+
print("Welcome to the start of Assignment 9...")
import random
class Char():
    def __init__(self, Name, Hp, Att, Def, Sp):   #Added Sp for Speical Move funcationality
        self.Name= str(Name)
        self.Hp= int(Hp)
        self.Att= int(Att)
        self.Def= int(Def)
        self.Sp = int(Sp)
        #self.Bag = []                       #Change from UML Char has bag rather than UI

    def __str__(self):
        print("put ascit drawing here")

    #def Access_Bag(Bag):
        #for i in bag:
            #print i

    def Use_Ability(Move, Move_Cost, Name, Type):
        if self.Mag >= Move_Cost:
            self.Mag -= Move_Cost
            if Type == "Att":
                self.Att += Move
            if Type == "Hp":
                self.Hp += Move
            print(self.name,' uses ',name,'!')
        else:
            print("You do not have enough Magic!")

class Mage(Char):
    def __init__(self, Name, Hp, Att, Def, Sp, Mag, c_type):
        super().__init__(Name, Hp, Att, Def, Sp)
        self.Mag = 4
        self.c_type = 'm'

    def __str__(self):
        print("put drawing in here")

    def Ability():
        Name = "FireBall"
        Move = self.Sp + 3
        Move_Cost = 1
        Type = "Att"
        self.Use_Ability(Move, Move_Cost, Name, Type)

class Knight(Char):
    def __init__(self, Name, Hp, Att, Def, Sp, Mag, c_type):
        super().__init__(Name, Hp, Att, Def, Sp)
        self.Mag = 4
        self.c_type = 'k'

    def __str__(self):
        print("put drawing in here")

    def Ability():
        Name = "Heal"
        Move = self.Sp + 2
        Move_Cost = 1
        Type = "Hp"
        self.Use_Ability(Move, Move_Cost, Name, Type)

class Archer(Char):
    def __init__(self, Name, Hp, Att, Def, Sp, Mag, c_type):
        super().__init__(Name, Hp, Att, Def, Sp)
        self.Mag = 4
        self.c_type = 'a'

    def __str__(self):
        print("put drawing in here")

    def Ability():
        Name = "Rain Arrows"
        Move = self.Sp + 2
        Move_Cost = 1
        Type = "Att"
        self.Use_Ability(Move, Move_Cost, Name, Type)
#---------------Character Class Above, Enemy Below -----------------------------------
class Mob():
    def __init__(self, Hp, Att):   #Added Sp for Speical Move funcationality
        self.Hp= int(Hp)              #Removed Name, mobs dont have uquie names
        self.Att= int(Att)
            
class Dragon(Mob):
    def __init__(self,Hp, Att, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Fire Breath","Dragons Claw","Tail Whip","Glazing Stare"]
        
    def __str__(self):
        print("put drawing in here")

class Wolf(Mob):
    def __init__(self, Hp, Att, Def, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Howel","Chomp","Claw","Tail Whip"]
        
    def __str__(self):
        print("put drawing in here")

class Zombie(Mob):
    def __init__(self, Hp, Att, Def, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Bite","Claw","Screech","Decaying Burst"]
        
    def __str__(self):
        print("put drawing in here")


class Boss(Mob):
    def __init__(self, Hp, Att, Def, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Python Mastery","Lazer Eyes","Fire Breath","One Inch Punch"]
        
    def __str__(self):
        print("put drawing in here")
#-------------------Enemies Above, Biome Below--------------------
class Biome():
    def __init__(self,Forest_Area, Mountian_Area, Sand_Area, choice):
        self.Forest_Area = Forest_Area
        self.Mountian_Area = Mountian_Area
        self.Sand_Area = Sand_Area
        self.choice = "G"
        
    def PickArea(self, Area):
        if Area == "F":
            self.choice = "F"

        elif Area == "M":
            self.choice = "M"
            
        elif Area == "D":
            self.choice = "D"

    def setChoice(self,new):
        self.choice = new
        return self.choice

    def PickAreaEvent(self,choice):
        if choice == "F":
            Event = random.choice(self.Forest_Area)
            print(Event)
        elif choice == "M":
            Event = random.choice(self.Mountian_Area)
            print(Event)
        elif choice == "D":
            Event = random.choice(self.Deseart_Area)
            print(Event)
            

        
#---------BIOME CLASS ABOVE, ITEMS CLASS BELOW------------------------
class Items():
    def __init__(self,knightems,archItems,mageItems):
            self.knightems = knightems
            self.archItems = archItems
            self.mageItems = mageItems

    def getItems(self,player):
        if player.c_type == "k":
            print(random.choice(list(self.knightems)))
        elif player.c_type == "a":
            print(random.choice(list(self.archItems)))
        elif player.c_type == "m":
            print(random.choice(list(self.mageItems)))
            
gameItems= Items({"Dagger":1,"Broadsword":2,"Greataxe":2,"Rubber Chicken":3,'Apple':1,"Turkey leg":2,"Chipotle":3},
                 {"Yew longbow":2,"Nerf bow":1,"Magic bow":3,"Crossbow":2,'Apple':1,"Turkey leg":2,"Chipotle":3},
                 {"Choatic staff":3,"Spellbook":2,"Useless stick":1,"Magic wand":2,'Apple':1,"Turkey leg":2,"Chipotle":3})
#-------------Openning Credits-------------------------------
import time
import random
#import pygame



creditPage = '''
   Written by Billy Duggleby and Brendon Lugo
for IT209 at George Mason University, Spring 2019.
Ascii art wizard created by Morfina at www.asciiart.eu
Ascii art knight created by fsc at http://ascii.co.uk
Ascii art archer created by Erorppn Xrzavgm at http://ascii.co.uk
Ascii art dragon created by Joan at asciiart.website//joan/www.geocities.com
'''


choose = '''
      * ***      *                                                                                                          
    *  ****  * **                                                                                                           
   *  *  ****  **                                                                                                           
  *  **   **   **                                                                                                           
 *  ***        **           ****       ****       ****                 **   ****         ****    **   ****     ***  ****    
**   **        **  ***     * ***  *   * ***  *   * **** *    ***        **    ***  *    * ***  *  **    ***  *  **** **** * 
**   **        ** * ***   *   ****   *   ****   **  ****    * ***       **     ****    *   ****   **     ****    **   ****  
**   **        ***   *** **    **   **    **   ****        *   ***      **      **    **    **    **      **     **         
**   **        **     ** **    **   **    **     ***      **    ***     **      **    **    **    **      **     **         
**   **        **     ** **    **   **    **       ***    ********      **      **    **    **    **      **     **         
 **  **        **     ** **    **   **    **         ***  *******       **      **    **    **    **      **     **         
  ** *      *  **     ** **    **   **    **    ****  **  **            **      **    **    **    **      **     **         
   ***     *   **     **  ******     ******    * **** *   ****    *      *********     ******      ******* **    ***        
    *******    **     **   ****       ****        ****     *******         **** ***     ****        *****   **    ***       
      ***       **    **                                    *****                ***                                        
                      *                                                   *****   ***                                       
                     *                                                  ********  **                                        
                    *                                                  *      ****                                          
                   *                                                                                                        
                                                                                                                            
                                                                                                                            
                   ***                           *                                                                                          
                 ** ***    *                   **            *                                                                              
                **   ***  ***                  **           **                                                                              
                **         *                   **           **                                                                              
                **                             **         ********           ***  ****                                                      
                ******   ***         ****      **  ***   ********     ***     **** **** *                                                   
                *****     ***       *  ***  *  ** * ***     **       * ***     **   ****                                                    
                **         **      *    ****   ***   ***    **      *   ***    **                                                           
                **         **     **     **    **     **    **     **    ***   **                                                           
                **         **     **     **    **     **    **     ********    **                                                           
                **         **     **     **    **     **    **     *******     **                                                           
                **         **     **     **    **     **    **     **          **                                                           
                **         **     **     **    **     **    **     ****    *   ***                                                          
                **         *** *   ********    **     **     **     *******     ***                                                         
                 **         ***      *** ***    **    **             *****                                                                  
                                          ***         *                                                                                     
                                     ****   ***       *                                                                                      
                                    *******  **       *                                                                                       
      	                           *     ****        * 
'''

title = '''
                                                                                                                             
     ***** *    **   ***              ***                                                                                    
  ******  *  *****    ***              ***                                                                                   
 **   *  *     *****   ***              **                                                                                   
*    *  **     * **      **             **                                                                                   
    *  ***     *         **             **                  ****                                                             
   **   **     *         **    ***      **       ****      * ***  * *** **** ****       ***                                  
   **   **     *         **   * ***     **      * ***  *  *   ****   *** **** ***  *   * ***                                 
   **   **     *         **  *   ***    **     *   ****  **    **     **  **** ****   *   ***                                
   **   **     *         ** **    ***   **    **         **    **     **   **   **   **    ***                               
   **   **     *         ** ********    **    **         **    **     **   **   **   ********                                
    **  **     *         ** *******     **    **         **    **     **   **   **   *******                                 
     ** *      *         *  **          **    **         **    **     **   **   **   **                                      
      ***      ***      *   ****    *   **    ***     *   ******      **   **   **   ****    *                               
       ******** ********     *******    *** *  *******     ****       ***  ***  ***   *******                                
         ****     ****        *****      ***    *****                  ***  ***  ***   *****                               
                                                                                             *                            
                                                                                             *                           
                                                                                            *                           
                                                                                                                          
                                                                                                                             
                                                                                                                             
        **             **                                                                                                    
     *****              **                                           *                                                       
    *  ***              **   **                                     **                                                       
       ***              **   **                                     **                                                       
      *  **             **    **    ***                           ******** **   ****     ***  ****              ***  ****    
      *  **         *** **     **    ***     ***    ***  ****    ********   **    ***  *  **** **** *    ***     **** **** * 
     *    **       *********   **     ***   * ***    **** **** *    **      **     ****    **   ****    * ***     **   ****  
     *    **      **   ****    **      **  *   ***    **   ****     **      **      **     **          *   ***    **         
    *      **     **    **     **      ** **    ***   **    **      **      **      **     **         **    ***   **         
    *********     **    **     **      ** ********    **    **      **      **      **     **         ********    **         
   *        **    **    **     **      ** *******     **    **      **      **      **     **         *******     **         
   *        **    **    **     **      *  **          **    **      **      **      **     **         **          **         
  *****      **   **    **      *******   ****    *   **    **      **       ******* **    ***        ****    *   ***        
 *   ****    ** *  *****         *****     *******    ***   ***      **       *****   **    ***        *******     ***       
*     **      **    ***                     *****      ***   ***                                        *****                
*                                                                                                                            
 **
'''

knightImg = '''
                          ,dM
                         dMMP
                        dMMM'
                        \\MM/
                        dMMm.
                       dMMP'_\\---.
                      _| _  p ;88;`.
                    ,db; p >  ;8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  ;_  |
                   |    |`T88P_ /  `\;
                   :_.-~|d8P'`Y/    /
                    \\_   TP    ;   7`\\
         ,,__        >   `._  /'  /   `\\_
         `._ """"~~~~------|`\\;' ;     ,'
            """~~~-----~~~'\\__[|;' _.-'  `\\
                    ;--..._     .-'-._     ;
                   /      /`~~"'   ,'`\\_ ,/
                  ;_    /'        /    ,/
                  | `~-l         ;    /
                  `\\    ;       /\\.._|
                    \\    \\      \\     \\
                    /`---';      `----'
                   (     / 
                    `---'
'''

wizardImg ='''
                    / \\
                  .'* */
               __/_*_*(_
              / _______ \\
             _\\_)/___\\(_/_ 
            / _((\\0-0/))_ \\
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \\
           / _ \ - | - /_  \\
          (   ( .;""";. .)  )
         _\\"__ /(    )\\ __"/_
            \\/  \\'  ' /  \\/
             ( ' '...' ' )
              / /  |  \\ \\
             / .   .   . \\
            /   .     .   \\
           /   /   |   \\   \\
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(___________\____.dBBBb.________)____)
'''

archerImg = '''
                                                       \\. 
                                                      /|.
                                                   /   |.
                                                 /     |.
                                               /       |.
                                             /         |.
                                          /            |.
        -\\                              /              |.
          \\\                          /                |.
           \\\                       /                  |.
            \\|                    /                    |\\
              \\#####\\           /                      ||
          ==###########>      /                        ||
           \\##==      \\     /                          ||
      ______ =       =|___/__                          ||
  ,--' ,----`-,__ ___/'  --,-`-========================##==========>
 \\               '        ##______ ____ ____,--,_____,=##,__
  `,    __==    ___,-,__,--'#'  ==='   `-'           | ##,-/
    `-,____,---'       \\####\\          |     ____,---\_##,/
        #_              |##   \\  __,--==,__,--'        ##
         #              ]===--==\\                      ||
         #,             ]         \\                    ||
          #_            |           \\                  ||
           ##_       __/'             \\                ||
            ####='     |                \\              |/
             ###       |                  \\            |.
             ##       _'                    \\          |.
            ###=======]                       \\        |.
           ///        |                         \\      |.
           //         |                           \\    |.
                                                    \\  |.
                                                      \\|.
                                                       /.
'''

dragon = '''\
                                                    ___
                                                  .~))>>
                                                 .~)>>
                                               .~))))>>>
                                             .~))>>             ___
                                           .~))>>)))>>      .-~))>>  
                                         .~)))))>>       .-~))>>)>
                                       .~)))>>))))>>  .-~)>>)>
                   )                 .~))>>))))>>  .-~)))))>>)>
                ( )@@*)             //)>))))))  .-~))))>>)>
              ).@(@@               //))>>))) .-~))>>)))))>>)>
            (( @.@).              //))))) .-~)>>)))))>>)>
          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>
       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>
      )) @@*. )@@ )   (\\_(\\-\\b  |))>)) //)))>>)))))))>>)>
    (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>
     )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>
   (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._
    )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-.
 ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,
  ((@@ @@@*.(@@ .   \^^^/' (  ^   \b)))>>        .'         `,
   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,
     (@@. (@@ ).           (((   ^    `\\        |               `.
       (*.@*              / ((((        \\        \      .         `.
                         /   (((((  \\    \\    _.-~\     Y,          \\
                        /   / (((((( \\    \\.-~   _.`" _.-~`,        ;
                       /   /   `(((((()    )    (((((~      `,      ;
                     _/  _/      `"""/   /'                  ;     ;
                 _.-~_.-~           /  /'                _.-~   _.'
               ((((~~              / /'              _.-~ __.--~
                                  ((((          __.-~ _.-~
                                              <.~~~.~'
'''

turnCount = 1

print(title)
time.sleep(1)
print(choose)
time.sleep(1)

classType = input('''
Enter 1 of the following: 
 --- Knight
 --- Mage
 --- Archer
''')
name = input("What is your name?: ")
if classType == "Knight":
    Player = Knight(name,2,3,4,5,2,'k')
elif classType == "Archer":
    Player = Archer(name,2,3,4,5,2,'a')
elif classType == "Mage":
    Player = Mage(name,2,3,4,5,2,'m')
else:
    print("Uh ohs. we made an oopsie UwU")

GameWorld = Biome(['Red Wood National Park','Spooky Woods','Hidden Grove','Forest Hut'],
                  ['Mount Denali National Park','Snowy Peaks','Raging River','Log Cabin'],
                  ['Grand Cayone','Ososis','Dunes','Hidden Cave'],"G")
choice = input("Choose an area, F,M,D")
GameWorld.PickAreaEvent(choice)
gameItems.getItems(Player)

#-----GLOBAL CODE BELOW----------------------------------------
#player = Mage('billy',2,3,4,5,2,'m')
#gameItems.getItems(player)
        

#Comment turn counter increase dark clouds recycle strs with while loop

