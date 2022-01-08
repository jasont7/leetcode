class Solution {
    public String frequencySort(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (!map.containsKey(c))
                map.put(c, 1);
            else map.put(c, map.get(c)+1);
        }

        TreeMap<Integer, ArrayList<Character>> tmap = new TreeMap<>();
        for (char c : map.keySet()) {
            int freq = map.get(c);
            if (tmap.containsKey(freq))
                tmap.get(freq).add(c);
            else {
                ArrayList<Character> newList = new ArrayList<>();
                newList.add(c);
                tmap.put(freq, newList);
            }
        }

        StringBuilder result = new StringBuilder();
        for (int freq : tmap.descendingKeySet()) {
            for (char c : tmap.get(freq)) {
                for (int i=0; i < freq; i++)
                    result.append(c);
            }
        }
        return result.toString();
    }
}