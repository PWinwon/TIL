import java.io.*;
import java.util.*;


public class BOJ_1717 {
	static int N;
	static int[] parents;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		parents = new int[N+1];
		
		for (int n = 0; n <= N; n++) {
			parents[n] = n;
		}
		
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int flag = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (flag == 0) {
				union(a, b);
			}
			else {
				if (find(b) == find(a)) {
					System.out.println("YES");
				}
				else {
					System.out.println("NO");
				}
			}
		}
	}
	
	public static void union(int a, int b) {
		a = find(a);
		b = find(b);
		
		if (a < b) {
			parents[b] = a;			
		}
		else {
			parents[a] = b;
		}
	}
	
	public static int find(int a) {
		if (a == parents[a]) {
			return a;
		}		
		return parents[a] = find(parents[a]);
	}

}
