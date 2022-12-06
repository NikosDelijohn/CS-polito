import unicodedata
# more info about this package here: https://docs.python.org/3/library/unicodedata.html


def main():
  
    emoji_1 = "🤣"
    emoji_2 = "😍"
    emoji_3 = "😎"  

    # function ord() returns the unicode character encoding
    print(f"U+{ord(emoji_1):4X} - {unicodedata.name(emoji_1):40} - {emoji_1} - RANK  3")

    print(f"U+{ord(emoji_2):4X} - {unicodedata.name(emoji_2):40} - {emoji_2} - RANK  9")

    print(f"U+{ord(emoji_3):4X} - {unicodedata.name(emoji_3):40} - {emoji_3} - RANK 31")


if __name__ == "__main__":
    main()