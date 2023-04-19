import java.io.*;
import java.util.*;


public class BOJ_1707 {
	
	static int N;
	static int M;
	
	static ArrayList<Integer>[] Map;
	static int[] visited;
	
	static boolean res;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			Map = new ArrayList[N+1];
			visited = new int[N+1];
			
			for (int n = 1; n <= N; n++) {
				Map[n] = new ArrayList<Integer>();
				visited[n] = 0;
			}
			
			for (int m = 0; m < M; m++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				Map[a].add(b);
				Map[b].add(a);
			}
			res = false;
			
			for (int i = 1; i <= N; i++) {
				if (res) {
					break;
				}
				
				if (visited[i] == 0) {
					visited[i] = 1;
					myDFS(i);
				}
			}
			
			if (res) {
				System.out.println("NO");
			}
			else {
				System.out.println("YES");
			}
		}
		
		
	}
	
	public static void myDFS(int node) {
		if (res) {
			return;
		}
		
		for (int next: Map[node]) {
			if (visited[next] == 0) {
				visited[next] = visited[node] * -1;
				myDFS(next);
			}
			else {
				if (visited[next] == visited[node]) {
					res = true;
					return;
				}
			}
		}
		return;
	}

}
