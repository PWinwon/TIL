import java.io.*;
import java.util.*;


public class BOJ_7785 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		
		HashMap<String, Integer> myMap = new HashMap<String, Integer>();
		
		for (int n = 0; n < N; n++) {
			st = new StringTokenizer(br.readLine());
			String name = st.nextToken();
			if (st.nextToken().equals("enter")) {
				myMap.put(name, 1);
			}
			else {
				myMap.put(name, 0);
			}
		}
		
		ArrayList<String> answer = new ArrayList<String>();
		int cnt = 0;
		
		for (String key : myMap.keySet()) {
			if (myMap.get(key) == 1) {
				answer.add(key);
				cnt++;
			}
		}
		
		Collections.sort(answer);
		
		while (cnt > 0) {
			cnt--;
			System.out.println(answer.get(cnt));
		}

	}

}
