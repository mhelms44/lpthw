# I cant believe I spent this much time writing this out
# Anyway, here's wonderwall
# uses argparse since I've been playing with it lately to give us some help and versioning info when calling this script
import argparse
#creates a parser from argparse with a description that displays when using -h, --help, -v, or --version
parser = argparse.ArgumentParser(description="A crude fishing game.")
# adds an optional version argument
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
# sets args value to be whatever the parser is
args = parser.parse_args()

# a bunch of print statements follow along with some nested if statements. No different than basically any other language. 
print("""You find yourself at the shores of a lake spanning the horizon.
A summer breeze gently blows from the water. You have a fishing pole and 3 worms.
If you don't catch dinner by nightfall you will starve.

Where will you start fishing from first?""")

print("1. Here, from the shore.")
print("2. Walk over to the brush pile a few hundred yards to your left.")
print("3. Walk over to the dock in the distance to your right and fish from there")
print("4. Get in the boat here by the shore and row out to the middle of the lake.")

spot = input("> ")

if spot == "1":
    print("You decide to start fishing here. The first worm you hook wasn't secured well and falls off the hook you cast.")
    print("You bait your hook again, hoping for better luck.")
    print("The third time is the charm, and the worm sticks, but several casts later nothing is biting.")
    print("What will you do now?")

    print("1. Stay here and keep fishing.")
    print("2. Move to another spot, the brush pile in the distance looks tempting")

    spot_choice = input("> ")

    if spot_choice == "1":
        print("""You decide to stick it out. Sure enough, your luck pays off. You land a very large bass, 10 or 15 lbs at least!
        Now, its time to eat! You take the fish back to your camp to begin the process of cleaning it and preparing it for the fire. 
        The fish is absolutely fantastic, especially after not eating for what must be at least a week now. 
        Later that night, you awake from your sleep in a cold sweat. You feel like your insides are going to explode.
        Stumbling out of your tent, you collapse on the ground from the intense pain, seering hot from your torso.
        You begin to vomit blood. This is the end for you.
        You will be dead before the sun comes up.""")
    elif spot_choice == "2":
        print("""You decide to try your luck at another spot, the brush pile in the distance looks very tempting.
        It is several hundred yards, but that shouldn't be too bad on your bad ankle. You being walking to it.
        As you approach, a mountain lion has been creeping behind you slowly without you noticing for some time now.
        Suddenly without warning you find yourself inside of a mouth with sharp teeth puncturing your face and cracking your skull.
        Screaming, you're thrashed around as it tightens its grip on your throat, suffocating you slowly. You pass out choking on your own blood, too weak to fight back.""")   
    else:
        print("You can't decide where to go. The crippling anixety of being unable to make a decision leads to you doing nothing.")
        print("You die without even making an effort")

elif spot == "2":
    print("""You decide to try your luck at another spot, the brush pile in the distance looks very tempting.
        It is several hundred yards, but that shouldn't be too bad on your bad ankle. You being walking to it.
        As you approach, a mountain lion has been creeping behind you slowly without you noticing for some time now.
        Suddenly without warning you find yourself inside of a mouth with sharp teeth puncturing your face and cracking your skull.
        Screaming, you're thrashed around as it tightens its grip on your throat, suffocating you slowly. You pass out choking on your own blood, too weak to fight back.""")

elif spot == "3":
    print("""The dock way off in the distance to the right looks good.
    Once you finally arrive, you realize its in worse shape than you expected. What will you do?""")
    print("1. Get on the dock anyway")
    print("2. Fish from the shore here.")

    dock_choice = input("> ")

    if dock_choice == "1":
        print("""You hazard getting on the dock anyway. It holds your weight somehow and you begin to cast your line.
        You manage to get lucky and a very large fish bites your hook. Unfortunately you lose your balance and fall into the water.
        Normally this wouldn't be a problem, but your injury to your ankle has rendered you useless in the water.
        You drown in 10 feet of water, only a few yards from the shore.""")

    elif dock_choice == "2":
        print("""You play it safe and fish from the shore instead.
        Sure enough, your luck pays off. You land a very large bass, 10 or 15 lbs at least!
        Now, its time to eat! You take the fish back to your camp to begin the process of cleaning it and preparing it for the fire. 
        The fish is absolutely fantastic, especially after not eating for what must be at least a week now. 
        Later that night, you awake from your sleep in a cold sweat. You feel like your insides are going to explode.
        Stumbling out of your tent, you collapse on the ground from the intense pain, seering hot from your torso.
        You begin to vomit blood. This is the end for you.
        You will be dead before the sun comes up.""")

    else:
        print("Lightening from a nearby storm strikes you and you die, with millions of volts surging through your body")

elif spot == "4":
    print("Despite how obvious of a bad idea it is, you get in the boat anyway.")
    print("You row out to the middle of the lake, when suddenly the water becomes very rough.")
    print("Suddenly an absolutely titanic eldtrich abomination surfaces, swallowing you and the boat in one gulp.")
    print("Wasn't it obvious this was a bad place?")

else:
    print("You turn inside out instantly and die slowly in unimaginable pain. This is a dark and dangerous place indeed.")
    


    
        




