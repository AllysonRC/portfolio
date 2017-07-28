start = '''
You and two friends are staying in a cabin in the woods. You are planning on having a good time and partying 'til the early morning.
Suddenly, a trapdoor opens, showing a grey, stone staircase that seems to never end. Do you enter?
'''

Good1 = '''
You eventually make it down all the stairs, and you find yourself in a series of underground tunnels.
There's a fork in the road, and one of your friends wants to go back, while the other wants to keep going. Do you split up, go back together, or go forward together?
'''

Good2 = '''
You hear an ominous scream that sounds like one of your friends. Then, dead silence. Do you go back or continue forward?
'''

Good3 = '''
You manage to get to the end of the tunnel and meet up with only one friend. You hear noises coming from the woods. Do you inspect the noises or go back?
'''

Good4 = '''
A herd of zombies comes out of the woods and eats your friend alive in front of you. You manage to escape from the herd, but you have to find safety immediately.
You happen to come across a ladder and a house. Choose.
'''

Good5 = '''
You find yourself at a helicopter pad, you hear a helicopter flying overhead, and decide to signal it. After it recieves your signal,
they help you get out of the woods by flying you back home. You are saved
'''

Bad1 = '''
While walking through the tunnels, a ravenous wolf attacks one of your friends, do you help them, or run?
'''

Bad2 = '''
You help your friend. The wolf runs away, but your friend is bleeding out. Do you leave them behind or take them with you?
'''

#How to win, yes, split up, forward, inspect, ladder

print(start)

print("Type 'yes' to enter, or type 'no' to stay in the cabin.")
user_input = input()

if user_input == "no":
	print("You refuse to go down the stairs. So you go on a walk with your friends to forget about the trapdoor, and absentmindedly, you all fall off a cliff. You are dead. Retry?")

elif user_input == "yes":
	print("You decide to go down the stairs.")
	print(Good1)
	print("Type 'back' to go back, type 'together' to go fowrward together, or type 'split up' to split up.")
	user_input = input()

	if user_input == "back":
		print("You all go back. A huntsmen thinks you have invaded his house, and shoots you all. You are dead. Retry?")

	elif user_input == "together":
		print("Do you choose to go left or right?")
		print("Type 'left' to go left, or type 'right' to go right.")
		input = raw_input()

		if user_input == "right":
			print("You decide to go right. You all run into a lagoon and decide to swin across it, while swimming a serpent finds you and eats you alive. You are dead. Retry?")

		elif user_input == "left":
			print("You decide to go left.")
			print(Bad1)
			print("Type 'help' to help your friend, or type 'run' to run away.")
			user_input = input()

			if user_input == "run":
				print("You choose to run. The wolf catches up to you and kills your friend. Then, it finds you and kills you too. You are dead. Retry?")

			elif user_input == "help":
				print("You decide to help.")
				print(Bad2)
				print("Type 'leave' to leave them, or type 'go' to take them with you")
				user_input = input()

				if user_input == "go":
					print("You choose to take your friend with you. Your friend has contracted rabbies from the attack and attacks you and your friend. You both are killed instantly. You are dead. Retry?")

				elif user_input == "leave":
					print("You choose to leave your friend. You run into a Satanic cult in the tunnels. They capture you and your friend, and perform a human sacrifice on you two. You are dead. Retry?")

				else:
					print("That is not an option, retry.")

			else:
				print("That is not an option, retry.")


	elif user_input == "split up":
		print("You decide to split up.")
		print(Good2)
		print("Type 'back' to inspect the scream, or type 'forward' to continue down the tunnel.")
		user_input = input()

		if user_input == "back":
			print("You choose to go back. You are confronted by a murderer, who slits your throat. You are dead. Retry?")

		elif user_input == "forward":
			print("You decide to continue down the tunnel.")
			print(Good3)
			print("Type 'back' to go back into the tunnels, or type 'inspect' to inspect the noises.")
			user_input = input()

			if user_input == "back":
				print("You choose to go back. You are confronted by Slenderman, and he strangles you and your friend to death. You are dead. Retry?")

			elif user_input == "inspect":
				print("You decide to inspect the noises coming from the woods.")
				print(Good4)
				print("Type 'ladder' to climb the ladder, or type 'house' to go in the house.")
				user_input = input()

				if user_input == "house":
					print("You choose to go in the house. The family lets you into their sweet humble abode.")
					print("Little do you know, they are cannibles, and they invite you for dinner, cooking you and eating you alive. You are dead. Retry?")

				elif user_input == "ladder":
					print("You decide to climb the ladder.")
					print(Good5)
					print("You win.")

				else:
					print("That is not an option, retry.")

			else:
				print("That is not an option, retry.")

		else:
			print("That is not an option, retry.")

	else:
		print("That is not an option, retry.")

else:
	print("That is not an option, retry.")
