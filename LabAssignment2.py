from collections import Counter

spectrum = [
    0,97,97,99,101,103,196,198,198,200,202,
    295,297,299,299,301,394,396,398,400,400,497
]

parent = max(spectrum)

amino = [
    57,71,87,97,99,101,103,
    113,114,115,128,129,131,
    137,147,156,163,186
]

mass_to_aa = {
    57:"G",71:"A",87:"S",97:"P",99:"V",101:"T",103:"C",
    113:"I/L",114:"N",115:"D",128:"K/Q",129:"E",131:"M",
    137:"H",147:"F",156:"R",163:"Y",186:"W"
}

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