import turtle

turtle.Turtle()
turtle.hideturtle()
turtle.pensize(4)
turtle.lt(90)


linha = int(input("Digite o tamanho de cada linha:"))#tamanho de cada linha
ang = int(input("Digite o angulo:"))
n = int(input("Quantas vezes deseja repetir o trajeto? :")) #numero de rept.
codigo = str(input("Digite uma série de strings (F = frente ,+ = direita , - = esquerda, [ = volta):"))
cor = input("Digite uma cor (red,green,blue):")

def desenho (l, ang,n):
	turtle.speed(10)
	p=0
	while p<n:
		d = codigo
		print(d)
		for i in range(len(d)):
			if d[i] == 'F':
				turtle.forward(l)
			if d[i] == '+':
				turtle.rt(ang)
			if d[i] == '-':
				turtle.lt(ang)
			if d[i] == '[':
				turtle.back(l)
		p=p+1
turtle.pencolor(cor)
desenho(linha, ang,n)


turtle.done()