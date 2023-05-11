import java.util.*;
import java.io.*;


public class Main
{
    static int N;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static int[][] Map;
    static boolean[][] used;

    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        Map = new int[N][N];
        used = new boolean[N][N];

        for (int r = 0; r < N; r++) {
            char[] temp = br.readLine().toCharArray();
            for (int c = 0; c < N; c++) {
                if (temp[c] == '1') Map[r][c] = 1;
                else Map[r][c] = 0;
            }
        }

        ArrayList<Integer> answer = new ArrayList<Integer>();

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (Map[r][c] == 1 && used[r][c] == false) {
                    answer.add(myBFS(r, c));
                }
            }
        }

        System.out.println(answer.size());
        for (int a = 0; a < answer.size(); a++) {
            System.out.println(answer.get(a));
        }

    }

    public static int myBFS(int sr, int sc) {
        int ret = 0;

        ArrayDeque<Node> que = new ArrayDeque<>();
        que.add(new Node(sr, sc));
        used[sr][sc] = true;

        while (!que.isEmpty()) {
            Node now = que.poll();
            ret++;
            for (int i = 0; i < 4; i++) {
                int yr = now.r + dr[i];
                int xr = now.c + dc[i];
                if (yr < 0 || yr >= N || xr < 0 || xr >= N) continue;
                if (used[yr][xr]) continue;
                if (Map[yr][xr] == 0) continue;
                used[yr][xr] = true;
                que.add(new Node(yr, xr));
            }
        }


        return ret;
    }

    static class Node {
        int r;
        int c;
        Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}