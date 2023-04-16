import java.io.*;
import java.util.*;


public class BOJ_1929 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		for (int i = M; i < N+1; i++) {
			boolean flag = false;
			if (i == 1) {
				continue;
			}
			for (int j = 2; j <= Math.sqrt(i); j++) {
				if (flag) {
					break;
				}
				if (i % j == 0) {
					flag = true;
				}
			}
			
			if (flag) {
				continue;
			}
			System.out.println(i);
		}
	}

}
