from inspect import _empty
import sys
import time

item = []
party = []
savior = []
status = []
ending = []
discovered_items = set()
discovered_companions = set()
discovered_paths = set()

def typewriter(text, delay=0.06, newline=True):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(delay)
	if newline:
		print()

def type_inline(text, delay=0.06):
	typewriter(text, delay, newline=False)

def game_over():
	typewriter("YOU HAVE DIED")
	typewriter("🧿: It's not your time yet...")
	typewriter("(You see everything that has happen till this point flashing past your subconscious body...)")
	typewriter("🧝: I'm back here again?")
	print()

def intro():
	typewriter("You open your eyes and see a floating ball of blue light.")
	typewriter("🧝: Huh? Who are you? Why was I asleep on the school hallway?")
	typewriter("🧿: I don't have time to explain why I don't have time to explain!")
	typewriter("🧿: I'll tell you the details when we are on the way.")
	
	typewriter("🧿: Never noticed you in these halls before. What is your name?")
	name = input("Enter your nickname: ")
	typewriter("🧿: Woah, kid, you've got the same name as the famous " + name + " VI.")
	typewriter("🧿: I can tell you're going places.")
	typewriter("🧝: Thanks...I guess?")
	typewriter("🧿: Anyways, it's dangerous to go empty-handed! Take this!")
	typewriter("(Receives Sword of Truth 🗡️)")
	typewriter("🧝: The sword is cool and all, but where are we going?")
	typewriter("🧝: Who or what are you? What happened to everybody?")
	print()
	typewriter("(You see students collapsed all over the floor...)")
	print()
	typewriter("🧿: I am an overseer of time and space.")
	typewriter("🧿: A primordial being named Chronos has escaped from the prison we created.")
	typewriter("🧿: As you can see, the people in this region have fallen into eternal slumber.")
	typewriter("🧿: With each passing minute, their energy is slowly being drained. I came here to set things straight.")
	typewriter("🧿: I can't see what makes you special; nonetheless, you are the only one awake in this school.")

	while True:
		save_world = input("Please tell me you will help save the world...(Y/N)\n").lower().strip()
		if save_world == "y":
			savior.append("y")
			act_1_1()
		elif save_world == "n":
			savior.append("n")
			act_1_2()
		else:
			typewriter("Invalid input. Try again.")
			continue
def act_1_1():
	typewriter("🧝: Of course I will! These are my people! I can't just survive alone.")
	typewriter("🧿: Okay then... I sense some energy in the Administration Building.\n🧿: Let's head over there first.")
	print()
	path_1()

def act_1_2():
	print()
	typewriter("🧝: Why should I? There's nothing in it for me and I do just fine on my own.")
	typewriter("🧿: What a relief! I was forced to come and act as the savior's helper when that's just not me!")
	typewriter("🧿: I would much prefer just chilling in this new world.")
	typewriter("🧿: Why don't we check out the Administration Building? I sense some energy. \n🧿: Maybe we can find others to join us!")
	print()
	typewriter("🧝: A bit of company wouldn't hurt I guess...")
	path_1()

def path_1():
	typewriter("🧝: Hey, I don't remember these two hallways in school before.")
	typewriter("🧿: I guess space and time really got messed up.")
	print()
	typewriter("[Path #1: a straight but long hallway with no end in sight.]")
	typewriter("🧿: I feel like this is a trap...")
	print()
	typewriter("[Path #2: a dim hallway with the largest spiders you can imagine crawling on the walls.]")
	typewriter("🧿: I hate spiders, but if I know my movies, it might be guarding something?")
	print()

	while True:
		path_choice_1 = input("Which path do you want to take? (Enter 1 or 2)\n")
		if path_choice_1 == "1":
			path_1_1()
			break
		elif path_choice_1 == "2":
			path_1_2()
			break
		else:
			typewriter("Invalid path. Try again.")
			continue

def path_1_1():
	typewriter("(You continue down the straight hallway, waiting for some event to occur...)")
	typewriter("(Nothing happens and you start sprinting down the hall.)")
	battle_1()

def path_1_2():
	typewriter("(You take a step towards the spider-infected halls...)")
	typewriter("(The spiders seem to sense your fear and start moving in on you!)")
	typewriter("🧿: I should have guessed this would happen!")
	print()
	typewriter("(You take out the sword and swing it at one of the spiders.)")
	typewriter("(The spider's head comes flying off and it lets out a final shriek.)")
	typewriter("(You received the spider carcass 🕷️)")
	item.append("Spider carcass")
	typewriter("(The other spiders cower and flee.)")
	typewriter("🧿: Woah... You are either really strong or just really lucky...")
	typewriter("(You rush past the dingy hallway.)")
	print()
	battle_1()

def battle_1():
	typewriter("(You see your homeroom teacher Ellie but she seems weirdly shrouded in some kind of mist.)")
	typewriter("(You hurry towards her...)")
	typewriter("Ellie: Heh! Didn't think that you of all people would be facing me!")
	typewriter("🧝: What are you talking about? Are you really my teacher?")
	typewriter("Ellie: I'm not the old and weak me you knew before. I'm the few chosen by Chronos and I feel great!")
	typewriter("Ellie: I won't have you ruin this new world! Face me!")
	time.sleep(1)
	menu_1()
