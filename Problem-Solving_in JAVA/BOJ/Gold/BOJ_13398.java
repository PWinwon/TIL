import java.io.*;
import java.util.*;


public class BOJ_13398 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] dpL = new int[N];
		int[] dpR = new int[N];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		dpL[0] = arr[0];
		dpR[N-1] = arr[N-1];
		int answer = arr[0];
		
		for (int i = 1; i < N; i++) {
			dpL[i] = Math.max(arr[i], dpL[i-1] + arr[i]);
//			dpR[N-1-i] = Math.max(arr[N-1-i], dpR[N-i] + arr[N-1-i]);
			answer = Math.max(answer, dpL[i]);
		}
		
		for (int i = N-2; i >= 0; i--) {
			dpR[i] = Math.max(arr[i], dpR[i+1] + arr[i]);
		}
		
		
		for (int i = 1; i < N-1; i++) {
			answer = Math.max(answer,  dpL[i-1] + dpR[i+1]);
		}
		
		System.out.println(answer);

	}

}
