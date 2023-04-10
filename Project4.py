def most_frequent(word):
    frequency_dict={}
    for letter in word:
        if letter in frequency_dict:
            frequency_dict[letter]+=1
        else:
            frequency_dict[letter]=1
    sorted_dict=dict(sorted(frequency_dict.items(),key=lambda x:x[1],reverse=True))

    for key,value in sorted_dict.items():
        print(key,":",value)

print(most_frequent("Mississippi"))
        
