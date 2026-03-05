def swap_case(s):
    a=""
    for word in s:
        if word.islower():
            a+=(word.upper())
        else:
            a+=(word.lower())
    return a
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)