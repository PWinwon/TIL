import java.util.*;
import java.io.*;


public class Main
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int W = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        // VVS[] vvss = new VVS[N];
        PriorityQueue<VVS> pq = new PriorityQueue<VVS>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            pq.add(new VVS(w, p));
        }

        int bag = 0;
        int answer = 0;

        while (bag <= W && !pq.isEmpty()) {
            VVS vvs = pq.poll();
            int nowW = Math.min(vvs.w, W - bag);
            int nowP = vvs.p;
            bag += nowW;
            answer += nowP * nowW;
        }

        System.out.println(answer);

    }

    static class VVS implements Comparable<VVS> {
        int w;
        int p;

        VVS(int w, int p) {
            this.w = w;
            this.p = p;
        }

        @Override
        public int compareTo(VVS o) {
            return o.p - this.p;
        }

    }
}