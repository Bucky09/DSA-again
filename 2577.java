class Node{

    int x;
    int y;
    int time;
    Node(int xx, int yy, int tt){
        x = xx;
        y = yy;
        time = tt;
    }

}

class Solution {
    public int minimumTime(int[][] grid) {
        
        int m = grid.length;
        int n = grid[0].length;

        if(grid[0][1] > 1  && grid[1][0] > 1) return -1;

        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.time - b.time);

        pq.add(new Node(0, 0, 0));

        int[] xdir = { 0, 0, 1, -1};
        int[] ydir = { 1, -1, 0, 0};

        int[][] vis = new int[m][n];
        for(int[] temp: vis) Arrays.fill(temp, -1);

        while(!pq.isEmpty()){

            Node curr = pq.remove();

            if(curr.x == m-1 && curr.y == n-1) return curr.time;

            vis[curr.x][curr.y] = 1;

            int curr_time = curr.time + 1;
            
            for(int i =0; i<4; i++){
                int newx = curr.x + xdir[i];
                int newy = curr.y + ydir[i];

                if(newx >= 0 && newy >= 0 && newx <m && newy < n && vis[newx][newy] == -1)
                {

                    vis[newx][newy] =1;

                    if(grid[newx][newy] <= curr_time){
                        pq.add(new Node(newx, newy, curr_time));
                    }
                    else{
                        if(( grid[newx][newy] - curr.time) % 2 == 0){
                            pq.add(new Node(newx, newy, grid[newx][newy] +1 ));
                        } else{
                            pq.add(new Node(newx, newy, grid[newx][newy] ));
                        }
                    }
                }
            }
        }


        return -1;
    }

}
