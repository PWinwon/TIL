import java.io.*;
import java.util.*;


public class BOJ_10986 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		long[] S = new long[N];
		long[] C = new long[M];
		
		long answer = 0;
		
		S[0] = sc.nextInt();
		
		for (int i = 1; i < N; i++) {
			S[i] = S[i-1] + sc.nextInt();
		}
		
		for (int i = 0; i < N; i++) {
			int temp = (int) (S[i] % M);
			if (temp == 0) {
				answer += 1;
			}
			C[temp]++;
		}
		
		for (int i = 0; i < M; i++) {
			if (C[i] > 1) {
				answer += (C[i] * (C[i] - 1) / 2);
			}
		}
		
		System.out.print(answer);
		
		
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//		Scanner sc = new Scanner(System.in);
//		
//		StringTokenizer st = new StringTokenizer(br.readLine());
//		
//		int N = Integer.parseInt(st.nextToken());
//		int M = Integer.parseInt(st.nextToken());
//		
//		long sumArray[] = new long [N+1];
//		long modReturn[] = new long [M];
//		
//		int answer = 0;
//		
////		st = new StringTokenizer(br.readLine());
//		
//		for (int i = 1; i <= N; i++) {
////			sumArray[i] = (sumArray[i-1] + Integer.parseInt(st.nextToken())) % M;
//			sumArray[i] = (sumArray[i-1] + sc.nextInt()) % M;
//			modReturn[(int) sumArray[i]] += 1;
//			if (sumArray[i] == 0) {
//				answer += 1;
//			}
//		}
//		
//		for (int m = 0; m < M; m++) {
//			if (modReturn[m] > 1){				
//				answer = answer + (int) (modReturn[m] * (modReturn[m] - 1) / 2);
//			}
//		}
//		
//		System.out.print(answer);
////		bw.write(answer + "");
////		bw.close();
	}

}
