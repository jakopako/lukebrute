#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

map<char, map<string, int>> letter_values = {
        {'a', {{"points",  1}, {"tiles",  9}}},
        {'c', {{"points",  3}, {"tiles",  2}}},
        {'b', {{"points",  3}, {"tiles",  2}}},
        {'d', {{"points",  2}, {"tiles",  4}}},
        {'e', {{"points",  1}, {"tiles", 12}}},
        {'f', {{"points",  4}, {"tiles",  2}}},
        {'g', {{"points",  2}, {"tiles",  3}}},
        {'h', {{"points",  4}, {"tiles",  2}}},
        {'i', {{"points",  1}, {"tiles",  9}}},
        {'j', {{"points",  8}, {"tiles",  1}}},
        {'k', {{"points",  5}, {"tiles",  1}}},
        {'l', {{"points",  1}, {"tiles",  4}}},
        {'m', {{"points",  3}, {"tiles",  2}}},
        {'n', {{"points",  1}, {"tiles",  6}}},
        {'o', {{"points",  1}, {"tiles",  8}}},
        {'p', {{"points",  3}, {"tiles",  2}}},
        {'q', {{"points", 12}, {"tiles",  1}}},
        {'r', {{"points",  1}, {"tiles",  6}}},
        {'s', {{"points",  1}, {"tiles",  4}}},
        {'t', {{"points",  1}, {"tiles",  6}}},
        {'u', {{"points",  2}, {"tiles",  4}}},
        {'v', {{"points",  6}, {"tiles",  2}}},
        {'w', {{"points",  5}, {"tiles",  2}}},
        {'x', {{"points",  7}, {"tiles",  1}}},
        {'y', {{"points",  5}, {"tiles",  2}}},
        {'z', {{"points",  8}, {"tiles",  1}}}
    };

class Board {

    vector<vector<int> > layout;
    string dict_path;
    vector<string> words;
    map<int, vector<string>> word_lists;
    map<int, map<int, set<string>>> lookup_dict;

    private:

    map<int, vector<string>> generate_word_lists() {
        map<int, vector<string>> word_lists;
        set<int> word_lengths = extract_word_lengths();
        for (int l: word_lengths) {
            vector<string> tmp_words;
            if (l == 1) {
                for(map<char, map<string, int>>::iterator it = letter_values.begin(); it != letter_values.end(); ++it) {
                    string s(1, it->first);
                    tmp_words.push_back(s);
                }
            } else {
                std::copy_if(words.begin(), words.end(), std::back_inserter(tmp_words), [l](string s){return s.length()==l;} );
            }
            sort(tmp_words.begin(), tmp_words.end(), compare_words);
            word_lists.insert({l, tmp_words});
        }
        return word_lists;
    }

    static bool compare_words(string &word1, string &word2) {
        return get_word_value(word1) > get_word_value(word2);
    }

    static int get_word_value(string &word) {
        int val = 0;
        for (char const &c: word) {
            val += letter_values[c]["points"];
        }
        return val;
    }

    set<int> extract_word_lengths() {
        int tmp_len;
        set<int> lengths;
        vector<vector<int>> layout_transpose = get_layout_transpose();
        vector<vector<vector<int>>> lt = {layout, layout_transpose};
        for (vector<vector<int>> l: lt) {
            for (vector<int> row: l) {
                tmp_len = 0;
                for (int val: row) {
                    if (val == 1) {
                        tmp_len++;
                    } else if (tmp_len > 0) {
                        lengths.insert(tmp_len);
                        tmp_len = 0;
                    }
                }
                if (tmp_len > 0) {
                    lengths.insert(tmp_len);
                }
            }
        }
        return lengths;
    }

    vector<vector<int>> get_layout_transpose() {
        vector<vector<int>> tr;
        for (int i=0; i < layout[0].size(); i++) {
            vector<int> col;
            for (int j=0; j < layout.size(); j++) {
                col.push_back(layout[j][i]);
            }
            tr.push_back(col);
        }
        return tr;
    }

    vector<string> load_words() {
        vector<string> w;
        ifstream in(dict_path);
        string word;
        while (getline(in, word))
        {
            word.pop_back();
            if(word.size() > 0)
                w.push_back(word);
        }
        return w;
    }

    set<string> extract_prefixes(vector<string> &word_list, int prefix_len) {
        set<string> prefix_set;
        for (string s: word_list) {
            prefix_set.insert(s.substr(0, prefix_len));
        }
        return prefix_set;
    }

    map<int, map<int, set<string>>> generate_word_lookup_dict() {
        map<int, map<int, set<string>>> lookup_dict;
        for (map<int, vector<string>>::iterator it = word_lists.begin(); it != word_lists.end(); it++) {
            for (int prefix_len = 1; prefix_len <= it->first; prefix_len++){
                lookup_dict[it->first][prefix_len] = extract_prefixes(it->second, prefix_len);
            }
        }
        return lookup_dict;
    }

    public:
    
    Board (vector<vector<int> > l, string d) {
        layout = l;
        dict_path = d;
        words = load_words();
        word_lists = generate_word_lists();
        lookup_dict = generate_word_lookup_dict();
    }

    void print_layout() {
        for (std::vector<int> row: layout) {
            for (int val: row) {
                std::cout << val << " ";
            }
            std::cout << '\n';
        }
    }
};

int main()
{
    vector<vector<int>> layout1 {
        {1, 1, 1},
        {0, 1, 1},
        {0, 0, 1}
        };
    vector<vector<int>> layout2 {
        {1, 1, 1},
        {1, 1, 1},
        {1, 1, 1}
        };
    vector<vector<int>> layout3 {
        {1, 1, 1},
        {1, 1, 1},
        {0, 1, 0}
        };
    string d_path = "./english.dic";
    Board b (layout3, d_path);
}