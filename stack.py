class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def sort_and_merge(firstlist, secondlist):
    Element = ListNode()
    latest = Element

    while firstlist is not None and secondlist is not None:
        if firstlist.value < secondlist.value:
            latest.next = firstlist
            firstlist = firstlist.next
        else:
            latest.next = secondlist
            secondlist = secondlist.next

        latest = latest.next


    if firstlist is not None:
        latest.next = firstlist
    elif secondlist is not None:
        latest.next = secondlist

    return Element.next

def print_list(head):
    latest = head
    while latest is not None:
        print(latest.value, end="→")
        latest = latest.next
    print("None")


firstlist = ListNode(1, ListNode(2, ListNode(4)))
secondlist = ListNode(1, ListNode(3, ListNode(4)))

merged_list = sort_and_merge(firstlist, secondlist)
print("Merged List:", end=" ")
print_list(merged_list)