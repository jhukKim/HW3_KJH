def fact(num):
    
    if num==0:
        return 1
    else:
        return fact(num-1)*num
    

def main():
    for i in range(0,16,2):
        print("{} factorial: {}\n".format(i,fact(i)))
    

if __name__=="__main__":
    main()
    
