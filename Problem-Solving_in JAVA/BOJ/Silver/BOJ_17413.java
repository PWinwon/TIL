import java.io.*;
import java.util.*;


public class BOJ_17413 {
	static Stack<Character> stck;
	static StringBuilder sb;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] c = br.readLine().toCharArray();
		stck = new Stack<Character>();
		sb = new StringBuilder();
		
		boolean tag = false;
		
		for (int i = 0; i < c.length; i++) {
			switch (c[i]) {
				case '<':
					tag = true;
					sToSb();
					sb.append(c[i]);
					break;
				case '>':
					tag = false;
					sb.append(c[i]);
					break;
				case ' ':
					sToSb();
					sb.append(c[i]);
					break;
				default:
					if (tag) {
						sb.append(c[i]);
					}
					else {
						stck.add(c[i]);
					}
					break;
			}
			
		}
		sToSb();
		System.out.println(sb.toString());

	}
	
	public static void sToSb() {
		while (!stck.isEmpty()) {
			sb.append(stck.pop());
		}
	}

}
