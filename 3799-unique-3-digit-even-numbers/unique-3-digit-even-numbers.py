
class Solution(object):
    def totalNumbers(self, digits):
        freq = Counter(digits)
        valid_count = 0

        # Check all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10

            req = Counter([d1, d2, d3])

            # Check if all required digits are available in sufficient quantities
            if all(freq[d] >= req[d] for d in req):
                valid_count += 1

        return valid_count
        