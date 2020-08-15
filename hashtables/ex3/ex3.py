def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # iterate over each  list and sublist
    # store element as key and counter as value
    # if key in h has value = length of the given array of arrays
    # key exists in all suybarrays
    h = {}
    results = []
    for l in arrays:
        for i in l:
            if i not in h:
                h[i] = 1
            else:
                h[i] +=1
            if h[i] == len(arrays):
                results.append(i)

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
