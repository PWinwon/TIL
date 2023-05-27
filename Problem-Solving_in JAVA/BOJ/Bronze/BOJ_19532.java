import java.io.*;
import java.util.*;


public class BOJ_19532 {
	static int a, b, c, d, e, f;
	static boolean flag;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		f = Integer.parseInt(st.nextToken());
		
		int ansX = 0;
		int ansY = 0;
		
		for (int x = -999; x < 1000; x++) {
			if (flag) break;
			for (int y = -999; y < 1000; y++) {
				if (flag) break;
				if (chkTrue(x, y)) {
					flag = true;
					ansX = x;
					ansY = y;
				}
			}
		}
		
		System.out.println(ansX + " " + ansY);

	}
	
	public static boolean chkTrue(int x, int y) {
		if (a * x + b * y == c && d * x + e * y == f) return true;
		return false;
	}

}
