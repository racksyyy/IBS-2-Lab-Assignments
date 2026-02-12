def CyclopeptideSequencing(Spectrum):
    Mass={
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
        'X': 0
        }
    parent=max(Spectrum)
    CandidatePeptides={}
    FinalPeptides=[]
    while (CandidatePeptides):
        for peptide in CandidatePeptides:
            if Mass[peptide] == parent:
                if 


from collections import Counter

spectrum = [
    0,97,97,99,101,103,196,198,198,200,202,
    295,297,299,299,301,394,396,398,400,400,497
]


specC = Counter(spectrum)


def mass(p):
    return sum(p)


def linear(p):
    s = [0]
    for i in range(len(p)):
        t = 0
        for j in range(i,len(p)):
            t += p[j]
            s.append(t)
    return s


def cyclic(p):
    s = [0]
    n = len(p)
    d = p+p

    for l in range(1,n):
        for i in range(n):
            s.append(sum(d[i:i+l]))

    s.append(sum(p))
    return sorted(s)


def ok(p):
    c = Counter(linear(p))
    for x in c:
        if c[x] > specC[x]:
            return False
    return True


def expand(S):
    return {p+(a,) for p in S for a in amino}


def solve():

    cand = {()}
    res = set()

    while cand:

        cand = expand(cand)
        new = set()

        for p in cand:

            m = mass(p)

            if m == parent:

                if cyclic(list(p)) == sorted(spectrum):
                    res.add(p)

            elif m < parent and ok(list(p)):
                new.add(p)

        cand = new

    return res


def to_letters(p):
    return "".join(mass_to_aa[x] for x in p)


ans = solve()

print("List of consistent 5-mers:\n")

for p in sorted(ans):
    print(to_letters(p))