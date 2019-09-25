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
    NG_word_list = []
    while True:
        print('NGワードを入力してください。')
        NG_word = input("これ以上必要ないときはそのままエンターを押してください。　＞　")
        if NG_word == '':
            break
        NG_word_list.append(NG_word)
    replace_word = input("置き換えるワードを入力してください。　＞　")

    my_filter = WordFilter(NG_word_list=NG_word_list, replace_word=replace_word)

    # NGワードが含まれている場合
    my_filter.censor("昨日のアーセナルの試合アツかった！")

    # NGワードが含まれていない場合
    my_filter.censor("昨日のリバプールの試合アツかった！")


if __name__ == '__main__':
    main()
