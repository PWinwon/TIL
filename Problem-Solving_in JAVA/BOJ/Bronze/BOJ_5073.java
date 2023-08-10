import java.io.*;
import java.util.*;


public class BOJ_5073 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		while (true) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			if (a == 0 && b == 0 && c == 0) break;
			
			int maxV = -1;
			maxV = Math.max(a, Math.max(b, c));
			
			if (a == b && b == c && c == a) System.out.println("Equilateral");
			else if (maxV >= a + b || maxV >= b + c || maxV >= c + a) System.out.println("Invalid");
			else if (a == b || b == c || c == a) System.out.println("Isosceles");
			else if (maxV < a + b && maxV < b + c && maxV < c + a) System.out.println("Scalene");
			else System.out.println("Invalid");
		}

	}

}
