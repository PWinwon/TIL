import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int A[] = new int[N];
		for (int i = 0; i < N; i++) {
			A[i] = sc.nextInt();
		}
//		System.out.print(A[0]);
		
		int s = 0;
		int max_value = -1;
		
		for (int i = 0; i < N; i++) {
			if (A[i] > max_value) {
				max_value = A[i];
			}
			s += A[i];
		}
		System.out.println((s * 100.0) / max_value / N);
//		System.out.println(max_value);

	}

}
