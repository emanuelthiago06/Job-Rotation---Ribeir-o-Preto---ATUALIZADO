def reverse_string(string: str):
        s_rev= ''
        for character in string:
            s_rev =character+s_rev
        return s_rev


def test_no_func():
    string_to_be_reverted = "exemplo"
    string_reverse = string_to_be_reverted[::-1]
    print(string_reverse)

def test_func():
    string_test = "exemplo"
    string_reversed = reverse_string(string_test)
    print(string_reversed)

if __name__ == "__main__":
    test_func()
    test_no_func()


