class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        
        for (int n = 0; n < mats.length; n++) {
            for (int r = 0; r < park.length; r++) {
                for (int c = 0; c < park[r].length; c++) {
                    if (park[r][c].equals("-1")) {
                        if (isSquare(mats[n], r, c, park)) {
                            if (answer < mats[n]) {
                                answer = mats[n];
                            }
                        }
                    }
                }
            }
        }
        
        return answer;
    }
    
    private static boolean isSquare(int n, int sr, int sc, String[][] p) {
        boolean ret = true;
        
        for (int r = sr; r < sr + n; r++) {
            for (int c = sc; c < sc + n; c++) {
                if (r >= p.length || c >= p[r].length) return false;
                if (!p[r][c].equals("-1")) return false;
            }
        }
        
        
        return ret;
    }
}