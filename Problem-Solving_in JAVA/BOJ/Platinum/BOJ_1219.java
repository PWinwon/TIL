import java.io.*;
import java.util.*;


public class Main {
	static int N, S, E, M;
	
	// 거리 저장할 배열
	static long[] dist;
	
	// 도로 정보 저장할 배열
	static Edge[] edges;
	
	// 각 도시에서 얻을 이득을 저장할 배열
	static long[] moneys;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		dist = new long[N];
		edges = new Edge[M];
		moneys = new long[N];
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			edges[m] = new Edge(s, e, c);
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int n = 0; n < N; n++) {
			dist[n] = Long.MIN_VALUE;
			moneys[n] = Long.parseLong(st.nextToken());
		}
		
		dist[S] = moneys[S];
		
		for (int i = 0; i < N + 101; i++) {
			for (int j = 0; j < M; j++) {
				Edge edge = edges[j];
				if (dist[edge.start] == Long.MIN_VALUE) continue;
				else if (dist[edge.start] == Long.MAX_VALUE)	dist[edge.end] = Long.MAX_VALUE;
				else if (dist[edge.end] < dist[edge.start] + moneys[edge.end] - edge.cost) {
					dist[edge.end] = dist[edge.start] + moneys[edge.end] - edge.cost;
					if (i >= N-1) dist[edge.end] = Long.MAX_VALUE;
				}
			}
		}
		
		if (dist[E] == Long.MIN_VALUE) System.out.println("gg");
		else if (dist[E] == Long.MAX_VALUE) System.out.println("Gee");
		else System.out.println(dist[E]);

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