class Search:

    # depth first search
    def depthFirstSearch(self, tree, parent, visited=[]):
        
        # visit the node and store it so that you do not traverse it again
        visited = visited + [parent]

        # get the children of the root node
        children = tree[parent]

        # iterates through all the children
        for child in children:

            # only look at edges that have not been traversed yet
            if child not in visited:

                # recursive call 
                visited = self.depthFirstSearch(tree, child, visited)
        
        # return all visited
        return visited

    def breadthFirstSearch(self, tree, parent, visited=[]):

        # create a queue from a list
        queue = []

        # add the parent node to the queue
        queue.append(parent)

        # mark node as visited to ensure it's not traversed again
        visited = visited + [parent]

        # exit when the queue is empty
        while len(queue) > 0:

            # dequeue element            
            parent = queue.pop(0)

            # get the children of the parent
            children = tree[parent]

            # iterates through all the children
            for child in children:

                # only traverse nodes not already visited
                if child not in visited:
                
                    # add child to queue for exporation
                    queue.append(child)

                    # visit child node
                    visited = visited + [child]

        # return all visited
        return visited

    def binarySearch(self):
        return NotImplemented

