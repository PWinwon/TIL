import java.io.*;
import java.util.*;


public class BOJ_11652 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		HashMap<Long, Integer> myMap = new HashMap<Long, Integer>();
		
		long answer = Long.MAX_VALUE;
		int cnt = 0;
		
		for (int n = 0; n < N; n++) {
			long num = sc.nextLong();
			
			// 기존에 들어온 카드가 있다면
			if (myMap.containsKey(num)) {
				myMap.put(num, myMap.get(num) + 1);
			} 
			else {
				myMap.put(num, 1);
			}
			
			if (cnt < myMap.get(num)) {
				answer = num;
				cnt = myMap.get(num);
			}
			else if (cnt == myMap.get(num) && num < answer) {
				answer = num;
			}
		}
		
		System.out.println(answer);

	}

}
