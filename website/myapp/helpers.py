def per_round(lst, divider):
    return [lst[i:i+divider] for i in range(0, len(lst), divider)]
