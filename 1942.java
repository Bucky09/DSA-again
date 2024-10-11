class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        int n = times.length;
        int[][] friends = new int[n][4];

        for (int i = 0; i < n; i++) {
            friends[i][0] = times[i][0];
            friends[i][1] = times[i][1];
            friends[i][2] = i;
        }

        Arrays.sort(friends, (f1, f2) -> f1[0] - f2[0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((f1, f2) -> f1[1] - f2[1]);
        PriorityQueue<Integer> availableSeats = new PriorityQueue<>();
        int nextSeat = 0;

        for (int[] f : friends) {
            while (!pq.isEmpty() && pq.peek()[1] <= f[0]) {
                availableSeats.add(pq.poll()[3]);
            }
            int seat = availableSeats.isEmpty() ? nextSeat++ : availableSeats.poll();
            if (targetFriend == f[2]) return seat;
            f[3] = seat;
            pq.add(f);
        }
        return -1;
    }
}
