import java.io.*;
import java.util.*;


public class BOJ_1722 {
	static int N;
	static long K;
	static long[] F;
	static int[] S;
	static boolean[] visited;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		F = new long[N+1];
		S = new int[N+1];
		visited = new boolean[N+1];
		
		F[0] = 1;
		for (int i = 1; i <= N; i++) {
			F[i] = F[i-1] * i;
		}
		
		st = new StringTokenizer(br.readLine());
		
		int Q = Integer.parseInt(st.nextToken());
		
		if (Q == 1) {
			K = Long.parseLong(st.nextToken());
			getS(K);
			for (int i = 1; i <= N; i++) {
				System.out.print(S[i] + " ");
			}
		}
		else {
			long K = 1;
			for (int i = 1; i <= N; i++) {
				S[i] = Integer.parseInt(st.nextToken());
				long cnt = 0;
				for (int j = 1; j < S[i]; j++) {
					if (visited[j] == false) cnt++;
				}
				K += cnt * F[N-i];
				visited[S[i]]= true;
			}
			System.out.println(K);
		}
		

	}
	
	public static void getS(long k) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1, cnt = 1; j <= N; j++) {
				if (visited[j]) continue;
				if (k <= cnt * F[N-i]) {
					k -= ((cnt - 1) * F[N-i]);
					S[i] = j;
					visited[j] = true;
					break;
				}
				cnt++;
			}
		}
	}

}
