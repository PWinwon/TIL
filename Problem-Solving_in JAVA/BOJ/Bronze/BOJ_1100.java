import java.io.*;
import java.util.*;


public class BOJ_1100 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[][] board = new char[8][8];
		
		for (int i = 0; i < 8; i++) {
			board[i] = br.readLine().toCharArray();
		}
		
		int answer = 0;
		
		for (int i = 0; i < 8; i += 2) {
			for (int j = 0; j < 8; j+= 2) {
				if (board[i][j] == 'F') answer++;
			}
		}
		
		for (int i = 1; i < 8; i += 2) {
			for (int j = 1; j < 8; j += 2) {
				if (board[i][j] == 'F') answer++;
			}
		}
		
		System.out.println(answer);
		

	}

}