def menu_1():
	print()
	print("==============")
	print("=  (A)ttack  =")
	print("=   (T)alk   =")
	print("=   (I)tem   =")
	print("==============")
	print()

	player_select_1 = input("Choose your action: (Enter a/t/i.)\n").lower().strip()
	if player_select_1 == "a":
		print()
		print("======================")
		print("=   (S)word Slash    =")
		print("= (C)ompanion Attack =")
		print("=       (B)ack       =")
		print("======================")
		attack_choice = input("Choose your attack: (Enter s/c/b.)\n").lower().strip()
		print()
		if attack_choice == "s":
			typewriter("(You swing your sword and slashed through Ellie in a split second.)")
			typewriter("Ellie: I wasn't expecting you to be able to just kill someone so easily...\nI guess I was too naive...")
			typewriter("(Ellie collapses with a thud.)")
			typewriter("🧿: Even I didn't see that coming...Good job?")
			typewriter("🧝: Hmm, I don't really feel that awful. In fact, I love the raw power I now wield.")
			path_2()
		elif attack_choice == "c":
			if any(party):
				print(*party, sep="\n ")
				party_choice = input("Choose a member: (Enter first letter)\n")
				print()
			else:
				typewriter("You do not have any companions.")
				menu_1()
		elif attack_choice == "b":
			menu_1()
		else:
			typewriter("Invalid input. Try again.")
			menu_1()
	elif player_select_1 == "t":
		print()
		if "y" in savior:
			typewriter("🧝: I never thought you were weak before. When being good is not always rewarded,\nthe kindness you possessed was what I regard as the rarest power.")
			typewriter("🧝: Can you really live in this world without belonging to any community?")
			typewriter("🧝: Please, think twice. Helping me save the world is the best way to show your true strength.")
			typewriter("Ellie: You make a good point... Its only been a few minutes, but I already feel bored.")
			typewriter("Ellie: Why don't I join you? I want to take some time on the road to figure out where I really belong.")
			party.append("Ellie")
			path_2()
		if "n" in savior:
			typewriter("🧝: Wait up, I don't want to defeat you. I just came to see if anyone was also awake and want to chill with us!")
			typewriter("Ellie: So...You don't want to save everybody? Interesting...")
			typewriter("Ellie: How can I believe you? ")
			typewriter("🧝: Why don't you join us and see for yourself?")
			typewriter("Ellie: You know what, why not! I'm pretty bored anyways.")
			typewriter("(Ellie joins the party.)")
			party.append("Ellie")
			path_2()
		else:
			typewriter("Invalid input. Try again.")
			print()
			menu_1()
	elif player_select_1 == "i":
		if any(item):
			print("================")
			print(*item, sep="\n")
			print("================")
			print("(B)ack")
			print()
			item_choice = input("Choose an item: (Enter first letter)\n").lower().strip()
			print()
			if item_choice == "s":
				typewriter("(You pulled out the spider carcass...)")
				item.remove("Spider carcass")
				typewriter("Ellie screams in shock and fainted!")
				typewriter("🧝: Well, that was unexpected! Good thing I didn't have to attack her.")
				path_2()
			elif item_choice == "b":
				menu_1()
			else:
				typewriter("Invalid input. Try again.")
				print()
				menu_1()
		else:
			typewriter("(You rummaged through your bag, but cannot find anything useful.)")
			print()
			menu_1()
	else:
		typewriter("Invalid input. Try again.")
		print()
		menu_1()

def path_2():
	typewriter("(You opened the door behind Ellie and walked out of the school)")
	print()
	typewriter("You enter the city and everything is out of order as expected.")
	typewriter("There are cars in the middle of the road and people are laying all over the ground.")
	print()
	
	if "y" in savior:
		typewriter("🧿: I really think you'll be crushed by Chronos in your current state.")
		typewriter("🧿: Maybe we should look around the city to find something to protect ourselves.")
	elif "n" in savior:
		typewriter("🧿: If we run into Chronos by mistake, you will definitely be crushed.")
		typewriter("🧿: Maybe we should look around the city to find something to protect ourselves.")
	
	typewriter("🧝: Good idea. Why don't we head over there?")
	typewriter("(You point towards the east.)")
	typewriter("(There are two buildings that connect different parts of the city.)")
	print()
	typewriter("[Building #1: a local coffee shop]")
	typewriter("🧿: I cannot explain the warm, fuzzy feeling I feel when I look at this place.")
	print()
	typewriter("[Building #2: a robot factory]")
	typewriter("🧿: That looks like a fun place for adventuring.")
	print()

	while True:
		path_choice_2 = input("🧿: Where should we go? (Enter 1 or 2)\n")
		if path_choice_2 == "1":
			path_2_1()
		elif path_choice_2 == "2":
			path_2_2()
		else:
			typewriter("Invalid input. Try again")
			continue
