i = 0
#break loop
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

print("---separator---")

i = 0
# continue loop
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
   
print("---separator---")  

# Skipping vowels from a text
text = "CoderAcademy"
vowels = "aeiouAEIOU"

for each in text:
    if each in vowels:
        continue
    print(each, end=" ")

print("---separator---")



# Stop when there is 'stop'
signals = ['start', 'halt', 'continue', 'start', 'stop', 'hold', 'halt', 'go']

for each in signals:
    if each == 'stop':
        break
    print(each)