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

def score(peptide, spectrum, cyclic_mode=False):
    if cyclic_mode:
        theo = Counter(cyclic(peptide))
    else:
        theo = Counter(linear(peptide))
    exp = Counter(spectrum)
    return sum(min(theo[x], exp[x]) for x in theo)

def expand(S):
    return [p+(a,) for p in S for a in amino]

def solve():
    cand = {()}
    res = set()
    target = sorted(spectrum)

    while cand:
        cand = {p+(a,) for p in cand for a in amino}
        new = set()

        for p in cand:
            m = mass(p)

            if m == parent:
                if cyclic(p) == target:
                    res.add(p)

            elif m < parent:
                c = Counter(linear(p))
                valid = True
                for x in c:
                    if c[x] > specC[x]:
                        valid = False
                        break
                if valid:
                    new.add(p)

        cand = new

    return res

def trim(leaderboard, spectrum, N):
    scored = [(p, score(p, spectrum)) for p in leaderboard]
    scored.sort(key=lambda x: x[1], reverse=True)

    if len(scored) <= N:
        return [p for p, s in scored]

    cutoff = scored[N-1][1]
    return [p for p, s in scored if s >= cutoff]

def leaderboard_cyclopeptide_sequencing(spectrum, N):
    leaderboard = [()]
    leader = ()
    parent_mass = max(spectrum)

    while leaderboard:
        leaderboard = expand(leaderboard)
        new_board = []

        for peptide in leaderboard:
            m = mass(peptide)

            if m == parent_mass:
                if score(peptide, spectrum, cyclic_mode=True) > score(leader, spectrum, cyclic_mode=True):
                    leader = peptide

            if m <= parent_mass:
                new_board.append(peptide)

        leaderboard = trim(new_board, spectrum, N)

    return leader

def to_letters(p):
    return "".join(mass_to_aa[x] for x in p)

ans_branch = solve()
ans_leader = leaderboard_cyclopeptide_sequencing(spectrum, 10)

print("Branch and Bound Results:\n")
for p in sorted(ans_branch):
    print(to_letters(p))

print("\nLeaderboard Result:\n")
print(to_letters(ans_leader))