def move_forward():
    print("Move forward")

def turn(direction):
    print(f"Turn {direction}")

def start_engine():
    print("Start engine")

def stop_engine():
    print("Stop engine")

def follow_roundabout(exit_number):
    print(f'taking exit number {exit_number} from the roundabout')


start_engine()
destination = input("Where is your desired destination?")
roundabout_exits = ["hospital", "mall", "airport", "university", "stadium"]
if destination == "library":
    move_forward()
    turn("left")
    print(f'You have arrived at {destination}')
elif destination == "tech park":
    move_forward()
    turn("right")
    print(f'You have arrived at {destination}')
elif destination in roundabout_exits:
    move_forward()
    print(f'You enter a roundabout')
    if destination == "hospital":
        print(f'Take the 1st exit')
        print(f'You have arrived at {destination}')
    elif destination == "mall":
        print(f'Take the 2nd exit')
        move_forward()
        turn("right")
        print(f'You have arrived at {destination}')
    elif destination == "airport":
        print(f'Take the 3rd exit')
        print(f'You have arrived at {destination}')
    elif destination == "university" or destination == "stadium":
        print(f'Take the 4th exit')
        move_forward()
        if destination == "university":
            turn("left")
            print(f'You have arrived at {destination}')
        elif destination == "stadium":
            turn("right")
            print(f'You have arrived at {destination}')
else:
    print(f'your destination: {destination} was not found in the techville')
stop_engine()




