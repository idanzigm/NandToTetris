// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

//a multiplication tool

@mult
M=0

(MULT) 
  @y 
  D=M 
  
  @mult 
  M=M+D
  
  @x
  M=M-1
  D=M 
  
  @MULT
  D; JGT
  
(END) 
  @END
  0; JMP
  
  
