string = input("Enter a string : ")
string = string.lower()
vowel_count = 0
consonant_count = 0

for i in range(len(string)):
    ch = string[i]
    if(ch.isalpha()):
        if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
            vowel_count+=1
        else:
            consonant_count+=1
        
print(f"Number of vowels : {vowel_count}")
print(f"Number of consonants : {consonant_count}")