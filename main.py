

letter_value = {
        "a": {"points":  1, "tiles":  9},
        "b": {"points":  3, "tiles":  2},
        "c": {"points":  3, "tiles":  2},
        "d": {"points":  2, "tiles":  4},
        "e": {"points":  1, "tiles": 12},
        "f": {"points":  4, "tiles":  2},
        "g": {"points":  2, "tiles":  3},
        "h": {"points":  4, "tiles":  2},
        "i": {"points":  1, "tiles":  9},
        "j": {"points":  8, "tiles":  1},
        "k": {"points":  5, "tiles":  1},
        "l": {"points":  1, "tiles":  4},
        "m": {"points":  3, "tiles":  2},
        "n": {"points":  1, "tiles":  6},
        "o": {"points":  1, "tiles":  8},
        "p": {"points":  3, "tiles":  2},
        "q": {"points": 10, "tiles":  1},
        "r": {"points":  1, "tiles":  6},
        "s": {"points":  1, "tiles":  4},
        "t": {"points":  1, "tiles":  6},
        "u": {"points":  1, "tiles":  4},
        "v": {"points":  4, "tiles":  2},
        "w": {"points":  4, "tiles":  2},
        "x": {"points":  8, "tiles":  1},
        "y": {"points":  4, "tiles":  2},
        "z": {"points": 10, "tiles":  1},
        "blank": {"tiles": 2}
    }


def load_dict(path, word_length=None):
    print("Loading dictionary...")
    with open(path, 'r') as f:
        d = f.read().split('\n')
        if word_length is None:
            return d
        else:
            return filter_on_length(word_length, d)


def filter_on_length(length, words):
    result_set = []
    for w in words:
        if len(w) == length:
            result_set.append(w)
    return result_set


def print_progress(curr, tot, sols):
    if curr % 10000000 == 0:
        perc = curr / tot * 100
        print("Calculated %f percent of all possible combinations. Found %d solutions so far." % (perc, len(sols)))
        highest = 0
        highest_sol = None
        for s in sols:
            c_value = 0
            for w in s:
                for l in w:
                    c_value += letter_value[l]["points"]
            if c_value > highest:
                highest = c_value
                highest_sol = s
        print("Most valuable solution: %s %d points" % (str(highest_sol), highest))


def word_value(w):
    value = 0
    for l in w:
        value += letter_value[l]["points"]
    return value


def total_value(wa):
    value = 0
    for w in wa:
        for l in w:
            value += letter_value[l]["points"]
    return value


def sort_words_value(d):
    with_values = []
    for w in d:
        with_values.append((w, word_value(w)))
    sorted_desc = reversed(sorted(with_values, key=lambda tup: tup[1]))
    return [w for w, v in sorted_desc]


def calculate_solution_square(du):
    print("Calculating solution...")
    d = sort_words_value(du)
    d_set = set(d)
    d_set_2 = set()
    d_set_3 = set()
    for w in d:
        d_set_2.add(w[:2])
        d_set_3.add(w[:3])
    solution = []
    total_nr_combs = len(d)**4
    print("There are %d combinations to be checked." % total_nr_combs)
    nr_combs_checked = 0
    for w1 in d:
        for w2 in d:
            for j in range(4):
                tmp_word_2 = '%s%s' % (w1[j], w2[j])
                if tmp_word_2 not in d_set_2:
                    nr_combs_checked += len(d)**2
                    print_progress(nr_combs_checked, total_nr_combs, solution)
                    break
                elif j == 3:
                    for w3 in d:
                        for k in range(4):
                            tmp_word_3 = '%s%s%s' % (w1[k], w2[k], w3[k])
                            if tmp_word_3 not in d_set_3:
                                nr_combs_checked += len(d)
                                print_progress(nr_combs_checked, total_nr_combs, solution)
                                break
                            elif k == 3:
                                for w4 in d:
                                    tmp_solution = []
                                    for i in range(4):
                                        tmp_word = '%s%s%s%s' % (w1[i], w2[i], w3[i], w4[i])
                                        if tmp_word in d_set:
                                            tmp_solution.append(tmp_word)
                                            if i == 3:
                                                nr_combs_checked += 1
                                                solution.append(tmp_solution)
                                        else:
                                            nr_combs_checked += 1
                                            print_progress(nr_combs_checked, total_nr_combs, solution)
                                            break
    return solution


en_dict_path = './words_alpha.txt'
d = load_dict(en_dict_path, word_length=4)
solution = calculate_solution_square(d)



