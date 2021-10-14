import random

file = open("words.txt", "r")

wordlist = []

for line in file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    wordlist.append(line_list)

file.close()

word = random.choice(wordlist)
word2 = random.choice(wordlist)

num1 = random.randint(1,9)
num2 = random.randint(1,9)
num3 = random.randint(1,9)
num4 = random.randint(1,9)

print("Your password is: " + str(word) + str(word2) + str(num1) + str(num2) + str(num3) + str(num4))
