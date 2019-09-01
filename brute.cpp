#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <set>

using namespace std;


class Board {

    vector<vector<int> > layout;
    string dict_path;
    vector<string> words;
    map<int, vector<string>> word_lists;

    private:

    map<int, vector<string>> generate_word_lists() {
        map<int, vector<string>> word_lists;
        set<int> word_lengths = extract_word_lengths();

        return word_lists;
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
            //word.erase( std::remove(word.begin(), word.end(), '\r'), word.end() );
            word.pop_back();
            if(word.size() > 0)
                w.push_back(word);
        }
        return w;
    }

    public:
    
    Board (vector<vector<int> > l, string d) {
        layout = l;
        dict_path = d;
        words = load_words();
        word_lists = generate_word_lists();
        
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

/*     vector<string> msg {"Hello", "C++", "World", "from", "VS Code!", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl; */
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