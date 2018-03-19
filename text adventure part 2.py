name = input("What's your name?")

print("Hi" ,name)

location = input ("do you want to go far or close?")

if location == ("far"):
    print("Pack your bags, we're heading for Spain! Oh no. The airport lost our luggage! What do we do?")
    luggage = input ("Stay or leave?")
    if luggage ==("stay"):
         print ("We fall asleep waiting for our luggage and wake up 2 hours later to see that they found it. Yay!")
    elif luggage == ("leave"):
        print ("We decide to come back later after we go to the car rental but when we're comming back, we get a flat tire. What a bust. Guess we're walking...")
    else: print("Zombies attack.")
elif location == ("close"):
    print("Get the dog, we're going to Virginia!! While watching fireworks, the dog gets scared and runs off! What do we do?")
    dog = input ("look for it or let it find us?")
    if dog == ("look for it"):
        print ("Great! We found the dog. We continue to watch the fireworks and have a great time. Later, you give the dog a bath and we go to sleep.")
    elif dog == ("let it find us"):
        print ("The dog comes back to us as we watch the fireworks and in the morning we all head home.")
    else: print ("Zombies come and eat you.")
else: print ("Boii")

enjoy = input ("Did you enjoy your vacation?")
if enjoy == ("yes"):
    print ("Great! The end.")
while enjoy != ("yes"):
    print ("Another vacation then?")
    location = input ("do you want to go far or close?")
    if location == ("far"):
        print("Pack your bags, we're heading for Spain! Oh no. The airport lost our luggage! What do we do?")
        luggage = input ("Stay or leave?")
        if luggage ==("stay"):
             print ("We fall asleep waiting for our luggage and wake up 2 hours later to see that they found it. Yay!")
        elif luggage == ("leave"):
            print ("We decide to come back later after we go to the car rental but when we're comming back, we get a flat tire. What a bust. Guess we're walking...")
        else: print("Zombies attack.")
    elif location == ("close"):
        print("Get the dog, we're going to Virginia!! While watching fireworks, the dog gets scared and runs off! What do we do?")
        dog = input ("look for it or let it find us?")
        if dog == ("look for it"):
            print ("Great! We found the dog. We continue to watch the fireworks and have a great time. Later, you give the dog a bath and we go to sleep.")
        elif dog == ("let it find us"):
            print ("The dog comes back to us as we watch the fireworks and in the morning we all head home.")
        else: print ("Zombies come and eat you.")
    else: print ("Boii")
    enjoy = input ("Did you enjoy your vacation?")
    if enjoy == ("yes"):
        print ("Great! The end.")
    else: print ("Anotha one.")

