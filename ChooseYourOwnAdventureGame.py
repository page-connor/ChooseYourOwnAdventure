print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")

print("Your mission is to find the treasure.\n")

print('You come to a fork in the road! There is a sign in the center thar reads \"Left\" or \"Right\".')
print('\nThe left sign has moss covering the border of the sign.')
print('The right sign looks to be a bit worn and neglected.')

choice_1 = input("\nWhich direction do you choose to go? (Left or Right): ")

if choice_1.lower() == 'right':
    print('\nYou decide to go right!\n')

    print('You begin walking along a trail that is quite dry and dilapidated. After a few minutes of walking, you hear a crack and snap!')
    print('The ground below you begins to give way! The earth around you swoops past you as you become surrounded in darkness!')
    print('\nYou fell into a deep hole! Game Over!\n')
elif choice_1.lower() == 'left':
    print('\nYou choose to go left!\n')

    print('You travel along a path surrounded by a lush forest. The emerald hues of hope guide you forward to safety.')
    print('After walking for about twenty peaceful minutes, you see a river in front of you and you stop before it.')
    print(r"""
    **********************************************************************************
                                  _.._
               _________....-~    ~-.______
            ~~~                            ~~~~-----...___________..--------
                                                       |   |     |
                                                       | |   |  ||
                                                       |  |  |   |
                                                       |'. .' .`.|
            ___________________________________________|0oOO0oO0o|____________
             -          -         -       -      -    / '  '. ` ` \    -    -
                  --                  --       --   /    '  . `   ` \    --
            ---            ---          ---       /  '                \ ---
                 ----               ----        /       ' ' .    ` `    \  ----
            -----         -----         ----- /   '   '        `      `   \
                 .-~~-.          ------     /          '    . `     `    `  \
                         -------           /  '    '      '      `
                                 --------/     '     '   '
    ***********************************************************************************
    """)

    print('\nYou take a moment to observe the river. It appears as deep as your waist, you could wade through it. But, the water seems to be flowing a little strong.')
    print('However, you see a ferry to your right. No one appears to be present to sail you across. But, you could wait to see if the owner appears.')

    choice_2 = input("\nWhat do you decide to do? (Swim or Wait): ")

    if choice_2.lower() == 'swim':
        print('\nYou decide to swim!\n')
        print('You plunge into the water. It is indeed waist deep, and you find your footing on the riverbed. You wade through the treacherous water.')
        print('You emerge victorious! No river shall conquer you!')
        print('Upon climbing out of the river, a dirt path sits before you.')
        print('You walk along the path to find a shack with three different colored doors.')
        print('One is red, one is yellow, and one is blue.')
        print(r"""
        ***************************
                __________
               |  __  __  | 
               | |  ||  | |  
               | |  ||  | |
               | |__||__| |
               |  __  __()|
               | |  ||  | |
               | |  ||  | |
               | |  ||  | |
               | |  ||  | |
               | |__||__| |
               |__________|
        ***************************
        """)

        choice_3 = input('\nWhich door do you decide to open? (Red, Yellow, or Blue): ')
        if choice_3.lower() == 'red':
            print('\nYou decide to open the Red door!\n')
            print('Upon placing your hand on the doorknob, you noticed it felt warm to the touch. This was odd, but you remained steadfast.')
            print('You firmly grasped the doorknob, twisted it, and yanked the door open, only to be met with fierce flames that engulf the air around you!')
            print('\nYou met a painful death and burned alive! Congratulations! You did not find the treasure! Game Over!\n')
            print(r"""
            ******************************************
                        (  .      )
                   )           (              )
                         .  '   .   '  .  '  .
                (    , )       (.   )  (   ',    )
                 .' ) ( . )    ,  ( ,     )   ( .
              ). , ( .   (  ) ( , ')  .' (  ,    )
             (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ******************************************
            """)
        elif choice_3.lower() == 'blue':
            print('\nYou decide to open the Blue door!\n')
            print('You just noticed that the blue door seems a little more worn than the rest. No matter, you will press on!')
            print('You swiftly open the blue door and are quite surprised by what you see. Inside the room is...')
            print()
            print()
            print()
            print()
            print('Nothing!')
            print()
            print()
            print()
            print()
            print('As in, the black nothingness of space! You are sucked into a black hole!')
            print('After all of the air was sucked out of your lungs and your eyes forced their way out of your skull, you wondered why you didn\'t open a different door.')
            print('You were met with a dark and lonely end in space. At least it was a quick death. Congratulations! You did not find the treasure! Game Over!')
            print(r"""
            *********************************************************
                                           .       . 
                             +  :      .
                                       :       _
                                   .   !   '  (_)
                                      ,|.' 
                            -  -- ---(-O-`--- --  -
                                     ,`|'`.
                                   ,   !    .
                                       :       :  " 
                                       .     --+--
                             .:        .       !
            ********************************************************
            """)
        elif choice_3.lower() == 'yellow':
            print('\nYou decide to open the Yellow door!\n')
            print('You faced the yellow door with determination. You stared at it with pure intent.')
            print('You said aloud \"I will open you.\"')
            print('And with that final word, you twisted the brass doorknob with confidence, and pulled the door open with tremendous gusto.')
            print('Finally, you laid your weary eyes upon the most beautiful treasure chest you had ever seen.')
            print('Lacquered mahogany was bordered with golden seals. And to your surprise, there was no lock!')
            print(r"""
            **************************************************************
                                            _.--.
                                        _.-'_:-'||
                                    _.-'_.-::::'||
                               _.-:'_.-::::::'  ||
                             .'`-.-:::::::'     ||
                            /.'`;|:::::::'      ||_
                           ||   ||::::::'     _.;._'-._
                           ||   ||:::::'  _.-!oo @.!-._'-.
                           \'.  ||:::::.-!()oo @!()@.-'_.|
                            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
                              `>'-.!@%()@'@_%-'_.-o _.|'||
                               ||-._'-.@.-'_.-' _.-o  |'||
                               ||=[ '-._.-\U/.-'    o |'||
                               || '-.]=|| |'|      o  |'||
                               ||      || |'|        _| ';
                               ||      || |'|    _.-'_.-'
                               |'-._   || |'|_.-'_.-'
                                '-._'-.|| |' `_.-'
                                    '-.||_/.-'

            **************************************************************
            """)
            print('This was what you were waiting for! The moment of truth! You were finally going to see this treasure!')
            print('You planted your hands firmly on top of the chest, and lifted with all your might!')
            print('On the inside of this fabulous chest was...')
            print('A mirror???')
            print('Why of course it\'s a mirror! Because you were the treasure all along!!! ^_^')
            print('\nCongratulations! You found the treasure! Now go have a good day you wonderful soul!')
        else:
            print('\nYou did not choose to open a door!\n')
            print('You should know by now that indecision is still a decision. A decision to make no decision.')
            print('You did not open any door, and stood there like a silly goose choosing between doors.')
            print('Because you stood in the same place without choosing a door, a meteorite flew threw the sky and embedded itself in the grass before you.')
            print('You only had mere seconds to realize that the meteorite plunged its way through your entrails and eviscerated you.')
            print('You see the words \"YOU DIED\" appear in front of your eyes like you were playing some game.')
            print('\nA meteorite destroyed your guts and killed you because you did not choose a door! You did not find the treasure! Game Over!\n')
    else:
        print('\nYou decide to wait!\n')
        print('After waiting for about an hour, you hear a snap in the forest behind you.')
        print('Suddenly, a whizzing sound announces the immediate dark that envelopes you. An arrow planted itself firmly into your cranium.')
        print('\nYou waited too long and a bandit archer snuck up on you. You died from an arrow to the head! Game Over!\n')
        print(r"""
        *************************
                  |-  -|    //
             <----|O  O|---<<<
                  |  ^ |    \\
                  | -- |
                   \__/
        *************************
        """)

else:
    print('You did not choose left or right!\n')
    print('After a while of staring at the signs, without making a decision, day turns to night.')
    print('The only light you see are blue rays from the full moon in the sky. Through the moonlight peering through trees you see a silhouette move closer to you.')
    print('Suddenly, the silhouette appears in front of your face! You remember the full moon, and breathe your last.')
    print('\nBecause you did not make a decision, a werewolf found you and murdered you! Game Over!\n')
    print(r"""
    *************************************************************************
                                /\
                                ( ;`~v/~~~ ;._
                             ,/'"/^) ' < o\  '".~'\\\--,
                           ,/",/W  u '`. ~  >,._..,   )'
                          ,/'  w  ,U^v  ;//^)/')/^\;~)'
                       ,/"'/   W` ^v  W |;         )/'
                     ;''  |  v' v`" W }  \\
                    "    .'\    v  `v/^W,) '\)\.)\/)
                             `\   ,/,)'   ''')/^"-;'
                                  \
                                   '". _
                                        \
    ************************************************************************
    """)
