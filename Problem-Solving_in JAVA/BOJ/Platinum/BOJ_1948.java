import java.io.*;
import java.util.*;


public class BOJ_1948 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		ArrayList<Node>[] Map = new ArrayList[N+1];
		ArrayList<Node>[] MapRvs = new ArrayList[N+1];
		
		int[] indeg = new int [N+1];
//		int[] indegRvs = new int [N+1];
		
		int[] times = new int[N+1];
		
		for (int n = 0; n <= N; n++) {
			Map[n] = new ArrayList<>();
			MapRvs[n] = new ArrayList<>();
			indeg[n] = 0;
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());
			
			Map[s].add(new Node(e, time));
			MapRvs[e].add(new Node(s, time));
			indeg[e]++;
		}
		
		st = new StringTokenizer(br.readLine());
		
		int startNode = Integer.parseInt(st.nextToken());
		int endNode = Integer.parseInt(st.nextToken());
		
		ArrayDeque<Integer> que = new ArrayDeque<Integer>();
		que.add(startNode);
		
		while (!que.isEmpty()) {
			int now = que.pollFirst();
			
			for (Node next : Map[now]) {
				indeg[next.nextNode]--;
				times[next.nextNode] = Math.max(times[next.nextNode], times[now] + next.value);
				if (indeg[next.nextNode] == 0) {
					que.add(next.nextNode);
				}
			}
		}
		
		que = new ArrayDeque<Integer>();
		boolean[] visited = new boolean[N+1];
		int result = 0;

		que.add(endNode);
		visited[endNode] = true;		
		
		while (!que.isEmpty()) {
			int now = que.pollFirst();
			
			for (Node next : MapRvs[now]) {
//				if (visited[next.nextNode]) continue;
				if (times[next.nextNode] + next.value == times[now]) {
					result++;
					if (visited[next.nextNode] == false) {					
						visited[next.nextNode] = true;
						que.add(next.nextNode);
					}
				}
			}
		}
		
		System.out.println(times[endNode]);
		System.out.println(result);
		
//		for (int i = 1; i < N+1; i++) {
//			System.out.print(times[i]);
//		}
		
		
	}
	
	static class Node{
		int nextNode;
		int value;
		
		Node(int nextNode, int value) {
			this.nextNode = nextNode;
			this.value = value;
		}
	}

}
