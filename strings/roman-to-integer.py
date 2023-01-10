
def romanToInt(s: str) -> int:
    sum = 0
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    check_again = ['I', 'X', 'C']
    i = 0
    while (i < len(s)):
        a = s[i]
        if a in check_again and i+1 < len(s):
            b = s[i+1]
            c = a+b
            if c in value:
                sum += value[c]
                i += 1
            else:
                sum += value[a]
        else:
            sum += value[a]
        i += 1
    return sum


def main():
    s = "MCMXCIV"
    print(romanToInt(s))
