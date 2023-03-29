import java.io.*;
import java.util.*;


public class BOJ_2178 {
	static int[][] myMap;
	static boolean[][] used;
	
	static int N;
	static int M;
	
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		myMap = new int [N][M];
		used = new boolean [N][M];
		
		for (int n = 0; n < N; n++) {
			st = new StringTokenizer(br.readLine());
			String temp = st.nextToken();
			for (int m = 0; m < M; m++) {
				myMap[n][m] = Integer.parseInt(temp.substring(m, m+1));
			}
		}
		
		int answer = myBFS(0, 0);
		System.out.println(answer);
	}
	
	public static int myBFS(int r, int c) {
		Deque<int[]> deque = new ArrayDeque<>();
		used[r][c] = true;
		deque.offerLast(new int[] {r, c, 1});
		
		while (!deque.isEmpty()) {
			int now[] = deque.pollFirst();
			if (now[0] == N-1 && now[1] == M-1) {
				return now[2];
			}
			for (int i = 0; i < 4; i++) {
				int yr = now[0] + dr[i];
				int xr = now[1] + dc[i];
				if (yr < 0 || yr >= N || xr < 0 || xr >= M) {
					continue;
				}
				if (used[yr][xr]) {
					continue;
				}
				if (myMap[yr][xr] == 0) {
					continue;
				}
				used[yr][xr] = true;
				deque.offerLast(new int[] {yr, xr, now[2] + 1});
			}
		}
		return -1;
		
		
//		Deque<Node> deque = new ArrayDeque<>();
//		deque.offerLast(new Node(r, c, 0));
//		used[r][c] = true;
//		int ret = 0;
//		
//		while (!deque.isEmpty()) {
//			Node node = deque.pollFirst();
//		}
//		
	}
	
//	static class Node {
//		public int r;
//		public int c;
//		public int cnt;
//		
//		Node(int r, int c, int cnt) {
//			this.r = r;
//			this.c = c;
//			this.cnt = cnt;
//		}
//	}

}
