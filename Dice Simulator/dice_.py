import random
def draw_dice(no):
    if(no == 1):
        print("[-----------]")
        print("[           ]")
        print("[     0     ]")
        print("[           ]")
        print("[-----------]")
    elif(no == 2):
        print("[-----------]")
        print("[           ]")
        print("[   0   0   ]")
        print("[           ]")
        print("[-----------]")
    elif(no == 3):
        print("[-----------]")
        print("[     0     ]")
        print("[     0     ]")
        print("[     0     ]")
        print("[-----------]")
    elif(no == 4):
        print("[-----------]")
        print("[  0     0  ]")
        print("[           ]")
        print("[  0     0  ]")
        print("[-----------]")
    elif(no == 5):
        print("[-----------]")
        print("[  0     0  ]")
        print("[     0     ]")
        print("[  0     0  ]")
        print("[-----------]")
    elif(no == 6):
        print("[-----------]")
        print("[  0     0  ]")
        print("[  0     0  ]")
        print("[  0     0  ]")
        print("[-----------]")
temp = random.randint(1,6)
print("\nNumber on the dice is : ",temp)
draw_dice(temp)
def not_y():
    x= input("Press y to roll the dice again : ")
    if(x == 'y'.lower()):
        number = random.randint(1,6)
        print("\nNumber on the dice is : ",number)
        draw_dice(number)
        not_y()
    else:
        print("Thx For Playing")
        return 
not_y()
