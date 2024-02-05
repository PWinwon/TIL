import java.io.*;
import java.util.*;


public class BOJ_1446 {
	static int N, D;
	static PriorityQueue<Road> pq;
	static int[] dist;
	static Road[] graph;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		
		dist = new int[D+1];
		graph = new Road[N];
		
		for (int i = 0; i < D+1; i++) {
			dist[i] = i;
		}
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			graph[i] = new Road(s, e, w);
		}
		
		dijkstra(0);
		System.out.println(dist[D]);

	}

	private static void dijkstra(int i) {
		// TODO Auto-generated method stub
		pq = new PriorityQueue<>();
		
		pq.offer(new Road(i, 0, 0));
		dist[i] = 0;
		
		while(!pq.isEmpty()) {
			Road road = pq.poll();
			int destination = road.e;
			boolean flag = false;
			
			for (Road r : graph) {
				if (r.s >= destination) {
					if (r.e > D) continue;
					
					int temp = r.s - destination;
					flag = true;
					if (dist[r.e] > dist[destination] + r.w + temp) {
						dist[r.e] = dist[destination] + r.w + temp;
						pq.offer(new Road(destination, r.e, dist[r.e]));
					}
				}
			}
			
			dist[D] = Math.min(dist[destination] + D - destination, dist[D]);
		}
		
	}

}


class Road implements Comparable<Road> {
	int s;
	int e;
	int w;
	
	Road(int s, int e, int w) {
		this.s = s;
		this.e = e;
		this.w = w;
	}
	
	@Override
	public int compareTo(Road r) {
		return this.w - r.w;
	}
}
