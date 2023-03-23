import java.io.*;
import java.util.*;


public class BOJ_11003 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		
		int[] lst = new int [N];
		
		for (int n = 0; n < N; n++) {
			lst[n] = Integer.parseInt(st.nextToken());
		}
		
		int[] D = new int [N];
		int d = 0;
		
		Deque<Node> deque = new ArrayDeque<>();
		
		Node temp = new Node(-1, -1);
		
		for (int i = 0; i < L; i++) {
			while (!deque.isEmpty() && deque.peekLast().value >= lst[i]) {
				deque.pollLast();
			}
			temp = new Node(lst[i], i);
			deque.addLast(temp);
			d = deque.peekFirst().value;
			D[i] = d;
		}
		
		for (int i = L; i < N; i++) {
			while (!deque.isEmpty() && deque.peekFirst().idx < i - L + 1) {
				deque.pollFirst();
			}
			while (!deque.isEmpty() && deque.peekLast().value >= lst[i]) {
				deque.pollLast();
			}
			temp = new Node(lst[i], i);
			deque.addLast(temp);
			d = deque.peekFirst().value;
			D[i] = d;
		}
		
		for (int i = 0; i < N; i++) {
			sb.append(D[i]).append(" ");
		}
		System.out.print(sb);
	}

	
	static class Node {
		public int value;
		public int idx;
		
		Node(int value, int idx) {
			this.value = value;
			this.idx = idx;
		}
	}
}
