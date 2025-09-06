def countwords(string):
    return len(string.split())

def countchars(string):
    lower_case =  string.lower()
    letters = {}
    for char in lower_case:
        try:
            letters[char] += 1
        except KeyError:
            letters[char] = 1
    return letters

def report(counts: dict, words: int, filedir):
    keys = counts.keys()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filedir}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in keys:
        print(f"{char}: {counts[char]}")
    print("============= END ===============")