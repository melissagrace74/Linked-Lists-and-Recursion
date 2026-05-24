from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_front(5)

    # 3) Display the list
    print("Original List:")
    ll.display()

    # 4) Recursive sum
    total = ll.recursive_sum()
    print("Recursive Sum:", total)

    # 5) Recursive search
    target = 20
    found = ll.recursive_search(target)
    print(f"Search {target}:", found)

    # 6) Recursive reverse + display
    ll.recursive_reverse()
    print("Reversed List:")
    ll.display()
    