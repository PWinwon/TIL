import java.util.*;


class Solution {
    
    static final int[] dr = {-1, 1, 0, 0};
    static final int[] dc = {0, 0, -1, 1};
    
    static int R, C;
    
    public int solution(int[][] land) {
        int answer = 0;
        
        R = land.length;
        C = land[0].length;

        int ret = -1;
        
        for (int c = 0; c < C; c++) {
            ret = getGas(land, c);
            // System.out.println("c : " + c + " ret : " + ret);
            if (ret > answer) {
                answer = ret;
            }
        }
        
        return answer;
    }
    
    private int getGas(int[][] myMap, int c) {
        boolean[][] visited = new boolean[R][C];
        ArrayDeque<Point> que = new ArrayDeque<>();
        int ret = 0;
        
        for (int r = 0; r < R; r++) {
            if (myMap[r][c] == 1) {
                visited[r][c] = true;
                que.add(new Point(r, c));
            }
        }
        
        while(!que.isEmpty()) {
            Point now = que.pollFirst();
            ret++;
            for (int i = 0; i < 4; i++) {
                int yr = now.y + dr[i];
                int xr = now.x + dc[i];
                if (yr < 0 || yr >= R || xr < 0 || xr >= C) continue;
                if (myMap[yr][xr] == 0) continue;
                if (visited[yr][xr]) continue;
                visited[yr][xr] = true;                
                que.add(new Point(yr, xr));
            }
        }
        
        return ret;        
    }    
}


class Point{
    int y;
    int x;
    Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}
