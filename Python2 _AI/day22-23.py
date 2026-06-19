"""names = ["Tom","Jack","Rose","Alice"]
scores = [95,58,88,92]
for name,score in zip(names, scores):
    if score > 80:
        print(name,"进入面试")"""

"""files = [
    "report.pdf",
    "photo.jpg",
    "resume.pdf",
    "music.mp3"
]

for tile in files:
    if "pdf" in tile:
        print("发现pdf:",tile)"""

messages = [
    "hello",
    "free money",
    "how are you",
    "buy now"
]
for message in messages:
    if "free" in message or "buy" in message:
        print("Rubbish")
    else:
        print("Normal")