def path_2_1():
	print()
	typewriter("🧝: I'm really craving some coffee now. I might be able to make some in that shop!")
	typewriter("(You enter the shop and made some coffee.)")
	typewriter("(You drink the coffee and feel energized.)")

	if "Ellie" in party:
		typewriter("🧝: Ellie, you wanna drink some coffee for the road?")
		typewriter("Ellie: Feels like a century since I had a nice cup of joe.\n I guess tagging along might be good after all.")

	typewriter("🧿: Coffee is one of the few humanly things I'm curious about.\nToo bad I'll never have the chance to really taste it though.")
	typewriter("(You found a bottle of coffee ☕ and put it in your bag.)")
	status.append("Coffee")
	item.append("Coffee")
	print()
	battle_2()

def path_2_2():
	print()
	typewriter("🧝: How'd you know I love adventuring? Always wanted to check out that kind of factory.")
	typewriter("(You enter the factory and see half-built robots scattered all around.)")
	typewriter("🧿: They almost seem sad to me in this state.")
	print()
	typewriter("🧝: These look like the tenth-gen V2077s.")
	typewriter("🧝: You know... So many machines get put out of use every time a new generation is released.")
	typewriter("🧝: Perhaps its better that production factories shut down once and for all.")
	print()
	typewriter("(A shadow moved slightly upon hearing your words.)")
	print()
	typewriter("Third-gen robot: Human, special. I am ROB. Very Scared here... \nROB: Request to follow and serve human. Please say 'Okay, Rob' to issue command.")
	print()
	typewriter("🧝: Woah, a Replicant Ops Bot! Glad to have you joining us little guy!")
	typewriter("🧝: I mean, okay ROB, follow me.")
	typewriter("(ROB joins the party.)")
	print()

	if "Ellie" in party:
		typewriter("Ellie: Brings back my memories as a lonely kid. \nEllie: My grandma had one of these and I would spend the whole night talking to ROB \neven if he could only respond in the simplest way.")
		if "y" in savior:
			typewriter("🧝: Maybe he can make you recall parts of yourself that you didn't think still exists.")
		elif "n" in savior:
			typewriter("🧝: Hard to imagine you so soft. Hope ROB won't kill your vibe now.")

	typewriter("* In thought: I wonder why this old model is here? It seems to have developed more emotional capabilities than I remember...*")
	print()
	party.append("Rob")
	battle_2()

def battle_2():
	typewriter("(You exit the back and see another figure shrouded in mist.)")
	print()
	typewriter("(A weary and gruff man stood up beside a little girl in slumber as you entered his sight.)")
	typewriter("Weary Man: Hmm... there are others that are also awake...Meeting the lot of you here kinda messes up my plan...")

	if "y" in savior:
		typewriter("🧝: Who are you? What were you doing to that girl?")
	elif "n" in savior:
		typewriter("🧝: Nice flannel dude! What plan are you taking about?")

	typewriter("Weary Man: You can call me Joe. As for what I plan to do, there's ain't no use telling you.")
	typewriter("🧝: Why not? It's not like we can spill your secret to the whole world.")
	typewriter("Joe: Don't need to tell nothin to someone who ain't gonna survive beyond this point.")
	menu_2()

