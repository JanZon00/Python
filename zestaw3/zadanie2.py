def intToRoman(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
    
    roman = (thousands + hundreds + tens + ones)
    return roman

def romanToInt(num):
    
    sum = 0
    pairs = {3000: "MMM", 2000: "MM", 1000: "M", 900: "CM", 800: "DCCC", 700: "DCC",
         300: "CCC", 600: "DC", 400: "CD", 200: "CC", 500: "D", 100: "C", 
         80: "LXXX", 70: "LXX", 30: "XXX", 90: "XC", 40: "XL", 60: "LX", 50: "L",
         20: "XX", 8: "VIII", 7: "VII", 3: "III", 9: "IX", 6: "VI",
         4: "IV", 2: "II", 1: "I", 10: "X", 5: "V"}
    
    for roman in pairs.values():
        if roman in num:
            l = list({i for i in pairs if pairs[i]==roman})
            if(len(l) > 0):
                key_int = l[0]
                num = num.replace(roman, '', 1)
                sum += key_int
                new_dict = {key: val for key, val in pairs.items() if len(str(key)) < len(str(key_int))}
                pairs = new_dict

    return sum   
   
print("Int to Roman")
valid = False

while valid == False :
    number = int(input("Integer number : "))
    if(number > 0 and number < 4000):
        valid = True
            
print(number, " - ", intToRoman(number))

print("Roman to Int")
number = input("Roman number : ")          
print(number, " - ", romanToInt(number))