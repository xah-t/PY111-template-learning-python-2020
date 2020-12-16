"""
My little Queue
"""
from typing import Any


my_gueue = [] #конец справа


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """

    my_gueue.append(elem)
    #print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """

    return my_gueue.pop(0) if my_gueue else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """

    print(ind)
    return None if ind >= len(my_gueue) else my_gueue[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """

    my_gueue.clear()
    return None


if __name__ == '__main__':
    enqueue("aerfg")
    enqueue(25)
    clear()
    print(my_gueue)
    dequeue()
    enqueue(256)
    print(my_gueue)
    enqueue(236)
    print(my_gueue)
    print(peek(0))
    print(my_gueue)



