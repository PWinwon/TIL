import java.io.*;
import java.util.*;


public class BOJ_5972 {
	static int N, M;
	static ArrayList<Edge>[] Map;
	static int[] dist;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		Map = new ArrayList[N+1];
		dist = new int[N+1];
		
		for (int i = 0; i < N+1; i++) {
			Map[i] = new ArrayList<Edge>();
			dist[i] = Integer.MAX_VALUE;
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			Map[a].add(new Edge(b, c));
			Map[b].add(new Edge(a, c));
		}
		
		PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
		pq.add(new Edge(1, 0));
		dist[1] = 0;
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			for (Edge next : Map[now.target]) {
				if (now.cost + next.cost < dist[next.target]) {
					dist[next.target] = now.cost + next.cost;
					pq.add(new Edge(next.target, now.cost + next.cost));
				}
			}
		}
		
		System.out.println(dist[N]);

	}
	
//	static class Edge{
//		int target;
//		int cost;
//		
//		Edge(int e, int c) {
//			this.target = e;
//			this.cost = c;
//		}
//	}
	
	static class Edge implements Comparable<Edge> {
//		int start;
		int target;
		int cost;
		
		Edge(int e, int c) {
//			this.start = s;
			this.target = e;
			this.cost = c;
		}
		
		@Override
		public int compareTo(Edge o) {
			// TODO Auto-generated method stub
			return this.cost - o.cost;
		}
	}

}