def menu_2():
	print()
	print("==============")
	print("=  (A)ttack  =")
	print("=   (T)alk   =")
	print("=   (I)tem   =")
	print("==============")
	print()

	player_select_2 = input("Choose your action: (Enter a/t/i.)\n").lower().strip()
	if player_select_2 == "a":
		print("======================")
		print("=   (S)word Slash    =")
		print("= (C)ompanion Attack =")
		print("=       (B)ack       =")
		print("======================")
		attack_choice = input("Choose your attack: (Enter s/c/b.)\n").lower().strip()
		print()
		if attack_choice == "s":
			if "Coffee" in status:
				typewriter("(You still feel the buzz of that coffee.)")
				typewriter("(You swing the sword with lightning speed!)")
				typewriter("(Joe didn't even have a chance to open his mouth before you cut through him like butter...)")
				status.append("joe_dead")
				if "Ellie" in party:
					typewriter("Ellie: How did you do that without any hesitation!?")
					typewriter("🧝: Survival instincts...? It was either him or us. I couldn't take the risk.")
					typewriter("Ellie: Kinda got chills thinking one of MY students can do these sort of things...")
					typewriter("🧝: I could really use a break...")
					path_3()
				else:
					typewriter("🧿: Whatever his plan was, there's no way for him to succeed now.")
					typewriter("🧝: I could really use a break...")
					path_3()
			else:
				typewriter("(You still feel tired from the last encounter...)")
				typewriter("(You swing the sword with all the strength left in your body!)")
				typewriter("(Joe took a small sidestep and dodged the attack.)")
				if item or party is empty:
					typewriter("(Joe counters with a punch to your stomach.)")
					typewriter("(You fall to the ground, defeated.)")
					game_over()
				else:
					menu_2()
		elif attack_choice == "c":
			print("======================")
			if any(party):
				print(*party, sep="\n")
				print("======================")
				party_choice = input("Choose a member: (Enter first letter)\n")
				if party_choice == "r":
					typewriter("🧝: Okay, ROB, enter attack mode!")
					typewriter("ROB: Initiating combat scenario 2...")
					typewriter("(ROB's parts begin to move into place...)")
					typewriter("(ROB transforms into a beam cannon!)")
					typewriter("(Joe didn't even get the chance to open his mouth before he was obliterated into ashes...)")
					typewriter("🧝: That was a bit extreme...But good job ROB! Thanks for saving us!")
					typewriter("ROB: First... Human saved me... Am Eternally grateful...")
					status.append("joe_dead_rob")
					path_3()
				elif party_choice == "e":
					typewriter("🧝: Ellie, do you have any tricks up your sleeve?")
					typewriter("Ellie: Actually, I do. I think Chronos gave me this to help me defeat people like you.")
					typewriter("(Ellie hands you a purple glowing crystal.)")
					item.append("Dark crystal")
					typewriter("Ellie: It's supposed to make you invincible and can make your body auto-parry any attacks for 5 minutes.")
					typewriter("🧝: The thing looks evidently evil. Is there anything else I should know?")
					typewriter("Ellie: Besides the fact that it can be only used once per day, I swear it won't hurt you in any way!")
					typewriter("Joe: Enough! It's my turn now! Take this!")
					print()
					while True:
						use_crystal = input("Use the crystal (Y/N):\n").lower().strip()
						print()
						if use_crystal == "y":
							typewriter("(Your body starts pulsing...)")
							typewriter("(You dodge Joe's steel knuckles and summon your sword to deal devastating damage all in one swift movement.)")
							typewriter("🧝: Never dreamed that my body could move like this!)")
							print()
							status.append("joe_dead_crystal")
							break
						elif use_crystal == "n":
							typewriter("(Joe smashed your head with his steel knuckles in one hit.)")
							print()
							game_over()
						else:
							typewriter("Invalid input. Try again.")
							print()
							continue
					path_3()
				else:
					typewriter("Invalid input. Try again.")
					print()
					menu_2()
			else:
				typewriter("You do not have any companions.")
				menu_2()
		elif attack_choice == "b":
			menu_2()
		else:
			typewriter("Invalid input. Try again.")
			menu_2()
	elif player_select_2 == "t":
		print()
		if "y" in savior:
			typewriter("🧝: Hold up! I don't plan on fighting anyone.")
			status.append("joe_peaceful")
			typewriter("(You hold up both hands in surrender.)")
			talk_ellie_2()
			path_3()
		elif "n" in savior:
			typewriter("🧝: Hold up! I don't plan to stop you from doing anything.")
			typewriter("🧝: I'm just curious about how other people who are still awake choose to pass their time.")
			talk_ellie_2()
			talk_n_savior_2()
			path_3()
	elif player_select_2 == "i":
		if any(item):
			print("================")
			print(*item, sep="\n")
			print("================")
			print("(B)ack")
			print()
			item_choice = input("Choose an item: (Enter first letter)\n").lower().strip()
			print()
			if item_choice == "s":
				typewriter("(You show the spider carass to Joe.)")
				typewriter("(Joe does not react at all...)")
				menu_2()
			elif item_choice == "c":
				typewriter("* In thought: It's not the best time to drink coffee now...*")
				menu_2()
			elif item_choice == "b":
				menu_2()
			else:
				typewriter("Invalid input. Try again.")
				print()
				menu_2()
		else:
			typewriter("(You rummaged through your bag, but cannot find anything useful.)")
			print()
			menu_2()
	else:
		typewriter("Invalid input. Try again.")
		print()
		menu_2()

def talk_ellie_2():
	if "Ellie" in party:
		typewriter("Ellie: Look! I can prove that the kid is telling the truth!")
		typewriter("(Ellie rolls up her sleeve and reveal a scar in the shape of a 'C'.")
		typewriter("The moment she touched the scar, Joe immediately stopped in his tracks.)")
		print()
		typewriter("Joe: You're one of Chronos' agents huh? Fine. I'll give you three minutes to talk.")
		typewriter("🧝: So...Does your plan involve a little girl? I saw you looking at a child over there.")
		talk_savior_2()
	else:
		typewriter("Joe: How the hell am I supposed to believe you? You might just come after me.")
		typewriter("🧝: Why would I do that? Does that mean you're looking for something?")
		typewriter("Perhaps...a little girl?")
		typewriter("Joe: How did you know that? Who told you!? Spill!")
		typewriter("🧝: Calm down, I just saw you looking at a child over there.")
		talk_savior_2()
