import copy

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
        "z": {"points": 8, "tiles":  1}
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


def print_square(sol):
    r = "\n"
    for s in sol:
        r += "%s\n" % s
    return r


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
    print("Most valuable solution: %s%d points" % (print_square(highest_sol), highest))


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


class Board:
    def __init__(self, dict_path, layout):
        self.layout = layout
        self.words = self.load_words(dict_path)
        self.word_lists = self.generate_word_lists()
        self.lookup_dict = self.generate_word_lookup_dict()
        self.state = self.generate_index_list()
        self.state_word_index = 0

    def find_solutions(self, limit=None):
        """
        This method finds the actual solutions by iterating over all states and checking whether
        they make sense or not.
        :param limit: if not None this determines after how many solutions the process shall stop.
        :return: An array with the solutions sorted in reverse order according to their values.
        """
        solutions = []
        while self.has_next_state():
            self.go_to_next_state()
            if self.is_valid_state():
                if self.all_filled_in():
                    fl = self.get_filled_layout()
                    solutions.append((fl, Board.score_solution(fl)))
                    if limit is not None:
                        if len(solutions) == limit:
                            return sorted(solutions, key=lambda tup: tup[1], reverse=True)
                else:
                    self.state_word_index += 1

        return sorted(solutions, key=lambda tup: tup[1], reverse=True)

    @staticmethod
    def load_words(path):
        """
        This method reads the file at the given path and returns a
        list containing the newline-separated words of this file.
        :param path: The path to be read.
        :return: A list of words contained within the given file.
        """
        with open(path, 'r') as f:
            d = f.read().split('\n')
            return [w.lower() for w in d]

    def generate_word_lists(self):
        """
        This method returns a dictionary containing all the words
        for each word-length that is contained in this Board's layout.
        The lists are sorted according to the word's values in descending order.
        :return: A dictionary containing all the relevant words for this Board's layout.
        """
        lengths = set()
        word_lists = {}
        for row in self.layout:
            lengths |= Board.extract_word_lengths(row)
        for col in Board.get_transpose(self.layout):
            lengths |= Board.extract_word_lengths(col)
        for l in lengths:
            if l == 1:
                word_lists[l] = sort_words_value(letter_value.keys())
            else:
                word_lists[l] = sort_words_value(filter_on_length(l, self.words))
        return word_lists

    def generate_word_lookup_dict(self):
        """
        This method generates a dictionary of word lists of the following structure:
        { 1: {1: set(words of length 1)},
          2: {1: set(prefixes of length 1 from words of length 2),
              2: set(words of length 2)},
          3: {1: set(prefixes of length 1 from words of length 3),
              2: set(prefixes of length 2 from words of length 3),
              3: set(words of length 3)},
          4: {1: set(prefixes of length 1 from words of length 4),
              2: set(prefixes of length 2 from words of length 4),
              3: set(prefixes of length 3 from words of length 4),
              4: set(words of length 4)}
          .
          .
          .
        The algorithm only generates these sets for word lengths that occur
        in this Board's layout.
        :return: A dictionary of the structure described above.
        """

        lookup_dict = {}
        for word_length, word_list in self.word_lists.items():
            for prefix_len in range(1, word_length+1):
                if prefix_len == 1:
                    lookup_dict[word_length] = {prefix_len: self.extract_prefixes(word_list, prefix_len)}
                else:
                    lookup_dict[word_length][prefix_len] = self.extract_prefixes(word_list, prefix_len)
        return lookup_dict

    def generate_index_list(self):
        """
        This list represents the initial state of the algorithm.
        An item in this list is a tuple of the following form:
        (row_index, word_index, dict_index, max_dict_index, word_length)
        row_index:      The index of the row where this tuple's word is located.
        word_index:     The position in this word's row.
        dict_index:     The index of the current word in the respective dictionary.
                        This dictionary is the list of all words with the same
                        length as the current word. Initially, this value will be
                        -1 which means that there is no word filled in yet.
        max_dict_index: The maximum dictionary index. This differs depending on the
                        word's length.
        word_length:    The length of the current word.

        Example of the initial list for layout0.

        layout0 = [[1, 0, 0, 0, 0, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 0, 0, 0, 0, 1]]

        [(0, 0, -1, 25, 1),
         (0, 5, -1, 25, 1),
         (1, 0, -1, dict_len_wordlen_2-1, 2),
         (1, 4, -1, dict_len_wordlen_2-1, 2),
         (2, 0, -1, dict_len_wordlen_6-1, 6),
         (3, 0, -1, dict_len_wordlen_6-1, 6),
         (4, 0, -1, dict_len_wordlen_2-1, 2),
         (4, 4, -1, dict_len_wordlen_2-1, 2),
         (5, 0, -1, 25, 1),
         (5, 5, -1, 25, 1)]

        :return: A list of the form described above.
        """

        index_list = []
        for row_index in range(len(self.layout)):
            word_len = 0
            word_index = 0
            for col_index in range(len(self.layout[row_index])):
                el = self.layout[row_index][col_index]
                if el == 1:
                    word_len += 1
                elif word_len > 0:
                    index_list.append((row_index, col_index - word_len, -1, len(self.word_lists[word_len]) - 1, word_len))
                    word_index += 1
                    word_len = 0
            if word_len > 0:
                index_list.append((row_index, len(self.layout[row_index]) - word_len, -1, len(self.word_lists[word_len]) - 1, word_len))
        return index_list

    def has_next_state(self):
        """
        This method checks whether there are still possible states of this Board that
        have not been checked yet.
        :return: True if there are more states to check, else False.
        """
        for _, _, dict_index, max_dict_index, _ in self.state:
            if dict_index < max_dict_index:
                return True
        return False

    def go_to_next_state(self):
        """
        This method brings this Board to the next state. It increases the right index by
        one and handles the carry-logic if necessary. This method is not concerned whether
        the next state is a valid state or not. This logic is handled by the method
        is_valid_state().
        """
        while self.state_word_index >= 0:
            ri, wi, di, mdi, wl = self.state[self.state_word_index]
            if di < mdi:
                di += 1
                self.state[self.state_word_index] = ri, wi, di, mdi, wl
                break
            else:
                self.state[self.state_word_index] = ri, wi, -1, mdi, wl
                self.state_word_index -= 1

    def get_filled_layout(self):
        """
        This method returns a copy of the layout field but with all the current state's
        letters filled in instead of 1's.
        :return: This Board's layout with the current state's letters filled in.
        """
        filled_layout = copy.deepcopy(self.layout)
        for ri, wi, di, _, wl in self.state:
            if di >= 0:
                word = self.word_lists[wl][di]
                for i in range(len(word)):
                    filled_layout[ri][wi + i] = word[i]
            else:
                break
        return filled_layout

    def is_valid_state(self):
        """
        This method checks whether this Board's state is valid. I.e. whether the current state could
        lead to or is a valid solution to the game.
        :return: True or False depending on this Board's state.
        """
        filled_layout = self.get_filled_layout()
        t = Board.get_transpose(filled_layout)
        for row in t:
            tmp_word = ''
            tmp_word_len = 0
            for poss_letter in row:
                if isinstance(poss_letter, str):
                    tmp_word += poss_letter
                    tmp_word_len += 1
                elif poss_letter == 1:
                    tmp_word_len += 1
                else:
                    if not not tmp_word:
                        if tmp_word not in self.lookup_dict[tmp_word_len][len(tmp_word)]:
                            return False
                        tmp_word = ''
                        tmp_word_len = 0
            if not not tmp_word:
                if tmp_word not in self.lookup_dict[tmp_word_len][len(tmp_word)]:
                    return False
        return True

    def all_filled_in(self):
        """
        This method checks whether all fields of the Board's layout are filled in.
        :return: True if all fields are filled in, False otherwise.
        """
        for _, _, di, _, _ in self.state:
            if di == -1:
                return False
        return True

    @staticmethod
    def score_solution(m):
        """
        This method returns the score of the given layout m.
        :param m: The filled in layout to be scored.
        :return: The score of the given layout m.
        """
        s = 0
        for r in m:
            for l in r:
                if isinstance(l, str):
                    s += letter_value[l]['points']
        return s

    @staticmethod
    def get_transpose(m):
        trans = []
        for i in range(len(m[0])):
            col = []
            for j in range(len(m)):
                col.append(m[j][i])
            trans.append(col)
        return trans

    @staticmethod
    def extract_word_lengths(arr):
        ls = set()
        tmp_len = 0
        for el in arr:
            if el == 1:
                tmp_len += 1
            elif tmp_len > 0:
                ls.add(tmp_len)
                tmp_len = 0
        if tmp_len > 0:
            ls.add(tmp_len)
        return ls

    @staticmethod
    def extract_prefixes(word_list, prefix_len):
        prefixes = set()
        for word in word_list:
            prefixes.add(word[:prefix_len])
        return prefixes


