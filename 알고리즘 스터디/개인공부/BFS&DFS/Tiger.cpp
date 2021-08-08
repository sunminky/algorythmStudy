#include<iostream>
#include<vector>
#include<stack>

using namespace std;


bool dig(const vector<vector<int>> &cake, stack<int> &answer, const int cur_idx, volatile const int prev_idx, const int prev_cake) {
	// 기저조건
	if (cur_idx == prev_idx) {
		if (prev_cake != cake[prev_idx][0]) {
			return true;
		}
		return false;
	}

	for (vector<int>::const_iterator it = cake[cur_idx].begin(); it != cake[cur_idx].end(); it++) {
		if (*it == prev_cake)
			continue;
		if (dig(cake, answer, cur_idx + 1, prev_idx, *it)) {
			answer.push(*it);
			return true;
		}
	}

	return false;
}


int main() {
	vector<vector<int>> cake;
	int n_day, n_cake, prev_single;
	stack<int> answer;
	bool success = true;

	cin >> n_day;

	for (int i = 0, tmp; i < n_day; i++) {
		cin >> tmp;
		vector<int> tmp_vector;
		for (int j = 0, data; j < tmp; j++) {
			cin >> data;
			tmp_vector.push_back(data);
		}
		cake.push_back(tmp_vector);
	}

	prev_single = cake.size();
	cake.push_back(vector<int>({-2}));

	for (int i = cake.size() - 2; i > -1; i--) {
		// # 떡이 하나밖에 없음
		if (cake[i].size() == 1 || i == 0) {
			// # 현재위치 ~ 이전 하나밖에 없는 위치까지 도달가능한지 체크
			success = dig(cake, answer, i, prev_single, -1);
			prev_single = i;
			if (!success)
				break;
		}
	}

	if (success) {
		while (!answer.empty())
		{
			cout << answer.top() << endl;
			answer.pop();
		}
	}
	else
		cout << -1 << endl;

	return 0;
}