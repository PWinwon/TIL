import java.io.*;
import java.util.*;


public class BOJ_1753 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		int K = Integer.parseInt(br.readLine());
		
		ArrayList<Node>[] Map = new ArrayList[V+1];
		int[] used = new int[V+1];
		boolean[] visited = new boolean[V+1];
		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		
		for (int v = 0; v <= V; v++) {
			Map[v] = new ArrayList<Node>();
			used[v] = Integer.MAX_VALUE;
		}
		
		for (int e = 0; e < E; e++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int val = Integer.parseInt(st.nextToken());
			
			Map[start].add(new Node(end, val));
		}
		
		pq.add(new Node(K, 0));
		used[K] = 0;
		
		while (!pq.isEmpty()) {
			Node now = pq.poll();
			if (visited[now.target]) continue;
			visited[now.target] = true;
			for (Node next : Map[now.target]) {
				if (used[next.target] <= used[now.target] + next.value) continue;
				used[next.target] = used[now.target] + next.value;
				pq.add(new Node(next.target, used[next.target]));
			}
		}
		
		for (int i = 1; i <= V; i++) {
			if (used[i] != Integer.MAX_VALUE) System.out.println(used[i]);
			else System.out.println("INF");
		}
		
	}
	
	static class Node implements Comparable<Node>{
		int target;
		int value;
		
		Node(int target, int value) {
			this.target = target;
			this.value = value;
		}
		public int compareTo(Node n) {
			if (this.value > n.value) return 1;
			return -1;
		}
	}
	

}
