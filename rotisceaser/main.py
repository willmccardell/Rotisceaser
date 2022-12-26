# https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
import enchant
import string
import re


def main(original_cypher,fulloutput = True):
    # Use a breakpoint in the code line below to debug your script.
    caeser = range(26)
    results = {}
    global d
    d = enchant.Dict("en_US")

    cleaned_cypher = cleanup_original_cypher(original_cypher)

    init_dicts()

    # rotate (ha!) through all cyphers, store results.
    for i in caeser:
        results[i] = rot_string(cleaned_cypher, i)  # Press Ctrl+F8 to toggle the breakpoint.

    # Make a list of all the tuples of cypher, rotational index,
    # and probability that the rotation is the real one
    final_results = []
    for v in results:
        final_results.append((results[v], v, check_cypher_word_percentage(results[v])))

    # Sort the results in numeric order based on the probability.


    # Only include tuples that are at least 50% correct
    # according to the dictionary
    s = [(cypher, index, prob) for (cypher, index, prob) in final_results if prob >= 0.5]
    s = sorted(s, key=lambda likelihood: likelihood[2], reverse=True)

    # pretty print it
    retval = format_results(s, cleaned_cypher, fulloutput)

    if fulloutput:
        print(retval)

    return retval

def format_results(final_results, orig_cypher, fulloutput):
    retval = ""
    if fulloutput:
        retval = f'The original cypher was \"{orig_cypher}\".\n'
        retval += 'Determining most likely rotation factor.\n'
        for (cypher, index, prob) in final_results:
            retval += f'ROT-{index}: Probability: {convert_to_percentage(prob)} : {cypher}\n'
    else:
        retval = f'ROT-{final_results[0][1]}: Probability: {convert_to_percentage(final_results[0][2])} : {final_results[0][0]}'
    return retval

def rot_string(cypher, rot_index):
    ret = ''.join([rot(i, rot_index) for i in cypher])
    return ret;


# apply Rot-X to a single character
def rot(cypher_char, rot_index):
    if cypher_char.isspace() or cypher_char in string.punctuation:
        return cypher_char
    else:
        return mapping[(revmap[cypher_char] + rot_index) % 26]


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


def check_cypher_word_percentage(cypher):
    cy_list = cypher.split(' ')
    ret = 0.0
    flag = 0.0
    for word in cy_list:
        if d.check(word):
            flag += 1.0
    ret = (flag) / (len(cy_list))

    return ret


def cleanup_original_cypher(cypher):
    # can't handle punctuation or uppercase, so flip and strip them.
    # Truthfully, it's edge-cases I don't want to deal with.
    # Any real cypher of this probably wouldn't include it either
    # because that would give away a lot more information
    cypher = cypher.lower()
    cypher = re.sub(r'[^\w\s]', '', cypher)
    return cypher


def convert_to_percentage(dbl):
    return str(dbl * 100.0) + '%'


def init_dicts():
    global mapping, revmap

    mapping = dict(zip(range(26), char_range('a', 'z')))
    revmap = dict((v, k) for k, v in mapping.items())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     main('no, I am the brave computer')
    #main('zxq,ald! yxq')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
