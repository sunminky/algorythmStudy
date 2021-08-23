#include<iostream>
#include<vector>

using namespace std;

int main() {
	int n_city, n_bus;
	vector<vector<int>> costs;

	cin >> n_city >> n_bus;
	costs = vector<vector<int>>(n_city, vector<int>(n_city, 10000001));

	for (int i = 0; i < n_city; i++)
		costs[i][i] = 0;

	for (int i = 0, src, dst, cost; i < n_bus; i++) {
		scanf("%d %d %d", &src, &dst, &cost);
		costs[src - 1][dst - 1] = min(costs[src - 1][dst - 1], cost);
	}

	// �÷��̵� �ͼ�
	for (int passby = 0; passby < n_city; passby++) {	// ��ġ�� ���
		for (int row = 0; row < n_city; row++) {
			for (int col = 0; col < n_city; col++) {
				// �ٸ��� ���İ��°� �� ������ ����
				costs[row][col] = min(costs[row][passby] + costs[passby][col], costs[row][col]);
			}
		}
	}

	for (int row = 0; row < n_city; row++) {
		for (int col = 0; col < n_city; col++) {
			if (costs[row][col] == 10000001)
				printf("0 ");
			else
				printf("%d ", costs[row][col]);
		}
		printf("\n");
	}

	return 0;
}