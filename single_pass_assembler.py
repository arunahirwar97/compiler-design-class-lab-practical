from sys import exit
motOpCode = {
    "MOV": 1,
    "A": 2,
    "S": 3,
    "M": 4,
    "D": 5,
    "AN": 6,
    "O": 7,
    "ADD": 8,
    "SUB": 9,
    "MUL": 10,
    "DIV": 11,
    "AND": 12,
    "OR": 13,
    "LOAD": 14,
    "STORE": 15,
    "DCR": 16,
    "INC": 17,
    "JMP": 18,
    "JNZ": 19,
    "HALT": 20
}

motSize = {
    "MOV": 1,
    "A": 1,
    "S": 1,
    "M": 1,
    "D": 1,
    "AN": 1,
    "O": 1,
    "ADD": 1,
    "SUB": 2,
    "MUL": 2,
    "DIV": 2,
    "AND": 2,
    "OR ": 2,
    "LOAD": 3,
    "STORE": 3,
    "DCR": 1,
    "INC": 1,
    "JMP": 3,
    "JNZ": 3,
    "HALT": 1
}

l = []
relativeAddress = []
machineCode = []
RA = 0
current = 0
count = 0
n = int(input("Enter the no of instruction lines : "))
for i in range(n):
    instructions = input("Enter instruction line {} : ".format(i + 1))
    l.append(instructions)
l = [x.upper() for x in l]		# Converting all the instructions to upper case
for i in range(n):
    x = l[i]
    if " " in x:
        s1 = ''.join(x)
        a, b = s1.split()
        if a in motOpCode:		# Checking if Mnemonics is present in MOT or not
            value = motOpCode.get(a)
            size = motSize.get(a)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            if b.isalpha() is True:
                machineCode.append(str(value))
            else:
                temp = list(b)
                for i in range(len(temp)):
                    if count == 2:
                        temp.insert(i, ',')
                        count = 0
                    else:
                        count = count + 1
                s = ''.join(temp)
                machineCode.append(str(value) + "," + s)
        else:
            print("Instruction is not in Op Code Table.")
            exit(0)				# EXIT if Mnemonics is not in MOT
    else:
        if x in motOpCode:
            value = motOpCode.get(x)
            size = motSize.get(x)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            machineCode.append(value)
        else:
            print("Instruction is not in Op Code Table.")
            exit(0)

print("Relative Address	Instruction	    OpCode")
for i in range(n):
    print("{}                 {}          {}".format(relativeAddress[i], l[i], machineCode[i]))