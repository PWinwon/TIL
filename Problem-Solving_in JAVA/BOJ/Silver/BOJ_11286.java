import java.io.*;
import java.util.*;


public class BOJ_11286 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		PriorityQueue<Integer> pQue = new PriorityQueue<>((num1, num2) -> {
			int abs1 = Math.abs(num1);
			int abs2 = Math.abs(num2);
			
			if (abs1 == abs2) {
				if (num1 > num2) {
					return 1;
				}
				else {
					return -1;
				}
			}
			else {
				if (abs1 > abs2) {
					return 1;
				}
				else {
					return -1;
				}
			}
		});
		
		int num = 0;
		
		for (int n = 0; n < N; n++) {
			num = Integer.parseInt(br.readLine());
			if (num == 0) {
				if (pQue.isEmpty()) {
					System.out.println('0');
				}
				else {
					System.out.println(pQue.poll());
				}
			}
			else {
				pQue.offer(num);
			}
		}
	}

}
