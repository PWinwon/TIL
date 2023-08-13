import java.io.*;
import java.util.*;


public class BOJ_1233 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int s1 = Integer.parseInt(st.nextToken());
		int s2 = Integer.parseInt(st.nextToken());
		int s3 = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[s1 + s2 + s3 + 1];

		for (int i = 1; i <= s1; i++) {
			for (int j = 1; j <= s2; j++) {
				for (int k = 1; k <= s3; k++) {
					arr[i+j+k]++;
				}
			}
		}
		
		int cnt = -1;
		int answer = -1;
		
		for (int i = 0; i < arr.length; i++) {
			if (cnt < arr[i]) {
				answer = i;
				cnt = arr[i];
			}
		}
		
		System.out.println(answer);
	}

}
