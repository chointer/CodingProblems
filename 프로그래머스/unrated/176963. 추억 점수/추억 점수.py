def solution(name, yearning, photo):
    # dictionary!
    people = {}
    for n, y in zip(name, yearning):
        people[n] = y

    answer = []
    for pho in photo:
        score = 0
        for character in pho:
            if character in people.keys():
                score += people[character]
        answer.append(score)
    return answer