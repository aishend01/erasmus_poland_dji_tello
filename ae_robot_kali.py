#leandro dji tello code
#@leandroafonso.m


#mission pad detection
#only works with drone tello EDU

from djitellopy import Tello
from math import sqrt

TAG_HEIGHT = 100
TAG_DISTANCE = 20
MAX_TRIES = 6


def get_distance(drone: Tello):
    dx = drone.get_mission_pad_distance_x()
    dy = drone.get_mission_pad_distance_y()

    return sqrt(pow(dx, 2) + pow(dy, 2))


def forward(drone: Tello, tag_id):
    tries = 0
    mission_pad = -1

    while mission_pad != tag_id:
        if tries == MAX_TRIES:
            print("Stopping after 6 tries")
            drone.land()
            quit(0)

        drone.move_forward(40)
        mission_pad = drone.get_mission_pad_id()
        print(f"Mission pad is: {mission_pad}")
        tries += 1

    distance = get_distance(drone)
    print(f"Distance: {distance}")

    while distance > TAG_DISTANCE:
        drone.go_xyz_speed_mid(0, 0, TAG_HEIGHT, 10, tag_id)
        distance = get_distance(drone)
        print(f"Distance: {distance}")

def back(drone: Tello, tag_id):
    tries = 0
    mission_pad = -1

    while mission_pad != tag_id:
        if tries == MAX_TRIES:
            print("Stopping after 6 tries")
            drone.land()
            quit(0)

        drone.move_back(40)
        mission_pad = drone.get_mission_pad_id()
        print(f"Mission pad is: {mission_pad}")
        tries += 1
        
    distance = get_distance(drone)
    print(f"Distance: {distance}")

    while distance > TAG_DISTANCE:
        drone.go_xyz_speed_mid(0, 0, TAG_HEIGHT, 10, tag_id)
        distance = get_distance(drone)
        print(f"Distance: {distance}")   
        
def right(drone: Tello, tag_id):
    tries = 0
    mission_pad = -1

    while mission_pad != tag_id:
        if tries == MAX_TRIES:
            print("Stopping after 6 tries")
            drone.land()
            quit(0)

        drone.move_right(70)
        mission_pad = drone.get_mission_pad_id()
        print(f"Mission pad is: {mission_pad}")
        tries += 1

    distance = get_distance(drone)
    print(f"Distance: {distance}")

    while distance > TAG_DISTANCE:
        drone.go_xyz_speed_mid(0, 0, TAG_HEIGHT, 10, tag_id)
        distance = get_distance(drone)
        print(f"Distance: {distance}")

def left(drone: Tello, tag_id):
    tries = 0
    mission_pad = -1

    while mission_pad != tag_id:
        if tries == MAX_TRIES:
            print("Stopping after 6 tries")
            drone.land()
            quit(0)

        drone.move_left(70)
        mission_pad = drone.get_mission_pad_id()
        print(f"Mission pad is: {mission_pad}")
        tries += 1

    distance = get_distance(drone)
    print(f"Distance: {distance}")

    while distance > TAG_DISTANCE:
        drone.go_xyz_speed_mid(0, 0, TAG_HEIGHT, 10, tag_id)
        distance = get_distance(drone)
        print(f"Distance: {distance}")
    
        
    

while True:
    try:
        cor = int(input("What is the color?\n1 - red\n2 - green\n3 - blue\n\nSelect: "))
        if cor > 3 or cor < 1:
            raise ValueError
        break
    except ValueError:
        print("The input is not valid\n------------------------")

while True:
    try:
        first = int(input("What's the first number? "))
        if (first > 8 or first < 6):
            raise ValueError
        break
    except ValueError:
        print("The input is not valid\n-------------------")
while True:
    try:
        second = int(input("What's the second number? "))
        if (second > 8 or second < 6 or second == first):
            raise ValueError
        break
    except ValueError:
        print("The input is not valid!\n-------------------")
possible = [6, 7, 8]
for num in possible:
    if num != first and num != second:
        third = num 
print(cor)
print(first, second, third)


tello = Tello()
tello.connect()
tello.takeoff()
forward(tello, 2)
tello.land()
tello.takeoff()
forward(tello, 4)

if cor == 1:
    left(tello, 3)
    tello.land()
    tello.takeoff()
    right(tello, 4)
elif cor == 2:
    tello.land()
    tello.takeoff()
else:
    right(tello, 5)
    tello.land()
    tello.takeoff()
    left(tello, 4)
    
forward(tello, 7)

if first == 7:
    tello.land()
    tello.takeoff()
    if second == 8:
        right(tello, 8)
        tello.land()
        tello.takeoff()
        left(tello, 7)
        left(tello, 6)
        tello.land()
        tello.takeoff()
        right(tello, 7)
        back(tello, 4)
        back(tello, 2)
        back(tello, 1)       
        tello.land()
        
    elif second == 6:
        left(tello, 6)
        tello.land()
        tello.takeoff()
        right(tello, 7)
        right(tello, 8)
        tello.land()
        tello.takeoff()
        left(tello, 7)
        back(tello, 4)
        back(tello, 2)
        back(tello, 1)       
        tello.land()
        
elif first == 8:
    right(tello, 8)
    tello.land()
    tello.takeoff()
    if second == 7:
        left(tello, 7)
        tello.land()
        tello.takeoff()
        left(tello, 6)
        tello.land()
        tello.takeoff()
        right(tello, 7)
        back(tello, 4)
        back(tello, 2)
        back(tello, 1)       
        tello.land()
    else:
        left(tello, 7)
        left(tello, 6)
        tello.land()
        tello.takeoff()
        right(tello, 7)
        tello.land()
        tello.takeoff()
        back(tello, 4)
        back(tello, 2)
        back(tello, 1)       
        tello.land()
        
elif first == 6:
    left(tello, 6)
    tello.land()
    tello.takeoff()
    if second == 7:
        right(tello, 7)
        tello.land()
        tello.takeoff()
        right(tello, 8)
        tello.land()
        tello.takeoff()
        left(tello, 7)
        back(tello, 4)
        back(tello, 2)
        back(tello, 1)       
        tello.land()
    else:
        right(tello, 7)
        right(tello, 8)
        tello.land()
        tello.takeoff()
        left(tello, 7)
        tello.land()
        tello.takeoff()
        back(tello, 4)
        back(tello, 2)
        back(tello, 1)       
        tello.land()        
        
tello.takeoff()
tello.flip_left()
tello.flip_right()
tello.land()