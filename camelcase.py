def camelcase(sentence):
    """ Convert sentence to camelCase, for example, "Display all books"
is converted to "displayAllBooks" """
    title_case = sentence.title() # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '') # remove spaces
# Lowercase first letter, join with rest of string
# Slices don't produce index out of bounds errors.
# So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def instructions():
    print("    THESE ARE THE INSTRUCTIONS FOR YOU TO FOLLOW:")
    print("Step 1. Think of a sentence you want to turn into camelCase.")
    print("Step 2. Type the sentence into the prompt.")
    print("Step 3. Press 'ENTER' and read the camelCased sentence/word.")   # Added some instructions to test
def display_banner():
    """ Display program name in banner """
    msg = 'Bryan\'s awesome BRANCH 5 camelCaseGenerator PROGRAM'
    stars = '\/' * (len(msg)-25)
    print(f'\n {stars} \n {msg} \n {stars}\n')  # I just made some minute changes to test pushing to GitHub

def main():
    display_banner()
    instructions()
    sentence = input('Enter your sentence: ')   # If I understand branches correctly, this comment should appear on GitHub
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()