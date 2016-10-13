// Instantiate Variables

// R0 == 255
@255
D=A
@R0
M=D

// n = R0
@0
D=M
@n
M=D

// n2 = 16
@32
D=A
@n2
M=D

// i = 0
@i
M=0 

// i2 = 2
@i2
M=0

// addr = 16384
@SCREEN
D=A
@addr
M=D 
    
// Main Program


(LOOP)
@i
D=M
@n
D=D-M
@END
D;JGT // if i > n goto END
  
    (LOOP2)
    @i2
    D=M
    @n2
    D=D-M
    @END2
    D;JGT // if i2 > n2 goto END2

    
    @addr
    A=M
    M=-1 // RAM[addr]= 1111111111111111
    
    @i2
    D=M
    @addr
    A=M+D
    M=-1 // RAM[addr+2]= 1111111111111111
    
    @2
    D=A
    @i2
    M=M+D
    
    @LOOP2
    0;JMP
    

(END2)

@i2
M=0

@i
M=M+1 // i = i + 1
@32
D=A
@addr
M=D+M // addr = addr + 32

@LOOP
0;JMP // goto LOOP


(END)
@END
0;JMP