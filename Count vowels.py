n=input("Enter word:")

count=0

for i in n:
  if i in "aeiouAEIOU":
    count=count+1

print("Number of Vowels:",count)
