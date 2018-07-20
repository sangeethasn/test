in_text = open("input", "r")
out_text = open("output.txt", "w")


# Function to shuffle the chars around
def shuffle(word):
    if len(word) == 1:
        return word
    else:
        half = int(len(word) / 2)
        # First half in reverse
        first = word[:half][::-1]
        # Last half in reverse
        last = word[half:len(word)][::-1]

        # First + Last in reverse
        return str(first + last)[::-1]


# Function to scramble the word
def scramble(word):
    if len(word) < 3:
        return word

    first = word[:1]
    last = word[-1:]
    mid = word[1:-1]

    if last == "." or last == ",":
        last = word[-2:]
        mid = word[1:-2]

    return str(first) + str(shuffle(mid)) + str(last)


# Read the input and write the scrambled words to the output
for line in in_text:
    line = line.strip()
    new_line = ""
    #print new_line
    #print
    for word in line.split(" "):
        new_line += scramble(word) + " "
        #print new_line



    out_text=open('output.txt','w')
    content=out_text.write(new_line)
    print content



# Close open files
in_text.close()
out_text.close()