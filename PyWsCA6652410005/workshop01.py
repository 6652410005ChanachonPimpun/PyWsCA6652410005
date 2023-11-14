def analyze_sentence(hello):
    words = hello.split()

    totalW = len(words)

    wordCO = {}
    for word in words:
        if word in wordCO:
            wordCO[word] += 1
        else:
            wordCO[word] = 1

    dupword = [word for word, count in wordCO.items() if count > 1]
    countdupword = len(dupword)
    print(f"มีคำรวมทั้งหมด {totalW} คำ")
    print(f"มีคำที่ซ้ำกัน {countdupword} คำ คือ: {', '.join(dupword)}")

    for word, count in wordCO.items():
        if count > 1:
            print(f"คำ '{word}' ซ้ำกัน {count} ครั้ง")

userin = input("ป้อนข้อความ: ")

analyze_sentence(userin)