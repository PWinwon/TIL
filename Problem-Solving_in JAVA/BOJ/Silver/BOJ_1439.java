import java.io.*;
import java.util.*;


public class BOJ_1439 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		char[] c = str.toCharArray();
		int[] cnt = new int[2];
		char chk = c[0];
		
		cnt[chk - '0']++;
		
		for (int i = 1; i < c.length; i++) {
			if (chk != c[i]) {
				chk = c[i];
				cnt[c[i] - '0']++;
			}
		}
		
		System.out.println(Math.min(cnt[0], cnt[1]));
		
//		int zeroCnt = str.split("0").length;
//		int oneCnt = str.split("1").length;
//		
//		System.out.println(zeroCnt);
//		System.out.println(oneCnt);

	}

}
