import java.io.*;
import java.util.*;


public class BOJ_18352 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		ArrayList<Integer>[] Map = new ArrayList[N+1];
		int[] visited = new int [N+1];
		
		for (int i = 1; i <= N; i++) {
			Map[i] = new ArrayList<Integer>();
			visited[i] = -1;
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			Map[a].add(b);
		}
		
		Deque<Integer> que = new ArrayDeque<Integer>();
		que.add(X);
		visited[X]++;
		
		while (!que.isEmpty()) {
			int now = que.pollFirst();
			for (int i : Map[now]) {
				if (visited[i] == -1) {
					visited[i] = visited[now] + 1;
					que.add(i);
				}
			}
		}
		
		boolean flag = false;
		
		for (int i = 1; i < N+1; i++) {
			if (visited[i] == K) {
				flag = true;
				System.out.println(i);
			}
		}
		
		if (!flag) {
			System.out.println(-1);
		}
	}

}
