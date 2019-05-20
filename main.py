

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
        "q": {"points": 12, "tiles":  1},
        "r": {"points":  1, "tiles":  6},
        "s": {"points":  1, "tiles":  4},
        "t": {"points":  1, "tiles":  6},
        "u": {"points":  2, "tiles":  4},
        "v": {"points":  6, "tiles":  2},
        "w": {"points":  5, "tiles":  2},
        "x": {"points":  7, "tiles":  1},
        "y": {"points":  5, "tiles":  2},
        "z": {"points": 8, "tiles":  1},
        "blank": {"tiles": 2}
    }


def load_dict(path, word_length=None):
    print("Loading dictionary...")
    with open(path, 'r') as f:
        d = f.read().split('\n')
        d = [w.lower() for w in d]
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


def print_best_solution(sols):
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


def print_progress(curr, tot, sols):
    if curr % 10000000 == 0:
        perc = curr / tot * 100
        print("Calculated %f percent (%d combinations) of all possible combinations. Found %d solutions so far." % (perc, curr, len(sols)))
        print_best_solution(sols)


def print_progress_2(indices, len_word_list, tot, sols):
    curr = 0
    for i in range(len(indices)):
        curr += indices[i]*len_word_list**(len(indices) - (i + 1))
    if curr % 10000000 == 0:
        perc = curr / tot * 100
        print("Calculated %f percent (%d combinations) of all possible combinations. Found %d solutions so far." % (perc, curr, len(sols)))
        print_best_solution(sols)


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


def calculate_solution_square_4(du):
    print("Calculating solution...")
    print("There are %d words in the list." % len(du))
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


def calculate_solution_square_3(du):
    print("Calculating solution...")
    print("There are %d words in the list." % len(du))
    d = sort_words_value(du)
    d_set = set(d)
    d_set_2 = set()
    for w in d:
        d_set_2.add(w[:2])
    solution = []
    total_nr_combs = len(d) ** 3
    print("There are %d combinations to be checked." % total_nr_combs)
    nr_combs_checked = 0
    for w1 in d:
        for w2 in d:
            for j in range(3):
                tmp_word_2 = '%s%s' % (w1[j], w2[j])
                if tmp_word_2 not in d_set_2:
                    nr_combs_checked += len(d)
                    print_progress(nr_combs_checked, total_nr_combs, solution)
                    break
                elif j == 2:
                    for w3 in d:
                        tmp_solution = []
                        for k in range(3):
                            tmp_word = '%s%s%s' % (w1[k], w2[k], w3[k])
                            if tmp_word in d_set:
                                tmp_solution.append(tmp_word)
                                if k == 2:
                                    nr_combs_checked += 1
                                    solution.append(tmp_solution)
                            else:
                                nr_combs_checked += 1
                                print_progress(nr_combs_checked, total_nr_combs, solution)
                                break
    return solution


def increment_indice(indice, index_index, nr_words, tmp_solution):
    indice[index_index] += 1
    new_index = index_index
    if not not tmp_solution:
        tmp_solution.pop(index_index)
    if indice[index_index] == nr_words:
        c = 0
        for i in reversed(range(len(indice))):
            if i == index_index:
                indice[i] = 0
                c = 1
                new_index -= 1
                if not not tmp_solution:
                    tmp_solution.pop(i - 1)
            elif i < index_index:
                indice[i] += c
                if indice[i] % nr_words == 0:
                    c = 1
                    indice[i] = 0
                    new_index -= 1
                    if not not tmp_solution:
                        tmp_solution.pop(i - 1)
                else:
                    c = 0
            elif i > index_index:
                indice[i] = 0
    return new_index, indice


def calculate_solution_square(dict_path, side_length):
    d = load_dict(dict_path, word_length=side_length)
    d = sort_words_value(d)
    print("Calculating solution...")
    print("There are %d words in the list." % len(d))
    total_nr_combs = len(d) ** side_length
    print("There are %d combinations to be checked." % total_nr_combs)
    word_sets = []
    for i in range(2, side_length + 1):
        tmp_set = set()
        for w in d:
            tmp_set.add(w[:i])
        word_sets.append(tmp_set)
    solutions = []
    indice = [0] * side_length
    tmp_solution = []
    j = 0
    while j < side_length:
        tmp_solution.append(d[indice[j]])
        if j > 0:
            for k in range(side_length):
                tmp_vertical = '%s'*(j+1) % tuple([tmp_solution[l][k] for l in range(j+1)])
                if tmp_vertical not in word_sets[j-1]:
                    j, indice = increment_indice(indice, j, len(d), tmp_solution)
                    print_progress_2(indice, len(d), total_nr_combs, solutions)
                    break
                elif k == side_length - 1:
                    if j == side_length - 1:
                        solutions.append(tmp_solution.copy())
                        print_progress_2(indice, len(d), total_nr_combs, solutions)
                        j, indice = increment_indice(indice, j, len(d), tmp_solution)
                        if indice == [0, 0, 0]:
                            return solutions
                    else:
                        j += 1
                        print_progress_2(indice, len(d), total_nr_combs, solutions)
        else:
            j += 1





def square_recursive_finder(words, words_set, current_row, partial_solution):
    word_len = len(words[0])
    if word_len - current_row == 1:
        pass
    else:
        partial_solution = [words[0]]
        return [words[0]].extend(square_recursive_finder(words, words_set, current_row + 1, partial_solution))


def find_square_solution(dict_path, side_length):
    d = load_dict(dict_path, word_length=side_length)
    d = sort_words_value(d)
    d_set = set(d)
    return square_recursive_finder(d, d_set, 0)


def fac_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fac_recursive(n - 1)

# en_dict_path = './words_alpha.txt'
en_dict_path = './english.dic'
print_best_solution(calculate_solution_square(en_dict_path, 5))
# d = load_dict(en_dict_path, word_length=3)
# solution = calculate_solution_square_3(d)
# d = sort_words_value(d)
# d_set = set(d)
# solution = calc_recurs_sol_square(0, d, d_set, [])
# print(solution)
# find_square_solution(en_dict_path, 2)

