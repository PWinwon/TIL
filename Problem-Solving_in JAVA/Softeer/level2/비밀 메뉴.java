import java.util.*;
import java.io.*;


public class Main
{
    static int M;
    static int N;
    static int K;

    static int[] secretN;
    static int[] userN;

    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        secretN = new int[M];
        userN = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < M; i++) {
            secretN[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            userN[i] = Integer.parseInt(st.nextToken());
        }

        boolean isSecret = false;
        int idx = 0;

        while (idx < N && !isSecret) {
            if (userN[idx] == secretN[0]){
                if (chkSecret(idx)) isSecret = true;
            }
            idx++;
        }

        if (isSecret) System.out.println("secret");
        else System.out.println("normal");

    }

    public static boolean chkSecret(int idx) {
        int ret = 0;
        int sIdx = 0;
        while (idx < N && sIdx < M) {
            if (userN[idx] == secretN[sIdx]) ret++;
            else break;
            idx++;
            sIdx++;
        }

        if (ret == M) return true;
        return false;

    }
}