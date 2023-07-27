import java.io.*;
import java.util.*;


public class BOJ_11365 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb;
		
		while (true) {
			String str = br.readLine();
			if (str.equals("END")) break;
			
			sb = new StringBuffer();
			
			sb.append(str);
			
			sb.reverse();
			
			System.out.println(sb);
		}

	}

}
