
str_manip = input("Write a sentence about your favourite animal")
print(str_manip)

length = len (str_manip)
print(length)

last_character = str_manip[-1]
print(last_character)

replaced_character = str_manip.replace( last_character,'@')
print(replaced_character)

mirror_sentence = str_manip[::-1]

last_three = mirror_sentence [0:3]
print(last_three)

slice1=str_manip[0:3]
slice2=str_manip[-2:]

add_slice = slice1 + slice2
print(add_slice)