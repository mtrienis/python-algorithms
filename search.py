from queue import Queue

# A class for search algorithms
class Search:

    # depth first search
    def depth_first_search(self, tree, parent, visited=[]):
        
        # visit the node and store it so that you do not traverse it again
        visited = visited + [parent]

        # get the children of the root node
        children = tree[parent]

        # iterates through all the children
        for child in children:

            # only look at edges that have not been traversed yet
            if child not in visited:

                # recursive call 
                visited = self.depth_first_search(tree, child, visited)
        
        # return all visited
        return visited

    # breadth first search
    def breadth_first_search(self, tree, parent, visited=[]):

        # create a queue from a list
        queue = Queue()

        # add the parent node to the queue
        queue.enqueue(parent)

        # mark node as visited to ensure it's not traversed again
        visited = visited + [parent]

        # exit when the queue is empty
        while queue.is_empty() == False:

            # dequeue element            
            parent = queue.dequeue()

            # get the children of the parent
            children = tree[parent]

            # iterates through all the children
            for child in children:

                # only traverse nodes not already visited
                if child not in visited:
                
                    # add child to queue for exporation
                    queue.enqueue(child)

                    # visit child node
                    visited = visited + [child]

        # return all visited
        return visited

    # 
    def binary_search(self, b_tree):
        return NotImplemented

