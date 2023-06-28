import java.io.*;
import java.util.*;

public class BOJ_11721 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		int l = str.length();
		int idx = 0;
		
		for (int i = 0; i < l / 10; i++) {
			System.out.println(str.substring(i*10, i*10+10));
		}
		
		if (l % 10 > 0) System.out.println(str.substring((l / 10) * 10, l));		

	}

}
