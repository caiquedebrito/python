import turtle

t = turtle.Turtle()

#Estrela
t.lt(36)
for c in range(5):
	t.fd(200)
	t.lt(144)

t.penup()
t.goto(-100, -200)
t.pendown()
t.rt(35)
for c in range(4):
	t.fd(200)
	t.rt(90)

turtle.mainloop()