#include <cstdint>
#include <cstdio>

#include <string>
#include <vector>
#include <set>

int main() {

    const std::string input_s = "hepxcrrq";
    const size_t input_len = input_s.size();

    std::vector<uint8_t> input(input_len);
    for (size_t i = 0; i < input_len; ++i) { input[i] = input_s[i] - 'a'; }

    auto is_valid = [&input, &input_len]() -> bool {
        bool test_seq3 = false;
        bool test_letters = true;
        for (unsigned int i = 0; i + 2 < input_len; ++i) {
            if (input[i] + 1 == input[i+1] && input[i] + 2 == input[i+2]) {
                test_seq3 = true;
                break;
            }
        }
        if (!test_seq3) {
            return false;
        }

        for (unsigned int i = 0; i < input_len; ++i) {
            if (input[i] == 'i' - 'a' || input[i] == 'o' - 'a' || input[i] == 'l' - 'a') {
                test_letters = false;
                break;
            }
        }
        if (!test_letters) {
            return false;
        }

        std::set<uint8_t> pairs;
        for (unsigned int i = 0; i + 1 < input_len; ++i) {
            if (input[i] == input[i+1]) {
                pairs.insert(input[i]);
                ++i;
            }
        }
        return pairs.size() >= 2;
    };

    auto increment = [&input, &input_len]() {
        bool carry = true;
        for (unsigned int i = 0; i < input_len && carry; ++i) {
            auto &in = input[input_len - i - 1];
            ++in;
            if (in == 26) {
                in = 0;
            }
            else {
                carry = false;
            }
        }
    };

    increment();
    while (!is_valid()) {
        increment();
    }
    std::string output_s;
    for (auto c : input) { output_s.push_back(char(c + 'a')); }
    puts(output_s.c_str());

    
    increment();
    while (!is_valid()) {
        increment();
    }
    output_s.clear();
    for (auto c : input) { output_s.push_back(char(c + 'a')); }
    puts(output_s.c_str());


    return 0;
}