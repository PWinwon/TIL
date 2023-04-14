import java.io.*;
import java.util.*;


public class BOJ_1744 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		PriorityQueue<Integer> minPq = new PriorityQueue<>(Collections.reverseOrder());
		PriorityQueue<Integer> maxPq = new PriorityQueue<>();
		
		int zeroCnt = 0;
		int oneCnt = 0;
		
		for (int n = 0; n < N; n++) {
			int a = Integer.parseInt(br.readLine());
			
			if (a < 0) {
				maxPq.add(a);
			}
			else if (a == 0) {
				zeroCnt++;
			}
			else if (a == 1) {
				oneCnt++;
			}
			else {
				minPq.add(a);
			}
			
		}
		
		int answer = 0;
		
		while (maxPq.size() > 1) {
			int a = maxPq.poll();
			int b = maxPq.poll();
			
			answer += a * b;
		}
		
		if (maxPq.size() == 1) {
			if (zeroCnt == 0) {
				int a = maxPq.poll();
				answer += a;
			}
			
		}
		
		while (minPq.size() > 1) {
			int a = minPq.poll();
			int b = minPq.poll();
			
			answer += a * b;
		}
		
		if (minPq.size() == 1) {
			answer += minPq.poll();
		}
		
		answer += oneCnt;
		
		System.out.println(answer);
	}

}
