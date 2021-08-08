#include<iostream>
#include<deque>

using namespace std;

struct queue_data{
	int cost;
	int pierce_cnt;
	int x_pos;
	int y_pos;

	queue_data(int cost, int pierce_cnt, int x_pos, int y_pos)
		:cost(cost), pierce_cnt(pierce_cnt), x_pos(x_pos), y_pos(y_pos){
	}
};

int main() {
	int height, width, pierce_cnt, answer = -1;
	string* field;
	bool*** visited;	//visited[y좌표][x좌표][남은 관통횟수]
	deque<queue_data> queue;
	const int movement[4][2] = { {1, 0},	// 우로 이동
								{-1, 0},	// 좌로 이동
								{0, 1},		// 위로 이동
								{0, -1}, };	// 아래로 이동
	int tmp = 0, tmp_x, tmp_y;

	cin >> height >> width >> pierce_cnt;

	field = new string[height];
	for(int x = 0; x < height; x++) {
		cin >> field[x];
	}

	visited = new bool** [height];
	for (int x = 0; x < height; x++)
	{
		visited[x] = new bool* [width];
		for (int y = 0; y < width; y++)
		{
			tmp = pierce_cnt + 1;
			visited[x][y] = new bool[tmp];
			for (int z = 0; z < tmp; z++) {
				visited[x][y][z] = false;
			}
		}
	}

	queue.push_back(queue_data(1, pierce_cnt, 0, 0));	// #시작지점을 큐에 넣음, (비용, 남은 관통횟수, (x좌표, y좌표))

	while (!queue.empty())
	{
		queue_data cur_data = queue.front();
		queue.pop_front();

		if ((cur_data.x_pos == width - 1) && (cur_data.y_pos == height - 1)) {
			answer = cur_data.cost;
			break;
		}

		for (int i = 0; i < 4; i++) {
			tmp_x = cur_data.x_pos + movement[i][0];
			tmp_y = cur_data.y_pos + movement[i][1];

			// # 바운더리
			if (-1 < tmp_x && tmp_x < width && -1 < tmp_y && tmp_y < height) {
				// # 벽을 부순 경우
				if (field[tmp_y][tmp_x] == '1' && cur_data.pierce_cnt > 0) {
					// # 비용 갱신
					if (!visited[tmp_y][tmp_x][cur_data.pierce_cnt]) {
						visited[tmp_y][tmp_x][cur_data.pierce_cnt] = true;
						queue.push_back(queue_data(cur_data.cost + 1, cur_data.pierce_cnt - 1, tmp_x, tmp_y));
					}
				}
				else if (field[tmp_y][tmp_x] == '0') {
					// # 비용 갱신
					if (!visited[tmp_y][tmp_x][cur_data.pierce_cnt]) {
						visited[tmp_y][tmp_x][cur_data.pierce_cnt] = true;
						queue.push_back(queue_data(cur_data.cost + 1, cur_data.pierce_cnt, tmp_x, tmp_y));
					}
				}
			}
		}
	}
	
	cout << answer << endl;

	return 0;
}