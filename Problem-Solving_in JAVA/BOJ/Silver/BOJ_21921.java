import java.io.*;
import java.util.*;


public class BOJ_21921 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		int[] visited = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		
		
		for (int i = 1; i <= N; i++) {
			visited[i] = Integer.parseInt(st.nextToken()) + visited[i-1];
//			System.out.print(visited[i] + " ");
		}
		
		int maxVisit = 0;
		int cnt = 0;
		
		for (int i = 0; i <= N - X; i++) {
			int temp = visited[X+i] - visited[i];
			if (maxVisit < temp) {
				maxVisit = temp;
				cnt = 1;
			}
			else if (maxVisit == temp) {
				cnt++;
			}
		}
		
		
		if (maxVisit <= 0) {
			System.out.println("SAD");
		}
		else {
			System.out.println(maxVisit);
			System.out.println(cnt);			
		}

	}

}
