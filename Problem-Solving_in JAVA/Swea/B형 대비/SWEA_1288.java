import java.io.*;
import java.util.*;


public class Swea_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc = 1; tc < T+1; tc++) {
			int N = sc.nextInt();
			
			int cnt = 1;
			int used = 0;
			int num = 0;
			
			int c = 0;
			
			while (c < 10) {
				num = N * cnt;
				while (num != 0) {
					int temp = num % 10;
					num /= 10;
					if ((used & (1 << temp)) == 0) {
//						System.out.println(cnt + " " + temp);
						used = used | (1 << temp);
						c++;
					}
				}
				cnt++;
			}
			cnt--;
			cnt *= N;
			System.out.println("#"+tc+" "+cnt);
		}
	}

}
