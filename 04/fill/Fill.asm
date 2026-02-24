// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.


    // Initialize screen pointer
    @SCREEN
    D=A
    @addr
    M=D         // addr = SCREEN (16384)

    // Infinite loop
    (LOOP)
    // Check keyboard
    @KBD
    D=M

    // Jump to FILL if key pressed (D > 0)
    @FILL
    D;JGT

    // Otherwise, CLEAR
    (CLEAR)
        @SCREEN
        D=A
        @addr
        M=D       // Reset addr to SCREEN

        @8192
        D=A
        @count
        M=D       // count = 8192

        (CLEAR_LOOP)
            @addr
            A=M
            M=0    // Write 0 (white)

            @addr
            M=M+1  // addr++

            @count
            MD=M-1 // count--, D=count

            @CLEAR_LOOP
            D;JGT  // Loop if count > 0

        @LOOP
        0;JMP     // Return to main loop

    (FILL)
        @SCREEN
        D=A
        @addr
        M=D       // Reset addr to SCREEN

        @8192
        D=A
        @count
        M=D       // count = 8192

        (FILL_LOOP)
            @addr
            A=M
            M=-1   // Write -1 (black, all 1s)

            @addr
            M=M+1   // addr++

            @count
            MD=M-1  // count--, D=count

            @FILL_LOOP
            D;JGT   // Loop if count > 0

        @LOOP
        0;JMP      // Return to main loop




//@SCREEN
//D=A
//@addr
//M=D

//(LOOP)
//  @KBD
//  D=M 
  
//  @FILLSCREEN
//  D;JGT 
  
  //(EMPTY_SCREEN)
//  @SCREEN
//  D=A 
//  @addr
//  M=D 
  
//  @8192
//  D=A 
  
//  @count
//  M=D
  
//  (EMPTY)
//    @addr
//    A=M 
//    M=0
    
//    @addr
//    M=M+1 
    
//    @count
//    MD=M-1
    
//    @EMPTY
//    D; JGT
      
//  @LOOP
//  0; JPM 

//  (FILL_SCREEN) 
//    @SCREEN
//    D=A 
//    @addr
//    M=D 
  
//    @8192
//    D=A 
  
//    @count
//    M=D
  
//    (FILL)
//      @addr
//      A=M 
//      M=-1
    
//      @addr
//      M=M+1 
    
//      @count
//      MD=M-1
    
//      @FILL
//      D; JGT 

//    @LOOP
//    0; JPM 
  
//  @LOOP 
//  0;JPM
  
//@LOOP
//0; JPM
