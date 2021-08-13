#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	int n;
	long long answer = 0;
	vector<int> member;
	int diff, high, low;

	cin >> n;
	
	member = vector<int>(n);
	
	for (int i = 0; i < n; i++) {
		cin >> member[i];
	}

	sort(member.begin(), member.end());
	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			diff = -(member[i] + member[j]);
			high = upper_bound(member.begin() + i + 1, member.begin() + j, diff) - member.begin();
			low = lower_bound(member.begin() + i + 1, member.begin() + high, diff) - member.begin();
			answer += high - low;
		}
	}
	cout << answer << endl;

	return 0;
}