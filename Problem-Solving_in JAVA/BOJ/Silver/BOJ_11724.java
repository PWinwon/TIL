import java.io.*;
import java.util.*;


public class BOJ_11724 {
	
	static ArrayList<Integer>[] A;
	static boolean used[];

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int V = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		A = new ArrayList [V+1];
		used = new boolean [V+1];
		
		for (int v = 1; v <= V; v++) {
			A[v] = new ArrayList<Integer>();
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			A[s].add(e);
			A[e].add(s);
		}
		
		int answer = 0;
		
		for (int i = 1; i < V+1; i++) {
			if (used[i]) {
				continue;
			}
			answer++;
			myDFS(i);
		}
		
		System.out.println(answer);

	}
	
	public static void myDFS(int a) {
		if (used[a]) {
			return;
		}
		
		used[a] = true;
		for (int i : A[a]) {
			if (used[i]) {
				continue;
			}
			myDFS(i);
		}
	}

}
