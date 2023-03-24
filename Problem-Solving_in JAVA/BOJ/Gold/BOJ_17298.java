import java.io.*;
import java.util.*;

public class BOJ_17298 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] lst = new int [N];
		
		for (int i = 0; i < N; i++) {
			lst[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] answer = new int [N];
		
		Deque<Integer> stck = new ArrayDeque<>();
		
		for (int i = 0; i < N; i++) {
			if (stck.isEmpty()) {
				stck.offerLast(i);
				continue;
			}
			
			else if (lst[stck.peekLast()] >= lst[i]) {
				stck.offerLast(i);			
			}
			else {
				while (!stck.isEmpty() && lst[stck.peekLast()] < lst[i]) {
					answer[stck.peekLast()] = lst[i];
					stck.pollLast();
				}
				stck.offerLast(i);
			}
			
		}
		
		while (!stck.isEmpty()) {
			answer[stck.pollLast()] = -1;
		}
		
		for (int n = 0; n < N; n++) {
			sb.append(answer[n]).append(" ");
		}
		System.out.print(sb);
	}

}
