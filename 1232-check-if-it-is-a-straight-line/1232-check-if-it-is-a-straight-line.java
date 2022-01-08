class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        if (coordinates.length <= 2)
            return true;

        int x1 = coordinates[0][0];
        int y1 = coordinates[0][1];
        int x2 = coordinates[1][0];
        int y2 = coordinates[1][1];

        for (int c = 2; c < coordinates.length; c++) {
            int xc = coordinates[c][0];
            int yc = coordinates[c][1];
            if (!collinear(x1,y1,x2,y2,xc,yc))
                return false;
        }

        return true;
    }

    public boolean collinear(int x1, int y1, int x2, int y2, int x3, int y3) {
        int a = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2);
        return a == 0;
    }
}