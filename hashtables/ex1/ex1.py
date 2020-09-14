def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # iterate over the given weights
    # for each weight as key store value limit - weight
    # iterate through hashtable 
    # if key + value = limit && value is in hashtable
    # return indeces of the key and value
    h = {}
    packages = None
    for n in weights:
        h[n] = limit - n
    
    if len(weights) == 2 and weights[0] + weights[1] == limit:
        packages = (1, 0)
        return packages
        
    for k in h:
        if k + h[k] == limit and h[k] in h:
            if weights.index(k) > weights.index(h[k]):

                packages = (weights.index(k), weights.index(h[k]))
            else:
                packages = (weights.index(h[k]), weights.index(k))
    return packages


# answer = get_indices_of_item_weights([4, 4], 2, 8)
# print(answer)