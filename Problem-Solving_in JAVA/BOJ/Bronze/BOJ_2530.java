import java.io.*;
import java.util.*;


public class BOJ_2530 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		int D = Integer.parseInt(br.readLine());
		
		C += D;
		
		if (C >= 60) {
			B += C / 60;
			C %= 60;
		}
		
		if (B >= 60) {
			A += B / 60;
			B %= 60;
		}
		
		if (A >= 24) {
			A %= 24;
		}
		
		System.out.println(A + " " + B + " " + C);

	}

}
