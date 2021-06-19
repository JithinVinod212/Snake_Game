from turtle import  Turtle
MOV_DISTANCE = 20
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)


    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def reset(self):
        for seg in self.segments:     #To make a Loop , that is for every segents.To make every segment to got a partriular self.head = self.segments[0] kcztion
            seg.goto(1000,1000)
        self.segments.clear()  # we are making SSanke
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segments(self.segments[-1].position() ) #so that last block gets answer

    def move(self):
        for seg_num in range(len(self.segments)- 1, 0,-1): # 210c 2
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # Linkig last to first two blocks
        self.head.forward(MOV_DISTANCE)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
     if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)

 
