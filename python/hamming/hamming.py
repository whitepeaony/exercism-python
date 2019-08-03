def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands should have the same length')
    
    for a, b in zip(strand_a, strand_b):
        if a != b:
            count += 1 
    return count 
