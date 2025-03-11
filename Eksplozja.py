def solve():
    import sys
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # Konwertujemy dane na inty
    it = iter(data)
    d = int(next(it))
    INF = 2000000000
    results = []
    for _ in range(d):
        N = int(next(it))
        # Przygotowujemy tablice (indeksujemy od 0 do N-1)
        P = [0] * N      # wskazania (później odejmujemy 1)
        S = [0] * N      # liczba wskazań skierowanych do danej osoby
        L = [0] * N      # kolejka (lista) do przetwarzania
        U = [0] * N      # oznaczenie, czy dany wierzchołek został już "odwiedzony"
        MT = [[0, 0] for _ in range(N)]  # MT[i][0], MT[i][1]
        MC = [[[0, 0], [0, 0]] for _ in range(N)]  # MC[i][j][k], j,k ∈ {0,1}
        
        # Inicjujemy: dla każdego i, MT[i][0] = 0, MT[i][1] = 1, S[i] = 0.
        for i in range(N):
            MT[i][0] = 0
            MT[i][1] = 1
            S[i] = 0

        # Wczytujemy P – pamiętając, że w C++ P[i] jest 0-indexowane (czyli odejmujemy 1)
        for i in range(N):
            p_val = int(next(it))
            P[i] = p_val - 1
            S[P[i]] += 1

        lb = 0
        le = 0
        # Wypełniamy listę L dla tych, którzy nie mają wskazań (S[i]==0)
        for i in range(N):
            if S[i] == 0:
                L[le] = i
                le += 1
            U[i] = 0

        # Propagacja w kolejce – zbieramy wyniki DP dla drzew (funkcjonalny graf poza cyklami)
        while lb < le:
            v = L[lb]
            lb += 1
            U[v] = 1
            p = P[v]
            MT[p][1] += MT[v][0]
            MT[p][0] += max(MT[v][0], MT[v][1])
            S[p] -= 1
            if S[p] == 0:
                L[le] = p
                le += 1

        sum_val = 0
        # Przetwarzamy pozostałe wierzchołki – te, które należą do cykli.
        for i in range(N):
            if U[i]:
                continue
            # Zgodnie z oryginałem: S[i] musi być > 0 (czyli i należy do cyklu)
            assert S[i] > 0
            MC[i][0][0] = MT[i][0]
            MC[i][1][0] = -INF
            MC[i][0][1] = -INF
            MC[i][1][1] = MT[i][1]
            prev = i
            curr = P[i]
            U[i] = 1
            while curr != i:
                # Każdy wierzchołek w cyklu jeszcze nie był odwiedzony
                assert U[curr] == 0
                U[curr] = 1
                MC[curr][0][1] = MT[curr][1] + MC[prev][0][0]
                MC[curr][0][0] = MT[curr][0] + max(MC[prev][0][0], MC[prev][0][1])
                if i == prev:
                    assert MC[prev][1][0] == -INF
                    MC[curr][1][1] = -INF
                else:
                    MC[curr][1][1] = MT[curr][1] + MC[prev][1][0]
                MC[curr][1][0] = MT[curr][0] + max(MC[prev][1][0], MC[prev][1][1])
                prev = curr
                curr = P[curr]
            if i != P[i]:
                # max3(MC[prev][0][0], MC[prev][1][0], MC[prev][0][1])
                sum_val += max(MC[prev][0][0], max(MC[prev][1][0], MC[prev][0][1]))
            else:
                sum_val += MT[i][0]
        assert 0 <= sum_val <= N
        results.append(str(N - sum_val))
    sys.stdout.write("\n".join(results))
    
if __name__ == '__main__':
    solve()
