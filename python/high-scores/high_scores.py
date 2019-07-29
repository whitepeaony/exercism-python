def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) < 3:
        scores.sort()
        scores.reverse()
        return scores
    else: 
        a = max(scores)
        scores.remove(a)
        b = max(scores)
        assert b is not None
        scores.remove(b)
        c = max(scores)
        return [a, b, c] 
