#Day 24

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                0: "",
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen"
            }
            return switcher.get(num, "")
        
        def tens(num):
            switcher = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety"
            }
            ten = num // 10
            rest = num - ten * 10
            if ten in switcher:
                if rest > 0:
                    return switcher[ten] + " " + one(rest)
                else:
                    return switcher[ten]
            return one(num)
        
        def two(num):
            if num == 0:
                return ""
            elif num < 20:
                return one(num)
            else:
                return tens(num)
        
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + " Hundred " + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + " Hundred"
            return ""
        
        def convert(num):
            billion = num // 1000000000
            million = (num - billion * 1000000000) // 1000000
            thousand = (num - billion * 1000000000 - million * 1000000) // 1000
            remainder = num - billion * 1000000000 - million * 1000000 - thousand * 1000
            
            result = ""
            if billion > 0:
                result += three(billion) + " Billion"
            if million > 0:
                if result:
                    result += " "
                result += three(million) + " Million"
            if thousand > 0:
                if result:
                    result += " "
                result += three(thousand) + " Thousand"
            if remainder > 0:
                if result:
                    result += " "
                result += three(remainder)
            
            return result.strip()
        
        if num == 0:
            return "Zero"
        
        return convert(num)
