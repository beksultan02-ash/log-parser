students = {
    "Bek": 85,
    "Ali": 92,
    "Tom": 70,
    "Sara": 99
}
max = 0
top_scores = {}
for name, scores in students.items():
    if scores > max :
        max = scores
    
    if scores >= 90:
       top_scores[name] = scores

print(f"Maximum score is {max}")
print(f"Best students are: {top_scores}")