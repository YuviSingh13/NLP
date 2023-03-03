'''observations = ("normal", "cold", "dizzy")
states = ("Healthy", "Fever")
start_p = {"Healthy": 0.6, "Fever": 0.4}
trans_p = {
    "Healthy": {"Healthy": 0.7, "Fever": 0.3},
    "Fever": {"Healthy": 0.4, "Fever": 0.6},
}
emit_p = {
    "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
    "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
}


def viterbi_algorithm(observations, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][observations[0]], "prev": None}

    for t in range(1, len(observations)):
        V.append({})
        for st in states:
            max_tr_prob = V[t - 1][states[0]]["prob"] * trans_p[states[0]][st]
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                tr_prob = V[t - 1][prev_st]["prob"] * trans_p[prev_st][st]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    prev_st_selected = prev_st

            max_prob = max_tr_prob * emit_p[st][observations[t]]
            V[t][st] = {"prob": max_prob, "prev": prev_st_selected}


    for line in dptable(V):
        print(line)

    opt = []
    max_prob = 0.0
    best_st = None

    for st, data in V[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st

    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]

    print("The steps of states are " + " ".join(opt) + " with highest probability of %s" % max_prob)


def dptable(V):
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

'''

pos = ["NNP", "MD", "VB", "JJ", "NN", "RB", "DT"]

trans = [[0.2767, 0.0006, 0.0031, 0.0453, 0.0449, 0.0510, 0.2026],
         [0.3777, 0.0110, 0.0009, 0.0084, 0.0584, 0.0090, 0.0025],
         [0.0008, 0.0002, 0.7968, 0.0005, 0.0008, 0.1689, 0.0041],
         [0.0322, 0.0005, 0.0050, 0.0837, 0.0615, 0.0514, 0.2231],
         [0.0366, 0.0004, 0.0001, 0.0733, 0.4509, 0.0036, 0.0036],
         [0.0096, 0.0176, 0.0014, 0.0086, 0.1216, 0.0177, 0.0068],
         [0.1147, 0.0102, 0.1011, 0.1012, 0.0120, 0.0728, 0.0479],
         [0.1147, 0.0021, 0.0002, 0.2157, 0.4744, 0.0102, 0.0017]]




sen = ["janet", "will", "back", "the", "bill"]

ems = [[0.000032, 0, 0, 0.000048, 0],
       [0, 0.308431, 0, 0, 0],
       [0, 0.000028, 0.000672, 0, 0.000028],
       [0, 0, 0.000340, 0, 0],
       [0, 0.000200, 0.000223, 0, 0.002337],
       [0, 0, 0.010446, 0, 0],
       [0, 0, 0, 0.506099, 0]]


start = 0
second = 0
index = 0
for i in range(len(pos)):
    if trans[0][i] > start:
        start = trans[0][i]
        index = i
    if start > trans[0][i] > second:
        second = trans[0][i]
# print(start, pos[index])
print(second, "second highest")

# for i in range(len(sen)):
#     for j in range(len(pos)):


# def viterbi()