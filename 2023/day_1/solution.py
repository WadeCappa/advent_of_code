import sys

def getEncodings():
    encodings = {str(x): str(x) for x in range(10)}
    encodings["one"] = "1"
    encodings["two"] = "2"
    encodings["three"] = "3"
    encodings["four"] = "4"
    encodings["five"] = '5'
    encodings["six"] = '6'
    encodings["seven"] = '7'
    encodings["eight"] = '8'
    encodings["nine"] = '9'
    return encodings

# This method finds the first and last number in the string
# and returns them as a two-digit number.
def findCodeInString(line, encodings):
    first = len(line)
    first_word = ""
    last = len(line)
    last_word = ""
    reversed_line = line[::-1]
    for encoding in encodings.keys():
        reversed_encoding = encoding[::-1]
        if encoding in line:
            forwardPlacement = line.find(encoding)
            reversePlacement = reversed_line.find(reversed_encoding)
            if forwardPlacement < first:
                first = forwardPlacement 
                first_word = encodings[encoding]
            if reversePlacement < last:
                print(reversePlacement, last, encoding)
                last = reversePlacement
                last_word = encodings[encoding]

    if first == len(line):
        print("failed to find first line")
    if last == len(line):
        print("failed to find last line")

    print(line, first_word, last_word)
    return int(first_word + last_word)

if __name__ == "__main__":
    
    file = sys.argv[1]
    sum = 0
    encodings = getEncodings()
    with open(file) as f:
        for l in f:
            sum += findCodeInString(l, encodings)

    print(sum)
