# section 1
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("bron my goatt.png")
player.set_size(.3)
stage.set_background("underwater")
lives = 2
#section 2
def falling_object():
    global lives

    if lives > 0:
        x_position = random.randint(-250,250)
        y = 250
        object = codesters.Sprite("basketball",x_position, y)
        object.set_size(0.4)
        object.set_y_speed(-2)
        object_speed = 0.5

stage.event_interval(falling_object, 1.5)
# section 3 - col
def collision(player, object):
    global lives

    if object.get_image_name() == "basketball":
            stage.remove_sprite(object)
            lives -= 1
            if lives == 0:
                player.say("gameover")
player.event_collision(collision)
# section 4

def go_right():
    player.move_right(10)

player.event_key("right",go_right)

def go_left():
    player.move_left(10)

player.event_key("left",go_left)
