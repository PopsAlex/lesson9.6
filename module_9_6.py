
def all_variants(text):
    index = 0
    index_2 = 0
    index_3 = 1
    first = ''

    while first != text:

        if index == len(text):
            index = 0
            index_2 -= (len(text) - 1)

        first = text[index : index_2]

        if first == '':
            index += 1
            index_2 += 1
            continue

        if first[len(first) - 1] == text[len(text) - 1]:
            if len(first) == index_3:
                yield first
                index_3 += 1
            index += 1
            index_2 += 1
            continue
        yield first
        index += 1
        index_2 += 1


a = all_variants("abc")
for i in a:
    print(i)