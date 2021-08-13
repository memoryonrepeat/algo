def isPresent (root,val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not
    if not root:
        return 0
    if val==root.value:
        return 1
    return isPresent(root.left, val) if val<root.value else isPresent(root.right, val)