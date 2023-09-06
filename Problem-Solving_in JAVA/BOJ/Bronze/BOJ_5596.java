import java.io.*;
import java.util.*;


public class BOJ_5596 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int mg = 0;
		int ms = 0;
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < 4; i++) {
			mg += Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < 4; i++) {
			ms += Integer.parseInt(st.nextToken());
		}
		
		System.out.println(Math.max(mg, ms));
		
		

	}

}
