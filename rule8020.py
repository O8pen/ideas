x = 100
total_information = x
learned_information = 0
remaining_information = x
number_of_turns = 0

while(True):
    remaining_information = remaining_information-(remaining_information*0.2)
    learned_information = total_information - remaining_information
    number_of_turns += 1
    print("total_information(" + str(total_information) + ") = learned_information("  + str(learned_information) + ") + remaining_information(" + str(remaining_information) + ")")
    print("number_of_turns = " + str(number_of_turns))
    input()