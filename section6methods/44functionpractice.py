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


