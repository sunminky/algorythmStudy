package week10;

public class Unionfind {
    static int getParent(int parent[], int x) {
        if(parent[x] == x) return x;
        return parent[x] = getParent(parent, parent[x]);
    }

    // 각 부모 노드를 합칩니다.
    static void unionParent(int parent[], int a, int b) {
        a = getParent(parent, a);
        b = getParent(parent, b);
        if(a < b) parent[b] = a;
        else parent[a] = b;
    }

    // 같은 부모 노드를 가지는지 확인합니다.
    static int findParent(int parent[], int a, int b) {
        a = getParent(parent, a);
        b = getParent(parent, b);
        if(a == b) return 1;
        else return 0;
    }

    public static void main(String[] args) {
        int parent[] = new int[11];
        for(int i = 1; i <= 10; i++) {
            parent[i] = i;
        }
        unionParent(parent, 1, 2);
        unionParent(parent, 2, 3);
        unionParent(parent, 3, 4);
        unionParent(parent, 5, 6);
        unionParent(parent, 6, 7);
        unionParent(parent, 7, 8);
        System.out.printf("1과 5는 연결되어있나요? %d\n", findParent(parent, 1, 5));
        for(int i = 1; i <= 10; i++) {
            System.out.print(parent[i] + " ");
        }
        System.out.println();
        unionParent(parent, 1, 6);
        System.out.printf("1과 5는 연결되어있나요? %d\n", findParent(parent, 1, 5));
        for(int i = 1; i <= 10; i++) {
            System.out.print(parent[i] + " ");
        }
        System.out.println();
    }
}
