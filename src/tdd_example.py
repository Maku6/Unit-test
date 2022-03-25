class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        str_reverse = str[::-1]
        return str_reverse

    def find_longest_word(self, str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest_word = ''
        sub = str.split()
        for word in sub:
            if len(word) > len(longest_word):
                longest_word = word
        return longest_word

    def reverse_list(self, list) -> list:
        """
        Reverses order of elements in list input_list.
        """
        return [i for i in reversed(list)]

    def count_digits(self, list, number_to_be_counted) -> int:
        """
        Return count of digitsb
        """
        count = 0
        for num in list:
            if num == number_to_be_counted:
                count += 1
        return count