def talk_savior_2():
	typewriter("Joe: Points to being observant. No harm in telling you if you're not gonna get in my way.")
	print()
	typewriter("Joe: The short version is that my daughter and I got separated a while back...")
	typewriter("Joe: Chronos showed me a vision of her lying on the ground like the rest and gave me something to revive her.")
	typewriter("Joe: Of course, in exchange I have to get rid of those that are immune to his curse.")
	typewriter("Joe: However, I'm not really the obeying type and don't plan on wasting my energy on anything except finding my baby girl.")
	print()

	if "y" in savior:
		typewriter("🧝: I understand the tough spot you are in... I want to help as many people I meet in this new world.")
		typewriter("🧝: I would love teaming up with you.")
		typewriter("🧝: Always better to have more eyes keeping a look out for your daughter, right?")
	else:
		typewriter("🧝: I see... I'm just trying to get the best out of this new world.")
		typewriter("🧝: Wouldn't mind joining paths with you and keeping a look out for your daughter.")

	typewriter("🧝: Could also use more people if we wanna survive in this strange universe.")
	typewriter("Joe: Survive... I've struggled for a long time with that word.")
	typewriter("Joe: No matter what, you keep finding something to fight for.")
	typewriter("Joe: I like the way you think, but I'm gonna have to say no.")
	print()
	typewriter("Joe: This is my own journey and I want to spend every second looking for her.")
	typewriter("Joe: If I join you, it's gonna be me who is at risk of Chronos finding out.")
	typewriter("🧝: You make a convincing point... Well, good luck then. Time to go our separate ways?")
	typewriter("Joe: Yeah, get out of here. I'll pretend I never met you.")
	typewriter("🧝: Maybe we'll meet again, hopefully with your daughter by your side!")
	print()

def talk_n_savior_2():
	typewriter("Joe: One more thing, if you want to truly live like a royal in this world, \nJoe: find Chronos and show your loyalty to him.")
	typewriter("Joe: Never in my life could I imagine a being with such overwhelming power.")
	typewriter("🧝: I'll keep your advice in my mind, thanks!")

def path_3():
	typewriter("(You start walking away from Joe and see a house in front of a bridge not far ahead.)")
	typewriter("🧝: I need a break...")
	typewriter("🧝: Let's go inside that house to rest up.")
	typewriter("(You and your party walk in silence towards the small building and you open the door.)")
	typewriter("(The wariness of pervious encounters creep up on your team all at once and everyone falls asleep...)")
	typewriter("(You wake up to a quiet morning as the sun shines on your party members' face.)")
	typewriter("(After rummaging for food in the kitchen, the party head towards the castle on the other side of the bridge.)")
	typewriter("(You and your party walks in silence...)")
	typewriter("(Suddenly, everything goes black before your eyes and you lose consciousness...)")
	print("")
	typewriter("(You open your eyes to what seems like a basement cell, where you and your party are trapped behind bars.)")
	typewriter("(You see 🧿 on the other side of the bars.)")
	typewriter("🧝: I should have known better than to trust a stranger.")

	if "ROB" in party:
		typewriter("🧝: ROB, get us out of here!")
		typewriter("(ROB raises his arm and fires a lazer beam from his fingertip...)")
		typewriter("(The bars are cut through with a single hit!)")
		typewriter("(Before 🧿 can react, you and your party escape the cell!)")
		status.append("cell_escape")
		secret_exit()
	else:
		battle_3()

def secret_exit():
	typewriter("🧝: Let's just try to head upstairs!")
	typewriter("(You run up the winding staircase and find a red potion on the floor.)")
	typewriter("(You grab the potion ⚗️ and stuffed it in your bag before running upstairs.)")
	item.append("Potion")
	typewriter("🧝: That door looks like it leads outside. Let's go!")

def battle_3():
	typewriter("(You open the door only to find an extravagant room with a giant creature with glowing blue eyes sitting on a throne.)")
	typewriter("🧿: You are still oh so naive...to think you can escape...")

	if "y" in savior:
		typewriter("🧝: Even if I get hurt thousands of times, I will still choose to believe.")
		typewriter("🧝: Chronos, tell me the truth. Why are you doing this?")
		typewriter("🧿: What is man? A miserable little pile of secrets. But enough talk… Have at you!")
		typewriter("🧝: You've made your choice. Let's get this over with.")
	else:
		typewriter("🧝: I guess we'll do this your way then.")
	menu_3()

