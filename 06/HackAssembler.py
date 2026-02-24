import sys 
import re 

print("Hack Assembler")
input("please enter the file path to an .asm file to convert to .hack: ")

#opens the file and converts to list 
file_lines= []
with open(file_path, "rt") as f : 
    for line in f: 
        file_lines.append(line)

# cleans list for assembly 
temp_file_lines = []
remove = []
for line in file_lines: 
    line = re.sub(r'\s+', '', line)
    temp_file_lines.append(line)

for line in temp_file_lines: 
    if re.match("\n|//", line): 
        remove.append(line)

for line in remove: 
    temp_file_lines.pop(temp_file_lines.index(line))
print(temp_file_lines)

clean_file_lines= []
for line in temp_file_lines: 
    line = re.sub(r"\n", "", line)
    clean_file_lines = list(filter(None, temp_file_lines))
print(clean_file_lines)

# dictionary of bit wise conversions 
comp0 = {'0':'0101010', '1':'0111111', '-1':'0111010' }

dest = {'null':'000', 'M=':'001', 'D=':'010', 'DM=':'011', 'A=':'100', 'AM=':'101', 'AD=':'110', 
        'ADM=':'111'}

comp1 = {'D':'0001100', 'A':'0110000', 'M':'1110000',}
comp2 = {'!D':'0001101','!A':'0110001', '-D':'0001111', '-A':'0110011', 'D+1':'0011111', 
         'A+1':'0110111', 'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011', 
         'A-D':'0000111','D&A':'0000000', 'D|A':'0010101', '!M':'1110011', '-M':'1110011',
         'M+1':'1110111', 'D+M':'1000010', 'D-M':'1010011', 'M-D':'1000111', 'D&M':'1000000', 
         'D|M':'1010101'}


jump = {'null':'000', ';JGT':'001', ';JEQ':'010', ';JGE':'011', ';JLT':';100', ';JNE':'101', ';JLE':'110', ';JMP':'111'}

address = {'R0': '0', 'R1':'1', 'R2':'2', 'R3':'3', 'R4':'4', 'R5':'5', 'R6':'6', 'R7':'7', 'R8':'8',
       'R9':'9', 'R10':'10', 'R11':'11', 'R12':'12', 'R13':'13', 'R14':'14', 'R15':'15', 'R16':'16', 
       'SCREEN':'4000', 'KBD':'4000'}

# variables for assembly, includes variable for assembled file lines, jump locations, and line counting 
assembled_file_lines= []
jump_origins= {} 
jump_locations= {}
line_count=0 

for line in clean_file_lines: 
    
    comp_value= ''
    dest_value= ''
    jump_value= ''
    # start with seeing if it is an A instruction 
    if re.match("@", line): 
        line = re.sub("@", "", line)
        i=0 
        # match with inbuilt values like R0 and SCREEN 
        for key, value in address.items():
            if re.match(key, line):
                assembled_file_lines.append(('{0:016b}'.format(int(value)))) 
                i+=1
        # match with Loop variables 
        if i==0: 
            if re.match('[a-zA-Z]+r[a-zA-Z1-100$._]?', line): 
                jump_origins.setdefault(line, []).append(line_count)
                assembled_file_lines.append(line) 
                i+=1
        # match with integer values 
        if i==0: 
            assembled_file_lines.append(('{0:016b}'.format(int(line))))
    # match with loop destinations 
    elif re.match( r"\(", line):
        line = re.sub(r'[()]', '', line)
        jump_locations[line]= line_count
        line_count-=1 
    else: 
        #handle jump values first 
        if re.search(';', line): 
            for key, value in jump.items(): 
                if re.search(re.escape(key), line):
                    jump_value= value
                    line = re.sub(key, "", line)
        else: 
            jump_value= '000'
        # handle compvalues of 0, 1 and -1 
        for key, value in comp0.items(): 
            if re.search(key, line): 
                comp_value= value
        # handle dest values next 
        if re.search('=', line): 
            for key, value in dest.items():
                if re.search(key, line):
                    dest_value= value
                    line = re.sub(key, "", line)
        else: 
            dest_value= '000'
        # finish with all other comp values (comp1 first becuase comp2 will over ride)
        for key, value in comp1.items(): 
            if re.search(re.escape(key), line): 
                comp_value= value
        for key, value in comp2.items(): 
            if re.search(re.escape(key), line):
                comp_value= value
        # assemble the line of code for C instruction 
        line="".join(['111', comp_value, dest_value, jump_value])
        assembled_file_lines.append(line)
    # increment the line count for purposes of tracking loops 
    line_count+=1

# places jump locations into assembly code 
for key, value in jump_origins.items(): 
    for number in value: 
        assembled_file_lines[number]= '{0:016b}'.format(int(jump_locations[key]))

# creates hack file with assembled code 
file_path= re.sub(".asm", ".hack", file_path)
with open(file_path, 'w') as file:
    for lines in assembled_file_lines:
        file.write(lines+'\n')



        

