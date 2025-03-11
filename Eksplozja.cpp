#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;

const int MAXN = 100000;
const int INF = 2000000000;
#define max3(a, b, c) max((a), max((b), (c)))

int N;
int P[MAXN];
int S[MAXN];
int L[MAXN];
int lb, le;

int MT[MAXN][2];
int MC[MAXN][2][2];
int U[MAXN];

int main(){
    int d, i, sum;
    if (scanf("%d", &d) < 1) assert(0);
    assert(d > 0);
    while(d--){
        if (scanf("%d", &N) < 1) assert(0);
        assert((N >= 2) && (N <= MAXN));
        for(i = 0; i < N; i++){
            MT[i][0] = 0;
            MT[i][1] = 1;
            S[i] = 0;
        }
        for(i = 0; i < N; i++){
            if (scanf("%d", &P[i]) < 1) assert(0);
            assert((P[i] >= 1) && (P[i] <= N));
            P[i]--;  // indeksujemy od 0
            S[P[i]]++;
        }
        lb = le = 0;
        for(i = 0; i < N; i++){
            if(S[i] == 0){
                L[le++] = i;
            }
            U[i] = 0;
        }
        
        while(lb < le){
            int v = L[lb++];
            U[v] = 1;
            int p = P[v];
            MT[p][1] += MT[v][0];
            MT[p][0] += max(MT[v][0], MT[v][1]);
            S[p]--;
            if(S[p] == 0)
                L[le++] = p;
        }
        
        sum = 0;
        for(i = 0; i < N; i++){
            if(U[i]) continue;
            assert(S[i] > 0);
            MC[i][0][0] = MT[i][0];
            MC[i][1][0] = -INF;
            MC[i][0][1] = -INF;
            MC[i][1][1] = MT[i][1];
            int prev = i;
            int curr = P[i];
            U[i] = 1;
            while(curr != i){
                assert(!U[curr]);
                U[curr] = 1;
                MC[curr][0][1] = MT[curr][1] + MC[prev][0][0];
                MC[curr][0][0] = MT[curr][0] + max(MC[prev][0][0], MC[prev][0][1]);
                if(i == prev){
                    assert(MC[prev][1][0] == -INF);
                    MC[curr][1][1] = -INF;
                }
                else
                    MC[curr][1][1] = MT[curr][1] + MC[prev][1][0];
                MC[curr][1][0] = MT[curr][0] + max(MC[prev][1][0], MC[prev][1][1]);
                prev = curr;
                curr = P[curr];
            }
            if(i != P[i])
                sum += max3(MC[prev][0][0], MC[prev][1][0], MC[prev][0][1]);
            else
                sum += MT[i][0];
        }
        assert(sum >= 0 && sum <= N);
        printf("%d\n", N - sum);
    }
    return 0;
}
