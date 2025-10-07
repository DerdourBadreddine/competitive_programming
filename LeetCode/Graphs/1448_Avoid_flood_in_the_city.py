# 🧠 Problem: Avoid Flood in The City
# Platform: LeetCode
# Author: Badreddine 
# Method: Greedy + SortedList

from typing import List
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        # nmedlo -1 par defaut (youm fih chtaa)
        result = [-1] * n

        # had list n7ot fiha liyam li fihom chams bach nchofo win n9dro njfou bihom any lake
        sunny_days = SortedList()

        # had dict y7at fih a5er nhar t3mrat fih lake
        # key = num dyal lake, value = nhar li jat fih chtaa 3liha
        last_rain_day = {}

        for day, lake in enumerate(rains):
            if lake > 0:
                # nhar fih chtaa (lake > 0)
                # check wach had l lake t3mrat ou nn mn 9bl
                if lake in last_rain_day:
                    # donc lzm n7awso 3la nhar fih chams ba3d a5er marra t3mrat
                    sunny_day_idx = sunny_days.bisect_right(last_rain_day[lake])

                    # ila makanch ayyam chams ba3d had nhar => had l flood rahet (ma3ndna ma ndirou)
                    if sunny_day_idx == len(sunny_days):
                        return []

                    # nhar li na9dro nechfo fih had lake
                    dry_day = sunny_days[sunny_day_idx]
                    result[dry_day] = lake

                    # na7iw had nhar mn sunny_days 
                    sunny_days.discard(dry_day)

                # nupdate l nhar li jat fih chtaa 3la had lake
                last_rain_day[lake] = day

            else:
                # nhar ta3 chams (lake == 0)
                # nzido had nhar f sunny_days bach n9dro nkhdmo bih
                sunny_days.add(day)
                # par defaut, nktebo 1 (ta9dr tbdlha ay lake valid)
                result[day] = 1

        return result
