/* https://www.acmicpc.net/problem/2343 */
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main() {
	int n_lesson, n_cd;
	long long min_time, middle_time, max_time;
	long long acc_cnt, cd_cnt;
	vector<long long> lessons;

	cin >> n_lesson;
	cin >> n_cd;

	lessons = vector<long long>(n_lesson);

	for (int i = 0; i < lessons.size(); i++)
		cin >> lessons[i];

	min_time = lessons[max_element(lessons.begin(), lessons.end()) - lessons.begin()];
	max_time = 20000000001ULL;

	while(min_time < max_time){
		middle_time = (min_time + max_time) / 2;
		acc_cnt = 0;
		cd_cnt = 0;

		for (int i = 0; i < lessons.size(); i++) {
			if (acc_cnt - lessons[i] < 0) {
				acc_cnt = middle_time;
				cd_cnt++;
			}
			acc_cnt -= lessons[i];
		}

		if (cd_cnt <= n_cd)
			max_time = middle_time;
		else
			min_time = middle_time + 1;
	}

	cout << max_time << endl;

	return 0;
}