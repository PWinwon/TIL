import java.io.*;
import java.util.*;


public class BOJ_1715 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		
		for (int i = 0; i < N; i++) {
			pq.add(Integer.parseInt(br.readLine()));
		}
		
		int answer = 0;
		
		while (pq.size() != 1) {
			int a = pq.poll();
			int b = pq.poll();
			answer += a+b;
			pq.add(a+b);
		}
		
		
		System.out.println(answer);
		

	}

}
