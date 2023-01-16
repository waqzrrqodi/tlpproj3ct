#introduction
INTRO_TXT = '''
You wake up in the middle of a street, surrounded by dilapidated buildings and rubbish. 
After looking around you realize that the area is completely empty. 
The rain weighs down on your shoulders and it grows heavier with every second that passes. 
You take a few steps forward and notice a sign that reads "Rimbo Bus Station". 
The words make you fall to your knees, and you realize that you are in the middle of Sweden's 
most dangerous city. You build up the courage to stand back up. The only path is forward.
'''
INTRO_TXT = [INTRO_TXT]


#Route 1 - "Bus Stop"
R1_TXT1 = '''
You decide to wait for the bus. You stand there in the cold for hours on end, 
until you see a pair of headlights in the distance. A bus approaches and a group 
of rogue goblins hop out. They run towards you and a fight breaks out.
'''
# Battle - Goblins
R1_TXT2 = '''
You won the battle and proceed to steal the bus and drive away. You drive until you run out of fuel.
'''
ROUTE1 = [R1_TXT1, R1_TXT2]


#Route 2 - "The Dark Alley"
R2_TXT = '''
You enter the alley, and find a suspicious wardrobe. 
Your curiosity makes you want to open it, but it might be dangerous. 
You open it, only to find a strange man with glasses and a bowl cut. 
He jumps out at you and a fight begins.
'''
# Battle - Simpa
ROUTE2 = [R2_TXT]


#Route 3 - "Go Beyond the Rickety Bridge"
R3_TXT = '''You go towards the rickety bridge and get approached by a massive muscular testosterone-
fueled man. He presents himself as Martin Loman. He gets extremely close 
to you and whispers in your ear "don't go beyond the rickety bridge" before disappearing without a trace. 
You ignore his warning and go beyond the bridge only to see a strange man running in your direction. You realize that it isn't 
an ordinary man, it's Pangloss from the hit new york time's best seller candide, written by Voltaire. 
He swings his arms towards you in a wild manner, and a fight breaks out.
'''
# Battle - Pangloss
ROUTE3 = [R3_TXT]


#Route 4 - "Missile silo"
R4_TXT = '''
You enter the abandoned missile silo and see two people fighting over a protein shake. 
One of the people is Neo Malmros, a local warlord. The other one is Bilo, an infamous sex-offender. 
Neo asks you to help him take the protein shake, Bilo also asks you to steal the shake. You choose
to help Neo, because nobody wants to help a sex offender.
'''
#Battle - Bilo
ROUTE4 = [R4_TXT]


#Route 5 - "Penjamin City"
R5_TXT1 = ''' 
You make your way towards the house but a group of goblins storm you before there is a chance to react. 
A fight begins.
'''
# Battle - Goblins
R5_TXT2 = '''
You beat the goblins and enter the house. You're greeted by a strange man who sits on a throne. 
He takes a sip from his vape before introducing himself to you. He says that his name is Fulcrum and 
that he's the leader of the goblins. He offers a treaty of peace but a dire political situation breaks out
in the city of Manzanillo, New Mexico, which causes him to reconsider his offer and violently insult you
instead. You feel offended and decide that you have to attack him to protect your honour.
'''
# Battle - Fulcrum
ROUTE5 = [R5_TXT1, R5_TXT2]


#Route 6 - "Dark Forest"
R6_TXT = '''
You enter the forest and find a giant man surrounded by steroid needles. He looks at you and starts
speaking gibberish. He pulls out a rolling pin and a fight breaks out.
'''
#Battle - Steroid Beast
ROUTE6 = [R6_TXT]


#Route 7 - "Shop"
R7_TXT1 = '''
You enter the small shop and decide to browse through the various products that are on display.
'''
# Enter shop
ROUTE7 = [R7_TXT1]


#Route 8 - "Landfill"
R8_TXT1 = '''
You dig around in the landfill and find a rare item!
'''
#Gives the player an item.
ROUTE8 = [R8_TXT1]


#Route 9 - "Shitty game development studio"
R9_TXT1 = '''
You come closer and see a massive sign with the words "Candide Productions". A homeless man stumbles out of the
building and attempts to rob you. A fight begins.
'''
#Battle - Homeless man
R9_TXT2 = '''
After defeating him you realize that he's just a victim of Candide Productions, and their awful ways. You
take him to a homeless shelter and are rewarded with a bag of cocaine.
'''
#Gives the player a bag of cocaine
ROUTE9 = [R9_TXT1, R9_TXT2]


#Route 10 - "Concentration camp for virgins"
R10_TXT1 = '''
You walk towards the concentration camp and decide that you have to free all of the virgins. You unsheathe your blade
challenge the guards to a duel.
'''
#Battle - The Anti-Virgin
R10_TXT2 = '''
You win and free all of the virgins. They run into the sunset and live to fuck another day.
'''
ROUTE10 = [R10_TXT1, R10_TXT2]


# Coward Ending
COWARD_END = '''
You attempt to flee but get tracked down and captured by Rimbo advanced special forces. 
They attack you with spears and tie you to a cross. You are branded as a coward and live your 
life in agony, unable to ever escape from Rimbo.
'''


NORMAL_DEATH = '''
You have fallen, and have thus been eternally condemned to the endless dead end that is Rimbo. Any chance of
escaping has vanished into thin air, as you draw your last breath and become a trapped spirit, forever chained
to the worst hellscape in all of the realms.
'''


# The Ending
TRUE_END = '''
You see the road to Norrtälje, but there is an intimidating figure in the distance blocking your path. 
The figure sprints towards you at an inhuman speed. You get a closer look and realize that it's the 
infamous finnish terrorist, Valma the Soulbroken. She is your final obstacle, if you want to get to Norrtälje you 
have to defeat her. 
'''
# Battle - Waldy
TRUE_END_WIN = '''
You have won, finally. Now you have one final choice, will you send Valma to the shadow realm or 
let her walk among mortals?
'''
TRUE_END_DEATH = '''
Valma deals her final blow, killing you and binding your soul into an eternal contract. You become her
pawn, unable to make your own decisions or think for yourself. Your foolish ambitions has led to a fate 
worse than death. You grasp the last piece of your conciousness as it fades away, leaving you as a mindless
husk.
'''
FINAL_SCENE = '''

'''
# Choices:
# 1 - Kill her
# 2 - Let her live

ROUTE = [ROUTE1, ROUTE2, ROUTE3, ROUTE4, ROUTE5, ROUTE6, ROUTE7, ROUTE8, ROUTE9, ROUTE10]