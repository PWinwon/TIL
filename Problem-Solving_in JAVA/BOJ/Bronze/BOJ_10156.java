import java.io.*;
import java.util.*;


public class BOJ_10156 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int K = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int total = K * N - M;
		
		if (total >= 0) System.out.println(total);
		else System.out.println(0);
	}

}
