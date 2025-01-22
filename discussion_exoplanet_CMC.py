"""Linked list for 03B Exoplanet Discussion."""

from exoplanet_node import exoplanetNode

class LinkedList:
    """Create a generic linked list."""
    def __init__(self):
        self.head = None

    def push(self, node):
        """Add note to head of list."""
        new_node = node
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> exoplanetNode:
        """Remove the earliest item on list."""
        temp_node = self.head
        self.head = temp_node.next
        return temp_node

    def _print_nodes(self, node):
        """Print all nodes from given node using recursion."""
        if node is None:  # base case
            return
        else:
            self._print_nodes(node.next)
            print(node, "\n")

    def print_all_nodes(self):
        """Print all nodes in list."""
        print("\nPrinting all nodes:")
        self._print_nodes(self.head)

    def _find_parent_node(self, child_ID) -> exoplanetNode:
        """Find parent node of node with child_ID."""
        parent_node = self.head
        next_node = self.head.next
        while next_node is not None:
            if next_node.ID == child_ID:
                return parent_node
            if next_node is None:
                return None
            else:
                parent_node = next_node
                next_node = next_node.next

    def find_ID(self, ID):
        """Find and print node with given ID."""
        parent_node = self._find_parent_node(ID)
        if parent_node is None:
            print("Error: ID not found")
        else:
            print("Found a match!")
            print(parent_node.next)

    def delete_ID(self, ID):
        """Find and print node with given ID."""
        parent_node = self._find_parent_node(ID)
        if parent_node is None:
            print("Error: ID not found")
        else:
            parent_node.remove_after()
            print(f"\nDeleted {ID}")

def main():
    # create linked list
    exoplanet_list = LinkedList()
    exoplanet_list.push(exoplanetNode("1-HD-191939-e", 0.397, 101.5, 2022, 0.33981))
    exoplanet_list.push(exoplanetNode("2-TOI-4504 d", 1.425, 323.1, 2024, 1.4166))
    exoplanet_list.push(exoplanetNode("3-KMT-2024-BLG-1044L b", 218.5, 333, 2024, 1.0))
    exoplanet_list.push(exoplanetNode("4-TOI-5688 A b", 0.967, 395.2, 2020, 0.39))
    exoplanet_list.push(exoplanetNode("5-TOI-6383", 0.529, 122.8, 2018, 0.85))

    # print list, then remove last added node and reprint remaining list
    exoplanet_list.print_all_nodes()
    print("*** Test removing (pop) last added node")
    exoplanet_list.pop()
    exoplanet_list.print_all_nodes()

    # find and delete exoplanet with a particular ID
    print("*** Test finding and then deleting exoplanet with ID '2-TOI-4504 d'")
    exoplanet_list.find_ID("2-TOI-4504 d")
    exoplanet_list.delete_ID("2-TOI-4504 d")
    exoplanet_list.print_all_nodes()


if __name__ == "__main__":
    main()
