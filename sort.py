class Sort:

    # recursive solution
    def quick_sort(self):
        return NotImplemented

    # recursive solution
    def merge_sort(self, items=[]):
        if len(items) < 2:
            return items

        middle = len(items) / 2

        return self.merge(
                    self.merge_sort(items[:middle]), 
                    self.merge_sort(items[middle:])
                )

    # private function for merge sort
    def merge(self, left=[], right=[]):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1


        result += left[i:]
        result += right[j:]

        return result


    def bucket_sort(self):
        return NotImplemented