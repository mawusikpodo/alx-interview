#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list where each element is a list of keys present in a box.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()

    def dfs(box_number):
        """
        Depth-first search to explore the boxes.

        Args:
        - box_number (int): The current box number to explore.
        """
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

