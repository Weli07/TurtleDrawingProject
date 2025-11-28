import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle Drawing Screen")

turtle_instance=turtle.Turtle()

'''
#Kare çizmek 
turtle_instance.forward(100)

turtle_instance.left(90)
turtle_instance.forward(100)

turtle_instance.left(90)
turtle_instance.forward(100)

turtle_instance.left(90)
turtle_instance.forward(100)


for i in range(4):
    turtle_instance.left(90)
    turtle_instance.forward(100)

syc=1
while syc<5:
    turtle_instance.left(90)
    turtle_instance.forward(100)
    syc=syc+1
    


# yıldız çizmek
turtle_instance.left(30)
turtle_instance.forward(200)
turtle_instance.left(210)
turtle_instance.forward(200)

turtle_instance.left(210)
turtle_instance.forward(200)

turtle_instance.left(210)
turtle_instance.forward(200)

turtle_instance.left(225)
turtle_instance.forward(200)

for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(200)
    
'''

# polygon

num_slides=5
angle=360.0/num_slides*2
side_length=200

for i in range(num_slides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)

turtle.done()
