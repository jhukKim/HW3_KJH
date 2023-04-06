def reverse_words(str1):
    str2=""
    str3=""
    for i in str1:
        if(i==" "or i=="\t"):
            str2=i+str3+str2
            str3=""
        else:
            str3+=i
    str2=str3+str2
    return str2

def main():
    str1="Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth"
    str2="Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print(reverse_words(str1))
    print(reverse_words(str2))

if __name__=="__main__":
          main()
