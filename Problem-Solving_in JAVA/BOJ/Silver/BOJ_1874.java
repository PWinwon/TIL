import java.io.*;
import java.util.*;


public class BOJ_1874 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int num = 0;
		int myNum = 1;
		
		char[] answer = new char [N * 2];
		int idx = 0;
		boolean flag = true;
		
		Deque<Integer> deque = new ArrayDeque<>();
		
		for (int n = 0; n < N; n++) {
			num = Integer.parseInt(br.readLine());
			
			while (myNum <= num) {
				deque.offerLast(myNum);
				myNum++;
				
				answer[idx] = '+';
				idx++;
			}
			
			if (deque.peekLast() == num) {
				deque.pollLast();
				answer[idx] = '-';
				idx++;
			}
			
			else {
				flag = false;
				break;
			}
		}
		
		if (flag) {
			for (int i = 0; i < N*2; i++) {
				System.out.println(answer[i]);
			}
		}
		else {
			System.out.println("NO");
		}
	}

}
