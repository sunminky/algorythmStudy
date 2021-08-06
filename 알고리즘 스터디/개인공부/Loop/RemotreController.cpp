// # https://www.acmicpc.net/problem/1107
#include<iostream>
#include<map>

using namespace std;

// 숫자의 자리수 반환
int int_length(int src) {
	int cnt = 0;

	do
	{
		cnt++;
		src /= 10;
	} while (src != 0);

	return cnt;
}

// # 현재 채널 중 고장난 버튼의 숫자가 들어가 있으면 False, 아니면 True
bool check(int src, map<int, bool> &broken) {
	int src_len = int_length(src);
	for (int i = 0; i < src_len; i++) {
		if (broken.find(src % 10) == broken.end()) {
			src /= 10;
			continue;
		}
		return false;
	}
	return true;
}

int main() {
	int target, n_broken, answer = 1000000, data;
	map<int, bool> broekn;
	int cnt, tmp;

	cin >> target;
	cin >> n_broken;
	
	for (int i = 0; i < n_broken; i++) {
		cin >> data;
		broekn[data] = true;
	}

	/*## 고장나지 않은 버튼으로 이루어진 채널 나올때 까지 목표로 하는 채널에서 1씩 빼기 ##*/
	cnt = 0;
	tmp = target;

	while (tmp > -1) {
		if (tmp == 100)
			break;

		//# 모든 숫자가 고장난 버튼이 아닌 경우는?
		if (check(tmp, broekn))
			break;

		tmp--;
		cnt++;
	}

	// # tmp가 -1인 경우는 체널이 0이 될 때까지 고장나지 않은 버튼으로 이루어진 채널을 찾지 못한 것
	if (tmp != -1) {
		// # 채널 번호 새로 누르는 것 보다 +, - 버튼 누르는게 더 나은 경우
		if (97 < tmp && tmp < 103)
			answer = min(answer, cnt + abs(100 - tmp));
		else
			// # - 버튼 누른 횟수 + 숫자 버튼 누른 횟수
			answer = min(answer, cnt + int_length(tmp));
	}

	/*## 고장나지 않은 버튼으로 이루어진 채널 나올때 까지 목표로 하는 채널에서 1씩 더하기 ##*/
	cnt = 0;
	tmp = target;

	while (tmp < 1000000) {
		if (tmp == 100)
			break;

		//# 모든 숫자가 고장난 버튼이 아닌 경우는?
		if (check(tmp, broekn))
			break;

		tmp++;
		cnt++;
	}

	// # tmp가 -1인 경우는 체널이 0이 될 때까지 고장나지 않은 버튼으로 이루어진 채널을 찾지 못한 것
	if (tmp != -1) {
		// # 채널 번호 새로 누르는 것 보다 +, - 버튼 누르는게 더 나은 경우
		if (97 < tmp && tmp < 103)
			answer = min(answer, cnt + abs(100 - tmp));
		else
			// # - 버튼 누른 횟수 + 숫자 버튼 누른 횟수
			answer = min(answer, cnt + int_length(tmp));
	}

	cout << answer << endl;

	return 0;
}