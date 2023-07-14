import java.io.*;
import java.util.*;


public class BOJ_11005 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int num = Integer.parseInt(st.nextToken());
		int div = Integer.parseInt(st.nextToken());
		
		StringBuffer sb = new StringBuffer();
		
		while (num > 0) {
			int myMod = num % div;
			char c;
			if (myMod > 9) c = (char) ('A' + myMod - 10);
			else c = (char) ('0' + myMod);
			
			num /= div;
			
			sb.append(c);
		}
		
		sb.reverse();
		
		System.out.println(sb.toString());
	}

}
