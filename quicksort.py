class QuickSort:

    # quicksort
    def quick_sort(self, items, left, right):

        index = self.partition(items, left, right)

        if left < index - 1:
            self.quick_sort(items, left, index - 1)

        if index < right:
            self.quick_sort(items, index, right)


        print str(index) + " " + str(left) + " " + str(right)
        print items

    def partition(self, items, left, right):

        pivot = items[(left+right) / 2]

        while (left <= right):

            # move the left pointer up until you find a value >= to the pivot value
            while (items[left] < pivot):
                left += 1

            # move the right pointer down until you find a value <= to the pivot value
            while (items[right] > pivot):
                right -= 1

            # only swap if the left index is <= to the right index
            if left <= right:
                items = self.swap(items, left, right)  
                left += 1
                right -= 1
                
        return left

    def swap(self, items, left, right):

        temp = items[right]
        items[right] = items[left]
        items[left] = temp

        return items