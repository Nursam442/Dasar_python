message = input(">>> ")

emoji_mapping = {
    ":)": "😊",
    ":D": "😁",
    ":|": "😑",
    "?" : "🤔",
    "l" : "❤️"
}

words = message.split(" ")

# print(message)
# print(words)

output = ""
for w in words:
    output = output + emoji_mapping.get(w, w) + " "

print(output)