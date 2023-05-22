import java.io.*;
import java.util.*;


public class BOJ_14425_2 {
	static int N, M;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		
		tNode root = new tNode();
		
		for (int n = 0; n < N; n++) {
			String txt = sc.next();
			tNode now = root;
			
			for (int i = 0; i < txt.length(); i++) {
				char c = txt.charAt(i);
				if (now.next[c - 'a'] == null) {
					now.next[c - 'a'] = new tNode();
				}
				now = now.next[c - 'a'];
				if (i == txt.length() - 1) now.isEnd = true;
			}
		}
		
		int cnt = 0;
		
		for (int m = 0; m < M; m++) {
			String txt = sc.next();
			tNode now = root;
			for (int i = 0; i < txt.length(); i++) {
				char c = txt.charAt(i);
				
				if (now.next[c - 'a'] == null) {
					break;
				}
				
				now  = now.next[c - 'a'];
				if (i == txt.length() - 1 && now.isEnd) cnt++;
			}
		}
		
		System.out.println(cnt);

	}
	
}

class tNode {
	tNode[] next = new tNode[26];
	boolean isEnd;
}
