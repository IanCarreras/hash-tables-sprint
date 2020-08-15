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
        
    for k in h:
        if k + h[k] == limit and h[k] in h:
            if weights.index(k) > weights.index(h[k]):
                packages = (weights.index(k), weights.index(h[k]))
            else:
                packages = (weights.index(h[k], weights.index(k)))
    return packages


answer = get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7)

print(answer)