def menu_3():
	print()
	print("==============")
	print("=  (A)ttack  =")
	print("=   (T)alk   =")
	print("=   (I)tem   =")
	print("==============")
	print()
	player_select_3 = input("Choose your action: (Enter a/t/i.)\n").lower().strip()
	if player_select_3 == "a":
		print("======================")
		print("=   (S)word Slash    =")
		print("= (C)ompanion Attack =")
		print("=       (B)ack       =")
		print("======================")
		attack_choice = input("Choose your attack: (Enter s/c/b.)\n").lower().strip()
		print()
		if attack_choice == "s":
			typewriter("(You are filled with rage and swing the sword with might and speed.)")
			if item or party or status is empty and "n" in savior:
				typewriter("🧿: Do you seriously think that's gonna work?")
				typewriter("(Chronos smirks and catches your blade with a single hand.)")
				typewriter("(The contempt in Chrono's eyes is the last thing you saw before everything goes black and silent...)")
				bad_end()
			elif "Potion" in status and "y" in savior:
				typewriter("(You feel the power of the potion surging within your veins!)")
				typewriter("(Your sword glows brighter and brighter as its tip nears Chronos ✨✨✨)")
				typewriter("🧿: Since when did you harness the light of truth!? Wait, I...")
				typewriter("(Chronos' head had departed from their body and comes off flying before they could finish the sentence...)")
				good_end()
			elif "Potion" in status and "n" in savior:
				typewriter("🧿: Do you seriously think that's gonna work?")
				typewriter("(Chronos smirks and catches your blade with a single hand.)")
				follower_end()
			else:
				typewriter("(Your attack has no effect on Chronos)")
				menu_3()
		elif attack_choice == "c":
			print("======================")
			if any(party):
				print(*party, sep="\n")
				print("======================")
				party_choice = input("Choose a party member: (Enter first letter)\n")
				if party_choice == "r":
					typewriter("🧝: Okay, ROB, enter attack mode!")
					typewriter("(ROB transforms into its ultimate cannon form and fires a shot!)")
					typewriter("🧿: Still too naive! When will you learn?")
					typewriter("(Chronos deflected the shot with a single wave of their hand)")
					typewriter("(ROB's cannon shot is the last thing you see before everything turns black...)")
					bad_end()
				elif party_choice == "e":
					typewriter("🧝: Ellie, I don't suppose you have another trick that can help?")
					typewriter("(Ellie turns to Chronos and says: At least hear me out!)")
					typewriter("🧿: I am a bit curious about your betrayal. Talk.")
					typewriter("Ellie: I know the reason you are doing this. You only want whats best for this planet right?")
					typewriter("Ellie: I believe 🧝 can relieve you of this burden and help you achieve your goal!")
					good_end()
				else:
					typewriter("Invalid input. Try again.")
					print()
					menu_3()
			else:
				typewriter("You do not have any companions.")
				menu_3()
		elif attack_choice == "b":
			menu_3()
		else:
			typewriter("Invalid input. Try again.")
			menu_3()
	elif player_select_3 == "t":
		print()
		if "y" in savior:
			typewriter("🧝: Don't I at least deserve a small piece of truth from you?")
			typewriter("🧿: Well...I did drag you into all this...")
			good_end()
		elif "n" in savior:
			follower_end()
	elif player_select_3 == "i":
		if any(item):
			print("================")
			print(*item, sep="\n")
			print("================")
			print("(B)ack")
			print()
			item_choice = input("Choose an item: (Enter first letter)\n").lower().strip()
			print()
			if item_choice == "p":
				typewriter("(You drink the potion and wait for something to happen)")
				typewriter("(You feel pure unrestrained power entering your body 💪)")
				status.append("Potion")
			elif item_choice == "b":
				menu_3()
			elif item_choice == "d" or "s":
				typewriter("(This does not have any effect on Chronos.)")
				menu_3()
			else:
				typewriter("Invalid input. Try again.")
				print()
				menu_3()
		else:
			typewriter("(You rummaged through your bag, but cannot find anything useful.)")
			print()
			menu_3()
	else:
		typewriter("Invalid input. Try again.")
		print()
		menu_3()

def good_end():
    ending.append("master")
    print("")
    print("Your ending:")
    print("╔════════════════════════════╗")
    print("║      Master of Time        ║")
    print("╚════════════════════════════╝")
    typewriter("🧿: I've witnessed humanity's endless cycles of creation and destruction.")
    typewriter("🧿: I've tried to guide, to control, and even to abandon—but no path breaks the loop.")
    typewriter("🧿: This time, I thought removing time itself would bring peace.")
    typewriter("🧿: Without time, there is no beginning or end—only nature's eternal balance.")
    typewriter("🧝: But isn’t it the passage of time that gives our actions meaning?")
    typewriter("🧝: Without time, love, growth, and even loss lose their weight.")
    typewriter("🧝: Let me guide this era. Give me the power to make this cycle different.")
    typewriter("🧿: Your argument is compelling... Perhaps the answer lies not in erasing time but in granting it new purpose.")
    typewriter("🧿: Very well. I relinquish my role. Let’s see what you can do.")
    typewriter("(You transform into a radiant sphere of light 🌟)")
    typewriter("(Time itself bends to your will, and energy flows back into the world.)")
    typewriter("🌟: I am neither ruler nor destroyer. I am the navigator of time.")
    typewriter("🌟: Together, we will forge a path where every choice matters, where free will shapes a brighter tomorrow.")
    typewriter("(Your journey as the Master of Time begins -- a new chapter in this timeless story.)")
    print("")
    typewriter("Congratulations on becoming the Master of Time!")
    calculate_stats()
    play_again()

