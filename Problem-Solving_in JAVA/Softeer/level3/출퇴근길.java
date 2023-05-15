import java.util.*;
import java.io.*;


public class Main
{
    static int N, S, T;

    // Map과 역방향 Map
    static ArrayList<Integer>[] Map;
    static ArrayList<Integer>[] MapR;

    // 방문배열 정방향과 역방향
    static boolean[] usedS;
    static boolean[] usedSR;
    static boolean[] usedT;
    static boolean[] usedTR;

    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map = new ArrayList[N+1];
        MapR = new ArrayList[N+1];

        usedS = new boolean[N+1];
        usedSR = new boolean[N+1];
        usedT = new boolean[N+1];
        usedTR = new boolean[N+1];

        for (int i = 0; i <= N; i++) {
            Map[i] = new ArrayList<Integer>();
            MapR[i] = new ArrayList<Integer>();
        }

        for (int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Map[a].add(b);
            MapR[b].add(a);
        }

        st = new StringTokenizer(br.readLine());

        S = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        usedS[T] = true;
        myBfs(S, T, Map, usedS);
        usedT[S] = true;
        myBfs(T, S, Map, usedT);
        // for (int i = 1; i < N+1; i++) {
        //     System.out.print(used[i] + " ");
        // }
        // System.out.println();

        myBfs(S, T, MapR, usedSR);
        myBfs(T, S, MapR, usedTR);

        // for (int i = 1; i < N+1; i++) {
        //     System.out.print(usedR[i] + " ");
        // }
        // System.out.println();

        int answer = 0;

        for (int i = 1; i < N+1; i++) {
            if (i == S || i == T) continue;
            if (usedS[i] && usedSR[i] && usedT[i] && usedTR[i]) answer++;
        }

        System.out.println(answer);
    }


    static public void myBfs(int start, int end, ArrayList<Integer>[] myMap, boolean[] myUsed) {

        ArrayDeque<Integer> que = new ArrayDeque<Integer>();
        que.add(start);
        myUsed[start] = true;

        while (!que.isEmpty()) {
            int now = que.poll();
            // if (now == end) continue;
            for (int next : myMap[now]) {
                if (myUsed[next]) continue;
                myUsed[next] = true;
                que.add(next);
            }
        }
    }
}