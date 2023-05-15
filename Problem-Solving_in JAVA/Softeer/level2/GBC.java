import java.util.*;
import java.io.*;


public class Main
{
    static int N, M;
    static int[] limitSpeed = new int[100];
    static int[] testSpeed = new int[100];

    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int idx = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            fillArray(idx, a, b, limitSpeed);
            idx += a;
        }

        idx = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            fillArray(idx, a, b, testSpeed);
            idx += a;
        }


        // for (int i = 0; i < 100; i++) {
        //     System.out.print(limitSpeed[i] + " ");
        // }
        // System.out.println();
        // for (int i = 0; i < 100; i++) {
        //     System.out.print(testSpeed[i] + " ");
        // }
        // System.out.println();

        int answer = 0;
        for (int i = 0; i < 100; i++) {
            if (testSpeed[i] - limitSpeed[i] > answer) answer = testSpeed[i] - limitSpeed[i];
        }

        System.out.println(answer);
    }

    public static void fillArray(int start, int lng, int speed, int[] arr) {
        for (int i = start; i < start + lng; i++) {
            arr[i] = speed;
        }
    }
}