class WordFilter:
    def __init__(self, NG_word_list, replace_word):
        self.NG_word_list = NG_word_list
        self.replace_word = replace_word

    def censor(self, sentence):
        replace_sentence = sentence
        for NG_word in self.NG_word_list:
            replace_sentence = replace_sentence.replace(NG_word, self.replace_word)
        print(replace_sentence)


def main():
    while True:

        NG_word_list = make_NG_list()
        replace_word = input("置き換えるワードを入力してください。　＞　")
        my_filter = WordFilter(NG_word_list=NG_word_list, replace_word=replace_word)

        # NGワードが含まれている場合
        my_filter.censor("昨日のアーセナルの試合アツかった！")

        # NGワードが含まれていない場合
        my_filter.censor("昨日のリバプールの試合アツかった！")

        while True:
            change = input('NGワードを変更しますか？　[y/n] ＞　')
            if change == 'y' or change == 'n':
                break

        if change == 'y':
            continue
        elif change == 'n':
            break


def make_NG_list():
    NG_word_list = []
    while True:
        print('NGワードを入力してください。')
        NG_word = input("これ以上必要ないときはそのままエンターを押してください。　＞　")
        if NG_word == '':
            break
        NG_word_list.append(NG_word)
    return NG_word_list

if __name__ == '__main__':
    main()
