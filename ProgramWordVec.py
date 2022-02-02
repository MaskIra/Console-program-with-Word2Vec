import gensim.models.word2vec
from colorama import Fore, Style, init
import pathlib
from printy import inputy

# pyinstaller ProgramWordVec.py --icon=C:\Users\maske\Downloads\Word_Mac_23563.icon
# use Colorama on Windows too
init()
model = ""


def change_model():
    global model
    print(Style.RESET_ALL)
    type_model = input("rus - russian model / eng - english model    (default: eng): " + Fore.GREEN)
    print(Style.RESET_ALL + "Please, wait...\n")
    # Load pretrained model (since intermediate data is not included, the model cannot be refined with additional data)

    if type_model == "rus":
        model = gensim.models.KeyedVectors.load_word2vec_format(
            pathlib.Path().absolute() / 'model.bin', binary=True)
        print("_ADV\n_VERB\n_NOUN\n_NUM\n_ADJ\n")
    else:
        model = gensim.models.KeyedVectors.load_word2vec_format(
            pathlib.Path().absolute() / 'GoogleNews-vectors-negative300-SLIM.bin', binary=True)


def main():
    print(Style.RESET_ALL + "What you want?")
    print("1. Make a test`s question")
    print("2. Get most similar")
    print("3. Change model")
    print("other - Exit" + Fore.GREEN)
    res = input()
    if res == "1":
        test_question()
    if res == "2":
        second()
    if res == "3":
        change_model()
        main()


def second():
    print(Style.RESET_ALL)
    print("Write positive words or \'out\' to exit:")
    positive = []
    negative = []
    idx = 1
    while idx != 0:
        str = input(Style.RESET_ALL + "+ " + Fore.GREEN)
        if str == "out":
            idx = 0
        else:
            if str in model:
                positive.append(str)
            else:
                print(Style.RESET_ALL + '{0} is an out of dictionary word'.format(str))

    print(Style.RESET_ALL)
    print("Write negative words or \'out\' to exit:")
    idx = 1
    while idx != 0:
        str = input(Style.RESET_ALL + "- " + Fore.GREEN)
        if str == "out":
            idx = 0
        else:
            if str in model:
                negative.append(str)
            else:
                print(Style.RESET_ALL + '{0} is an out of dictionary word'.format(str))

    print(Fore.LIGHTBLUE_EX)
    print(model.most_similar(positive, negative)[0:6])
    print(Style.RESET_ALL)
    main()


def test_question():
    num = 0
    words = []

    print(Style.RESET_ALL)
    question = input("Your question: " + Fore.GREEN)
    answer = input(Style.RESET_ALL + "Your answer: " + Fore.GREEN)
    words.append(answer)
    num = num + 1

    if answer in model:
        print(Style.RESET_ALL + "y - yes / other symbol - no")
        for val in model.most_similar(positive=[answer]):
            if input(Style.RESET_ALL + "\"{0}\": ".format(val[0]) + Fore.GREEN) == 'y':
                words.append(val[0])
                num = num + 1
            if num == 4:
                break

        import random

        random.shuffle(words)

        print("\n" + Fore.LIGHTBLUE_EX + "\tTest's question:")
        print(question)
        idx = 0
        while idx < 4:
            words[idx] = "{0}) {1}".format(idx + 1, words[idx])
            print(words[idx].split("_", 1)[0])
            idx = idx + 1
    else:
        print('{0} is an out of dictionary word'.format(answer))

    if input(Style.RESET_ALL + "Make a file? (y/n)?: " + Fore.GREEN):
        f = open('questions.txt', 'a')
        f.write("%s\n" % question)
        for item in words:
            f.write("%s\n" % item.split("_", 1)[0])
        f.close()

    input(Style.RESET_ALL + "Press Enter to continue...\n")
    main()


if __name__ == "__main__":
    change_model()
    main()
