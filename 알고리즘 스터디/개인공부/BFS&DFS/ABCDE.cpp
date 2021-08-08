#include<iostream>
#include<vector>
#include<cstring>

using namespace std;


void dig(vector<int> people[], int n_people, bool* visited, int cur_node, int remain) {
	vector<int>::iterator it;

	if (remain == 0) {
		cout << 1 << endl;
		exit(0);
	}

	visited[cur_node] = true;
	for (it = people[cur_node].begin(); it != people[cur_node].end(); it++) {
		if (!visited[*it]) {
			dig(people, n_people, visited, *it, remain - 1);
		}
	}
	visited[cur_node] = false;
}


int main() {
	int n_people, n_line, answer = 0;
	int src, dst;
	vector<int>* people;
	bool *visited;

	cin >> n_people >> n_line;
	people = new vector<int>[n_people];
	visited = new bool[n_people];

	for (int i = 0; i < n_line; i++) {
		cin >> src >> dst;
		people[src].push_back(dst);
		people[dst].push_back(src);
	}

	for (int i = 0; i < n_people; i++) {
		memset(visited, false, n_people * sizeof(bool));
		dig(people, n_people, visited, i, 4);
	}

	cout << answer << endl;

	return 0;
}