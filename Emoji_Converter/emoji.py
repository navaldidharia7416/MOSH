def emoji_function(term):
    words = term.split(' ')
    dict = {
        ":)": "😀",
        ":(": "😭",
        "$": "🤑",
        "hi": "👋"
    }
    temp = ""
    for i in words:
        temp += dict.get(i, i) + " "
    return temp


term=input(">")
res=emoji_function(term)
print(res)