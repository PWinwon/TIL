import java.io.*;
import java.util.*;


public class BOJ_2252 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] indegree = new int [N+1];
		ArrayList<Integer> [] Map = new ArrayList[N+1];
		
		for (int i = 0; i < N+1; i++) {
			indegree[i] = 0;
			Map[i] = new ArrayList<Integer>();
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			Map[a].add(b);
			indegree[b]++;
		}
		
		ArrayDeque<Integer> que = new ArrayDeque<Integer>();
		
		for (int i = 1; i < N+1; i++) {
			if (indegree[i] == 0) {
				que.add(i);
			}
		}
		
		while (!que.isEmpty()) {
			int now = que.pollFirst();
			sb.append(now).append(" ");
			for (int x : Map[now]) {
				indegree[x]--;
				if (indegree[x] == 0) {
					que.add(x);
				}
			}
		}
		
		System.out.println(sb);
	}

}
