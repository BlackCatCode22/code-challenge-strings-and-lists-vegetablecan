'''
Code Challenge - Strings and Lists
Written by Donald Cao
Cao_Week5_CodeChallenge_Strings-List.py
09/10/2023
'''
#Part 1
str_one = " The quick brown fox jumps over the lazy dog. "
str_two = "The slow black dog bows before the regal fox."

str_no_spaces=str_one.strip().replace(" ","")
print("\n str_no_spaces is... " + str_no_spaces)

str_cat=str_one+str_two
print("\n str_cat is... " + str_cat)

str_len=str(len((str_cat)))
print("\n The length of " + str_cat + " is: " + str_len)

str_cat_lower=str_cat.lower()
print("\n str_cat_lower in lower case is: " + str_cat_lower)

str_cat_upper=str_cat.upper()
print("\n str_cat_upper in upper case is: " + str_cat_upper)

adjective = 'smart'
verb = 'ran'
preposition = 'through'
str_formatted = f"The {adjective} brown fox {verb} {preposition} the lazy dog."
print("\n str_formatted is: "+ str_formatted)

start_index=str_two.find("black dog")
print("\n start_index is: ", start_index)

substring=str_two[9:18]
print("\n substring is: " + substring)

#Part 2
str_for_list = "Natalia, Alice, Bob, Charlie, Sergei, David, Eve, Frank, Grace, Dmitri, Hannah, Isaac, Jack, Ivan, Olga"
list_of_names=str_for_list.split(",")
print("\n list_of_names is: " + str(list_of_names))

list_sorted=sorted(list_of_names)
print("\n list_sorted is: " + str(list_sorted))
print("\n list_of_names is: " + str(list_of_names))

list_reversed = list_sorted[::-1]
print("\n list_reversed is: " + str(list_reversed))

for name in list_reversed:
    print(name)

first_three=list_sorted[0:3]
print(first_three)
print(str(type(first_three)))

list_sorted.append("Yevgeny")
list_sorted.append("Svetlana")
list_sorted.insert(5,"Boris")
print(list_sorted)

list_sorted=sorted(list_sorted)
print(list_sorted)


list_sorted=sorted(list_of_names)
pop0=list_sorted.pop(0)
pop1=list_sorted.pop(1)
pop2=list_sorted.pop(2)
popped_list=[pop0,pop1,pop2]
extended_list=list_sorted.extend(popped_list)
print(list_sorted)

list_sorted=sorted(list_of_names)
print(list_sorted)

removedAlice=list_sorted.remove(" Alice")
print(list_sorted)

my_set = set(list_sorted)
list_sorted = list(my_set)
print(sorted(list_sorted))
