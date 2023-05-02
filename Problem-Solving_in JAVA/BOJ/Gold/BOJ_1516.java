import java.io.*;
import java.util.*;


public class BOJ_1516 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		// 각 건물을 짓는데 걸리는 시간을 저장하는 time
		// 각 건물의 우선적으로 건축되어야 하는 건물을 저장하는 Map
		// 위상 정렬에 필요한 indeg
		int[] times = new int[N+1];
		int[] indeg = new int[N+1];
		ArrayList<Integer>[] Map = new ArrayList[N+1];
		
		for (int n = 0; n < N+1; n++) {
			times[n] = 0;
			indeg[n] = 0;
			Map[n] = new ArrayList<>();
		}
		
		for (int n = 1; n <= N; n++) {
			st = new StringTokenizer(br.readLine());
			times[n] = Integer.parseInt(st.nextToken());
			while (true) {
				int a = Integer.parseInt(st.nextToken());
				if (a == -1) break;
				Map[a].add(n);
				indeg[n]++;
			}
		}
		
		ArrayDeque<Integer> que = new ArrayDeque<>();
		for (int n = 1; n <= N; n++) {
			if (indeg[n] == 0) que.add(n);
		}
		
		int[] answer = new int[N+1];
		
		while (!que.isEmpty()) {
			int now = que.pollFirst();
			for (int next : Map[now]) {
				indeg[next]--;
				
				answer[next] = Math.max(answer[next], answer[now] + times[now]);
				if (indeg[next] == 0) {
					que.add(next);
				}
			}
		}
		
		for (int i = 1; i <= N; i++) {
			System.out.println(times[i] + answer[i]);
		}
		
	}

}
