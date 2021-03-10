'''
Your task is to read in a Base64-encoded string, decode it and print it out. 

Sample input:

bGF0ZS1hdC1uaWdodA==
d2l0aC10aGUtcmlzaW5nLWFwZQ==
dGhlLXJ1dGhsZXNzLXNldmVu


Sample output:

late-at-night
with-the-rising-ape
the-ruthless-seven
'''
import base64

def main():
	base64_message=input()
	base64_bytes=  base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	print(message)


if __name__=='__main__':
	main()