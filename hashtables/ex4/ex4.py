def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # iterate through list of integers
    # store abs() of int as key in hashtable with a count value
    h = {}
    both = []
    for i in a:
        i = abs(i)
        if i not in h:
            h[i] = 1
        else:
            both.append(i)

    return both


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
