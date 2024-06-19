from collections import deque
def max_kernel(num_list, k):
  dq = deque()
  res = []

  for i in range(k):
        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()
        dq.append(i)
  res.append(num_list[dq[0]])

  for i in range(k, len(num_list)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()

        dq.append(i)
        res.append(num_list[dq[0]])

  return res

if __name__ == "__main__":
    assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_kernel(num_list, k))  # [5, 5, 5, 5, 10, 12, 33, 33]
    