layout1 = [[0, 0, 1],
           [0, 1, 1],
           [1, 1, 1]]

layout2 = [[1, 1, 1, 1],
           [1, 1, 1, 0],
           [1, 1, 0, 0],
           [1, 0, 0, 0]]

layout3 = [[1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1]]

layout4 = [[1, 1, 1, 0, 0, 0],
           [0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0],
           [0, 0, 0, 1, 1, 1]]

layout5 = [[1, 0, 0, 0, 0, 1],
           [1, 1, 0, 0, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 1, 1],
           [1, 0, 0, 0, 0, 1]]

layout6 = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]

layout7 = [[1, 0, 1],
           [1, 1, 1],
           [1, 0, 1]]

layout8 = [[1, 1, 0, 0, 1, 1],
           [1, 1, 0, 0, 1, 1]]

layout9 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

layout10 = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]

layout11 = [[1, 1, 1, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 1, 1]]

layout12 = [[1, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1]]


# en_dict_path = './words_alpha.txt'
en_dict_path = './english.dic'
b = Board(en_dict_path, layout12)
s = b.find_solutions(limit=50000)
for i in range(10):
    print(s[i])

# print_best_solution(calculate_solution_square(en_dict_path, 3))
# d = load_dict(en_dict_path, word_length=3)
# solution = calculate_solution_square_3(d)
# d = sort_words_value(d)
# d_set = set(d)
# solution = calc_recurs_sol_square(0, d, d_set, [])
# print(solution)
# find_square_solution(en_dict_path, 2)


# ['jazzer', 'oriole', 'tenuis', 'togate', 'eleven', 'rarest']
