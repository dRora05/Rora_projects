import turtle
import random
import math

screen = turtle.Screen()
screen.setup(500,500)
screen.title("Synchronized Fireflies")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)

# Constants
V_DARK = 0.1 # 
V_BRIGHT = 1 # 
FPS = 30 # 
TIMER_VALUE = 1000//FPS # 
CYCLE = 5 # 
LIGHTUP_TIME = 1 # 
SPEED = 20 # 
CLOSE_ENOUGH = 16 #
        
N = 300 # Number of fireflies

PHASE_DELTA = 0.01 # increment of phase when saw a neighbor fires up

# Variables
fireflies = [] # list of firefly turtles
v = [] # list of brightness values
phase = [] # list of phases
current_xpos = [] # list of current x coordinate
current_ypos = [] # list of current y coordinate
target_xpos = [] # list of target x coordinate
target_ypos = [] # list of raget y coordinate

def initialze_fireflies():
    for i in range(N):
        fireflies.append(turtle.Turtle()) # Add a turtle to the firefly turtle list
        v.append(V_DARK) # set them DARK first. The update function will update it to the correct value
        phase.append(random.uniform(0,CYCLE)) # phase is random from 0 to CYCLE
        current_xpos.append(random.uniform(-500,500)) # Let them go anywhere on screen
        current_ypos.append(random.uniform(-500,500))
        target_xpos.append(random.uniform(-500,500))
        target_ypos.append(random.uniform(-500,500))

    for firefly in fireflies: # initialize these turtles
        firefly.hideturtle()
        firefly.up()

# this function computes brightness based on phase
def compute_brightness(phase):
    if phase < CYCLE-LIGHTUP_TIME:
        temp = V_DARK # dormant period
    elif phase < CYCLE-LIGHTUP_TIME/2: # gradually (linearly) lighting up period
        temp = V_DARK + (V_BRIGHT-V_DARK)*(phase-(CYCLE-LIGHTUP_TIME))/(LIGHTUP_TIME/2)
    else: # gradually (linearly) dimming period
        temp = V_BRIGHT - (V_BRIGHT-V_DARK)*(phase-(CYCLE-LIGHTUP_TIME/2))/(LIGHTUP_TIME/2)
    return temp

def update_neibors(k):
    global phase
    for i in range(N):
        if i == k or phase[i] == CYCLE-LIGHTUP_TIME/2: # don't update phase for itself or fireflies at peak
            continue
        if phase[i] < CYCLE-LIGHTUP_TIME/2:
            phase[i] = min(CYCLE-LIGHTUP_TIME/2,phase[i]+PHASE_DELTA)
    
        else: 
            phase[i] += PHASE_DELTA 
            if phase[i] > CYCLE: 
                phase[i] -= CYCLE 
        v[i] = compute_brightness(phase[i])
        
def update_brightness():
    global phase,v
    for i in range(N):
        phase[i] += TIMER_VALUE/1000 
        if phase[i] > CYCLE: 
            phase[i] -= CYCLE 
        if phase[i] > CYCLE-LIGHTUP_TIME/2 and phase[i] - TIMER_VALUE/1000 < CYCLE-LIGHTUP_TIME/2: # skipped peak
            phase[i] = CYCLE-LIGHTUP_TIME/2  
        v[i] = compute_brightness(phase[i]) 

    for i in range(N): 
       if phase[i] == CYCLE-LIGHTUP_TIME/2: 
            update_neibors(i) 

def update_position():
    global current_xpos,current_ypos,target_xpos,target_ypos
    for i in range(N):
        angle_to_target = math.atan2(target_ypos[i]-current_ypos[i],target_xpos[i]-current_xpos[i])

        current_xpos[i] += SPEED/FPS*math.cos(angle_to_target)
        current_ypos[i] += SPEED/FPS*math.sin(angle_to_target)
        
        dist_to_target_squared = (current_xpos[i]-target_xpos[i])**2 + (current_ypos[i]-target_ypos[i])**2
        if dist_to_target_squared < CLOSE_ENOUGH:
            target_xpos[i] = random.randint(-500,500) 
            target_ypos[i] = random.randint(-500,500) 
        
def update_states():
    global should_draw
    update_brightness()
    update_position()
    should_draw = True
    screen.ontimer(update_states,TIMER_VALUE)

def draw():
    global v,fireflies,should_draw,current_xpos,current_ypos
    if should_draw == False:
        return
    for i in range(N):
        fireflies[i].clear()
        colors = ['cyan', 'lightgreen', 'pink', 'lightblue', 'yellow']
        fireflies[i].color(random.choice(colors))
        fireflies[i].goto(current_xpos[i],current_ypos[i])
        fireflies[i].dot(10)
    should_draw = False 

screen.bgcolor('black')
initialze_fireflies()                
update_states()
while True:
    draw() # draw forever
    screen.update()
