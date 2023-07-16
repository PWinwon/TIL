import java.io.*;
import java.util.*;


public class BOJ_5086 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		while (true) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (a == 0 && b == 0) break;
			
			if (a < b && b % a == 0) System.out.println("factor");
			else if (a > b && a % b == 0) System.out.println("multiple");
			else System.out.println("neither");
		}

	}

}
