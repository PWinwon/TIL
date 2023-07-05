import java.io.*;
import java.util.*;


public class BOJ_2902 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		
		String[] strs = br.readLine().split("-");
		
		for (int i = 0; i < strs.length; i++) {
			sb.append(strs[i].charAt(0));
		}
		
		System.out.println(sb.toString());

	}

}
