"https://edabit.com/challenge/QEDPxbfHjvWXQQtpH"        #1 - misol
"https://edabit.com/challenge/SKorutJdWGBzXJDRt"        #2 - misol


# def remove_vowels(input_string):                      # 3- misol
#     vowels = "aeiou"
#     i = 0
#     result_string = ""
#     while i < len(input_string):
#         a = input_string[i]
#         if a not in vowels:
#             result_string = result_string + a
#         i += 1
#
#     return result_string
#
#
# print(remove_vowels("I have never seen a thin person drinking Diet Coke."))


# def integer_boolean(lst):                     # 4 - misol
#     i = 0
#     list = []
#     while i < len(lst):
#         a = lst[i]
#         if a == '1':
#             print(True)
#         else:
#             print(False)
#         i += 1
#     return i
# print(integer_boolean("100101"))

# def first_and_last(lst):                  # 5 - misol
#     i = 0
#     line = []
#     while i < len(lst):
#         a = list(lst)
#         a.sort()
#         b = a[::-1]
#         i += 1
#     return a, b
#
# print(first_and_last("marmite"))


# def cap_to_front(lst):                            # 6 - misol
#     i = 0
#     upp_letter = ""
#     low_letter = ""
#     while i < len(lst):
#         a = lst[i]
#         if a.isupper():
#             upp_letter += a
#         else:
#             low_letter += a
#         i += 1
#     return upp_letter + low_letter
#
# print(cap_to_front("hApPy"))


# def left_digit(lst):              # 7 - misol
#     i = 0
#     while i < len(lst):
#         a = lst[i]
#         if a.isdigit():
#             return int(a)
#         i += 1
#
# print(left_digit("5TrAdE2W1n95!"))


# def vow_replace(lst):                 # 8 - misol
#     i = 0
#     while i < len(lst):
#         a = lst[i]
#         b = a.replace("a","u")
#         i += 1
#         print(b)
# print(vow_replace("apples and bananas"))




# def letters_only(lst):                # 9 - misol
#     i = 0
#     b = ''
#     while i < len(lst):
#         a = lst[i]
#         if a.isalpha():
#             b += a
#         i += 1
#     return b
#
#
# print(letters_only("R!=:~0o0./c&}9k`60=y"))




# def profit_margin(cost, sales):           # 10 - misol
#     a = ((sales - cost)/sales)*100
#     return a
#
# print(profit_margin(50, 50))
# print(profit_margin(28, 39))