def follower_end():
	ending.append("follower")
	print("")
	print("Your ending:")
	print("╔════════════════════════════╗")
	print("║      Follower of Time      ║")
	print("╚════════════════════════════╝")
	typewriter("🧝: Wait! You were with me from the start! You should see that I don't want to defeat you.")
	typewriter("🧝: I just want to find a way to exist in this new world order.")
	typewriter("🧿: You do speak the truth...Do you know why I am here though? Do you know what you need to give up?")
	typewriter("🧿: I've seen human race destroy this planet time and time again.")
	typewriter("🧿: No matter how I intervene, destruction is always at the end of each path.")
	typewriter("🧿: This time, I finally figured it out. I will take away free will of the human race.")
	typewriter("🧿: Nature will take back its reign and only then can there be a new beginning.")
	typewriter("🧝: Just tell me what I should do and I'll do it.")
	typewriter("🧿: I see... On the contrary, you don't need to do anything anymore. I'm sorry it has to be this way.")
	typewriter("(A blue mist surrounds you and you begin to forget what you were doing.)")
	typewriter("(Slowly but surely, you forget where you were, who you were, and why you were standing there in the first place.)")
	typewriter("(You become a lifeless shell of your former self and acts on Chronos' commands till your last breath.)")
	print("")
	typewriter("30 Years Later...")
	typewriter("(Nature has regained control of this planet. Greenry is everywhere while human-made structures are nowhere to be seen)")
	typewriter("🧿: It's finally my time to rest.")
	typewriter("(Chronos starts drifting into non-existence...)")
	typewriter("(This is the end of your journey. Who's to say this is a good or bad ending, huh?)")
	calculate_stats()
	play_again()

def bad_end():
	ending.append("captive")
	print("")
	print("Your ending:")
	print("╔════════════════════════════╗")
	print("║      Captive of Time       ║")
	print("╚════════════════════════════╝")
	typewriter("🧿: I'm sorry. Its the only way for this planet to survive.")
	typewriter("(You become a captive of Chronos and lies lifelessly on the ground till you become dust...)")
	print("")
	typewriter("30 Years Later...")
	typewriter("(Nature has regained control of this planet. Greenry is everywhere while human-made structures are nowhere to be seen)")
	typewriter("🧿: It's finally my time to rest.")
	typewriter("(Chronos starts drifting into non-existence...)")
	typewriter("Is this really the end of your journey? Is there no other way?")
	calculate_stats()
	play_again()

def play_again():
	while True:
		print("\nWould you like to try and conquer time again?")
		choice = input("Enter Y/N: ").lower().strip()
		if choice == "y":
			print("Where would you like to start from?")
			print("1. The Beginning (Fresh Start)")
			print("2. School Hallways")
			print("3. Meeting Ellie")
			print("4. City Buildings")
			print("5. To Final Destination")
			
			choice = input("\nEnter your choice (1-5): ").strip()
			if choice == "1":
				typewriter("\nRestarting from the very beginning...\n")
				reset_game()
				start_game()
				break
			elif choice == "2":
				reset_game()
				save_again_choice = input("Would you like to save the world? (Y/N)").lower().strip()
				if save_again_choice == "y":
					savior.append("y")
				else:
					savior.append("n")
				typewriter("\nStarting from the school hallways...\n")
				path_1()
				break
			elif choice == "3":
				reset_game()
				save_again_choice = input("Would you like to save the world? (Y/N)").lower().strip()
				if save_again_choice == "y":
					savior.append("y")
				else:
					savior.append("n")
				hallway_again_choice = input("Would you go down the spider infected path? (Y/N)").lower().strip()
				if hallway_again_choice == "y":
					item.append("Spider carcass")
				typewriter("\nStarting from meeting Ellie...\n")
				battle_1()
				break
			elif choice == "4":
				reset_game()
				save_again_choice = input("Would you like to save the world? (Y/N)").lower().strip()
				if save_again_choice == "y":
					savior.append("y")
				else:
					savior.append("n")
				hallway_again_choice = input("Would you go down the spider infected path? (Y/N)").lower().strip()
				if hallway_again_choice == "y":
					item.append("Spider carcass")
				ellie_again_choice = input("Would you like to recruit Ellie? (Y/N)").lower().strip()
				if ellie_again_choice == "y":
					party.append("Ellie")
					item.append("Dark Crystal")
				typewriter("\nStarting from city buildings...\n")
				path_2()
				break
			elif choice == "5":
				reset_game()
				save_again_choice = input("Would you like to save the world? (Y/N)").lower().strip()
				if save_again_choice == "y":
					savior.append("y")
				else:
					savior.append("n")
				hallway_again_choice = input("Would you go down the spider infected path? (Y/N)").lower().strip()
				if hallway_again_choice == "y":
					item.append("Spider carcass")
				ellie_again_choice = input("Would you like to recruit Ellie? (Y/N)").lower().strip()
				if ellie_again_choice == "y":
					party.append("Ellie")
					item.append("Dark Crystal")
				typewriter("\nStarting from path to final destination...\n")
				path_3()
				break
		elif choice == "n":
			typewriter("\nThank you for this journey. See you another time!\n")
			break
		else:
			print("Invalid input. Please enter Y or N.")


