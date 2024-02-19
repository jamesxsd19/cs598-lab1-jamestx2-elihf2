
from sense_hat import SenseHat
sense = SenseHat()
x, y = 0, 0
old_x, old_y = x, y
colours = [[255,255,255],[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]
colour = 0
sense.clear()
Run = True
while Run:
    for event in sense.stick.get_events():
        sense.clear()
        sense.set_pixel(x, y, colours[colour])
        print(event.direction,event.action)
        if event.action == 'pressed' and event.direction == 'up':
            if y > 0:
                y -= 1
        if event.action == 'pressed' and event.direction == 'down':
            if y < 7:
                y += 1
        if event.action == 'pressed' and event.direction == 'right':
            if x < 7:
                x += 1
        if event.action == 'pressed' and event.direction == 'left':
            if x > 0:
                x -= 1
        if event.direction=="middle":
            sense.clear()
            Run = False
            break
        old_x, old_y = x, y

            
            
