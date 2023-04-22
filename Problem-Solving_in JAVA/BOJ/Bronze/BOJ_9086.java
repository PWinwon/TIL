import java.io.*;
import java.util.*;


public class BOJ_9086 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < T; tc++) {
			char[] str = br.readLine().toCharArray();
			StringBuffer sb = new StringBuffer();
			sb.append(str[0]).append(str[str.length-1]);
			System.out.println(sb);
		}
	}

}
