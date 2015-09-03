	
section .data
   msg db "The sum of the two numbers", 0xA,0xD 
   len equ $ - msg   
   segment .bss
   sum resb 1

section	.text
   global _start    
	
_start:             
   mov	rax, '4'
   sub  rax, '0'
	
   mov 	rbx, '5'
   sub  rbx, '0'
   add 	rax, rbx
   add	rax, '0'
	
   mov 	[sum], rax
   mov	rcx,msg	
   mov	rdx, len
   mov	rbx,1	
   mov	rax,4	
   int	0x80	
	
   mov	rcx,sum
   mov	rdx, 1
   mov	rbx,1	
   mov	rax,4	
   int	0x80	
	
   mov	rax,1	
   int	0x80	

