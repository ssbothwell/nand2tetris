// Main Loop
(KBD_LOOP)

// Instantiate Variables
// Draw loop iterator
@i
M=0
// Draw loop terminator
@255
D=A
@n
M=D
// Draw Value
@0
D=A
@Color
M=D
// Screen Address
@SCREEN
D=A
@addr
M=D

// Set Color on keypress
@Color
M=-1
// Jump on keypress
@KBD
D=M
@DRAW
D;JGT

// Clear Screen
@Color
M=0
@DRAW
D;JMP
// End Main Loop


// Draw Loop
(DRAW)
// Iterate i
@i
M=M+1
// Draw to screen
  // Draw Inner Loop
  // Reset Addr
  // instantiate iterator j
  @j
  M=0
  (INNER)
  //// Instantiate Terminator m
  @32
  D=A
  @m
  M=D

  // Draw next column 
  @addr
  D=M
  @Column
  M=D
  @j
  D=M
  @Column
  M=M+D
  @Color
  D=M
  @Column
  A=M
  M=D
  
  // Iteratate J
  @j
  M=M+1
  // Check if m-j == 0
  @m
  D=M
  @j
  D=D-M
  @OUTER
  D;JEQ
  // Jump to (INNER)
  @INNER
  0;JMP
  // End Inner Loop
(OUTER)
// Update addr to next row
@32
D=A
@addr
M=D+M // addr = addr + 32
// Terminate if i > n (16)
@i
D=M
@n
D=D-M
@KBD_LOOP
D;JGT
// Draw Loop Jump
@DRAW
0;JMP
// End Draw Loop
