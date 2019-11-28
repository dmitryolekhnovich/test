def most_wanted_letter(text):
    text = text.lower()
    dictionary = {}
    for t in text:
        if t in "abcdefghijklmnopqrstuvwxyz":
            dictionary[t] = text.count(t)
    m = max(dictionary.values())
    l = []
    for key in dictionary:
        if dictionary[key] == m:
            l.append(key)
    l = sorted(l)
    return l[0]
