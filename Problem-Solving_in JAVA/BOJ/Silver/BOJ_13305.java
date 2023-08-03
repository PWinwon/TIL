import java.io.*;
import java.util.*;


public class BOJ_13305 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		long[] dist = new long[N-1];
		long[] cost = new long[N];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N-1; i++) {
			dist[i] = Long.parseLong(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			cost[i] = Long.parseLong(st.nextToken());
		}
		
		long answer = dist[0] * cost[0];
		long minCost = cost[0];
		
		for (int i = 1; i < N-1; i++) {
			minCost = Math.min(minCost, cost[i]);
			answer += dist[i] * minCost;
		}
		
		System.out.println(answer);

	}

}
