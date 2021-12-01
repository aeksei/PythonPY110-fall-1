import re


def task():
    word_list = [
        ",./ sdfsdf",
        "Ddfsdf",
        "@@##,sdfsdf",
        "123_sdfsdf",
        "123sdfsdf",
        ", s,dfsdf",
        "123, fewfew",
    ]
    regex = r"\w+"
    word_pattern = re.compile(regex)  # TODO записать регулярное выражение для поиска слова любой длины

    for word in word_list:
        # print(re.search(regex, word).group())
        print(word_pattern.search(word).group())  # TODO вызвать от регулярного выражения методы search и group


if __name__ == "__main__":
    task()
