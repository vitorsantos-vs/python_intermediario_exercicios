print("Crie um programa que desenhe formas geométricas básicas usando o módulo `turtle`.\n")

import turtle

def desenhar_quadrado(t):
    for _ in range(4):
        t.forward(100)
        t.right(90)
        
def desenhar_circulo(t):
    t.circle(50)
    
def desenhar_triangulo(t):
    for _ in range(3):
        t.forward(100)
        t.right(120)
        
t = turtle.Turtle()

desenhar_quadrado(t)
t.penup()
t.forward(150)
t.pendown()

desenhar_circulo(t)
t.penup()
t.forward(150)
t.pendown()

desenhar_triangulo(t)
turtle.done()
