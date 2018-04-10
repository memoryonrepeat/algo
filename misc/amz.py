# Convert number to words
# 1273 --> one thousand two hundred and seventy three
# Integer 0 -> 999999999

single = {
    0: 'zero',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine'
}

teens = {
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'forteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen'
}

tens = {
	10: 'ten',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety'
}

def convert(number):
	if number<10:
		return single[number]
	if number==10:
		return tens[number]
	if number<20:
		return teens[number]
	if number<100:
		return tens[((number%100)//10)*10] + ' ' + single[number%10] if number%10!=0 else tens[((number%100)//10)*10]
	if number<1000:
		return convert(number//100) + ' hundred ' + convert(number%100) if number%100!=0 else convert(number//100) + ' hundred'
	if number<1000000:
		return convert(number//1000) + ' thousand ' + convert(number%1000) if number%1000!=0 else convert(number//1000) + ' thousand '
	if number<1000000000:
		return convert(number//1000000) + ' million ' + convert(number%1000000) if number%1000000!=0 else convert(number//1000000) + ' million '
	return 'Number exceeded limit'

print(convert(110))








