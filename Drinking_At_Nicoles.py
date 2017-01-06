from sys import exit

def do_we_drive():
	print "You can't drive home..."
	print "Do you still want to drive?"

	choice2 = raw_input("> ")

	if choice2=="yes":
		print "Congratulations on your first DUI"
		exit(0)
	elif choice2=="no":
		print "Wise choice, find another way home."
		exit(0)
	else:
		print "I have no idea what that means, you must be WASTED"

def Uber():
	print "Do you want to take a regular Uber or an UberX?"

	choice3 = raw_input("> ")

	if choice3 == "UberX":
		print "Youz goin home in styyyllleee"
		exit(0)
	else:
		print "You'll probably go home in some old dude's minivan."
		exit(0)

def howmanyglasses(CarOrT):	
	print "Would you like another glass of wine?"
	i = 0
	yes_or_no = raw_input("> ")
	while "yes" in yes_or_no:
		print "Let's have another glass!"
		i=i+1
		print "You've had %r glasses" %i
		print "Would you like another glass of wine?"
		yes_or_no = raw_input("yes or no? >")
	CarOrT2(CarOrT, i)

def CarOrT(CarOrT):
	print "Excellent choice! We are taking the %r to Nicole's!" % CarOrT
	print "We arrive, we are having a smashing time."
	howmanyglasses(CarOrT)

def CarOrT2(CarOrT, glasses):
	print "How many glasses of wine did you have? Be honest..."
	
	choice = int(raw_input("> "))

	if choice != glasses:
		print "You're lying!"
	if glasses<=2 and CarOrT=="car":
		print "You haven't had too much, you can drive home!"
		exit(0)
	elif glasses >2 and CarOrT=="car":
		do_we_drive()
	elif glasses <=2 and CarOrT=="T":
		print "Why didn't you drink more?! That's a waste of wine!"
		exit(0)
	elif glasses >2 and CarOrT=="T":
		print "You are hammered! Take an Uber home?"
		Uber()
	else:
		"That was gibberish, you must be PLASTERED!"

def start():
	print "It's the end of the workday"
	print "It's time to drink wine at Nicole's place"
	print "How do we get there?"

	choice = raw_input("> ")

	if "car" in choice:
		CarOrT("car")
	elif "T" in choice:
		CarOrT("T")
	else:
		print "You are not fun!"

start()