import java.io.*;
import java.util.*;


public class BOJ_4659 {
	static Set<Character> mySet = new HashSet<Character>();

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuffer sb = new StringBuffer();
		
		mySet.add('a');
		mySet.add('e');
		mySet.add('i');
		mySet.add('o');
		mySet.add('u');
		
		while (true) {
			boolean answer = true;
			
			String str = br.readLine();

			if (str.equals("end")) break;
			
			char[] c = str.toCharArray();
			
			boolean hasMoum = false;
			boolean isMoum = false;
			int cnt = 0;
			
			// 모음이라면
			if (mySet.contains(c[0])) {
				hasMoum = true;
				isMoum = true;
			}
			cnt = 1;
			
			for (int i = 1; i < c.length; i++) {
				if (c[i] == c[i-1] && (c[i] != 'e' && c[i] != 'o')) {
					answer = false;
					break;
				}
				// 현재 모음 && 이전도 모음
				else if (mySet.contains(c[i])) {
					if (isMoum) {
						cnt++;
						hasMoum = true;
						continue;						
					}
					hasMoum = true;
				}
				else if (!mySet.contains(c[i]) && !isMoum) {
					cnt++;					
					continue;
				}
				
				if (cnt == 3) {
					answer = false;
					break;
				}
				
				isMoum = !isMoum;
				cnt = 1;
			}
			
			if (cnt == 3 || !hasMoum) answer = false;
			
			if (answer) {
				sb.append("<" + str + "> is acceptable.\n");
			}
			else {
				sb.append("<" + str + "> is not acceptable.\n");
			}
		}
		
		System.out.println(sb);

	}

}
