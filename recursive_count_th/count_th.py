'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # set total instances of "th" to 0 to initialize
    total = 0
    # base case
    if len(word) == 0:
        return 0
    # nested function that controls the recurvise operations
    def rec_count(string, position=1):
        # bring in nonlocal variable "total" to keep count of instances of "th"
        nonlocal total
        # exits recursive function if length of the string is equal to 1 which would mean there is no instance of the two letters "th"
        if len(string) == position:
            return total
        # concatenates first letter of string with second and compares to "th" to find equality
        if string[position - 1] + string[position] == "th":
            # increment total by 1
            total += 1
        # also increment position by 1 to repeat function if not at end of string
        position += 1
        # returns itself which is the nature of recursion
        return rec_count(string, position)
               
    return rec_count(word)


