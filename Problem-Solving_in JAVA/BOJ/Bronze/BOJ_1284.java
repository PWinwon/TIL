import java.io.*;
import java.util.*;


public class BOJ_1284 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			String str = br.readLine();
			if (str.equals("0")) break;
			char[] c = str.toCharArray();
			int s = 1;
			
			for (int i = 0; i < c.length; i++) {
				s += 1;
				switch (c[i]) {
					case '1':
						s += 2;
						break;
					case '0':
						s += 4;
						break;
					default:
						s += 3;
						break;
				}
			}
			
			System.out.println(s);
		}

	}

}
