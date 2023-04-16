import java.io.*;
import java.util.*;


public class BOJ_1456 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine());	
		
//		long A = Integer.parseInt(st.nextToken());
//		long B = Integer.parseInt(st.nextToken());
		
		Scanner sc = new Scanner(System.in);
		long A = sc.nextLong();
		long B = sc.nextLong();
		
		// 초기값 모두 false
		// 소수를 제외한 모두를 true로 만들기
		// false >> 소수, true >> 소수x
		boolean[] isPrime = new boolean[10000001];
		isPrime[0] = true;
		isPrime[1] = true;
		
		for (int i = 2; i <= Math.sqrt(isPrime.length); i++) {
			if (isPrime[i]) {
				continue;
			}
			int temp = i + i;
			while (temp < isPrime.length) {
				isPrime[temp] = true;
				temp += i;
			}
		}
		
		int answer = 0;
		
		for (int i = 2; i <= Math.sqrt((double)(B)); i++) {
			// 소수가 아니라면 continue
			if (isPrime[i]) {
				continue;
			}
			// 소수라면, 다음 제곱수부터 A, B 사이 범위에 들어오는지 확인
			// 범위에 들어오는 소수의 제곱형태라면 answer++;
			long temp = i;
			
			while (i <= (double)(B)/temp) {
				if (i >= (double)(A)/temp) {
					answer++;
				}
				temp *= i;
			}
		}
		
		System.out.println(answer);
	}

}
