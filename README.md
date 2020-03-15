# [glow wine](https://crackmes.one/crackme/5df26b4033c5d419aa013362)

Desafio simples (nivel 1) do site crackmes.one

Baixe o arquivo zipado e leia o FAQ para descobrir qual é a senha do zip.

## Pré-requisito:
- linux (ou algo compatível, foi feito e testando em um manjaro)
- python 3

## Informações sobre o binário:

```bash
$ file glowwine
glowwine: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=66947d7a8e07d92b59c63f9a1d6f8354573d9a8f, not stripped

$ readelf -a ./glowwine
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x5c0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          6568 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         9
  Size of section headers:           64 (bytes)
  Number of section headers:         29
  Section header string table index: 28

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         0000000000000238  00000238
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.ABI-tag     NOTE             0000000000000254  00000254
       0000000000000020  0000000000000000   A       0     0     4
  [ 3] .note.gnu.build-i NOTE             0000000000000274  00000274
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .gnu.hash         GNU_HASH         0000000000000298  00000298
       000000000000001c  0000000000000000   A       5     0     8
  [ 5] .dynsym           DYNSYM           00000000000002b8  000002b8
       00000000000000d8  0000000000000018   A       6     1     8
  [ 6] .dynstr           STRTAB           0000000000000390  00000390
       000000000000008e  0000000000000000   A       0     0     1
  [ 7] .gnu.version      VERSYM           000000000000041e  0000041e
       0000000000000012  0000000000000002   A       5     0     2
  [ 8] .gnu.version_r    VERNEED          0000000000000430  00000430
       0000000000000020  0000000000000000   A       6     1     8
  [ 9] .rela.dyn         RELA             0000000000000450  00000450
       00000000000000c0  0000000000000018   A       5     0     8
  [10] .rela.plt         RELA             0000000000000510  00000510
       0000000000000048  0000000000000018  AI       5    22     8
  [11] .init             PROGBITS         0000000000000558  00000558
       0000000000000017  0000000000000000  AX       0     0     4
  [12] .plt              PROGBITS         0000000000000570  00000570
       0000000000000040  0000000000000010  AX       0     0     16
  [13] .plt.got          PROGBITS         00000000000005b0  000005b0
       0000000000000008  0000000000000008  AX       0     0     8
  [14] .text             PROGBITS         00000000000005c0  000005c0
       0000000000000272  0000000000000000  AX       0     0     16
  [15] .fini             PROGBITS         0000000000000834  00000834
       0000000000000009  0000000000000000  AX       0     0     4
  [16] .rodata           PROGBITS         0000000000000840  00000840
       000000000000005a  0000000000000000   A       0     0     8
  [17] .eh_frame_hdr     PROGBITS         000000000000089c  0000089c
       0000000000000044  0000000000000000   A       0     0     4
  [18] .eh_frame         PROGBITS         00000000000008e0  000008e0
       0000000000000128  0000000000000000   A       0     0     8
  [19] .init_array       INIT_ARRAY       0000000000200da8  00000da8
       0000000000000008  0000000000000008  WA       0     0     8
  [20] .fini_array       FINI_ARRAY       0000000000200db0  00000db0
       0000000000000008  0000000000000008  WA       0     0     8
  [21] .dynamic          DYNAMIC          0000000000200db8  00000db8
       00000000000001f0  0000000000000010  WA       6     0     8
  [22] .got              PROGBITS         0000000000200fa8  00000fa8
       0000000000000058  0000000000000008  WA       0     0     8
  [23] .data             PROGBITS         0000000000201000  00001000
       0000000000000010  0000000000000000  WA       0     0     8
  [24] .bss              NOBITS           0000000000201010  00001010
       0000000000000008  0000000000000000  WA       0     0     1
  [25] .comment          PROGBITS         0000000000000000  00001010
       000000000000002b  0000000000000001  MS       0     0     1
  [26] .symtab           SYMTAB           0000000000000000  00001040
       0000000000000630  0000000000000018          27    43     8
  [27] .strtab           STRTAB           0000000000000000  00001670
       0000000000000238  0000000000000000           0     0     1
  [28] .shstrtab         STRTAB           0000000000000000  000018a8
       00000000000000fe  0000000000000000           0     0     1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  l (large), p (processor specific)

There are no section groups in this file.

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
  PHDR           0x0000000000000040 0x0000000000000040 0x0000000000000040
                 0x00000000000001f8 0x00000000000001f8  R      0x8
  INTERP         0x0000000000000238 0x0000000000000238 0x0000000000000238
                 0x000000000000001c 0x000000000000001c  R      0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000a08 0x0000000000000a08  R E    0x200000
  LOAD           0x0000000000000da8 0x0000000000200da8 0x0000000000200da8
                 0x0000000000000268 0x0000000000000270  RW     0x200000
  DYNAMIC        0x0000000000000db8 0x0000000000200db8 0x0000000000200db8
                 0x00000000000001f0 0x00000000000001f0  RW     0x8
  NOTE           0x0000000000000254 0x0000000000000254 0x0000000000000254
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_EH_FRAME   0x000000000000089c 0x000000000000089c 0x000000000000089c
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     0x10
  GNU_RELRO      0x0000000000000da8 0x0000000000200da8 0x0000000000200da8
                 0x0000000000000258 0x0000000000000258  R      0x1

 Section to Segment mapping:
  Segment Sections...
   00     
   01     .interp 
   02     .interp .note.ABI-tag .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt .init .plt .plt.got .text .fini .rodata .eh_frame_hdr .eh_frame 
   03     .init_array .fini_array .dynamic .got .data .bss 
   04     .dynamic 
   05     .note.ABI-tag .note.gnu.build-id 
   06     .eh_frame_hdr 
   07     
   08     .init_array .fini_array .dynamic .got 

Dynamic section at offset 0xdb8 contains 27 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x558
 0x000000000000000d (FINI)               0x834
 0x0000000000000019 (INIT_ARRAY)         0x200da8
 0x000000000000001b (INIT_ARRAYSZ)       8 (bytes)
 0x000000000000001a (FINI_ARRAY)         0x200db0
 0x000000000000001c (FINI_ARRAYSZ)       8 (bytes)
 0x000000006ffffef5 (GNU_HASH)           0x298
 0x0000000000000005 (STRTAB)             0x390
 0x0000000000000006 (SYMTAB)             0x2b8
 0x000000000000000a (STRSZ)              142 (bytes)
 0x000000000000000b (SYMENT)             24 (bytes)
 0x0000000000000015 (DEBUG)              0x0
 0x0000000000000003 (PLTGOT)             0x200fa8
 0x0000000000000002 (PLTRELSZ)           72 (bytes)
 0x0000000000000014 (PLTREL)             RELA
 0x0000000000000017 (JMPREL)             0x510
 0x0000000000000007 (RELA)               0x450
 0x0000000000000008 (RELASZ)             192 (bytes)
 0x0000000000000009 (RELAENT)            24 (bytes)
 0x000000000000001e (FLAGS)              BIND_NOW
 0x000000006ffffffb (FLAGS_1)            Flags: NOW PIE
 0x000000006ffffffe (VERNEED)            0x430
 0x000000006fffffff (VERNEEDNUM)         1
 0x000000006ffffff0 (VERSYM)             0x41e
 0x000000006ffffff9 (RELACOUNT)          3
 0x0000000000000000 (NULL)               0x0

Relocation section '.rela.dyn' at offset 0x450 contains 8 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000200da8  000000000008 R_X86_64_RELATIVE                    6c0
000000200db0  000000000008 R_X86_64_RELATIVE                    680
000000201008  000000000008 R_X86_64_RELATIVE                    201008
000000200fd8  000100000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_deregisterTMClone + 0
000000200fe0  000400000006 R_X86_64_GLOB_DAT 0000000000000000 __libc_start_main@GLIBC_2.2.5 + 0
000000200fe8  000500000006 R_X86_64_GLOB_DAT 0000000000000000 __gmon_start__ + 0
000000200ff0  000700000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_registerTMCloneTa + 0
000000200ff8  000800000006 R_X86_64_GLOB_DAT 0000000000000000 __cxa_finalize@GLIBC_2.2.5 + 0

Relocation section '.rela.plt' at offset 0x510 contains 3 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000200fc0  000200000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0
000000200fc8  000300000007 R_X86_64_JUMP_SLO 0000000000000000 strlen@GLIBC_2.2.5 + 0
000000200fd0  000600000007 R_X86_64_JUMP_SLO 0000000000000000 exit@GLIBC_2.2.5 + 0

The decoding of unwind sections for machine type Advanced Micro Devices X86-64 is not currently supported.

Symbol table '.dynsym' contains 9 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND strlen@GLIBC_2.2.5 (2)
     4: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.2.5 (2)
     5: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
     6: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@GLIBC_2.2.5 (2)
     7: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
     8: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@GLIBC_2.2.5 (2)

Symbol table '.symtab' contains 66 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000238     0 SECTION LOCAL  DEFAULT    1 
     2: 0000000000000254     0 SECTION LOCAL  DEFAULT    2 
     3: 0000000000000274     0 SECTION LOCAL  DEFAULT    3 
     4: 0000000000000298     0 SECTION LOCAL  DEFAULT    4 
     5: 00000000000002b8     0 SECTION LOCAL  DEFAULT    5 
     6: 0000000000000390     0 SECTION LOCAL  DEFAULT    6 
     7: 000000000000041e     0 SECTION LOCAL  DEFAULT    7 
     8: 0000000000000430     0 SECTION LOCAL  DEFAULT    8 
     9: 0000000000000450     0 SECTION LOCAL  DEFAULT    9 
    10: 0000000000000510     0 SECTION LOCAL  DEFAULT   10 
    11: 0000000000000558     0 SECTION LOCAL  DEFAULT   11 
    12: 0000000000000570     0 SECTION LOCAL  DEFAULT   12 
    13: 00000000000005b0     0 SECTION LOCAL  DEFAULT   13 
    14: 00000000000005c0     0 SECTION LOCAL  DEFAULT   14 
    15: 0000000000000834     0 SECTION LOCAL  DEFAULT   15 
    16: 0000000000000840     0 SECTION LOCAL  DEFAULT   16 
    17: 000000000000089c     0 SECTION LOCAL  DEFAULT   17 
    18: 00000000000008e0     0 SECTION LOCAL  DEFAULT   18 
    19: 0000000000200da8     0 SECTION LOCAL  DEFAULT   19 
    20: 0000000000200db0     0 SECTION LOCAL  DEFAULT   20 
    21: 0000000000200db8     0 SECTION LOCAL  DEFAULT   21 
    22: 0000000000200fa8     0 SECTION LOCAL  DEFAULT   22 
    23: 0000000000201000     0 SECTION LOCAL  DEFAULT   23 
    24: 0000000000201010     0 SECTION LOCAL  DEFAULT   24 
    25: 0000000000000000     0 SECTION LOCAL  DEFAULT   25 
    26: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    27: 00000000000005f0     0 FUNC    LOCAL  DEFAULT   14 deregister_tm_clones
    28: 0000000000000630     0 FUNC    LOCAL  DEFAULT   14 register_tm_clones
    29: 0000000000000680     0 FUNC    LOCAL  DEFAULT   14 __do_global_dtors_aux
    30: 0000000000201010     1 OBJECT  LOCAL  DEFAULT   24 completed.7697
    31: 0000000000200db0     0 OBJECT  LOCAL  DEFAULT   20 __do_global_dtors_aux_fin
    32: 00000000000006c0     0 FUNC    LOCAL  DEFAULT   14 frame_dummy
    33: 0000000000200da8     0 OBJECT  LOCAL  DEFAULT   19 __frame_dummy_init_array_
    34: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS somecrackme.c
    35: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    36: 0000000000000a04     0 OBJECT  LOCAL  DEFAULT   18 __FRAME_END__
    37: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS 
    38: 0000000000200db0     0 NOTYPE  LOCAL  DEFAULT   19 __init_array_end
    39: 0000000000200db8     0 OBJECT  LOCAL  DEFAULT   21 _DYNAMIC
    40: 0000000000200da8     0 NOTYPE  LOCAL  DEFAULT   19 __init_array_start
    41: 000000000000089c     0 NOTYPE  LOCAL  DEFAULT   17 __GNU_EH_FRAME_HDR
    42: 0000000000200fa8     0 OBJECT  LOCAL  DEFAULT   22 _GLOBAL_OFFSET_TABLE_
    43: 0000000000000830     2 FUNC    GLOBAL DEFAULT   14 __libc_csu_fini
    44: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
    45: 0000000000201000     0 NOTYPE  WEAK   DEFAULT   23 data_start
    46: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@@GLIBC_2.2.5
    47: 0000000000201010     0 NOTYPE  GLOBAL DEFAULT   23 _edata
    48: 0000000000000834     0 FUNC    GLOBAL DEFAULT   15 _fini
    49: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND strlen@@GLIBC_2.2.5
    50: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@@GLIBC_
    51: 0000000000201000     0 NOTYPE  GLOBAL DEFAULT   23 __data_start
    52: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    53: 0000000000201008     0 OBJECT  GLOBAL HIDDEN    23 __dso_handle
    54: 0000000000000840     4 OBJECT  GLOBAL DEFAULT   16 _IO_stdin_used
    55: 00000000000007c0   101 FUNC    GLOBAL DEFAULT   14 __libc_csu_init
    56: 0000000000201018     0 NOTYPE  GLOBAL DEFAULT   24 _end
    57: 00000000000005c0    43 FUNC    GLOBAL DEFAULT   14 _start
    58: 0000000000201010     0 NOTYPE  GLOBAL DEFAULT   24 __bss_start
    59: 00000000000006ca   213 FUNC    GLOBAL DEFAULT   14 main
    60: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@@GLIBC_2.2.5
    61: 0000000000201010     0 OBJECT  GLOBAL HIDDEN    23 __TMC_END__
    62: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    63: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@@GLIBC_2.2
    64: 0000000000000558     0 FUNC    GLOBAL DEFAULT   11 _init
    65: 000000000000079f    26 FUNC    GLOBAL DEFAULT   14 sorrybro

Version symbols section '.gnu.version' contains 9 entries:
 Addr: 0x000000000000041e  Offset: 0x00041e  Link: 5 (.dynsym)
  000:   0 (*local*)       0 (*local*)       2 (GLIBC_2.2.5)   2 (GLIBC_2.2.5)
  004:   2 (GLIBC_2.2.5)   0 (*local*)       2 (GLIBC_2.2.5)   0 (*local*)    
  008:   2 (GLIBC_2.2.5)

Version needs section '.gnu.version_r' contains 1 entry:
 Addr: 0x0000000000000430  Offset: 0x000430  Link: 6 (.dynstr)
  000000: Version: 1  File: libc.so.6  Cnt: 1
  0x0010:   Name: GLIBC_2.2.5  Flags: none  Version: 2

Displaying notes found in: .note.ABI-tag
  Owner                Data size 	Description
  GNU                  0x00000010	NT_GNU_ABI_TAG (ABI version tag)
    OS: Linux, ABI: 3.2.0

Displaying notes found in: .note.gnu.build-id
  Owner                Data size 	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 66947d7a8e07d92b59c63f9a1d6f8354573d9a8f
  
$ strings -t d -d ./glowwine
    568 /lib64/ld-linux-x86-64.so.2
    913 libc.so.6
    923 exit
    928 puts
    933 strlen
    940 __cxa_finalize
    955 __libc_start_main
    973 GLIBC_2.2.5
    985 _ITM_deregisterTMCloneTable
   1013 __gmon_start__
   1028 _ITM_registerTMCloneTable
   1675 =g	 
   1689 =j	 
   1984 AWAVI
   1991 AUATL
   2074 []A\A]A^A_
   2120 usage: ./glowwine <key>
   2144 nice one! Now, can you keygen me?
   2178 wrong key, try again :/
   2375 ;*3$"
```

