import turtle

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("blue")

    len = turtle.Turtle()
    len.color("red")
    len.shape("turtle")

    
    for i in range(1,37):
        for j in range(1,4):
            len.forward(200)
            len.right(120)
        len.left(10)
        
    len.right(90)  
    len.forward(250)   

    window.exitonclick()
          

draw_triangle()
              
        
    
