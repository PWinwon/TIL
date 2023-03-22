import java.io.*;
import java.util.*;

public class BOJ_1940 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		Scanner sc = new Scanner(System.in);

//		int N = sc.nextInt();
//		int M = sc.nextInt();
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		int ingres[] = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			ingres[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(ingres);
		
		int startIdx = 0;
		int endIdx = N-1;
		
		int subSum = 0;
		int answer = 0;
		
		while (startIdx < endIdx) {
			subSum = ingres[startIdx] + ingres[endIdx];
			if (subSum == M) {
				answer++;
				startIdx++;
				endIdx--;
			}
			else if (subSum > M) {
				endIdx--;
			}
			else {
				startIdx++;
			}
		}
		
		System.out.print(answer);
		br.close();
	}

}
