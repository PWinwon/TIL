import java.io.*;
import java.util.*;


public class BOJ_1264 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			char[] c = br.readLine().toCharArray();
			
			if (c[0] == '#') break;
			
			int cnt = 0;
			
			for (int i = 0; i < c.length; i++) {
				if (c[i] == 'a' || c[i] == 'e' || c[i] == 'i' || c[i] == 'o' || c[i] == 'u') cnt++;
				else if (c[i] == 'A' || c[i] == 'E' || c[i] == 'I' || c[i] == 'O' || c[i] == 'U') cnt++;
			}
			
			System.out.println(cnt);
		}
		

	}

}
