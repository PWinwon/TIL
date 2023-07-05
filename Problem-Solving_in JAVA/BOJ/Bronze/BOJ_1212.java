import java.io.*;
import java.util.*;


public class BOJ_1212 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String[] myBin = {"000", "001", "010", "011", "100", "101", "110", "111"};
		char[] c = br.readLine().toCharArray();
		
		for (int i = 0; i < c.length; i++) {
			int idx = c[i] - '0';
			sb.append(myBin[idx]);
		}
		
		if (c[0] == '0') System.out.println(0);
		else {
			while (sb.charAt(0) == '0') sb = new StringBuilder(sb.substring(1));
			System.out.println(sb.toString());
		}

	}

}
