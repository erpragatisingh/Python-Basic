from turtle import *

print("Turtle graphics is a popular way for introducing programming to kids. \nIt was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.")
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
