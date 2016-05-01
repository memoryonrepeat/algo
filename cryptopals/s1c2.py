import operator
string1 = 0x1c0111001f010100061a024b53535009181c
string2 = 0x686974207468652062756c6c277320657965

# Why is there a redundant 'L' at the end of the result ?
print hex(operator.xor(string1,string2))