def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) < 3:
        return sorted(scores, reverse=True)
    else: 
        a = max(scores)
        scores.remove(a)
        b = max(scores)
        scores.remove(b)
        c = max(scores)
        return [a, b, c] 
