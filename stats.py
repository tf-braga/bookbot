def word_count(book):   
    words = book.split()
    count = len(words)
    return count

def count_characters(text):
    text = text.lower()
    dict = {}
    for characters in text:
        if characters in dict:
            dict[characters] += 1
        else:
            dict[characters] = 1
    return dict

def sort_on(item):
    return item["num"]

def sort_items(char_counts):
    items = []
    for char, count in char_counts.items():
        items.append({"char": char, "num": count})
    items.sort(reverse=True, key=sort_on)
    return items