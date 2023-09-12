import java.io.*;
import java.util.*;


public class BOJ_22233 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		HashMap<String, Integer> myMap = new HashMap<String, Integer>();
		
		int total = N;
		
		for (int n = 0; n < N; n++) {
			String str = br.readLine();
			myMap.put(str, 1);
		}
		
		for (int m = 0; m < M; m++) {
			String[] strs = br.readLine().split(",");
			for (int i = 0; i < strs.length; i++) {
				String str = strs[i];
				if (myMap.containsKey(str) && myMap.get(str) >= 1) {
					myMap.put(str, 0);
					total--;
				}
			}
			System.out.println(total);
		}

	}

}
