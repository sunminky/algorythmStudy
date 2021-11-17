// https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AW1l1s2KWn4DFARC&categoryId=AW1l1s2KWn4DFARC&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=4&&&&&&&&&&
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	int tc = 0, k = 0, max_exp = 1;
	long long target = 0LL, remain = 0LL;
	vector<pair<long, long>> memo;

	cin >> tc;
	memo.push_back(pair<long long, long long>({ 1LL, 0LL }));
	memo.push_back(pair<long long, long long>({2LL, 1LL}));

	for (int i = 1; i <= tc; i++) {
		cin >> k;

		if (memo.size() - 1 < k) {
			for (int j = memo.size() - 1; j < k; j++) {
				target = memo[j].first;
				remain = memo[j].second;

				memo.push_back(pair<long long, long long>(target + remain, target));
			}
		}

		target = memo[k].first;
		remain = memo[k].second;

		max_exp = max(k, max_exp);
		printf("#%d %lld %lld\n", i, target, remain);
	}

	return 0;
}