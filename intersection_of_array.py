from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        result = set()

        for num in nums2:
            if num in nums1_set:
                result.add(num)

        return list(result)


if __name__ == "__main__":
    # Take input from terminal
    nums1_input = input("Enter elements of nums1 separated by space: ")
    nums2_input = input("Enter elements of nums2 separated by space: ")

    nums1 = list(map(int, nums1_input.split()))
    nums2 = list(map(int, nums2_input.split()))

    sol = Solution()
    output = sol.intersection(nums1, nums2)

    print("Intersection:", output)


"""
to run : python ./intersection_of_array.py
enter numbers of both list

git status
git add intersection_of_array.py
git commit -m "Intersection of Two Array"
git push

"""