def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    out2 = out[0].split(",")
    for i in range(0, len(out2)):
        out2[i] = int(out2[i])
    f.close()
    return out2

def oper_add(input,slice):
    print(slice)
    input[slice[3]] = input[slice[1]] + input[slice[2]]
    return input

def oper_multip(input,slice):
    input[slice[3]] = input[slice[1]] * input[slice[2]]
    return input

def main():
    input = read_input("aoc2_input.txt")
    # do the initial corrections first
    input[1] = 12
    input[2] = 2
    #print(input)
    counter = 0
    opcode = input[counter]
    print(opcode)
    while opcode:
        print("Opcode: ", opcode, ", counter: ", counter)
        if opcode == 1:
            input = oper_add(input, input[counter:counter+4])
            counter += 4
            opcode = input[counter]
        elif opcode == 2:
            input = oper_multip(input, input[counter:counter + 4])
            counter += 4
            opcode = input[counter]
        elif opcode == 99:
            print("Stop, code 99")
            break
        else:
            print("Stop, weird code")
            break


    print(input[0])



if __name__ == "__main__":
    main()