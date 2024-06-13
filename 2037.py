class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))
