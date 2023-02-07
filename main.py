import re


def create_mapping_list(strings, regexes):
    if not isinstance(strings, list) or not isinstance(regexes, list):
        raise ValueError("Input must be a list of strings.")

    if not all(isinstance(string, str) for string in strings) or \
            not all(isinstance(regex, str) for regex in regexes):
        raise ValueError("Input must be a list of strings.")

    result = []
    for regex in regexes:
        matches = (string for string in strings if re.search(regex, string))
        result.append((regex, tuple(matches)))

    return result


def main():
    strings = ['abcde', 'fghij', 'klmnoabc9', 'abc', 'hij']
    regexes = ['abc', 'hij', 'klmno', 'bcdno']
    try:
        result = create_mapping_list(strings, regexes)
    except ValueError as e:
        print(e)
    else:
        print(result)


if __name__ == '__main__':
    main()
