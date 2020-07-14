class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        deg_per_min = 6
        deg_per_hour = 30

        min_hand = minutes * deg_per_min
        hour_hand = (hour % 12 + float(minutes) / 60) * deg_per_hour

        diff = abs(hour_hand - min_hand)

        return min(diff, 360 - diff)


if __name__ == '__main__':
    s = Solution()
    print(s.angleClock(4, 40))
