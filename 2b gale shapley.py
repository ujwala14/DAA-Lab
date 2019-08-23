def m_over_m1(women_pl,w,m,m1):
    for man in women_pl[w]:
        if man==m:
            return 1
        if man==m1:
            return 0

def smatch(men_pl,women_pl,n):
    wpart=[-1 for x in range(n)]
    freemen=list(range(n))

    while freemen:
        for m in range(n):
            for w in range(n):
                if m in freemen:
                    woman=men_pl[m][w]
                    if wpart[woman]==-1:
                        wpart[woman]=m
                        freemen.remove(m)
                    else:
                        m1=wpart[woman]
                        if m_over_m1(women_pl,woman,m,m1):
                            wpart[woman]=m
                            freemen.remove(m)
                            freemen.append(m1)
    print(wpart)
    print("the pairs: ")
    for w in wpart:
        print("man {0} with woman {1}".format(wpart[w]+1,w+1))

men_pl,women_pl=[],[]
n=int(input("Enter no :"))
print("Enter pref. list for men: ")
for i in range(n):
    pl=[int(x)-1 for x in input("Man {0}: ".format(i+1)).split()]
    men_pl.append(pl)
print("Enter pref. list for women: ")
for i in range(n):
    pl=[int(x)-1 for x in input("Woman {0}: ".format(i+1)).split()]
    women_pl.append(pl)

#men_pl=[[1, 0, 3, 4, 2], [3, 1, 0, 2, 4], [1, 4, 2, 3, 0], [0, 3, 2, 1, 4], [1, 3, 0, 4, 2]]
#women_pl=[[4, 0, 1, 3, 2], [2, 1, 3, 0, 4], [1, 2, 3, 4, 0], [0, 4, 3, 2, 1], [3, 1, 4, 2, 0]]
print(men_pl)
print(women_pl)

smatch(men_pl,women_pl,n)
