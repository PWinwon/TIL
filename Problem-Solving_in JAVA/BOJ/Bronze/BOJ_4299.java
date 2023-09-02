import java.io.*;
import java.util.*;


public class BOJ_4299 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int s = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		int a = (s + c) / 2;
		int b = s - a;
		
		if ((s + c) % 2 != 0 || s < c) {
			System.out.println(-1);

		}
		else System.out.println(a + " " + b);

	}

}
