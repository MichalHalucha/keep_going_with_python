def most_frequent(data):
    d = {data.count(e): e for e in data}
    return d[max(d)]
