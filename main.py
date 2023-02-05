def create_mapping_list(strings, regexes):
    result = []
    for regex in regexes:
        result.append((regex, tuple(strings)))
    return result

def main():
    strings = ['string1', 'string2', 'string3']
    regexes = ['regex1', 'regex2', 'regex3']
    result = create_mapping_list(strings, regexes)
    print(result)

if __name__ == '__main__':
    main()

