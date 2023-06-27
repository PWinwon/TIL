import java.io.*;
import java.util.*;


public class BOJ_9252 {
	static char[] a, b;
	static int[][] dp;
	static ArrayList<Character> Path;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		a = sc.next().toCharArray();
		b = sc.next().toCharArray();
		dp = new int[a.length+1][b.length+1];
		Path = new ArrayList<Character>();
		
		for (int i = 1; i <= a.length; i++) {
			for (int j = 1; j <= b.length; j++) {
				if (a[i-1] == b[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
				else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
			}
		}
		
		System.out.println(dp[a.length][b.length]);
		
		getText(a.length, b.length);
		
		for (int i = Path.size()-1; i >= 0; i--) {
			System.out.print(Path.get(i));
		}

	}
	
	public static void getText(int r, int c) {
		if (r == 0 || c == 0) return;
		if (a[r-1] == b[c-1]) {
			Path.add(a[r-1]);
			getText(r - 1, c - 1);
		}
		else {
			if (dp[r-1][c] > dp[r][c-1]) getText(r-1, c);
			else getText(r, c-1);
		}
	}

}
