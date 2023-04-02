import java.io.*;
import java.util.*;

public class BOJ_14425 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		HashMap<String, Integer> myMap = new HashMap<>();
		
		for (int n = 0; n < N; n++) {
			myMap.put(br.readLine(), 1);
		}
		
		int answer = 0;
		
		for (int m = 0; m < M; m++) {
			if (myMap.containsKey(br.readLine())) {
				answer++;
			}
		}
		
		System.out.println(answer);
	}

}
