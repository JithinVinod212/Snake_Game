import time
from Snake import  Snake
from turtle import Screen
from food import  Food
from scoreboard import Scoreboard
from playsound import  playsound



screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # turtle animation on or off and set a delay for update drawings and we need update
#we created  a position  that can seperate from the variable
#in every -20 ,It get Sepearted..

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right , "Right")

game_is_on = True
while game_is_on:

     screen.update()
     time.sleep(0.1)
     # for making all the bocks to go one at a time
     snake.move()

     #Detect Collison with Food
     if snake.head.distance(food) < 15:         #food size is 10 *10 size
          food.refresh()
          snake.extend()
          scoreboard.increase_score()

     #detect collison with Wall:
     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
          scoreboard.reset()
          snake.reset()

     # Detetct collsio with tail
     # If head triggers collide with Ta

     for segment in snake.segments:
          if segment == snake.head:
               pass
          elif snake.head.distance(segment) < 10:
               scoreboard.reset()
               snake.reset()



screen.exitonclick()