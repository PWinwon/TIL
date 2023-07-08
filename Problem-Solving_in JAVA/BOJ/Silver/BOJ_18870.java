import java.io.*;
import java.util.*;


public class BOJ_18870 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[] a = new int[N];
		int[] sortA = new int[N];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			a[i] = Integer.parseInt(st.nextToken());
			sortA[i] = a[i];
		}
		
		Arrays.sort(sortA);
		
		HashMap<Integer, Integer> myMap = new HashMap<>();
		
		int idx = 0;
		
		for (int i = 0; i < N; i++) {
			if (!myMap.containsKey(sortA[i])) {
				myMap.put(sortA[i], idx);
				idx++;
			}
		}
		
		StringBuffer sb = new StringBuffer();
		
		for (int i = 0; i < N; i++) {
			sb.append(myMap.get(a[i])).append(" ");
		}
		
		System.out.print(sb.toString());

	}

}
