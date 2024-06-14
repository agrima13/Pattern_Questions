class Pangram:
    def is_pangram(test_string):
        test_string = test_string.lower()
        unique_letters = set(test_string)
        return (len(unique_letters) == 26)
            
    

    if __name__ == '__main__':
        test_str1 = "TheQuickBrownFoxJumpsOverTheLazyDog"
        test_str2 = "This is not a pangram"
        print(is_pangram(test_str2))

    