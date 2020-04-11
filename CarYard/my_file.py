palindromes = []


def print_all_n_length(my_set, k):
    n = len(my_set)
    print_all_n_length_rec(my_set, "", n, k)


def print_all_n_length_rec(my_set, prefix, n, k):
    if k == 0 and is_palindrome(prefix):
        palindromes.append(prefix)
        return

    for i in range(n):
        new_prefix = prefix + my_set[i]
        print_all_n_length_rec(my_set, new_prefix, n, k - 1)


def is_palindrome(word):
    length = len(word)
    for i in range(0, int(length/2)):
        if word[i] != word[length - i - 1]:
            return False
    return True

print_all_n_length(['a', 'b'], 2)
print(palindromes)
#print(generatePalindromes(['a', 'B', '5', '&', 't', 'X'],10))
