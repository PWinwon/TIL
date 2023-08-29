import java.io.*;
import java.util.*;


public class BOJ_3046 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int r1 = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());
		
		int gap = s - r1;
		int result = s + gap;
		
		System.out.println(result);

	}

}
