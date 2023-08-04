import java.io.*;
import java.util.*;


public class BOJ_20920 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		HashMap<String, Word> myMap = new HashMap<String, Word>();
		ArrayList<Word> lst = new ArrayList<Word>();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		for (int n = 0; n < N; n++) {
			String temp = br.readLine();
			if (temp.length() < M) continue;
			else if (myMap.containsKey(temp)) {
				myMap.get(temp).addCnt();
				continue;
			}
			
			Word word = new Word(temp);
			lst.add(word);
			myMap.put(temp, word);
		}
		
		Collections.sort(lst);
		
		StringBuffer sb = new StringBuffer();
		for (Word w : lst) {
			sb.append(w.name).append("\n");
		}
		
		System.out.println(sb);

	}

}

class Word implements Comparable<Word> {
	String name;
	int cnt;
	
	Word(String name) {
		this.name = name;
		cnt = 1;
	}
	
	void addCnt() {
		this.cnt++;
	}
	
	@Override
	public int compareTo(Word o) {
		if (this.cnt != o.cnt) {
			return o.cnt - this.cnt;
		}
		
		if (this.name.length() != o.name.length()) {
			return o.name.length() - this.name.length();
		}
		
		return this.name.compareTo(o.name);
	}
}
