import java.io.*;
import java.util.*;


public class BOJ_1316 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		HashMap<Character, Integer> myMap;
		
		int answer = 0;
		
		int N = Integer.parseInt(br.readLine());
		char[] str;
		
		for (int n = 0; n < N; n++) {
			myMap = new HashMap<Character, Integer>();
			boolean flag = true;
			
			str = br.readLine().toCharArray();
			
			for (int i = 0; i < str.length; i++) {
				// 이미 알파벳이 있다면.
				if (myMap.containsKey(str[i])) {
					// 현재 저장된 value + 1 == i 이면 연속된것임
					if (myMap.get(str[i]) + 1 == i) myMap.put(str[i], i);
					else {
						flag = false;
						break;
					}
				}
				else {
					myMap.put(str[i], i);
				}
			}
			
			if (flag) answer++;
		}
		
		System.out.println(answer);

	}

}
