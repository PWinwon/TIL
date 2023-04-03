import java.io.*;
import java.util.*;


public class BOJ_1167 {

	static int V;
	
	static ArrayList<Edge>[] myMap;
	static int[] distance;
	static boolean[] used;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
				
		V = Integer.parseInt(br.readLine());
		
		myMap = new ArrayList [V+1];
		
		for (int v = 1; v <= V; v++) {
			st = new StringTokenizer(br.readLine());
			int nodeNum = Integer.parseInt(st.nextToken());
			
			myMap[nodeNum] = new ArrayList<Edge>();
			
			while (true) {
				int E = Integer.parseInt(st.nextToken());
				if (E == -1) {
					break;
				}
				int val = Integer.parseInt(st.nextToken());
				
				myMap[nodeNum].add(new Edge(E, val));
			}
		}
		
		myBFS(1);
		
		int max_node = 1;
		
		for (int i = 2; i <= V; i++) {
			if (distance[max_node] < distance[i]) {
				max_node = i;
			}
		}
		
		myBFS(max_node);
		
		int answer = -1;
		
		for (int i = 1; i <= V; i++) {
			if (answer < distance[i]) {
				answer = distance[i];
			}
		}
		
		System.out.println(answer);
	}
	
	private static void myBFS(int start) {
		Deque<Integer> deque = new ArrayDeque<Integer>();
		used = new boolean [V+1];
		distance = new int [V+1];
		
		deque.offer(start);
		used[start] = true;
		
//		System.out.println("start : " + start);
		
		while (!deque.isEmpty()) {
			int now = deque.pollFirst();
//			System.out.println(now);
			for (Edge e : myMap[now]) {
				if (used[e.endNode]) {
					continue;
				}
				deque.add(e.endNode);
				distance[e.endNode] = distance[now] + e.value;
				used[e.endNode] = true;
			}
		}
	}
	
	static class Edge {
		int endNode;
		int value;
		
		public Edge(int endNode, int value) {
			this.endNode = endNode;
			this.value = value;
		}
	}
}
