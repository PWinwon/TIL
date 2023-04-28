import java.io.*;
import java.util.*;


public class Swea_13501 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		LinkedList<Integer> numList;
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc < T+1; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			
			numList = new LinkedList<>();
			st = new StringTokenizer(br.readLine());
			
			for (int n = 0; n < N; n++) {
				numList.add(Integer.parseInt(st.nextToken()));
			}
			
			for (int m = 0; m < M; m++) {
				st = new StringTokenizer(br.readLine());
				int idx;
				int val;
				
				switch (st.nextToken()) {
				case "I":
					idx = Integer.parseInt(st.nextToken());
					val = Integer.parseInt(st.nextToken());
					
					numList.add(idx, val);
					
					break;
					
				case "D":
					idx = Integer.parseInt(st.nextToken());
					numList.remove(idx);
					break;
					
				case "C":
					idx = Integer.parseInt(st.nextToken());
					val = Integer.parseInt(st.nextToken());
					
					numList.set(idx, val);
					break;
				}
			}
			int answer = -1;
			
			if (numList.size() > L) {
				answer = numList.get(L);
			}
			
			System.out.println("#" + tc + " " + answer);
		}

	}

}
