#include<iostream>
#include<set>
#include<algorithm>
#include<vector>

using namespace std;

int main() {
	int n_marvel;
	int data, seq = 0;
	set<long long> *position;
	set<long long> speed;
	long long* answer;

	cin >> n_marvel;
	answer = new long long[n_marvel];
	position = new set<long long>[n_marvel + 1];

	for (int i = 0; i < n_marvel + 1; i++) {
		for (int j = 0; j < n_marvel; j++) {
			cin >> data;
			position[i].insert(data);
		}
	}

	for (long long src : position[0])
		for (long long dst : position[n_marvel + 1 - 1])
			if ((dst - src) % n_marvel == 0)
				speed.insert((dst - src) / n_marvel);

	for (set<long long>::iterator src = position[0].begin(); src != position[0].end();src++) {
		for (long long velocity : speed) {
			bool break_flag = false;
			for (int i = 0; i < n_marvel + 1; i++) {
				if (position[i].find(*src + velocity * i) != position[i].end())
					continue;
				break_flag = true;
				break;
			}
			if (!break_flag) {
				answer[seq] = velocity;
				break;
			}
		}
		seq++;
	}

	seq = 0;
	for (set<long long>::iterator src = position[0].begin(); src != position[0].end(); src++)
		cout << *src << " " << answer[seq++] << endl;

	return 0;
}