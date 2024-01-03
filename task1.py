exam_scores = [
    {"student":"Alice","score":85},
    {"student":"Bob","score":92},
    {"student":"Charlie","score":78},
    {"student":"David","score":92},
    {"student":"Eve","score":88},
]

score_list = [x['score'] for x in exam_scores]
#iterate scores from array of dictionary
avarage = sum(score_list)/len(score_list)
print(f"Average score: {avarage}")

max_scores = [x for x in exam_scores if x['score'] == max(score_list)]
print(f"All students with the maximum score: {max_scores}")
#Using list comprehension method itrate score values from exam_scores and find the maximum scores by using max method and add if condition to check it.