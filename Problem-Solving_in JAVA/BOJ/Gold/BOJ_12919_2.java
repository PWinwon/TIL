import java.io.*;
import java.util.*;


public class BOJ_12919 {
	
	static String S, T;
	static int Slen;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		S = br.readLine();
		T = br.readLine();
		Slen = S.length();
		
		if (myFunc(T)) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}

	}

	private static boolean myFunc(String str) {
		// TODO Auto-generated method stub
		if (str.length() == Slen) {
			if(str.equals(S)) return true;
			return false;
		}
		
		if (str.charAt(str.length() - 1) == 'A') {
			if (myFunc(str.substring(0, str.length()-1))) return true;
		}
		
		if (str.charAt(0) == 'B') {
			StringBuilder reverse = new StringBuilder();
			reverse.append(str.substring(1, str.length()));
			if (myFunc(reverse.reverse().toString())) return true;
		}
		
		return false;
	}

}
