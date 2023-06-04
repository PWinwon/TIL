import java.io.*;
import java.util.*;


public class BOJ_0604 {
	static int N;
	static int[] parents;
	static PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		parents = new int [N+1];
		
		for (int i = 0; i <= N; i++) {
			parents[i] = i;
		}
		
		int M = Integer.parseInt(br.readLine());
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			pq.add(new Edge(s, e, c));
		}
		
		int answer = 0;
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			if (find(now.start) != find(now.end)) {
				answer += now.cost;
				union(now.start, now.end);
			}
		}
		
		System.out.println(answer);

	}
	
	public static void union(int x, int y) {
		x = parents[x];
		y = parents[y];
		
		if (x != y) {
			parents[y] = x;
		}
	}
	
	public static int find(int x) {
		if (x == parents[x]) {
			return x;
		}
		
		return parents[x] = find(parents[x]);
	}

}

class Edge implements Comparable<Edge>{
	int start;
	int end;
	int cost;
	
	Edge(int s, int e, int c) {
		this.start = s;
		this.end = e;
		this.cost = c;
	}
	
	@Override
	public int compareTo(Edge o) {
		return this.cost - o.cost;
	}
}
