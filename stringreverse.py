

while True:
    str=input("Enter your string here: ")
    def reverse(str):
        result=""
        for i in range(len(str)):
            result=str[i] + result
            
        return result
    print(reverse(str))
