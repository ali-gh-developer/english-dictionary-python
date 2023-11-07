from difflib import get_close_matches
import json

# next line , converts json data to python dictionary
data = json.load(open('words.json', encoding='utf-8'))

# adds color to the output
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def translate(word):
    global data
    if word in data:
        print('-' * 20)
        print('Translate : ')
        print(data[word]['translate'])
        print('-' * 20)
        print('Examples : ')
        for ex in data[word]['examples']:
            print('=> ', ex)
        print('-' * 20)

def add(word):
    examples = []
    example = ''
    meaning = input('Meaning : ')
    while (example != 'n'):
        example = input(f'{color.PURPLE}Example (or press n) : {color.END}')
        if (example != 'n'):
            examples.append(example)
    new_word = {
                word: {
                    "translate": meaning,
                    "examples": examples
                }
            }
    data.update(new_word)
    with open('words.json', 'w') as f:
        json.dump(data, f, indent=4)
    print('--- Bye ---')
    

def start():
    global data
    print('\n')
    print(f'{color.BOLD}{color.PURPLE}=========== Hi ==========={color.END}')
    print('\n')

    word = input('search a word : ')
    # with get_close_matches() , we will find closest word to the user word 
    alternate = get_close_matches(word, data.keys())

    if word in data:
        translate(word)
    elif len(alternate) > 0:
        check = input(f"Did you mean {color.PURPLE}{alternate[0]}{color.END} ? y/n : ")
        if check in ['Y', 'y']:
            translate(alternate[0])
        else:
            check = input(f"{color.PURPLE}Add this word ?  y/n : {color.END}")
            if check in ['Y', 'y']:
                add(word)
            else:
                print('--- Bye ---')
    else:
        print('--- not found ---')
        check = input(f"{color.PURPLE}Add this word ?  y/n : {color.END}")
        if check in ['Y', 'y']:
            add(word)
        else:
            print('--- Bye ---')


if __name__ == '__main__':
    start()
