class Solution {
    public boolean isBipartite(int[][] graph) {
        int N = graph.length;
        int[] colors = new int[N];
        
        for (int v = 0; v < N; v++) {
            if (colors[v] == 0 && !validColor(graph, colors, 1, v))
                return false;
        }
        return true;
    }

    private boolean validColor(int[][] graph, int[] colors, int color, int v) {
        if (colors[v] != 0)
            return colors[v] == color;
        
        colors[v] = color;
        for (int neighbor : graph[v]) {
            if (!validColor(graph, colors, -color, neighbor))
                return false;
        }
        return true;
    }
}