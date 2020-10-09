import random


def shuffle(string):
  templist = list(string)
  random.shuffle(templist)
  return ''.join(templist)


uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
punc1=chr(random.randint(33,42))
punc2=chr(random.randint(33,42))
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punc1 + punc2
password = shuffle(password)

print(password)
