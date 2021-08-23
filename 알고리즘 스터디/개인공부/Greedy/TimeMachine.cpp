#include<iostream>
#include<vector>
#include<map>

using namespace std;

int main() {
	long long n_node, n_edge;
	vector<long long> costs;
	vector<map<long long, long long>> edge;
	bool inf_loop = false;

	cin >> n_node >> n_edge;
	costs = vector<long long>(n_node, 5000001);
	edge = vector<map<long long, long long>>(n_node);

	for (long long i = 0, src, dst, cost; i < n_edge; i++) {
		scanf("%lld %lld %lld", &src, &dst, &cost);
		
		if (edge[src - 1].find(dst - 1) == edge[src - 1].end())
			edge[src - 1][dst - 1] = 5000001;

		edge[src - 1][dst - 1] = min(edge[src - 1][dst - 1], cost);
	}

	// ��������
	costs[0] = 0;	// ����� -> ����� : ��� 0
	for (long long i = 0; i < n_node - 1; i++) {
		for (long long cur_node = 0; cur_node < n_node; cur_node++) {
			if (costs[cur_node] != 5000001) {
				// ����ġ ����
				for (map<long long, long long>::iterator it = edge[cur_node].begin(); it != edge[cur_node].end(); it++)
					costs[it->first] = min(costs[it->first], costs[cur_node] + it->second);
			}
		}
	}

	// ���⼭ ������ �Ͼ�� ���� ���� ������ �����ϴ� ����
	for (long long cur_node = 0; cur_node < n_node; cur_node++) {
		if (costs[cur_node] != 5000001) {
			// ����ġ ����
			for (map<long long, long long>::iterator it = edge[cur_node].begin(); it != edge[cur_node].end(); it++) {
				if (costs[it->first] > costs[cur_node] + it->second) {
					inf_loop = true;
					goto collapse;
				}
			}
		}
	}

collapse:
	if (inf_loop)
		cout << -1 << "\n";
	else {
		// ��� ���
		for (int i = 1; i < n_node; i++) {
			if (costs[i] == 5000001)
				printf("-1\n");
			else
				printf("%lld\n", costs[i]);
		}
	}

	return 0;
}