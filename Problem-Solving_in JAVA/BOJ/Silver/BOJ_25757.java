import java.io.*;
import java.util.*;


public class BOJ_25757 {
	static int N, gn;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		HashMap<String, Integer> myMap = new HashMap<String, Integer>();
		int answer = 0;
		
		N = Integer.parseInt(st.nextToken());
		
		String game = st.nextToken();
		
		switch (game) {
			case "Y" :
				gn = 1;
				break;
			case "F" :
				gn = 2;
				break;
			case "O" :
				gn = 3;
				break;
			default:
				gn = -1;
				break;
		}
		
		int cnt = 0;
		
		for (int n = 0; n < N; n++) {
			String name = br.readLine();
			
			if (myMap.containsKey(name)) continue;
			
			myMap.put(name, 1);			
			cnt++;
			
			if (cnt == gn) {
				answer++;
				cnt = 0;
			}
		}
		
		System.out.println(answer);

	}

}
