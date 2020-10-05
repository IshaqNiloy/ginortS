import re
class BuiltiIns():
    def __init__(self, string):
        self.string = string

    def sort_the_string(self):
        even_digit_list = []
        odd_digit_list = []
        lowercase_list = sorted(re.findall('[a-z]', string))
        uppercase_list = sorted(re.findall('[A-Z]', string))
        digits_list = re.findall('[0-9]', string)
        for digit in digits_list:
            if int(digit) % 2 == 0:
                even_digit_list.append(digit)
            else:
                odd_digit_list.append(digit)

        even_digit_list = sorted(even_digit_list)
        odd_digit_list = sorted(odd_digit_list)        
        print(''.join(lowercase_list) + ''.join(uppercase_list) + ''.join(odd_digit_list) + ''.join(even_digit_list))

if __name__ == '__main__':
    string = input()

    my_object = BuiltiIns(string)
    my_object.sort_the_string()