def calculate_stats():
    # Update discovered sets with current run's findings
    for found_item in item:
        discovered_items.add(found_item)
    for companion in party:
        discovered_companions.add(companion)
    
    # Update discovered paths based on current run's choices
    if "Spider carcass" in item:
        discovered_paths.add("Path 1 - Spider Hallway")
    else:
        discovered_paths.add("Path 1 - Long Hallway")

    if "Coffee" in status:
        discovered_paths.add("Path 2 - Coffee Shop")
    if "Rob" in party:
        discovered_paths.add("Path 2 - Robot Factory")

    if "Ellie" in party:
        if "Dark crystal" in item:
            discovered_paths.add("Ellie - Combat Resolution")
        else:
            discovered_paths.add("Ellie - Peaceful Resolution")
    else:
        discovered_paths.add("Ellie - Conflict")

    # Track endings
    if "master" in ending:
        discovered_paths.add("Chronos - Master of Time Ending")
    elif "captive" in ending:
        discovered_paths.add("Chronos - Captive of Time Ending")
    elif "follower" in ending:
        discovered_paths.add("Chronos - Follower of Time Ending")

    # Display debug info
    print("Debug Info:")
    print(f"Items: {item}")
    print(f"Party: {party}")
    print(f"Status: {status}")
    print(f"Ending: {ending}")

    # Display current run stats
    time.sleep(3)
    print("\n╔════════════════════════════╗")
    print("║      CURRENT RUN           ║")
    print("╚════════════════════════════╝")
    print("\n🎒 ITEMS THIS RUN")
    print(*item, sep="\n- ") if item else print("None")

    print("\n👥 COMPANIONS THIS RUN")
    print(*party, sep="\n- ") if party else print("None")

    # Display accumulated progress
    time.sleep(3)
    print("\n╔════════════════════════════╗")
    print("║      TOTAL PROGRESS        ║")
    print("╚════════════════════════════╝")
    print("\n🎒 ALL ITEMS DISCOVERED")
    print(*discovered_items, sep="\n") if discovered_items else print("None yet")

    print("\n👥 ALL COMPANIONS MET")
    print(*discovered_companions, sep="\n") if discovered_companions else print("None yet")

    print("\n🛣️  ALL PATHS TAKEN")
    print(*discovered_paths, sep="\n") if discovered_paths else print("None yet")

    # Calculate completion percentages
    total_items = 4  # Spider carcass, Coffee, Dark crystal, Potion
    total_companions = 2  # Ellie, Rob
    total_paths = 15  # Update this number based on your total possible paths

    current_completion = (
        (len(item) + len(party) + len(status)) / 
        (total_items + total_companions + total_paths)
    ) * 100

    total_completion = (
        (len(discovered_items) + len(discovered_companions) + len(discovered_paths)) / 
        (total_items + total_companions + total_paths)
    ) * 100

    print(f"\n🎯 CURRENT RUN COMPLETION: {current_completion:.1f}%")
    print(f"🎯 TOTAL COMPLETION: {total_completion:.1f}%")

    # Display appropriate message based on total completion
    time.sleep(3)
    if total_completion == 100:
        print("\n🏆 PERFECT GAME!")
        print("You've discovered every single path, item, and companion!")
        print("You are truly a master of time!")
    elif total_completion >= 75:
        print("\n🌟 EXCELLENT PROGRESS!")
        print("You've uncovered most of the game's secrets!")
        print("Try different choices to find what you missed!")
    elif total_completion >= 50:
        print("\n✨ GOOD EFFORT!")
        print("There are still many paths to explore!")
        print("Try making different decisions next time!")
    else:
        print("\n💫 JUST BEGINNING!")
        print("There's so much more to discover!")
        print("Each choice leads to a different adventure!")

    # Display hints for undiscovered content
    time.sleep(3)
    print("\n💡 HINTS FOR NEXT TIME:")
    if "Spider carcass" not in discovered_items:
        print("- Try facing your fears in the spider hallway...")
    if "Rob" not in discovered_companions:
        print("- The robot factory might hide a lonely friend...")
    if "Coffee" not in discovered_items:
        print("- Sometimes a warm drink can give you strength...")
    if "Dark Crystal" not in discovered_items:
        print("- Try to win over Ellie with words...")
    print()

def reset_game():
	"""Reset all global variables to their initial state"""
	global item, party, savior, status, ending
	item = []
	party = []
	savior = []
	status = []
	ending = []

def start_game():
	"""Initialize and start the game"""
	print("╔════════════════════╗")
	print("║                    ║")
	print("║  A Quest in Time   ║")
	print("║                    ║")
	print("╚════════════════════╝")
	print()
	typewriter("🧿: Wake up... Hey...Wake up...!")

	while True:
		start_choice = input("Do you want to open your eyes? (Y/N)\n").lower().strip()
		if start_choice == "y":
			intro()
			break
		elif start_choice == "n":
			typewriter("You fall into eternal slumber and eventually fade to ashes.")
			play_again()
			break
		else:
			typewriter("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
	start_game()