## Assembly extraido via objdump:

```bash
$ objdump -M intel -d -C ./glowwine
```

```asm
./glowwine:     file format elf64-x86-64


Disassembly of section .init:

0000000000000558 <_init>:
 558:	48 83 ec 08          	sub    rsp,0x8
 55c:	48 8b 05 85 0a 20 00 	mov    rax,QWORD PTR [rip+0x200a85]        # 200fe8 <__gmon_start__>
 563:	48 85 c0             	test   rax,rax
 566:	74 02                	je     56a <_init+0x12>
 568:	ff d0                	call   rax
 56a:	48 83 c4 08          	add    rsp,0x8
 56e:	c3                   	ret    

Disassembly of section .plt:

0000000000000570 <.plt>:
 570:	ff 35 3a 0a 20 00    	push   QWORD PTR [rip+0x200a3a]        # 200fb0 <_GLOBAL_OFFSET_TABLE_+0x8>
 576:	ff 25 3c 0a 20 00    	jmp    QWORD PTR [rip+0x200a3c]        # 200fb8 <_GLOBAL_OFFSET_TABLE_+0x10>
 57c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000000580 <puts@plt>:
 580:	ff 25 3a 0a 20 00    	jmp    QWORD PTR [rip+0x200a3a]        # 200fc0 <puts@GLIBC_2.2.5>
 586:	68 00 00 00 00       	push   0x0
 58b:	e9 e0 ff ff ff       	jmp    570 <.plt>

0000000000000590 <strlen@plt>:
 590:	ff 25 32 0a 20 00    	jmp    QWORD PTR [rip+0x200a32]        # 200fc8 <strlen@GLIBC_2.2.5>
 596:	68 01 00 00 00       	push   0x1
 59b:	e9 d0 ff ff ff       	jmp    570 <.plt>

00000000000005a0 <exit@plt>:
 5a0:	ff 25 2a 0a 20 00    	jmp    QWORD PTR [rip+0x200a2a]        # 200fd0 <exit@GLIBC_2.2.5>
 5a6:	68 02 00 00 00       	push   0x2
 5ab:	e9 c0 ff ff ff       	jmp    570 <.plt>

Disassembly of section .plt.got:

00000000000005b0 <__cxa_finalize@plt>:
 5b0:	ff 25 42 0a 20 00    	jmp    QWORD PTR [rip+0x200a42]        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 5b6:	66 90                	xchg   ax,ax

Disassembly of section .text:

00000000000005c0 <_start>:
 5c0:	31 ed                	xor    ebp,ebp
 5c2:	49 89 d1             	mov    r9,rdx
 5c5:	5e                   	pop    rsi
 5c6:	48 89 e2             	mov    rdx,rsp
 5c9:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
 5cd:	50                   	push   rax
 5ce:	54                   	push   rsp
 5cf:	4c 8d 05 5a 02 00 00 	lea    r8,[rip+0x25a]        # 830 <__libc_csu_fini>
 5d6:	48 8d 0d e3 01 00 00 	lea    rcx,[rip+0x1e3]        # 7c0 <__libc_csu_init>
 5dd:	48 8d 3d e6 00 00 00 	lea    rdi,[rip+0xe6]        # 6ca <main>
 5e4:	ff 15 f6 09 20 00    	call   QWORD PTR [rip+0x2009f6]        # 200fe0 <__libc_start_main@GLIBC_2.2.5>
 5ea:	f4                   	hlt    
 5eb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000000005f0 <deregister_tm_clones>:
 5f0:	48 8d 3d 19 0a 20 00 	lea    rdi,[rip+0x200a19]        # 201010 <__TMC_END__>
 5f7:	55                   	push   rbp
 5f8:	48 8d 05 11 0a 20 00 	lea    rax,[rip+0x200a11]        # 201010 <__TMC_END__>
 5ff:	48 39 f8             	cmp    rax,rdi
 602:	48 89 e5             	mov    rbp,rsp
 605:	74 19                	je     620 <deregister_tm_clones+0x30>
 607:	48 8b 05 ca 09 20 00 	mov    rax,QWORD PTR [rip+0x2009ca]        # 200fd8 <_ITM_deregisterTMCloneTable>
 60e:	48 85 c0             	test   rax,rax
 611:	74 0d                	je     620 <deregister_tm_clones+0x30>
 613:	5d                   	pop    rbp
 614:	ff e0                	jmp    rax
 616:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 61d:	00 00 00 
 620:	5d                   	pop    rbp
 621:	c3                   	ret    
 622:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 626:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 62d:	00 00 00 

0000000000000630 <register_tm_clones>:
 630:	48 8d 3d d9 09 20 00 	lea    rdi,[rip+0x2009d9]        # 201010 <__TMC_END__>
 637:	48 8d 35 d2 09 20 00 	lea    rsi,[rip+0x2009d2]        # 201010 <__TMC_END__>
 63e:	55                   	push   rbp
 63f:	48 29 fe             	sub    rsi,rdi
 642:	48 89 e5             	mov    rbp,rsp
 645:	48 c1 fe 03          	sar    rsi,0x3
 649:	48 89 f0             	mov    rax,rsi
 64c:	48 c1 e8 3f          	shr    rax,0x3f
 650:	48 01 c6             	add    rsi,rax
 653:	48 d1 fe             	sar    rsi,1
 656:	74 18                	je     670 <register_tm_clones+0x40>
 658:	48 8b 05 91 09 20 00 	mov    rax,QWORD PTR [rip+0x200991]        # 200ff0 <_ITM_registerTMCloneTable>
 65f:	48 85 c0             	test   rax,rax
 662:	74 0c                	je     670 <register_tm_clones+0x40>
 664:	5d                   	pop    rbp
 665:	ff e0                	jmp    rax
 667:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
 66e:	00 00 
 670:	5d                   	pop    rbp
 671:	c3                   	ret    
 672:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 676:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 67d:	00 00 00 

0000000000000680 <__do_global_dtors_aux>:
 680:	80 3d 89 09 20 00 00 	cmp    BYTE PTR [rip+0x200989],0x0        # 201010 <__TMC_END__>
 687:	75 2f                	jne    6b8 <__do_global_dtors_aux+0x38>
 689:	48 83 3d 67 09 20 00 	cmp    QWORD PTR [rip+0x200967],0x0        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 690:	00 
 691:	55                   	push   rbp
 692:	48 89 e5             	mov    rbp,rsp
 695:	74 0c                	je     6a3 <__do_global_dtors_aux+0x23>
 697:	48 8b 3d 6a 09 20 00 	mov    rdi,QWORD PTR [rip+0x20096a]        # 201008 <__dso_handle>
 69e:	e8 0d ff ff ff       	call   5b0 <__cxa_finalize@plt>
 6a3:	e8 48 ff ff ff       	call   5f0 <deregister_tm_clones>
 6a8:	c6 05 61 09 20 00 01 	mov    BYTE PTR [rip+0x200961],0x1        # 201010 <__TMC_END__>
 6af:	5d                   	pop    rbp
 6b0:	c3                   	ret    
 6b1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
 6b8:	f3 c3                	repz ret 
 6ba:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]

00000000000006c0 <frame_dummy>:
 6c0:	55                   	push   rbp
 6c1:	48 89 e5             	mov    rbp,rsp
 6c4:	5d                   	pop    rbp
 6c5:	e9 66 ff ff ff       	jmp    630 <register_tm_clones>

00000000000006ca <main>:
 6ca:	55                   	push   rbp
 6cb:	48 89 e5             	mov    rbp,rsp
 6ce:	48 83 ec 10          	sub    rsp,0x10
 6d2:	89 7d fc             	mov    DWORD PTR [rbp-0x4],edi
 6d5:	48 89 75 f0          	mov    QWORD PTR [rbp-0x10],rsi
 6d9:	83 7d fc 01          	cmp    DWORD PTR [rbp-0x4],0x1
 6dd:	7f 16                	jg     6f5 <main+0x2b>
 6df:	48 8d 3d 62 01 00 00 	lea    rdi,[rip+0x162]        # 848 <_IO_stdin_used+0x8>
 6e6:	e8 95 fe ff ff       	call   580 <puts@plt>
 6eb:	b8 00 00 00 00       	mov    eax,0x0
 6f0:	e9 a8 00 00 00       	jmp    79d <main+0xd3>
 6f5:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 6f9:	48 83 c0 08          	add    rax,0x8
 6fd:	48 8b 00             	mov    rax,QWORD PTR [rax]
 700:	48 89 c7             	mov    rdi,rax
 703:	e8 88 fe ff ff       	call   590 <strlen@plt>
 708:	48 83 f8 05          	cmp    rax,0x5
 70c:	74 0a                	je     718 <main+0x4e>
 70e:	b8 00 00 00 00       	mov    eax,0x0
 713:	e8 87 00 00 00       	call   79f <sorrybro>
 718:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 71c:	48 83 c0 08          	add    rax,0x8
 720:	48 8b 00             	mov    rax,QWORD PTR [rax]
 723:	48 83 c0 01          	add    rax,0x1
 727:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 72a:	3c 40                	cmp    al,0x40
 72c:	74 0a                	je     738 <main+0x6e>
 72e:	b8 00 00 00 00       	mov    eax,0x0
 733:	e8 67 00 00 00       	call   79f <sorrybro>
 738:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 73c:	48 83 c0 08          	add    rax,0x8
 740:	48 8b 00             	mov    rax,QWORD PTR [rax]
 743:	48 83 c0 02          	add    rax,0x2
 747:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 74a:	0f be d0             	movsx  edx,al
 74d:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 751:	48 83 c0 08          	add    rax,0x8
 755:	48 8b 00             	mov    rax,QWORD PTR [rax]
 758:	48 83 c0 03          	add    rax,0x3
 75c:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 75f:	0f be c0             	movsx  eax,al
 762:	01 c2                	add    edx,eax
 764:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
 768:	48 83 c0 08          	add    rax,0x8
 76c:	48 8b 00             	mov    rax,QWORD PTR [rax]
 76f:	48 83 c0 04          	add    rax,0x4
 773:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 776:	0f be c0             	movsx  eax,al
 779:	01 d0                	add    eax,edx
 77b:	3d 2c 01 00 00       	cmp    eax,0x12c
 780:	74 0a                	je     78c <main+0xc2>
 782:	b8 00 00 00 00       	mov    eax,0x0
 787:	e8 13 00 00 00       	call   79f <sorrybro>
 78c:	48 8d 3d cd 00 00 00 	lea    rdi,[rip+0xcd]        # 860 <_IO_stdin_used+0x20>
 793:	e8 e8 fd ff ff       	call   580 <puts@plt>
 798:	b8 00 00 00 00       	mov    eax,0x0
 79d:	c9                   	leave  
 79e:	c3                   	ret    

000000000000079f <sorrybro>:
 79f:	55                   	push   rbp
 7a0:	48 89 e5             	mov    rbp,rsp
 7a3:	48 8d 3d d8 00 00 00 	lea    rdi,[rip+0xd8]        # 882 <_IO_stdin_used+0x42>
 7aa:	e8 d1 fd ff ff       	call   580 <puts@plt>
 7af:	bf 00 00 00 00       	mov    edi,0x0
 7b4:	e8 e7 fd ff ff       	call   5a0 <exit@plt>
 7b9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

00000000000007c0 <__libc_csu_init>:
 7c0:	41 57                	push   r15
 7c2:	41 56                	push   r14
 7c4:	49 89 d7             	mov    r15,rdx
 7c7:	41 55                	push   r13
 7c9:	41 54                	push   r12
 7cb:	4c 8d 25 d6 05 20 00 	lea    r12,[rip+0x2005d6]        # 200da8 <__frame_dummy_init_array_entry>
 7d2:	55                   	push   rbp
 7d3:	48 8d 2d d6 05 20 00 	lea    rbp,[rip+0x2005d6]        # 200db0 <__do_global_dtors_aux_fini_array_entry>
 7da:	53                   	push   rbx
 7db:	41 89 fd             	mov    r13d,edi
 7de:	49 89 f6             	mov    r14,rsi
 7e1:	4c 29 e5             	sub    rbp,r12
 7e4:	48 83 ec 08          	sub    rsp,0x8
 7e8:	48 c1 fd 03          	sar    rbp,0x3
 7ec:	e8 67 fd ff ff       	call   558 <_init>
 7f1:	48 85 ed             	test   rbp,rbp
 7f4:	74 20                	je     816 <__libc_csu_init+0x56>
 7f6:	31 db                	xor    ebx,ebx
 7f8:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
 7ff:	00 
 800:	4c 89 fa             	mov    rdx,r15
 803:	4c 89 f6             	mov    rsi,r14
 806:	44 89 ef             	mov    edi,r13d
 809:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
 80d:	48 83 c3 01          	add    rbx,0x1
 811:	48 39 dd             	cmp    rbp,rbx
 814:	75 ea                	jne    800 <__libc_csu_init+0x40>
 816:	48 83 c4 08          	add    rsp,0x8
 81a:	5b                   	pop    rbx
 81b:	5d                   	pop    rbp
 81c:	41 5c                	pop    r12
 81e:	41 5d                	pop    r13
 820:	41 5e                	pop    r14
 822:	41 5f                	pop    r15
 824:	c3                   	ret    
 825:	90                   	nop
 826:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 82d:	00 00 00 

0000000000000830 <__libc_csu_fini>:
 830:	f3 c3                	repz ret 

Disassembly of section .fini:

0000000000000834 <_fini>:
 834:	48 83 ec 08          	sub    rsp,0x8
 838:	48 83 c4 08          	add    rsp,0x8
 83c:	c3                   	ret    
```

