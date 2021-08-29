# translate to brainfuck
Brainfuck is an esoteric programming language created in 1993 by Urban Müller.

Notable for its extreme minimalism, the language consists of only eight simple commands, a data pointer and an instruction pointer. While it is fully Turing complete, it is not intended for practical use, but to challenge and amuse programmers.

### Commands in brainfuck
`>` 	Increment the data pointer (to point to the next cell to the right).<br>
`<` 	Decrement the data pointer (to point to the next cell to the left).<br>
`+` 	Increment (increase by one) the byte at the data pointer.<br>
`-` 	Decrement (decrease by one) the byte at the data pointer.<br>
`.` 	Output the byte at the data pointer.<br>
`,` 	Accept one byte of input, storing its value in the byte at the data pointer.<br>
`[`  If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching \] command.<br>
`]`  If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching \[ command.<br>

Brainfuck Commands in C:
```
> 	++ptr;
< 	--ptr;
+ 	++*ptr;
- 	--*ptr;
. 	putchar(*ptr);
, 	*ptr = getchar();
[ 	while (*ptr) {
] 	}
```

## usage:
```
~$: python3 translate2br.py "your plain text"
```
