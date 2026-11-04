class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        # give every different value a place number: smallest value = 1, next = 2, ...
        sorted_values = sorted(set(nums))
        size = len(sorted_values)
        place_of = {v: i + 1 for i, v in enumerate(sorted_values)}

        # counting table: how many numbers sit at each place, and their sum
        how_many = [0] * (size + 1)
        total = [0] * (size + 1)

        def change(place, count_change, sum_change):
            while place <= size:
                how_many[place] += count_change
                total[place] += sum_change
                place += place & -place

        def count_and_sum_up_to(place):
            c = s = 0
            while place > 0:
                c += how_many[place]
                s += total[place]
                place -= place & -place
            return c, s

        def middle_place():
            need = (x + 1) // 2          # the middle number is this far from the start
            place = 0
            for power in range(size.bit_length(), -1, -1):
                nxt = place + (1 << power)
                if nxt <= size and how_many[nxt] < need:
                    place = nxt
                    need -= how_many[nxt]
            return place + 1

        # STEP 1 + 2: cost of every chunk of length x
        chunk_cost = [0] * (n - x + 1)
        chunk_sum = 0
        for i in range(n):
            change(place_of[nums[i]], 1, nums[i])         # number enters the chunk
            chunk_sum += nums[i]
            if i >= x:
                change(place_of[nums[i - x]], -1, -nums[i - x])   # number leaves
                chunk_sum -= nums[i - x]
            if i >= x - 1:
                p = middle_place()
                middle = sorted_values[p - 1]
                small_count, small_sum = count_and_sum_up_to(p)   # numbers <= middle
                big_count = x - small_count
                big_sum = chunk_sum - small_sum
                chunk_cost[i - x + 1] = (middle * small_count - small_sum) + (big_sum - middle * big_count)

        # STEP 3: pick k chunks that do not overlap
        best_before = [0] * (n + 1)       # using 0 chunks, cost is 0
        for _ in range(k):
            best_now = [float('inf')] * (n + 1)
            for i in range(x, n + 1):
                skip = best_now[i - 1]
                take = best_before[i - x] + chunk_cost[i - x]
                best_now[i] = min(skip, take)
            best_before = best_now
        return best_before[n]