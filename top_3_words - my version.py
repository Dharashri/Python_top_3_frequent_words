def top3(text):
    sentence=""
    for char in text:
        if char.isalpha() or char == " ":
            sentence+= char.lower()
    words = sentence.split(" ")
    word_list = []
    count_list = []

    for word in words:
        if word=="":
            continue
        if word in word_list:
            index=word_list.index(word)
            count_list[index] +=1
        else:
            word_list.append(word)
            count_list.append(1)
    
    for i in range(len(word_list)-1):
        for j in range(len(word_list)-i-1):
            if count_list[j] < count_list[j+1]:
                count_list[j],count_list[j+1]=count_list[j+1],count_list[j]
                word_list[j],word_list[j+1]=word_list[j+1],word_list[j]

    output = []
    for i in range(min(3, len(word_list))):
        output.append(word_list[i])
    return output

text = input("Enter a sentence:")
print (top3(text))
