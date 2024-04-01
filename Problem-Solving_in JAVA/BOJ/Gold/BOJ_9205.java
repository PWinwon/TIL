import java.io.*;
import java.util.*;


public class BOJ_9205 {
	static int N;
	static boolean[] used;
	static Point[] points;
//	static Point start, end;
	static ArrayList<Integer>[] graph;
	static ArrayDeque<Integer> que;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < T; tc++) {
			N = Integer.parseInt(br.readLine());
			used = new boolean[N+2];
			points = new Point[N+2];
			graph = new ArrayList[N+2];
			
			// 0은 start, 1은 end
			for (int n = 0; n < N+2; n++) {
				st = new StringTokenizer(br.readLine());
				int y = Integer.parseInt(st.nextToken());
				int x = Integer.parseInt(st.nextToken());
				points[n] = new Point(y, x);
				graph[n] = new ArrayList<Integer>();
			}
			
			for (int n = 0; n < N+1; n++) {
				for (int m = n+1; m < N+2; m++) {
					// points[n]과 points[m]이 서로 연결되어있다면 서로 graph[n, m].add(n, m);
					if (myChk(n, m)) {
						graph[n].add(m);
						graph[m].add(n);
					}
				}
			}
			
			que = new ArrayDeque<>();
			que.add(0);
			boolean flag = false;
			
			while (!que.isEmpty()) {
				int now = que.pollFirst();
				
				if (now == N+1) {
					flag = true;
					break;
				}
				
				for (int x = 0; x < graph[now].size(); x++) {
					int next = graph[now].get(x);
					if (used[next]) continue;
					used[next] = true;
					que.add(next);
				}
			}
			
			if (flag) System.out.println("happy");
			else System.out.println("sad");
		}

	}
	

	private static boolean myChk(int n, int m) {
		// TODO Auto-generated method stub
		Point s = points[n];
		Point e = points[m];
		if (Math.abs(s.y - e.y) + Math.abs(s.x - e.x) <= 1000) {
			return true;
		}
		return false;
	}


	static class Point {
		int y;
		int x;
//		int cnt;
		Point(int y, int x) {
			this.y = y;
			this.x = x;
//			this.cnt = cnt;
		}
	}
}
