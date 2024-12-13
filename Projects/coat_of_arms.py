###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("winter")

codesters.Square(100, 100, 200, 'purple')
codesters.Square(-100, 100, 200, 'black')
codesters.Square(-100, -100, 200, 'yellow')
codesters.Square(100, -100, 200, 'white')


s1 = codesters.Sprite("the goat", 100, 100)
s1.set_size(0.1)
s2 = codesters.Sprite("lil bro", -100, -100)
s2.set_size(0.3)
s3 = codesters.Sprite("bron my goatt", 100, -100)
s3.set_size(0.1)
s4 = codesters.Sprite("shifty",-100, 100)
s4.set_size(0.1)

message1 = codesters.Text("kayden",0,220,"red")
message2 = codesters.Text("bron is the goat",0,-220,"black")