sentence = "im the best sceintist in the world"
sentence_str = " "

for i in range (len(sentence)):
    
    if i % 2 == 1:
        
        sentence_str += sentence[i].lower()
        
    else:
        
        sentence_str += sentence[i].upper()
        
print(sentence_str)

new_sentence = "im@the@best@sceintist@in@the@world"

new_split = new_sentence.split("@")

seperate_word = " "

for i in range(0, len(new_split)): #loop to make every second letter upper

    if i % 2 == 0:
        seperate_word = seperate_word + " "+ new_split[i].lower() 

    else:
        seperate_word = seperate_word +" " + new_split[i].upper()
        
final_word = "".join(seperate_word)
print (final_word)
