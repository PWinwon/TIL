import java.io.*;
import java.util.*;


public class BOJ_1916 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		ArrayList<Node>[] Map = new ArrayList[N+1];
		int[] dist = new int[N+1];
		boolean[] visited = new boolean[N+1];
		
		for (int i = 0; i <= N; i++) {
			Map[i] = new ArrayList<Node>();
			dist[i] = Integer.MAX_VALUE;
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			
			Map[s].add(new Node(e, v));
		}
		
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		
		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		
		dist[start] = 0;
		pq.add(new Node(start, 0));
		
		while (!pq.isEmpty()) {
			Node now = pq.poll();
			if (visited[now.target]) continue;
			visited[now.target] = true;
			
			for (Node next : Map[now.target]) {
				if (dist[next.target] >= dist[now.target] + next.value) {
					dist[next.target] = dist[now.target] + next.value;
					pq.add(new Node(next.target, dist[next.target]));
				}
			}
		}
		
		System.out.println(dist[end]);

	}
	
	static class Node implements Comparable<Node>{
		int target;
		int value;
		
		Node(int target, int value) {
			this.target = target;
			this.value = value;
		}
		
		public int compareTo(Node n) {
			return this.value - n.value; 
		}
	}

}
