import java.io.*;
import java.util.*;

public class BOJ_1562 {
	static String S, T;
	static int Slen;
	
	static boolean flag = false;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder sb = new StringBuilder();
		
		S = br.readLine();
		T = br.readLine();
		
		Slen = S.length();
		
		System.out.println(myFunc(S, T));

	}
	
	public static int myFunc(String s, String t) {
		if (s.length() == t.length()) {
			if (s.equals(t)) return 1;
			return 0;
		}
		
		int ret = 0;
		if (t.charAt(0) == 'B') {
			String sbs = t.substring(1);
			StringBuilder sb = new StringBuilder(sbs);
			String str = sb.reverse().toString();
			ret += myFunc(s, str);
		}
		if (t.charAt(t.length() - 1) == 'A') {
			ret += myFunc(s, t.substring(0, t.length()-1));
		}
		
		if (ret > 0) return 1;		
		return 0;
	}

}
