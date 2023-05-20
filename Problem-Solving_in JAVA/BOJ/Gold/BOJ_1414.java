import java.io.*;
import java.util.*;


public class BOJ_1414 {
	
	static int N;
	static PriorityQueue<Edge> pq;
	static int[] parents;

	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		pq = new PriorityQueue<Edge>();
		
		int totalL = 0;
		
		for (int i = 0; i < N; i++) {
			char[] temp = br.readLine().toCharArray();
			for (int j = 0; j < N; j++) {
				char c = temp[j];
				int l = 0;
				if ('a' <= c && c <= 'z') l += c - 'a' + 1;
				else if ('A' <= c && c <= 'Z') l += c - 'A' + 27;
				totalL += l;
				if (i != j && l != 0) pq.add(new Edge(i, j, l));
			}
		}
		
		parents = new int[N];
		
		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}
		
		int edgeCnt = 0;
		int answer = 0;
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			if (find(now.start) != find(now.end)) {
				union(now.start, now.end);
				edgeCnt++;
				answer += now.cost;
			}
		}
		
		if (edgeCnt == N - 1) System.out.println(totalL - answer);
		else System.out.println(-1);
	}
	
	public static int find(int x) {
		if (x == parents[x]) return x;		
		return parents[x] = find(parents[x]);
	}
	
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if (x < y) parents[y] = x;
		else parents[x] = y;
	}
	
	static class Edge implements Comparable<Edge> {
		int start;
		int end;
		int cost;
		
		Edge (int s, int e, int c) {
			this.start = s;
			this.end = e;
			this.cost = c;
		}
		@Override
		public int compareTo (Edge o) {
			return this.cost - o.cost;
		}
	}

}
