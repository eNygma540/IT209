# -----------------------------------------------
# //Game Title                                  |
# Billy Duggleby & Brendon Lugo                 |
# © 2019 B.Duggleby, B.Lugo All Rights Reserved |
# -----------------------------------------------
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
Enter 1 of the following: 
 --- Knight
 --- Mage
 --- Archer

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
time.sleep(15)
print(choose)
time.sleep(15)

print (menu)
classType = input('''
Enter 1 of the following: 
 --- Knight
 --- Mage
 --- Archer
'''
name = input("What is your name?: ")
if classType == lower("Knight"):
    k = Char(pname = Name,ClassType="knight",Hp, Att, Def)
elif classType == lower("Archer"):
    a = Char(pname = Name,ClassType="archer",Hp, Att, Def)
elif classType == lower("Mage"):
    k = Char(pname = Name,ClassType="mage",Hp, Att, Def)
else:
    print("Uh ohs. we made an oopsie UwU")



class Items(self,charType):
        if charType == lower("knight"):
            knightems = {"Dagger":1,"Broadsword":2,"Greataxe":2,"Rubber Chicken":3,'Apple':1,"Turkey leg":2,"Chipotle":3}
            return random.choice(list(knightems))
        elif charType == lower("archer"):
            archItems = {"Yew longbow":2,"Nerf bow":1,"Magic bow":3,"Crossbow":2,'Apple':1,"Turkey leg":2,"Chipotle":3}
            return random.choice(list(archItems))
        elif charType == lower("mage"):
            mageItems = {"Choatic staff":3,"Spellbook":2,"Useless stick":1,"Magic wand":2,'Apple':1,"Turkey leg":2,"Chipotle":3}
            return random.choice(list(mageItems))


if turnCount == 1:
    
