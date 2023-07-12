import java.io.*;
import java.util.*;


public class BOJ_8979 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		Country[] cs = new Country[N];
		Country k = new Country(0, 0, 0);
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			cs[i] = new Country(g, s, b);
			
			if (a == K) {
				k = cs[i];
			}
		}
		
		int answer = 1;
		
		for (int i = 0; i < N; i++) {
			if (cs[i].gold > k.gold || (cs[i].gold == k.gold && cs[i].silver > k.silver) || (cs[i].gold == k.gold && cs[i].silver == k.silver && cs[i].bronze > k.bronze)) answer++;
		}
		
		System.out.println(answer);
	}

}

class Country{
	int gold, silver, bronze;
	
	Country(int g, int s, int b) {
		this.gold = g;
		this.silver = s;
		this.bronze = b;
	}

//	@Override
//	public int compareTo(Country o) {
//		// TODO Auto-generated method stub
//		if (this.gold != o.gold) {
//			return o.gold - this.gold;
//		}
//		else if (this.silver != o.silver) {
//			return o.silver - this.silver;
//		}		
//		return o.bronze - this.bronze;
//	}
//	
	
}
