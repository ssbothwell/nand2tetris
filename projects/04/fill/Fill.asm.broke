// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

// initialize incrementer
@i
M=0
// addr = 16384
@SCREEN
D=A
@addr
M=D 
    
// Main Program

// Keyboard Scan Loop
(KBD_LOOP)
@i
M=0

@KBD
D=M
@LOOP
D;JGT // Jump to @LOOP if @KBD > 0

@KBD
D=M
@CLEAR
D;JEQ // Jump to CLEAR if @KBD == 0

@KBD_LOOP
0;JMP // Repeat KBD_Loop
// End Keyboard Scan Loop

// Screen Fill Loop
(LOOP)

// Check if i has reached end of screen map
@8160
D=A
@i
D=D-M
@KBD_LOOP
D;JEQ // Jump to @KBD_LOOP if i reaches end of screen map

// Add i to addr and set M = -1
@i
D=M
@addr
A=M+D
M=-1 

// Iterate i
@i
M=M+1

@KBD
D=M
@KBD_LOOP
D;JEQ // Jump to @KBD_LOOP if @KBD == 0

@LOOP
0;JMP // goto LOOP
// End Screen Fill Loop

// Screen Clear
(CLEAR)

// Check if i has reached end of screen map
@8160
D=A
@i
D=D-M
@KBD_LOOP
D;JEQ // Jump to @KBD_LOOP if i reaches end of screen map

// Add i to addr and set M = -1
@i
D=M
@addr
A=M+D
M=0 

// Iterate i
@i
M=M+1

@CLEAR
0;JMP // Repeat CLEAR
// End Screen Clear

// Program End loop
(END)
@END
0;JMP