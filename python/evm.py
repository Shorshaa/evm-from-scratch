#!/usr/bin/env python3

# EVM From Scratch
# Python template
#
# To work on EVM From Scratch in Python:
#
# - Install Python3: https://www.python.org/downloads/
# - Go to the `python` directory: `cd python`
# - Edit `evm.py` (this file!), see TODO below
# - Run `python3 evm.py` to run the tests

import json
import os

def push(idOP, iCode, iPc):
    ''' This function will take care of each of the PUSH opcode
        TO DO:
         + better parameter naming, these just suck
    '''
    PUSH_BASE = 0x5F
    nbElements = idOP-PUSH_BASE
    print("PUSH function. Length =%s\n"%(hex(idOP)))

    #Here we read each of the bytes in the Code structure and append on the previous reading 
    # example for PUSH4 test, ltmp will have the strings '00', '11', '22', '33' appended into
    # '00112233' then the format function on the return will transform those into valid number
    # forcing the convertion as if that were an HEX value.

    index = 0
    ltmp = ''
    while index < nbElements:
        print(index)
        ltmp += f'{iCode[iPc]:x}'
        iPc += 1
        index += 1

    return(int(ltmp,base=16),iPc)


def evm(code):
    pc = 0
    success = True
    stack = []

    while pc < len(code):
        op = code[pc]
        pc += 1

        # TODO: implement the EVM here!
        if op >= 0x60 and op<=0x7F:    # This is a PUSHxx OPCODE
           ltmp, pc = push(op, code, pc)
           stack.append(ltmp)
        
    print("strack is  %s\n"%(repr(stack)))
    return (success, stack)

def test():
    script_dirname = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(script_dirname, "..", "evm.json")
    with open(json_file) as f:
        data = json.load(f)
        total = len(data)

        for i, test in enumerate(data):
            # Note: as the test cases get more complex, you'll need to modify this
            # to pass down more arguments to the evm function
            code = bytes.fromhex(test['code']['bin'])
            (success, stack) = evm(code)

            expected_stack = [int(x, 16) for x in test['expect']['stack']]
            
            if stack != expected_stack or success != test['expect']['success']:
                print(f"❌ Test #{i + 1}/{total} {test['name']}")
                if stack != expected_stack:
                    print("Stack doesn't match")
                    print(" expected:", expected_stack)
                    print("   actual:", stack)
                else:
                    print("Success doesn't match")
                    print(" expected:", test['expect']['success'])
                    print("   actual:", success)
                print("")
                print("Test code:")
                print(test['code']['asm'])
                print("")
                print("Hint:", test['hint'])
                print("")
                print(f"Progress: {i}/{len(data)}")
                print("")
                break
            else:
                print(f"✓  Test #{i + 1}/{total} {test['name']}")

if __name__ == '__main__':
    test()
