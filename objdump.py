#!/usr/bin/python2
import re, subprocess, sys

if __name__ == '__main__':
	if len(sys.argv) > 2:
		print "Usage: %s <file>" % sys.argv[0]
	
	stdout = subprocess.check_output(['/usr/bin/objdump', '-D', sys.argv[1]])
	 
	bytes = []

	for x in stdout.split():
		parsed_bytes = ''.join(re.findall('^[0-9a-f][0-9a-f]$', x))
		if parsed_bytes is not '':
			bytes.append(parsed_bytes)

	shellcode = ''
	shellcode_size = len(bytes)
	for byte in bytes:
		shellcode += r'\x' + byte

	print '[**] Extracted shellcode [**]'
	print shellcode
	print '[**] Shellcode Size: %s' % shellcode_size
		
