def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = set()
    
    # DFS function to explore the boxes
    def dfs(box_number):
        # If the box is already opened, return
        if box_number in opened_boxes:
            return
        
        # Mark the box as opened
        opened_boxes.add(box_number)
        
        # Explore the keys in the current box
        for key in boxes[box_number]:
            dfs(key)
    
    # Start DFS from the first box
    dfs(0)
    
    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
