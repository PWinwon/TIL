import java.io.*;
import java.util.*;


public class BOJ_1302 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		HashMap<String, Integer> myMap = new HashMap<String, Integer>();
		
		for (int n = 0; n < N; n++) {
			String book = br.readLine();
			if (myMap.containsKey(book)) {
				myMap.put(book, myMap.get(book) + 1);
			} else {
				myMap.put(book, 1);
			}
		}
		
		ArrayList<String> al = new ArrayList<String>();
		int cnt = -1;
		
		for (String book : myMap.keySet()) {
			al.add(book);
			if (cnt < myMap.get(book)) {
				cnt = myMap.get(book);
			}
		}
		
		Collections.sort(al);
		for (int i = 0; i < al.size(); i++) {
			if (myMap.get(al.get(i)) == cnt) {
				System.out.println(al.get(i));
				break;
			}
		}

	}

}
