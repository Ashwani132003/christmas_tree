import turtle

t = turtle.Turtle()
turtle.Screen()
t.speed(10)

t.up()
t.goto(-10,-200)

t.begin_fill()
t.color("brown")
for i in range(2):
    t.down()
    t.fd(30)
    t.left(90)
    t.fd(90)
    t.left(90)
t.end_fill()


t.goto(-10,-110)
t.left(180)
t.begin_fill()

t.color("green")
for x in range(1):

    for j in range(35,15,-5):

        t.circle(280,j)
        t.left(15)
        t.circle(680,-15.9)
        t.right(20)


for x in range(1):
    t.right(71.8)

    for j in range(20,40,5):
        t.circle(680, -15.9)
        t.left(15)
        t.circle(280,j)
        t.right(20)

t.up()
t.end_fill()

# decoration

#star
t.goto(5,160)
t.down()
t.begin_fill()
t.color("yellow")
for x in range(5):
    t.left(180)
    t.circle(40,35)
    t.left(15)
    t.circle(140,-17)
t.end_fill()

t.up()

t.goto(45,-10)
t.down()
t.begin_fill()
t.color("yellow")
for x in range(5):
    t.left(180)
    t.circle(20,35)
    t.left(15)
    t.circle(120,-17)
t.end_fill()

t.up()

#balls
t.up()
t.goto(-60,-80)
t.down()
t.begin_fill()
t.color("orange")
t.circle(10)
t.end_fill()
t.up()

t.goto(-10,7)
t.begin_fill()
t.color("orange")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(-50,60)
t.begin_fill()
t.color("orange")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(20,90)
t.begin_fill()
t.color("orange")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(70,-90)
t.begin_fill()
t.color("orange")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(80,-20)
t.begin_fill()
t.color("orange")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(30,40)
t.begin_fill()
t.color("pink")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(-55,-20)
t.begin_fill()
t.color("pink")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(8,-50)
t.begin_fill()
t.color("pink")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.up()




#lights

#left
t.up()
t.goto(-158,-150)
t.down()
t.begin_fill()
t.color("yellow")
t.circle(10)
t.end_fill()
t.up()

t.goto(-127,-12)
t.begin_fill()
t.color("yellow")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(-95,78)
t.begin_fill()
t.color("yellow")
t.down()
t.circle(10)
t.up()
t.end_fill()

#top

t.goto(8,222)
t.begin_fill()
t.color("yellow")
t.down()
t.circle(10)
t.up()
t.end_fill()


#right


t.goto(182,-148)
t.begin_fill()
t.color("yellow")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(147,-12)
t.begin_fill()
t.color("yellow")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.goto(113,78)
t.begin_fill()
t.color("yellow")
t.down()
t.circle(10)
t.up()
t.end_fill()

t.up()





turtle.exitonclick()