import java.io.*;
import java.util.*;


public class BOJ_2845 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuffer sb = new StringBuffer();
		
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int total = a * b;
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < 5; i++) {
			int d = Integer.parseInt(st.nextToken()) - total;
			sb.append(d + " ");
		}
		System.out.println(sb);

	}

}
