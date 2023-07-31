import java.io.*;
import java.util.*;


public class BOJ_2864 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		String a_str = String.valueOf(a);
        String b_str = String.valueOf(b);

        int min = Integer.parseInt(a_str.replace("6", "5")) + Integer.parseInt(b_str.replace("6", "5"));
        int max = Integer.parseInt(a_str.replace("5", "6")) + Integer.parseInt(b_str.replace("5", "6"));
        System.out.println(min + " " + max);

	}

}
