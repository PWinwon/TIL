import java.io.*;
import java.util.*;

public class BOJ_2493 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		ArrayDeque<Node> que = new ArrayDeque<Node>();
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 1; i < N+1; i++) {
			int h = Integer.parseInt(st.nextToken());
			
			if (que.isEmpty()) {
				System.out.print("0 ");
				que.add(new Node(i, h));
			}
			else {
				while (true) {
					if (que.isEmpty()) {
						System.out.print("0 ");
						que.add(new Node(i, h));
						break;
					}
					
					Node np = que.peekLast();
					
					if (np.cost > h) {
						System.out.print(np.idx + " ");
						que.add(new Node(i, h));
						break;
					}
					else {
						que.pollLast();
					}
				}
			}
		}
		

	}
	
	static class Node {
		int idx;
		int cost;
		
		Node(int idx, int cost) {
			this.idx = idx;
			this.cost = cost;
		}
	}

}
