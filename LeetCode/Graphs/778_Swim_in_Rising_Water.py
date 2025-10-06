# 🧠 Problem: Swim in Rising Water
# Platform: LeetCode
# Author: Badreddine 
# Method: Union-Find (Disjoint Set)

from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        L'objectif:
            nkemlo nwaslo men coin l fou9 (0,0) l coin l taht (n-1,n-1)
            waqt ma lma ytla3 chwiya b chwiya.
            kull cella twli maftouha f waqt = elevation dyalha.

        L'idea:
            nbda b waqt 0 o nzid hata n*n.
            kull mara nchouf ida cells jdod tftaho,
            nwaslhom (union) m3a les voisins li rahom maftouhin.
            ida start o end tslslo (connected) => cbn njbo result.
        """

        n = len(grid)
        parent = list(range(n * n))  # parents dial Union-Find

        def find(x: int) -> int:
            """tjib l root dyal cella b path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            """twasel zouj cells m3a b3d."""
            parent[find(a)] = find(b)

        # mapping dyal elevation -> index dyal cella fel grid
        pos = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = i * n + j

        # simulation dyal waqt men 0 7ata n*n - 1
        for t in range(n * n):
            idx = pos[t]
            r, c = divmod(idx, n)

            # teb3at check l 4 jihat
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # ila voisin maytla3sh 3la waqt donc => nwaslohom
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
                    union(idx, nr * n + nc)
            
            if find(0) == find(n * n - 1):
                return t

        return -1  # ma khasnach nwslo hna
