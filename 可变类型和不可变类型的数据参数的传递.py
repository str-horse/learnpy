def test(a):
    a = 100


def demo(nums):
    nums[0] = 10


x = 1
test(x)
print(x)  # 1

y = [3, 5, 6, 2, 6, 7]
demo(y)
print(y)  # [10, 5, 6, 2, 6, 7]
