class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Find minimum time to swim from top-left to bottom-right.
        Uses Union-Find to connect cells as water level rises.
      
        Args:
            grid: 2D grid where grid[i][j] represents elevation at (i, j)
      
        Returns:
            Minimum time required to reach destination
        """
      
        def find(node: int) -> int:
            """Find root of the set containing node with path compression"""
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]
      
        n = len(grid)
      
        # Initialize Union-Find structure
        # Each cell (i, j) is mapped to index i * n + j
        parent = list(range(n * n))
      
        # Create mapping from elevation to cell position
        # elevation_to_position[h] stores the flattened index of cell with elevation h
        elevation_to_position = [0] * (n * n)
        for row_idx, row in enumerate(grid):
            for col_idx, elevation in enumerate(row):
                elevation_to_position[elevation] = row_idx * n + col_idx
      
        # Process cells in order of increasing elevation (time)
        for time in range(n * n):
            # Get coordinates of cell with current elevation
            current_cell_idx = elevation_to_position[time]
            current_row = current_cell_idx // n
            current_col = current_cell_idx % n
          
            # Check all four adjacent cells
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # left, right, down, up
            for delta_row, delta_col in directions:
                neighbor_row = current_row + delta_row
                neighbor_col = current_col + delta_col
              
                # If neighbor is valid and has elevation <= current time, union them
                if (0 <= neighbor_row < n and 
                    0 <= neighbor_col < n and 
                    grid[neighbor_row][neighbor_col] <= time):
                  
                    neighbor_idx = neighbor_row * n + neighbor_col
                    # Union the two cells
                    parent[find(neighbor_idx)] = find(current_cell_idx)
              
                # Check if start and end are connected
                start_idx = 0  # Top-left corner (0, 0)
                end_idx = n * n - 1  # Bottom-right corner (n-1, n-1)
                if find(start_idx) == find(end_idx):
                    return time
      
        return -1  # Should never reach here for valid input