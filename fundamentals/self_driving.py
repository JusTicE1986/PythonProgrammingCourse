
def move_forward():
    print("Move forward")


def turn(direction):
    print(f"Turn {direction}")


def start_engine():
    print("Start engine")


def stop_engine():
    print("Stop engine")


destination = input("Where do you want to go? ")

start_engine()
move_forward()

if destination == "school":
    turn("right")
    print(f"We arrived at {destination}")
elif destination == "grocery store":
    turn("right")
    print(f"We arrived at the {destination}")
elif destination == "restaurant":
    move_forward()
    print(f"We arrived at the {destination}")
else:
    print("We are stuck.")
