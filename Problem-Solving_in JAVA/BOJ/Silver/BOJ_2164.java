import java.io.*;
import java.util.*;

public class BOJ_2164 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		Deque<Integer> deque = new ArrayDeque<>();
		
		for (int i = 1; i < N+1; i++) {
			deque.offerLast(i);
		}
		
		int answer = -1;
		int temp = -1;
		boolean flag = true;
		
		while (!deque.isEmpty()) {
			if (flag) {
				answer = deque.pollFirst();
				flag = false;
			}
			else {
				temp = deque.pollFirst();
				deque.offerLast(temp);
				flag = true;
			}
		}
		
		System.out.print(answer);
	}

}
