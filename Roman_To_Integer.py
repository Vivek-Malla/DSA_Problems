def roman_int(s: str) -> int:

    roman_dic = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                      'D': 500,
                      'M' : 1000}
    
    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_dic[char]

        if value < prev_value:
            total = total - value
        else:
            total = total + value 

        prev_value = value    
    return total



value = str(input("enter the value :"))

print(roman_int(value))