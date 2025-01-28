words = ["data", "engineering", "python", "spark"]


def dictlen(words):
    res_dict = {word: len(word) for word in words}
    return (res_dict)


print(dictlen(words))