def repRate(responses, targets):
    repetitions = {}
    for i in range(len(responses)):
        if responses[i] != targets[i]:
            if responses[i] in repetitions:
                repetitions[responses[i]] += 1
            else:
                repetitions[responses[i]] = 1

    n_rep = 0
    for k, v in repetitions.items():
        if v > 1:
            n_rep += 1 #maybe v?
    return n_rep/len(responses)