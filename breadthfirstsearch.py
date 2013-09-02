from queue import Queue

class BreadthFirstSearch:

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