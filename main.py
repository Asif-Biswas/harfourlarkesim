def create_mapping_list(strings, regexes):
    if not isinstance(strings, list) or not isinstance(regexes, list):
        raise ValueError("Input must be a list of strings.")

    return [(regex, tuple(strings)) for regex in regexes]


def main():
    strings = ['string1', 'string2', 'string3']
    regexes = ['regex1', 'regex2', 'regex3']
    try:
        result = create_mapping_list(strings, regexes)
    except ValueError as e:
        print(e)
    else:
        print(result)


if __name__ == '__main__':
    main()

