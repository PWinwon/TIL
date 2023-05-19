import java.io.*;
import java.util.*;


public class BOJ_1068 {
	
	static int N;
	
	static ArrayList<Integer>[] Map;
	static int[] parents;
	static boolean[] visited;
	
	static int answer = 0;
	static int start = 0;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		parents = new int[N];
		Map = new ArrayList[N];
		visited = new boolean[N];
		
		for (int i = 0; i < N; i++) {
			Map[i] = new ArrayList<Integer>();
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			int a = Integer.parseInt(st.nextToken());
			parents[i] = a;
			if (a == -1) start = i;
			else Map[a].add(i);
		}

		int dnode = Integer.parseInt(br.readLine());
		visited[dnode] = true;
		
		if (dnode != start) {
			visited[start] = true;
			myDFS(start);			
		}
				
		System.out.println(answer);
	}
	
	public static void myDFS(int now) {
		
		boolean flag = false;
		
		for (int next : Map[now]) {
			if (visited[next]) continue;
			visited[next] = true;
			flag = true;
			myDFS(next);
		}
		
		if (flag) return;
		answer++;
		return;
	}

}
