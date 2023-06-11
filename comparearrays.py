myList = []
compareList = ['be']
print("To _ or not to _. That is the question.")
print("What is the missing word?")
num = int(input("How many words do you want?"))
if num == 0: 
    print("Please enter a number greater than 0")
    exit()
for i in range (0, num):
    word = input("Enter a word: ")
    myList.append(word)
    print(myList)
if myList == compareList:
    print("To be or not to be. That is the question.")
    print("You win!")
else:
    print("To " + word + " or not to " + word + ". That is the question.")
    print("You lose!")








#x = input("First Word:")
#y = input("Second Word:")
#z = input("Third Word:")
#a = {""}
#if # 