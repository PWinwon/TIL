import java.util.*;


class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int[][] answer = {};
        
        HashMap<String, Integer> extMap = new HashMap<>();
        extMap.put("code", 0);
        extMap.put("date", 1);
        extMap.put("maximum", 2);
        extMap.put("remain", 3);
        
        ArrayList<int []> filteredLst = new ArrayList<>();
        for (int i = 0; i < data.length; i++) {
            int[] now = data[i];
            if (now[extMap.get(ext)] < val_ext) {
                filteredLst.add(now);
            }
        }
        
        filteredLst.sort(Comparator.comparing(x -> x[extMap.get(sort_by)]));
        
        return filteredLst.toArray(int[][]::new);
    }
}