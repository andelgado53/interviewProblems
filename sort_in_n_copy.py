
unsorted_scores = [90, 90, 90, 90, 90]
HIGHEST_POSSIBLE_SCORE = 100

def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    possible_scores = [0] * (HIGHEST_POSSIBLE_SCORE + 1)
    sorted_scores = []
    for score in unsorted_scores:
        possible_scores[score] +=1 
    
    index = 100
    while index > 0:
        if possible_scores[index] > 0:
            for x in range(possible_scores[index]):
                sorted_scores.append(index)
        index -=1
    return sorted_scores


print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))


for i in xrange(10):
    print(i)