class Solution {
                            //북, 남, 서, 동
    static final int[] dr = {-1, 1, 0, 0};
    static final int[] dc = {0, 0, -1, 1};
    
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {0, 0};
        
        Puppy puppy = new Puppy(-1, -1);
        
        for (int r = 0; r < park.length; r++) {
            for (int c = 0; c < park[r].length(); c++) {
                if (park[r].charAt(c) == 'S') {
                    puppy = new Puppy(r, c);
                }
            }
        }
        
        // System.out.println("y : " + puppy.y + " x : " + puppy.x);
        
        for (String route : routes) {
            String[] r = route.split(" ");
            char dir = r[0].charAt(0);
            int n = Integer.parseInt(r[1]);
            int idx = -1;
            
            switch (dir) {
                case 'N':
                    idx = 0;
                    break;
                case 'S':
                    idx = 1;
                    break;
                case 'W':
                    idx = 2;
                    break;
                case 'E':
                    idx = 3;
                    break;
                default:
                    break;
            }
            
            // int yr = puppy.y + dr[idx] * n;
            // int xr = puppy.x + dc[idx] * n;
            int yr = puppy.y;
            int xr = puppy.x;
            
            boolean flag = true;
            for (int i = 0; i < n; i ++) {
                yr += dr[idx];
                xr += dc[idx];
                if (yr < 0 || yr >= park.length || xr < 0 || xr >= park[0].length()) {
                    flag = false;
                    break;
                }
                if (park[yr].charAt(xr) == 'X') {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                puppy.move(dr[idx]*n, dc[idx]*n);
                // System.out.println("y : " + puppy.y + " x : " + puppy.x);   
            }
        }
        
        answer[0] = puppy.y;
        answer[1] = puppy.x;
        
        return answer;
    }
}


class Puppy {
    int y;
    int x;
    Puppy(int y, int x) {
        this.y = y;
        this.x = x;
    }
    
    public void move(int y, int x) {
        this.y += y;
        this.x += x;
    }
}