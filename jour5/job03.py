def calc_str(str):
    x = 0
    if str == x:
        return x
    else:
        x += 1

def get_string_length(s):
    return 1 + get_string_length(s[1:]) if s else 0

print(get_string_length("oui"))