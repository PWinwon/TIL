import java.io.*;
import java.util.*;


public class BOJ_11438 {
	static int N, kmax;
	static ArrayList<Integer>[] tree;
	static int[] depth;
	static int[][] parent;
	static boolean[] visited;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		int temp = 1;
		kmax = 0;
		
		while (temp <= N) {
			temp <<= 1;
			kmax++;
		}
		
		tree = new ArrayList[N+1];
		visited = new boolean[N+1];
		depth = new int[N+1];
		parent = new int[kmax+1][N+1];
		
		for (int i = 1; i <= N; i++) {
			tree[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			tree[a].add(b);
			tree[b].add(a);
		}
		
		myBFS(1);
		
		for (int k = 1; k <= kmax; k++) {
			for (int n = 1; n <= N; n++) {
				parent[k][n] = parent[k - 1][parent[k - 1][n]];
			}
		}
		
		int M = Integer.parseInt(br.readLine());
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			System.out.println(getLCA(a, b));
		}

	}
	
	public static int getLCA(int a, int b) {
		int ret = -1;
		
		if (depth[a] > depth[b]) {
			int temp = a;
			a = b;
			b = temp;
		}
		
		for (int k = kmax; k >= 0; k--) {
			if (Math.pow(2, k) <= depth[b] - depth[a]) {
				if (depth[a] <= depth[parent[k][b]]) {
					b = parent[k][b];
				}
			}
		}
		
		for (int k = kmax; k >= 0 && a != b; k--) {
			if (parent[k][a] != parent[k][b]) {
				a = parent[k][a];
				b = parent[k][b];
			}
		}
		
		ret = a;
		
		if (a != b) ret = parent[0][ret];
		
		return ret;
	}
	
	public static void myBFS(int root) {
		ArrayDeque<Integer> que = new ArrayDeque<Integer>();
		que.add(root);
		visited[root] = true;
		depth[root] = 0;
		
		while (!que.isEmpty()) {
			int now = que.pollFirst();
			for (int next : tree[now]) {
				if (visited[next]) continue;
				visited[next] = true;
				que.add(next);
				depth[next] = depth[now] + 1;
				parent[0][next] = now;
			}
		}
		
		
	}

}