## Ponto de entrada do binário

Através do resultado do readelf, podemos ver que a entrada do binário está em: `Entry point address: 0x5c0`

## Análise e RE:
### Iniciando o debug com o texto "1234567890"

Rodando o binário no gdb, é possível perceber que existe uma comparação do length do texto fornecido com 0x5:
```asm
 708:	48 83 f8 05          	cmp    rax,0x5
 70c:	74 0a                	je     718 <main+0x4e>
```

Sem isto, o programa da um call para a função "sorrybro" (que da print da mensagem de erro e exit)

### Reiniciando o debug com o texto "12345"

Valor que entrou, a primeira letra, soma 1 (ex: 0x31 + 0x1, 0x32)

Compara o valor com 0x40, logo, precisa ser fornecido 0x39 (equivale ao texto "9")

Sem isto, voltamos a cair em "sorrybro"

Reiniciando...

### Reiniciando o debug com o texto "92345"

Continua errado... aparentemente, a comparação é com a segunda letra do texto inserido, 0x40

Reiniciando

### Reiniciando o debug com o texto "1@345"

É isso, agora passamos, agora, foram somados todos os outros caracteres (em ascii, 0x33 + 0x34 + 0x35= 0x9c)

Agora, é comparado se o valor é igual a 0x12c, ou seja, errei a combinação

É chamado sorrybro

Reiniciando com caracteres que, em ascii, somados, dão 0x12c

0x12c em decimal é igual a 300, na tabela ascii, d equivale a 100 (0x64), vamos tentar 1@ddd

### Reiniciando o debug com o texto "1@ddd"

É isso, após as consecutivas somas, temos o valor 0x12c, o código passa

Temos a resposta "nice one! Now, can you keygen me?"

Hora do keygen...


### Keygen

Rode o arquivo keygen.py, receba uma key e coloque como input do keygen.bin ou, se preferir, redirecione o stdin do script em python para o executável através do comando abaixo:

```bash
$ ./glowwine $(python3 ./keygen.py)
nice one! Now, can you keygen me?
```


