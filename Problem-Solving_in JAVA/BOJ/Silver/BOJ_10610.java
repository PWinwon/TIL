import java.io.*;
import java.util.*;


public class BOJ_10610 {

	public static void main(String[] args) throws Exception  {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		
		String str = br.readLine();
		char[] c = str.toCharArray();
		
		Arrays.sort(c);
		
		int num = 0;
		
		for (int i = c.length - 1; i >= 0; i--) {
			num += c[i] - '0';
			sb.append(c[i]);
		}
		
		if (c[0] != '0' || num % 3 != 0) {
			System.out.println(-1);
		}
		else System.out.println(sb.toString());

	}

}
