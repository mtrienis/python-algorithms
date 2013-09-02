class DepthFirstSearch:

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