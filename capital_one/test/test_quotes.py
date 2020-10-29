

def inside_quote(line, target_char, quote_lst):
    """
    A helper function to check whether the target_char is surrounded
    by quotation mark in a given line.

    Precondition: char in line == True
    :param line: str
    :param target_char: str
    :return: bool
    """
    target_index = line.rfind(target_char)
    quote_ch = None  # None if it's currently parsed to non-string

    for index, ch in enumerate(line):
        if quote_ch and index == target_index:
            return True
        if ch in quote_lst:
            if not quote_ch:
                quote_ch = ch
            else:
                if ch == quote_ch:
                    quote_ch = None
    return False


#testing edge cases on conmmnet symbol inside of quotation mark#
f = open("test_case.py", "r")
content = f.read().split("\n")
f.close()
for line in content:
    print(inside_quote(line, '#', ['"', "'"]))
