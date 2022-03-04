import turtle

#Configurações
t = turtle.Turtle()
t.fillcolor('red')
t3 = turtle.Turtle()

t3.shape('blank')
t.pensize(10)
t3.pensize(10)
#Contorno
t.penup()
t.sety(320)
t.pendown()
t.begin_fill()
t.setx(250)
t.sety(0)

t.rt(90) 
		
for c in range(10): 
	t.fd(43)
	t.rt(8) 
t.fd(20)


t.penup()
t.sety(320)
t.pendown()
t.setx(1)
t.setx(-250)
t.lt(80)
t.sety(0)

for c in range(10): 
	t.fd(43)
	t.lt(8) 
t.fd(20)
t.sety(-310)
t.end_fill()

t3.penup()
t3.sety(80)
t3.setx(-50)
t3.pendown()
t3.setx(-250)
t3.setx(-50)
t3.sety(320)

t.pensize(20)
t.pencolor('red')
t.sety(306.5)
t.pensize(10)
t.pencolor('black')
t.sety(320)
#Linhas 
#Linha 1
t.fillcolor('black')
t.begin_fill()
t.setx(250)
t.sety(240)
t.setx(-50)
t.sety(320)
t.setx(0)
t.end_fill()

#Linha 2
t.fillcolor('black')
t.begin_fill()
t.penup()
t.sety(160)
t.pendown()
t.setx(250)
t.sety(80)
t.setx(-50)
t.sety(160)
t.setx(0)
t.end_fill()


#linha 3
t.fillcolor('black')
t.begin_fill()
t.penup()
t.sety(0)
t.pendown()
t.setx(245)
t.sety(-80)
t.setx(-245)
t.sety(0)
t.setx(0)
t.end_fill()

#Linha 4
t.fillcolor('black')
t.begin_fill()
t.penup()
t.sety(-160)
t.pendown()
t.setx(215)
t.goto(160, -240)
t.setx(-160)
t.goto(-215, -160)
t.setx(0)
t.end_fill()


turtle.mainloop()