liste = [7,9,2,4,5,3,8]
print(liste)

for i in range(len(liste)-1):
    index_mini = i
    mini = liste[i]
    for j in range(i+1, len(liste)):
        if(liste[j] < mini):
            index_mini = j
            mini = liste[j]
    liste[i], liste[index_mini] = liste[index_mini], liste[i]
    
print(liste)
