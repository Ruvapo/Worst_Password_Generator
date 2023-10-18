import turtle
import random
import string

FONT = ("Agency", 18, 'normal')

password = "Password: "

turtle.colormode(255)
character_options = string.hexdigits

#setup screen
window = turtle.Screen()
window.bgcolor("white")
window.setup(height=600,width=600)
window.tracer(0)

#player piece
player = turtle.Turtle()
player.penup()
player.goto(0,-100)
player.shape("square")
player.color("black")
player.showturtle()
player.direction = "stop"

drops = []

for _ in range(20): #Amount of characters that fall
    new = turtle.Turtle()
    new.hideturtle()
    new.speed(3)
    new.color(random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255))
    new.setheading(-90)

    # new.penup()
    x = random.randint(-200, 200)
    y = random.randint(300, 600)
    new.goto(x, y)

    new.step = random.randint(1,2)
    new.letter = random.choice(character_options)
    new.write(new.letter, font=FONT)
    drops.append(new)

#movement
def turn_left():
  player.color('light green')
  player.forward(-10)

def turn_right():
  player.color('pink')
  player.forward(10)

window.listen()
window.onkeypress(turn_left, "Left")
window.onkeypress(turn_right, "Right")

max_left = -200
max_right = 200

new_password = turtle.Turtle()
new_password.penup()
new_password.goto(-180, -200)
new_password.write(password, font=FONT)
new_password.hideturtle()

end = turtle.Turtle()
end.penup()
end.goto(0,0)
end.hideturtle()

#game loop
while True:
    window.update()

    if max_left >= player.xcor():
        player.undo()

    if player.xcor() >= max_right:
        player.undo()

    for drop in drops:
        drop.sety(drop.ycor() - .5) #speed of fall letters

        if drop.ycor() < -300:
            drop.goto(0, 400)
            drop.setx(random.randint(-200, 200))
            drop.sety(random.randint(300, 400))
            drop.letter = random.choice(character_options)

        if drop.distance(player) < 20:
            drop.goto(0, 400)
            drop.setx(random.randint(-200, 200))
            drop.sety(random.randint(300, 400))

            new_password.clear()
            password += drop.letter
            print(password)

            if len(password) <= 20: #Length of the password
                new_password.write(password, font=FONT)
            else:
                new_password.write(password, font=FONT)
                end.write("End", font=FONT)
                window.mainloop()

            drop.letter = random.choice(character_options)

        drop.clear()
        drop.write(drop.letter, font=FONT)

