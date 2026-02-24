# NandToTetris
Building a tetris game out of Nand Gates    
   
   
This project takes you through the process of building a tetric game out of Nand Chips. To this end you start by building a variety of chips using a hardware definition language. Here is an example of building an And chip out of Nand gates.    
   
CHIP And {   
    IN a, b;   
    OUT out;   
       
    PARTS:   
    Nand(a = a , b = b , out = neq1);    
    Nand(a = neq1 , b = neq1 , out = out);    
    }   
   
The Truth table will summarize as follows; if A=1 and B=1 then neq1 will output 0, else output 1 (it is not A and B). This result once fed into the second nand gate will return 1 if neq1 is equal to 0, which is only the case under the condition that a=1 and b=1 (all other conditions as stated earlier produce and neq1 of 1). Yielding the proper conditions of the And gate. Thus it is made. Like wise we build a variety of chips including Or gates, Not gates, Xor gates, Demultiplexers, and Multiplexers, and from those built 8 and 16 way versions of each. These are the base components of the computer.   

From these we build the harware of the computer in the below architecture.    

![Alt text](https://github.com/idanzigm/NandToTetris/blob/main/screen%20shots%20/Untitled.jpeg)

This structure is capable of taking binary code and executing it. However for ease of use we develop an asembler in python to translate assemply language into bit wise code. This is the result of an application which draws a rectangle on the screen written in assembly but translated in into byte code and run on the CPU emulator.   

![Alt text](https://github.com/idanzigm/NandToTetris/blob/main/screen%20shots%20/Screenshot%20from%202026-02-24%2013-22-36.png)

The next steps of this project are to develop a Java like language and an operating system to run it on. To this end we need a virtual machine to run on the computer and we need a compiler, then finall an OS. These are the challenges tackled in the second half of the book and I'm developing them now. 
