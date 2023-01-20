# Name: Aiden Teal
# SID: 1724406
# CCID: ateal
# AnonID: 1000332190
# CMPUT274, Fall 2022
# Weekly Assignment #2: Unfair Dice
#

def biased_rolls(prob_list, s, n): 
    # Main function: Simulate n rolls of a biased m- sided die
    # and return a list containing the results .
    # Arguments: prob_list: A list of probabilities of rolling
    # a certain side of a n-sided dice. index[0] = 1 and so on.
    #            s: the seed to use when initializing the PRNG
    #            n: the number of rolls to return
    # Output: Returns a list called "rolls" containing the
    # rolls generated.

    import random
    random.seed(s)

    # Create a list to store the sum between elements of prob_list
    # as this is what the seeded m value will correlate to.
    Interval_of_values = [prob_list[0]]
    i = 1

    while i <= len(prob_list) - 1:
        # Adds the value taken from a certain index in 
        # prob_list added with the last value in list to
        # Interval_of_values
        Interval_of_values.append(prob_list[i] + Interval_of_values[-1])
        i = i + 1
        pass

    rolls = []
    L = 0

    # Generates a random seeded value m
    m = random.random()
    while len(rolls) < n:
        # if the value of m in in the first range
        # it adds the value 1 to the list rolls.
        # If not, the program will cycle through the 
        # elements in Interval_of_values until m falls 
        # between two, effectively finding the value
        # of the roll.
        if m < float(Interval_of_values[0]) and m >= 0:
                rolls.append(1)
                L = 0
                m = random.random()
        elif m >= float(Interval_of_values[L]) and \
             m < float(Interval_of_values[L+1]):
                rolls.append(L+2)
                L = 0
                m = random.random()
        else:
                L += 1
        pass

    return rolls

def draw_histogram(m, rolls, width):
    # Function: This function displays a histogram of all the rolls obtained 
    # from an m-sided die in "rolls" and scales it to the 
    # length "width". 
    # Arguments: m: Number of sides
    #        rolls: List of rolls obtained
    #        width: Length of histogram corresponding to the count of
    #               the most rolled number
    # Returns: Prints a histogram
    import statistics
    from statistics import mode

    sides = str(m)
    n = 1
   
    # Generates the histogram starting with the title.
    # After this, it cycles through the sides of the die,
    # printing a hyphen/dash graph of the amount of rolls
    # for each side. Note that the graph is scaled so that
    # the histogram is only as long as the width.

    print("Frequency Histogram: " + sides + "-sided Die")
    while n <= m:
        print(str(n) + "." + ("#" * int(round((rolls.count(n)*width)/
        rolls.count(mode(rolls)))) + ("-" * (width - 
        int(float(round((rolls.count(n)*width)/rolls.count(mode(rolls)))))))))
        n += 1

if __name__ == "__main__":
    pass
