#include<iostream>
#include<queue>
#include<vector>
#include<map>

using namespace std;

int main() {
	priority_queue<pair<int, int>> queue;	
	int n_city, n_edge, src, dst;
	pair<int, int> current;
	vector<int> cost;	// 출발지 -> i번째 도시 비용 저장
	vector<map<int, int>> path;		// 간선저장
	map<int, int>::iterator it;

	cin >> n_city >> n_edge;
	cost = vector<int>(n_city, 100000001);
	path = vector<map<int, int>>(n_city);

	for (int i = 0, _src, _dst, _cost; i < n_edge; i++) {
		scanf("%d %d %d", &_src, &_dst, &_cost);	// cin 쓰니까 시간초과 남
		
		// 요소가 없는 경우
		if (path[_src - 1].find(_dst - 1) == path[_src - 1].end()) {
			path[_src - 1][_dst - 1] = 100000001;
		}

		path[_src - 1][_dst - 1] = min(path[_src - 1][_dst - 1], _cost);
	}

	cin >> src >> dst;
	cost[src - 1] = 0;	// 자기자신 -> 자기자신 : 비용 0
	queue.push({cost[src - 1], src - 1});

	// 다익스트라
	while (!queue.empty()) {
		current = queue.top();
		queue.pop();

		for (map<int, int>::iterator it = path[current.second].begin(); it != path[current.second].end(); it++) {
			if (current.first + it->second < cost[it->first]) {
				cost[it->first] = current.first + it->second;
				queue.push({ cost[it->first], it->first });
			}
		}
	}

	cout << cost[dst - 1] << endl;

	return 0;
}