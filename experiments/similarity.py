question = "Why are hydrangeas blue ?"

chunk_a = "Hydrangea flowers can become blue depending on soil pH."

ques = question.split()
ans = chunk_a.split()
print(ques)
print(ans)

for word in ques:
    if word in ans:
        print(word)

