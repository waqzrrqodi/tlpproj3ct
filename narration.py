#introduction
intro_txt1 = '''
You wake up in the middle of a street, surrounded by dilapidated buildings and rubbish. 
After looking around you realize that the area is completely empty. 
The rain weighs down on your shoulders and it grows heavier with every second that passes. 
You take a few steps forward and notice a sign that reads "Rimbo Bus Station". 
The words make you fall to your knees, and you realize that you are in the middle of Sweden's 
most dangerous city. You build up the courage to stand back up. The only path is forward.
'''
intro_txt2 = '''
You notice a monitor below the sign, it displays the timetable for bus arrivals. 
The only trip is to Norrtälje, and the time of departure is suspiciously missing. 
Apart from that you see a dark alley and a rickety bridge. You have to choose between 
a bus that may never arrive, a mysterious dark alley and a rickety bridge. What will you do?
'''

# Choices:
# 1 - Wait for the bus
# 2 - Dark Alley
# 3 - Rickety Bridge


#Route 1 - "Wait for the bus"
r1_txt1 = '''
You decide to wait for the bus. You stand there in the cold for hours on end, 
until you see a pair of headlights in the distance. A bus approaches and a group 
of rogue goblins hop out. They run towards you and a fight breaks out.
'''
# Battle - Goblins
r1_txt2 = '''
You won the battle and proceed to steal the bus and drive away. You drive until you run out of fuel.
'''


#Route 2 - "The Dark Alley"
r2_txt1 = '''
You enter the alley, and find a suspicious wardrobe. 
Your curiosity makes you want to open it, but it might be dangerous. 
'''
# Choices:
# 1 - Approach
# 2 - Ignore
r2_txt2_option1 = '''
You open it, only to find a strange man with glasses and a bowl cut. 
He jumps out at you and a fight begins.
'''
# Battle - Simpa
r2_txt2_option2 = '''
You ignore the wardrobe, and proceed forward through the alley. 
Not getting any items and feeling depressed.
'''


#Route 3 - "Go Beyond the Rickety Bridge"
r3_txt1 = '''You go towards the rickety bridge and get approached by a massive muscular testosterone-
fueled man. He presents himself as Martin Loman, first of his name, king of the andals and the rhoynar 
and the first men, lord of the seven kingdoms and protector of the realm. He gets extremely close 
to you and whispers in your ear "don't go beyond the rickety bridge" before disappearing without a trace. 
Will you still continue?'''
# Choices:
# 1 - Proceed
# 2 - Go back
r3_txt2_option1 = '''
You go beyond the bridge and see a strange man running in your direction. You realize that it isn't 
an ordinary man, it's Pangloss from the hit new york time's best seller candide, written by Voltaire. 
He swings his arms towards you in a wild manner, and a fight breaks out.
'''
# Battle - Pangloss
r3_txt2_option2 = '''
You depressingly stumble back to the bus station, feeling like you missed out on something. 
The bus has already left, so your only choice is to go through the alley.
'''
# Sends you to Route 2


#Route 4 - "Missile silo"
r4_txt1 = '''
You enter the abandoned missile silo and see two people fighting over a protein shake. 
One of the people is Neo Malmros, a local warlord. The other one is Bilo, an infamous sex-offender. 
Neo asks you to help him take the protein shake, Bilo also asks you to steal the shake. 
What will you do? 
'''
# Choices:
# 1 - Help Neo (Battle - Bilo)
# 2 - Help Bilo (Battle - Neo)
# 3 - Escape (Coward Ending)


#Route 5 - "Penjamin City"
r5_txt1 = ''' 
You make your way towards the house but a group of goblins storm you before there is a chance to react. 
A fight begins.
'''
# Battle - Goblins
r5_txt2 = '''
You beat the goblins and enter the house. You're greeted by a strange man who sits on a throne. 
He takes a sip from his vape before introducing himself to you. He says that his name is Fulcrum and 
that he's the leader of the goblins. He offers a treaty of peace but a group of bandits storm into 
the room before you get to speak any further. You're gravely outnumbered, will you fight for the 
bandits or alongside Fulcrum?
'''
# Choices:
# 1 - Fight for Fulcrum (Battle - bandits)
# 2 - Fight for bandits (Battle - Fulcrum)
# 3 - Escape


# Coward Ending
coward_end = '''
You get tracked down and captured by Rimbo advanced special forces. 
They attack you with spears and tie you to a cross. You are branded as a coward and live your 
life in agony, unable to ever escape from Rimbo.
'''


# True Ending
true_end = '''
You stumble out the backdoor and see the road to Norrtälje, but there is an intimidating figure in 
the distance blocking your path. The figure runs towards you at an inhuman speed and attempts to punch 
you, and you just barely manage to dodge the blow. You get a closer look and realize that it's the 
infamous finnish terrorist, Valma. She is your final obstacle, if you want to get to Norrtälje you 
have to defeat her. 
'''
# Battle - Waldy
true_end_win = '''
You have won, finally. Now you have one final choice, will you send Valma to the shadow realm or 
let her walk among mortals?
'''