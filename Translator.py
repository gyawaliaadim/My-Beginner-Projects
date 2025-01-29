import googletrans

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None

def my_translator():
    list_ = googletrans.LANGUAGES
    d = {}
    for index, i in enumerate(list_):
        print(f"{index+1}) {list_[i].title()}")
        d[str(index+1)] = list_[i].title()

    while True:
        inp = input("Enter your text: ")
        inp1 = input("Convert from (by index or name): ")
        inp2 = input("Convert to (by index or name): ")

        try:
            src_lang = get_key(list_, d[str(inp1)].lower())
            dest_lang = get_key(list_, d[str(inp2)].lower())
        except KeyError:
            print("Invalid input, please try again.")
            continue

        translator = googletrans.Translator()
        translated_text = translator.translate(inp, src=src_lang, dest=dest_lang).text
        print(f"Your text in {d[str(inp2)]} is: {translated_text}")

        while True:
            choice = input("Do you want to continue (Y/N): ")
            if choice.lower() == "y":
                break
            elif choice.lower() == "n":
                return
            else:
                print("Invalid input, please try again.")

if __name__ == "__main__":
    my_translator()
