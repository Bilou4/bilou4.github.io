# Buffer Overflow

## Introduction - The Basics

Managing the memory of a binary:
* https://manybutfinite.com/post/anatomy-of-a-program-in-memory/

### Memory Segments

* **code**: contains the instructions to be executed. The instructions are not linear (presence of jumps to other addresses). It is a fixed size segment, read-only. If the program is run several times, this segment will only be present once in RAM.
* **data**: used to store *initialized* global and static variables. The segment is of fixed size, readable and writable.
* **bss**: allows you to store *uninitialized* global and static variables. Fixed size segment, readable and writable.
* **heap**: A segment used by the programmer to allocate memory. Once used, these blocks must be deallocated. It varies in size as the program uses it. It has a growing size towards the bottom (high memory addresses).
* **stack**: A variable size segment that contains the environment (function activation block) of each function, its parameters, its variables, the return address.


## Buffer Overflow (BOF)

The flaw: copying data without checking the size. This is a bug whereby a process, when writing to a buffer, writes outside the space allocated to the buffer, thereby overwriting information needed by the process. The aim is to make the process execute instructions.

## Security
It is impossible to eradicate application vulnerabilities because the processor does not differentiate between code and data. But there are ways of protecting against them:

* **ASLR (Address Space Layout Randomization)**: allows data zones to be placed randomly in virtual memory (position of heap, stack, libraries). This limits the effect of BOF attacks. `ldd /bin/sh` is used to check when a process changes address.
*  **Bit NX (non-executable memory page)**: Technique used in processors to separate areas of memory containing instructions, i.e. executable instructions, from areas containing data.
