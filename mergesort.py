class MergeSort:

    # merge sort
    def merge_sort(self, items=[]):

        if len(items) < 2:
            return items

        middle_items_index = len(items) / 2
        right_items = items[:middle_items_index]
        left_items = items[middle_items_index:]

        return self.merge(
                    self.merge_sort(right_items), 
                    self.merge_sort(left_items)
                )

    # merge and sorts two sets
    def merge(self, left_items=[], right_items=[]):

        sorted_items = []

        left_items_index = right_items_index = 0

        # generate a sorted array by merging two sets together
        while left_items_index < len(left_items) and right_items_index < len(right_items):

            if left_items[left_items_index] < right_items[right_items_index]:
                sorted_items.append(left_items[left_items_index])
                left_items_index += 1
            else:
                sorted_items.append(right_items[right_items_index])
                right_items_index += 1


        # the remaining elements are already sorted since it is either a singleton or previously sorted set
        sorted_items += left_items[left_items_index:] 
        sorted_items += right_items[right_items_index:]

        return sorted_items