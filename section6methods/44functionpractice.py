# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(find_seq, in_seq) -> bool:
    found_counter = 0
    in_seq_index = 0
    while (found_counter < len(find_seq) and in_seq_index < len(in_seq)):
        if (find_seq[found_counter] == in_seq[in_seq_index]):
            found_counter += 1
        in_seq_index += 1
            
    return found_counter == len(find_seq)


print(spy_game([0,0,7], [1,2,4,0,0,7,5]))
print(spy_game([0,0,7], [1,0,2,4,0,5,7]))
print(spy_game([0,0,7], [1,7,2,0,4,5,0]))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(number_seq):
    sum = 0;
    should_sum = True;
    for x in number_seq:
        if (x == 6):
            should_sum = False
        elif (x == 9):
            should_sum = True
        else:
            if should_sum:
                sum += x
    return sum

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))