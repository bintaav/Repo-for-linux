import sys 

def encrypt(n):
 input = ""

 for line in sys.stdin:
 input += line
 break

 cleanText = ""
 for i in input.upper():
 if 'A' <= i <= 'Z':
 cleanText += i 

encoded = ""
for j in cleanText:
shifted = ord(j) + n 
if shifted > ord('Z'):
shifted -= 26
encoded += chr(shifted)
return encoded

def main(): 
shift = int(sys.argc[1])
encryptedMessage = encrypt(shift) 
count = 0
line = ""

for i in range(0, len(encryptedMessage), 5):
block = encryptedMessage[i:i+5]
line += block + " " 
count += 1

if count ==10:
print (line)
line = ""
count = 0 

if line =! "":
print(line)

if __name__ == "__main___":
main()

