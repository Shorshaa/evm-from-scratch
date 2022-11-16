# General Information

Choice for implementation: Python

Links to documents used during this exercises:
- [https://cypherpunks-core.github.io/ethereumbook/13evm.html](https://cypherpunks-core.github.io/ethereumbook/13evm.html)
- [https://blog.trustlook.com/understand-evm-bytecode-part-1/](https://blog.trustlook.com/understand-evm-bytecode-part-1/)
- [https://ethereum.org/pt-br/developers/docs/evm/opcodes/](https://ethereum.org/pt-br/developers/docs/evm/opcodes/)

# Notes on the implementation and explanations on the choices

## PUSHxx

the PUSHxx OPCODES can go from PUSH1 (only 1 byte) to PUSH32 (32 bytes).
The codes go from 0x60 (decimal 96) to 0x7F (decimal 127). So the OPCODE is between these values and we substract 5F (decimal 95) the remainder would correspond to the number of bytes we need to PUSH to the stack
