words = input().split(" ")
s_end_word = []
for word in words:
    if word.endswith("s"):
        s_end_word.append(word)
print("_".join(s_end_word))
