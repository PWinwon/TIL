import java.io.*;
import java.util.*;


public class BOJ_1854 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		ArrayList<Node>[] Map = new ArrayList[N+1];
		PriorityQueue<Integer>[] used = new PriorityQueue[N+1];
		
		Comparator<Integer> cp = new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return o1 < o2 ? 1 : -1;
			}
		};
		
		for (int n = 0; n <= N; n++) {
			Map[n] = new ArrayList<Node>();
			used[n] = new PriorityQueue<Integer>(K, cp);
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			Map[a].add(new Node(b, c));
		}
		
		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		pq.add(new Node(1, 0));
		used[1].add(0);
		
		while (!pq.isEmpty()) {
			Node now = pq.poll();
			for (Node next : Map[now.node]) {
				if (used[next.node].size() < K) {
					used[next.node].add(now.cost + next.cost);
					pq.add(new Node(next.node, now.cost+next.cost));
				}
				else if (used[next.node].peek() > now.cost + next.cost) {
					used[next.node].poll();
					used[next.node].add(now.cost + next.cost);
					pq.add(new Node(next.node, now.cost + next.cost));
				}
			}
		}
		
		for (int i = 1; i <= N; i++) {
			if (used[i].size() == K) System.out.println(used[i].peek());
			else System.out.println(-1);
		}

	}
	
	static class Node implements Comparable<Node> {
		int node;
		int cost;
		Node (int node, int cost) {
			this.node = node;
			this.cost = cost;
		}
		
		@Override
		public int compareTo(Node o) {
			return this.cost < o.cost ? -1 : 1;
		}
	}

}
