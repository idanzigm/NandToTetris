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
   
The Truth table will summarize as if A=1 anb B=1 then it will out put 0, else output 1. Feed this result into into Nand again and it will either be 0 and 0 or 1 and 1, if a=1 and b=1 been the condition of the And chip then it will output 1 else it will output 0. Like wise we build a variety of chips including Or gates, Not gates, Xor gates, Demultiplexers, and Multiplexers, and from those built 8 and 16 way versions of each. These are the components of the computer.   
   
From these we build the harware of the computer in the below architecture.    


This structure is capable of taking binary code and executing it. However for ease of use we develop an asembler in python to translate assemply language into bit wise code. This is the result of an application which draws a rectangle on the screen written in assembly but translated in into byte code and run on a CPU emulator.   


The next steps of this project are to develop a Java like language and an operating system to run it on. To this end we need a virtual machine to run on the computer and we need a compiler, then finall an OS. These are the challenges tackled in teh second half of the book and I'm developing them now. 

