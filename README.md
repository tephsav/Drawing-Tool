# Drawing-Tool
Simple drawing tool. The program reads the input.txt, executes a set of commands from the file, step by step, and produces output.txt.

input.txt

    C w h
    L x1 y1 x2 y2
    R x1 y1 x2 y2
    B x y c

Create Canvas: create a new canvas of width (w) and height (h).

Create Line: create a new line from (x1,y1) to (x2,y2). Currently only horizontal or vertical lines are supported. 
Horizontal and vertical lines will be drawn using the 'x' character.

Create Rectangle: create a new rectangle, whose upper left corner is (x1,y1) and lower right corner is (x2,y2). 
Horizontal and vertical lines will be drawn using the 'x' character.

Bucket Fill: fill the entire area connected to (x,y) with "colour" (c). The behavior of this is the same as that of the "bucket fill" 
tool in paint programs.