class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        max_count = 0
        max_freq = 0
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            if max_freq == freq[ord(task) - ord('A')]:
                max_count += 1
            elif max_freq < freq[ord(task) - ord('A')]:
                max_freq = freq[ord(task) - ord('A')]
                max_count = 1

        gap_count = max_freq - 1
        gap_length = n - (max_count - 1)
        empty = gap_count * gap_length
        available_tasks = len(tasks) - max_freq * max_count
        idles = max(0, empty - available_tasks)

        return len(tasks) + idles
