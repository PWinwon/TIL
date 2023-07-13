import java.io.*;
import java.util.*;


public class BOJ_0713 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		System.out.println(rev(rev(a) + rev(b)));
		

	}
	
	public static int rev(int num) {
		int ret = 0;
				
		while (num > 0) {
			ret *= 10;
			ret += num % 10;
			num /= 10;
		}
		
		return ret;
	}

}
