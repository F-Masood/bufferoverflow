# Exploiting Buffer Overflow
Python2 based Bufferoverflow scripts I developed while doing the Vulnhub box Netsart by Foxlox 

Walkthrough link: https://grumpygeekwrites.wordpress.com/2020/12/07/netstart-vulnhub-walk-through-tutorial/

IMP steps to remember are:

0. Spiking.
1. Fuzzing / Crashing the program with some bytes.
2. Noting down those bytes.
3. Creating a unique pattern via MSF of those bytes length and sending it to the program.
4. Again crashing the program and noting down the value of EIP. 
5. Giving the EIP value to MSF offset for finding the exact crash point. 
6. Controlling EIP, to check whether our EIP is filled with 04 x B (EIP = 42 42 42 24)
7. Finding badchars, removing it from the BadChars array again and again. We should see neat and clean output from 0000-FFFF.
8. Finding the JMP address in ".dll" using mona. Use command = !mona find -s ‘\xff\xe4’ -m login_support.dll. Note down all the addresses
9. Generating a SHELL payload using MSF Venom; remember to select proper architecture and specifying the BADCHARS we found. 
10. We should now get shell, our PAYLOAD would be something like ---> A*(offset value) + JMP Address in little endian format + 8/16/32 NOPs + shellcode
