import java.io.*;
import java.util.*;


public class BOJ_11656 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		String[] strs = new String[str.length()];
		
		for (int i = 0; i < str.length(); i++) {
			strs[i] = str.substring(i, str.length());
//			System.out.println(strs[i]);
		}
		
		Arrays.sort(strs);
		
		for (int i = 0; i < strs.length; i++) {
			System.out.println(strs[i]);
		}
		

	}

}
