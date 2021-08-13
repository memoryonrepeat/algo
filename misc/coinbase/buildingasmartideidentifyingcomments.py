# NOTE: failed one test case, need to verify

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def parseComments(program):
    result = ""
    for i, char in enumerate(program):
        comments = ""
        if i<len(program)-1:
            # detect block comments
            if program[i:i+2]=="/*":
                comments += program[i:i+2]
                j = 2
                while (i+j)<len(program):
                    comments += program[i+j]
                    j += 1
                    if program[i+j-1:i+j+1]=="*/":
                        comments += program[i+j]
                        break
                result += comments.strip() if i+j>=len(program) else comments.strip()+"\n"
                i = i+j
            # detect single line comments
            elif program[i:i+2]=="//":
                comments += program[i:i+2]
                j=2
                while (i+j)<len(program):
                    comments += program[i+j]
                    j += 1
                    if "\n" in program[i+j-1:i+j+1]:
                        break
                result += comments.strip() if i+j>=len(program) else comments.strip()+"\n"
                i = i+j
    return result
    
program = sys.stdin.read()

print(parseComments(program))