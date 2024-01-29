import java.io.*;
import java.util.*;


public class BOJ_19941 {
	static int N, K;
	static int[] arr;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		String str = br.readLine();
		
		arr = new int[str.length()];
		
		// 사람 0, 햄버거 o = 1, x = -1
		
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == 'H') {
				arr[i] = 1;
			} else {
				arr[i] = 0;
			}
		}
		
		int result = 0;
		
		for (int i = 0; i < arr.length; i++) {
			// 사람일 경우
			if (arr[i] == 0) {				
				result += eatHamburger(i);
			}
		}
		
		System.out.println(result);

	}

	private static int eatHamburger(int i) {
		// TODO Auto-generated method stub
		// i 위치로부터 +- K를 탐색
		// 햄버거가 있다면 (arr[i] == 1)
		// *= -1 (햄버거 먹기) 후 return 1
		
		for (int j = i - K; j <= i+K; j++) {
			if (j < 0) continue;
			else if (j >= N) break;
			else if (arr[j] == 1) {
				arr[j] *= -1;
				return 1;
			}
		}
		return 0;
		
	}

}
