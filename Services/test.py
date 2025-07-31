# form = {"form": [{"text": "Date:", "label": "question", "words": [{"box": [461, 22, 508, 40], "text": "Date:"}]}, {"text": "on", "label": "question", "words": [{"box": [571, 75, 593, 93], "text": "on"}]}]}

# firstList = form["form"][i]["words"][0]["box"]
# secondList = form["form"][i]["words"][0]["box"]
# FinalList =[]
# for i in range(0,4):
#     x = firstList[i] + secondList[i]
#     FinalList.append(x)

# print(FinalList)


def solution(n):
    count = 0
    for a in range(1,n+1):
        for b in range(a,n+1):
            for c in range(b,n+1):
                if a**2 + b**2 == c**2:
                    count+1
    return count

print(solution(10))



