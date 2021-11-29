string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
strings = string.split(" ")
v_num = 0
for word in strings:
    for letter in list(word):
        if letter in list(vowels):
            v_num += 1
print(v_num)

