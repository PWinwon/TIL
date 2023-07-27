import java.io.*;
import java.util.*;

public class BOJ_1205 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int score = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		
		if (N == 0) {
			System.out.println(1);
			return;
		}
		
		int[] board = new int[N];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			board[i] = Integer.parseInt(st.nextToken());
		}
		
		int answer = 1;
		int sameS = 0;
		
		while (answer <= N) {
			if (board[answer-1] < score) break;
			else if (board[answer-1] == score) {
				sameS++;
			}
			answer++;
		}
		
		if (answer <= P) System.out.println(answer - sameS);
//		else if ()
		else System.out.println(-1);

	}

}
