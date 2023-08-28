import java.io.*;
import java.util.*;


public class BOJ_4470 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 1; i <= N; i++) {
			String str = br.readLine();
			
			System.out.println(i + ". " + str);
		}

	}

}
