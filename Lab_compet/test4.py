T = int(input())

for _ in range(T):
    n = int(input())
    boxes = list(map(int, input().split()))

    chip_score = 0
    dale_score = 0
    left = 0
    right = n - 1

    while left <= right:
        # Chip's turn
        if (n - left) % 2 == 1:
            if boxes[left] > boxes[right]:
                chip_score += boxes[left]
                left += 1
            else:
                chip_score += boxes[right]
                right -= 1
        # Dale's turn
        else:
            if boxes[left] > boxes[right]:
                dale_score += boxes[left]
                left += 1
            else:
                dale_score += boxes[right]
                right -= 1

    print(chip_score - dale_score)
