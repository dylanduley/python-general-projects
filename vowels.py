def main():
    user_input = input('Input a string: ')

    print(f'That string has {count_vowels(user_input)} vowels and {count_consonants(user_input)} consonants.')

def count_vowels(s):
    """Count the number of vowels in the input string."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for char in s:
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count

def count_consonants(s):
    """Count the number of consonants in the input string."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonant_count = 0

    for char in s:
        if char.isalpha() and char.lower() not in vowels:
            consonant_count += 1

    return consonant_count

main()
