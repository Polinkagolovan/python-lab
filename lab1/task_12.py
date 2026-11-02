def text_analisis():
    text=input("введите текст:")
    words=text.lower().split()
    print("Количество слов:" , len(words))
    dictionary={}
    for word in words:
        if word in dictionary:
            dictionary[word]=dictionary[word]+1
        else:
            dictionary[word]=1
    shortest=[0]
    longest=[0]
    for word in words:
        if len(word)<len(shortest):
            shortest=word
        if len(word)>len(longest) :
            longest=word
        print("Самое короткое словол:",shortest)
        print("Самое длинное слово:", longest )
    most_word=" "
    max_count=0
    for word in dictionary:
        if dictionary[word]>max_count:
            max_count=dictionary[word]
            most_word=word
    print("Самое часто встречающееся слово:", most_word)
    print("Встретилось раз:", max_count)

text_analisis()