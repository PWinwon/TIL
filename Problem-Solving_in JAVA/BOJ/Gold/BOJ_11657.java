import java.io.*;
import java.util.*;


public class BOJ_11657 {
	static int N, M;
	static Edge[] edges;
	static long[] dist;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		edges = new Edge[M+1];
		dist = new long[N+1];
		
		for (int i = 0; i < N+1; i++) {
			dist[i] = Integer.MAX_VALUE;
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			edges[m] = new Edge(start, end, cost);
		}
		
		dist[1] = 0;
		
		for (int i = 1; i < N; i++) {
			for (int j = 0; j < M; j++) {
				Edge edge = edges[j];
				
				if (dist[edge.start] != Integer.MAX_VALUE && dist[edge.end] > dist[edge.start] + edge.cost) {
					dist[edge.end] = dist[edge.start] + edge.cost;
				}
			}
		}
		
		boolean flag = false;
		
		for (int i = 0; i < M; i++) {
			Edge edge = edges[i];
			if (dist[edge.start] != Integer.MAX_VALUE && dist[edge.end] > dist[edge.start] + edge.cost) {
				flag = true;
			}
		}
		
		if (flag) {
			System.out.println(-1);
		}
		else {
			for (int i = 2; i <= N; i++) {
				if (dist[i] == Integer.MAX_VALUE) System.out.println(-1);
				else System.out.println(dist[i]);
			}
		}

	}
	
	static class Edge {
		int start;
		int end;
		int cost;
		
		Edge(int s, int e, int c) {
			this.start = s;
			this.end = e;
			this.cost = c;
		}
	}

}
