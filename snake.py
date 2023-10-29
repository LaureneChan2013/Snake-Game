import turtle
starting_positions = [(0,0), (-20,0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for position in starting_positions:
            self.add_segments(position)

    def add_segments(self, position):
        snake_segment = turtle.Turtle()
        snake_segment.shape("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())
    
    def move(self):
        for segment_number in range(len(self.segments)-1, 0 , -1):
            next_x = self.segments[segment_number-1].xcor()
            next_y = self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(next_x, next_y)
        self.segments[0].forward(20)

    def up(self):
       if (self.segments[0].heading() != 270):
        self.segments[0].seth(90)
        
    def left(self):
       if (self.segments[0].heading() != 0):
        self.segments[0].seth(180)
        
    def down(self):
       if (self.segments[0].heading() != 90):
        self.segments[0].seth(270)
        
    def right(self):
       if (self.segments[0].heading() != 180):
        self.segments[0].seth(0)
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
            
        self.segments.clear()
        self.create_snake()
       