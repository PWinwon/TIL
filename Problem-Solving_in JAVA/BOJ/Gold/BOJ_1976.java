import java.io.*;
import java.util.*;


public class BOJ_1976 {
	static int N;
	
	static int[] parents;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		parents = new int [N+1];
		
		for (int i = 0; i <= N; i++) {
			parents[i] = i;
		}
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				int a = Integer.parseInt(st.nextToken());
				if (a == 1) {
					union(i, j);
				}
			}
		}
		
		st = new StringTokenizer(br.readLine());
		
		int answer = find(parents[Integer.parseInt(st.nextToken())]);
		boolean flag = false;
		
//		System.out.println(answer);
		
		for (int i = 1; i < M; i++) {
			if (answer != find(parents[Integer.parseInt(st.nextToken())])) {
				flag = true;
				break;
			}
//			System.out.println(parents[i]);
		}
		
		if (flag) {
			System.out.println("NO");
		}
		else {
			System.out.println("YES");
		}
	}
	
	public static int find(int x) {
		if (x == parents[x]) {
			return x;
		}
		parents[x] = find(parents[x]);
		return parents[x];
	}

	
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if (x < y) {
			parents[y] = x;
		}
		else {
			parents[x] = y;
		}
		
	}
}
