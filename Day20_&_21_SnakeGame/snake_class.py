import turtle

starting_position = [(0,0), (-20,0), (-40,0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.new_segments = []
        self.segments()
        self.head = self.new_segments[0]
    
    def segments(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.pu()
        segment.goto(position)
        self.new_segments.append(segment)

    
    def extention(self):
        #add a new segment to the snake.
        self.add_segment(self.new_segments[-1].position())

    def move_snake(self):
        
        for seg_num in range(len(self.new_segments) - 1, 0, -1):
            new_x = self.new_segments[seg_num - 1].xcor()
            new_y = self.new_segments[seg_num - 1].ycor()
            self.new_segments[seg_num].goto(new_x, new_y)

        self.head.forward(move_distance)
        #self.new_segments[0].left(90)
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)



