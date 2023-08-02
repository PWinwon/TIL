import java.io.*;
import java.util.*;


public class BOJ_17266 {
	static int N;
	static int[] lights;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
			
		lights = new int[M];
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < M; i++) {
			lights[i] = Integer.parseInt(st.nextToken());
		}
		
		int left = 1;
		int right = 100000;
		
		int result = 0;
		
		while (left <= right) {
			int mid = (left + right) / 2;
			
			if (myFunc(mid)) {
				right = mid - 1;
			}
			else {
				left = mid + 1;
			}
		}
		
		result = left;
		
		System.out.println(result);
	}
	
	public static boolean myFunc(int h) {
		int lP = 0;
		
		for (int i : lights) {
			if (lP + h < i) {
				return false;
			}
			
			lP = i + h;
		}
		
		return lP >= N;
	}

}
