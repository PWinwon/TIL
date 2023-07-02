import java.io.*;
import java.util.*;


public class BOJ_9093 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int t = 0; t < TC; t++) {
			String[] s = br.readLine().split(" ");
			
			for (int i = 0; i < s.length; i++) {
				sb.append(new StringBuffer(s[i]).reverse().toString()).append(" ");
			}
			sb.append("\n");
			
		}
		
		System.out.println(sb);
	}

}
