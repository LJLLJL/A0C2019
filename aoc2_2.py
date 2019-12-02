def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    out2 = out[0].split(",")
    for i in range(0, len(out2)):
        out2[i] = int(out2[i])
    f.close()
    return out2

def oper_add(input,slice):
    #print(slice)
    input[slice[3]] = input[slice[1]] + input[slice[2]]
    return input

def oper_multip(input,slice):
    input[slice[3]] = input[slice[1]] * input[slice[2]]
    return input

def main():
    input = read_input("aoc2_input.txt")
    found = 0
    for noun in range (0,100):
        if found == 1:
            break
        for verb in range (0,100):
            input_temp = input.copy()
            print(noun, ", ", verb)

            input_temp[1] = noun
            input_temp[2] = verb
            print(input_temp)
            #print(input)
            counter = 0
            opcode = input_temp[counter]
            #print(opcode)
            while opcode:
                #print("Opcode: ", opcode, ", counter: ", counter)
                if opcode == 1:
                    input_temp = oper_add(input_temp, input_temp[counter:counter+4])
                    counter += 4
                    opcode = input_temp[counter]
                elif opcode == 2:
                    input_temp = oper_multip(input_temp, input_temp[counter:counter + 4])
                    counter += 4
                    opcode = input_temp[counter]
                elif opcode == 99:
                    print("Stop, code 99")
                    break
                else:
                    print("Stop, weird code")
                    break
            print("output is: ", input_temp[0])
            if input_temp[0] == 19690720:
                print("Input is: ", input_temp[0], ", noun is: ", noun, ", verb is: ", verb)
                found = 1
                print("Solution: ", 100*noun+verb)
                break



if __name__ == "__main__":
    main()