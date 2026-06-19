"""messages = [
    "hello",
    "FREE MONEY",
    "how are you",
    "buy now"
]
for message in messages:
    msg = message.lower()
    if "free" in msg or "buy" in msg:
        print("rubbish")
    else:
        print("normal")

"FREE MONEY".lower()"""

messages = [
    "FREE money now!!!",
    "Hello how are you",
    "buy cheap iphone",
    "Let's go to school"
]
count = 0
num = 0
for message in messages:
    msg = message.lower()
    if "free" in msg or "buy" in msg:
        print(message,"=>Rubbish")
        count += 1
    else:
        print(message,"=>Normal")
        num += 1
print("Rubbish:", count, "Normal:", num)