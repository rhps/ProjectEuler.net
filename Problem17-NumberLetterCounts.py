unit_names = """zero one two three four five six seven eight nine ten
                eleven twelve thirteen fourteen fifteen sixteen seventeen
                eighteen nineteen""".split()
tens_names = """zero ten twenty thirty forty fifty sixty seventy eighty
                ninety""".split()


def english(n):
    "Return the English name for n, from 0 to 999999."
    if n >= 1000:
        thous = english(n // 1000) + " thousand"
        n = n % 1000
        if n == 0:
            return thous
        elif n < 100:
            return thous + " and " + english(n)
        else:
            return thous + ", " + english(n)
    elif n >= 100:
        huns = unit_names[n // 100] + " hundred"
        n = n % 100
        if n == 0:
            return huns
        else:
            return huns + " and " + english(n)
    elif n >= 20:
        tens = tens_names[n // 10]
        n = n % 10
        if n == 0:
            return tens
        else:
            return tens + "-" + english(n)
    else:
        return unit_names[n]

def letter_count(s):
    "Return the number of letters in the string s."
    import re
    return len(re.findall(r'[a-zA-Z]', s))

def euler17():
    return sum(letter_count(english(i)) for i in range(1, 1001))

print(euler17())