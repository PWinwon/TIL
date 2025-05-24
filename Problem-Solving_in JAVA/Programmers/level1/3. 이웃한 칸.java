class Solution {
    
    static int N;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        
        N = board.length;
        
        for (int i = 0; i < 4; i++) {
            int r = h + dr[i];
            int c = w + dc[i];
            if (r < 0 || r >= N || c < 0 || c >= N) continue;
            if (board[r][c].equals(board[h][w])) answer++;
        }
        
        
        return answer;
    }
}