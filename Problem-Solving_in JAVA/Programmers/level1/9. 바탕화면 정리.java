class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = new int[4];
        
        int minX = wallpaper[0].length();
        int minY = wallpaper.length;
        int maxX = -1;
        int maxY = -1;
        
        for (int r = 0; r < wallpaper.length; r++) {
            for (int c = 0; c < wallpaper[0].length(); c++) {
                if (wallpaper[r].charAt(c) == '#') {
                    if (minY > r) minY = r;
                    if (maxY < r) maxY = r;
                    if (minX > c) minX = c;
                    if (maxX < c) maxX = c;
                }
            }
        }
        
        answer[0] = minY;
        answer[1] = minX;
        answer[2] = maxY+1;
        answer[3] = maxX+1;
        
        return answer;
    }
}