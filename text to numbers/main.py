#project to test my skills on create a program that converts text to numbers
# ex ("one hundred twenty three" -> 123)



# start
def run(input_text):
    # get user input
    if input_text == None:
        input_text = input("Enter a number in words: ")
    number = convert_text_to_number(input_text)
    print(f"The number is: {number}")
    if number == None:
        return 0
    return number

    
    

def convert_text_to_number(text):
    final = 0
    temp_numbers = []
    words = text.split()
    for word in words:
        temp_numbers.append(convert_word_to_number(word))
    # print(temp_numbers)
    # add the numbers together if less than 100\

    for number in temp_numbers:
        if number < 100:
            final += number
        else:
            final *= number
    print(final)
    return final


def convert_word_to_number(word):
    if word in get_small_dict():
        return get_small_dict()[word]
    elif word in get_large_dict():
        return get_large_dict()[word]
    return 0


def get_small_dict():
    # convert text to number
    # create a dictionary to map words to numbers
    dictionary = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    return dictionary

def get_large_dict():
    large_numbers = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000,
    }
    return large_numbers