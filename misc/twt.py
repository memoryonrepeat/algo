# example_text = "Write a function that splits long SMS string into smaller pieces. Each piece should be less than or equal to 160 characters and contains indices \
# at the end. Function should not break words into pieces. \
# If word does not fit -- it should go to the next SMS."
#
# 60 is used to limit the text length in editor.
# for line in split(example_text, 60):
#     print(line, len(line))
#
# Output:
# 
#   ('Write a function that splits long SMS string into (1/5)', 55)
#   ('smaller pieces. Each piece should be less than or (2/5)', 55)
#   ('equal to 160 characters and contains indices at the (3/5)', 57)
#   ('end. Function should not break words into pieces. If (4/5)', 58)
#   ('word does not fit -- it should go to the next SMS. (5/5)', 56)
# 

# Write a function that                           splits long SMS string into

def split(s, limit):
    
    SPACE_BUFFER = 1
    INDEX_BUFFER = 5
    
    result = []
    
    words = s.split(' ')
    
    chunk = ''
    
    for word in words:
        if not word:
            continue
        if len(chunk) + SPACE_BUFFER + len(word) + SPACE_BUFFER + INDEX_BUFFER <= limit:
            if not chunk:
                chunk += word
            else:
                chunk += ' ' + word
        else:
            result.append(chunk)
            chunk = ''+word
    
    if chunk:
        result.append(chunk)
    
    return list(map(lambda x: x[1] + ' (' + str(x[0]+1) + '/' + str(len(result)) + ')', enumerate(result)))
    # return list(map(lambda i, chunk: chunk + ' (' + str(i+1) + '/' + len(result) + ')', enumerate(result)))

s0 = "Write a function that splits long SMS string into smaller pieces. Each piece should be less than or equal to 160 characters and contains indices at the end. Function should not break words into pieces. If word does not fit -- it should go to the next SMS."

expected0 = ['Write a function that splits long SMS string into (1/5)', 'smaller pieces. Each piece should be less than or (2/5)', 'equal to 160 characters and contains indices at the (3/5)', 'end. Function should not break words into pieces. If (4/5)', 'word does not fit -- it should go to the next SMS. (5/5)']

for line in split(s0, 60):
    print(line, len(line))

assert split(s0, 60) == expected0, split(s0, 60)


