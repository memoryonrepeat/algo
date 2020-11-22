# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, number: int) -> str:
        single = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }

        teens = {
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }

        tens = {
            10: 'Ten',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }

        if number<10:
            return single[number]
        if number==10:
            return tens[number]
        if number<20:
            return teens[number]
        if number<100:
            return tens[((number%100)//10)*10] + ' ' + single[number%10] if number%10!=0 else tens[((number%100)//10)*10]
        if number<1000:
            return self.numberToWords(number//100) + ' Hundred ' + self.numberToWords(number%100) if number%100!=0 else self.numberToWords(number//100) + ' Hundred'
        if number<1000000:
            return self.numberToWords(number//1000) + ' Thousand ' + self.numberToWords(number%1000) if number%1000!=0 else self.numberToWords(number//1000) + ' Thousand'
        if number<1000000000:
            return self.numberToWords(number//1000000) + ' Million ' + self.numberToWords(number%1000000) if number%1000000!=0 else self.numberToWords(number//1000000) + ' Million'
        if number<1000000000000:
            return self.numberToWords(number//1000000000) + ' Billion ' + self.numberToWords(number%1000000000) if number%1000000000!=0 else self.numberToWords(number//1000000000) + ' Billion'
        return 'Number exceeded limit'
