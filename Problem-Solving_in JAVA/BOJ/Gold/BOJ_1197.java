import java.io.*;
import java.util.*;


public class BOJ_1197 {
	static int V, E;
	
	static int[] parents;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		
		parents = new int[V+1];
		
		for (int i = 0; i < V+1; i++) {
			parents[i] = i;
		}
		
		PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
		
		for (int e = 0; e < E; e++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			pq.add(new Edge(a, b, c));
		}
		
		int answer = 0;
		int cnt = 0;
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			if (find(now.s) == find(now.e)) continue;
			union(now.s, now.e);
			cnt += 1;
			answer += now.c;
			if (cnt == V) break;
		}
		
		System.out.println(answer);

	}

	static public int find(int x) {
		if (x == parents[x]) return x;
		parents[x] = find(parents[x]);
		return parents[x];		
	}
	
	static public void union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if (x > y) parents[x] = y;
		else parents[y] = x;
	}
	
	static class Edge implements Comparable<Edge> {
		int s;
		int e;
		int c;
		
		Edge(int s, int e, int c) {
			this.s = s;
			this.e = e;
			this.c = c;
		}
		
		@Override
		public int compareTo(Edge o) {
			return this.c - o.c;
		}
	}
}
