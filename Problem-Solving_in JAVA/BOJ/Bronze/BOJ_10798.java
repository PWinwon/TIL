import java.io.*;
import java.util.*;

public class BOJ_10798 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[][] c = new char[5][15];
		
		for (int i = 0; i < 5; i++) {
			c[i] = br.readLine().toCharArray();
		}
		
		int de = -1;
		
		for (int x = 0; x < 15; x++) {
			for (int y = 0; y < 5; y++) {
				if (x >= c[y].length) continue;
				System.out.print(c[y][x]);
			}
		}

	}

}
