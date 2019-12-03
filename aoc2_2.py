import aoc2_1 as ac


def main():
    input = ac.read_input("aoc2_input.txt")
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
                    input_temp = ac.oper_add(input_temp, input_temp[counter:counter+4])
                    counter += 4
                    opcode = input_temp[counter]
                elif opcode == 2:
                    input_temp = ac.oper_multip(input_temp, input_temp[counter:counter + 4])
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