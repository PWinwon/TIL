import java.util.*;


class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        
        HashMap<Character, Integer> myMap = new HashMap<>();
        for (int i = 0; i < keymap.length; i++) {
            String key = keymap[i];
            for (int j = 0; j < key.length(); j++) {
                char c = key.charAt(j);
                if (!myMap.containsKey(c) || myMap.get(c) > j+1) {
                    myMap.put(c, j+1);
                }
            }
        }
        
        for (int i = 0; i < targets.length; i++) {
            for (int j = 0; j < targets[i].length(); j++) {
                char c = targets[i].charAt(j);
                if (myMap.containsKey(c)) {
                    System.out.println(c + " " + myMap.get(c));
                    answer[i] += myMap.get(c);
                } else {
                    answer[i] = -1;
                    break;
                }
            }
        }
        
        return answer;
    }
}