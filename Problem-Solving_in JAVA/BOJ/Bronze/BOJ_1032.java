import java.io.*;
import java.util.*;


public class BOJ_1032 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		char[] temp = br.readLine().toCharArray();		
		
		char[][] c = new char[N-1][temp.length];
		
		for (int i = 0; i < N-1; i++) {
			c[i] = br.readLine().toCharArray();
		}
		
		boolean flag = false;
		
		for (int i = 0; i < temp.length; i++) {
			flag = false;
			for (int j = 0; j < N-1; j++) {
				if (temp[i] != c[j][i]) {
					flag = true;
					break;
				}
			}
			
			if (flag) System.out.print('?');
			else System.out.print(temp[i]);
			
		}

	}

}
