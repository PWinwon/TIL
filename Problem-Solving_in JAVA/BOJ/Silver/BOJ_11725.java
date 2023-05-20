import java.io.*;
import java.util.*;


public class BOJ_11725 {
	static int N;
	static int[] answer;
	
	static int[] visited;
	static ArrayList<Integer>[] tree;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		visited = new int [N+1];
		tree = new ArrayList[N+1];
		
		for (int i = 0; i < N+1; i++) {
			tree[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			tree[a].add(b);
			tree[b].add(a);
		}
		
		visited[1] = 1;
		myDFS(1);
		for (int i = 2; i < N+1; i++) {
			System.out.println(visited[i]);
		}
	}
	
	public static void myDFS(int num) {
		for (int next : tree[num]) {
			if (visited[next] != 0) continue;
			visited[next] = num;
			myDFS(next);
		}
	}

}
