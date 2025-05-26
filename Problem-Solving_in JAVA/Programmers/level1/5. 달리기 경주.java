import java.util.*;


class Solution {
    public String[] solution(String[] players, String[] callings) {
        
        HashMap<String, Integer> myMap = new HashMap<>();
        int idx = 0;
        for (String player : players) {
            myMap.put(player, idx);
            idx++;
        }
        
        for (String calling : callings) {
            // 불린 친구 index 찾아
            int nowIdx = myMap.get(calling);
            int targetIdx = nowIdx-1;
            
            String targetPlayer = players[targetIdx];
            players[targetIdx] = calling;
            players[nowIdx] = targetPlayer;
            
            myMap.put(calling, targetIdx);
            myMap.put(targetPlayer, nowIdx);
        }
        
        return players;
    }
}