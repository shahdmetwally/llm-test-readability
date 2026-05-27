import pytest
import queue_example as module_0
#1
# test_case_0
@pytest.mark.parametrize("max_size, expected_length, expected_full_status", [(1256, 1256, False)])
def test_initialization_and_full_status_of_queue(max_size, expected_length, expected_full_status):
    """
    This test verifies the initialization of the Queue class and the full status of an empty queue.
    It checks the type of queue object, the max size, head, tail, size, type and length of data,
    and the full status of the queue.
    The test covers the __init__ and full methods of the Queue class.
    """
    # Setup: Initialize a queue with max size
    queue = module_0.Queue(max_size)

    # Execution: Nothing to execute as we are checking the initial state of the queue

    # Assertions: Check the type, max size, head, tail, size, type and length of data, and full status of the queue
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    assert queue.max == max_size
    assert queue.head == 0
    assert queue.tail == 0
    assert queue.size == 0
    assert f"{type(queue.data).__module__}.{type(queue.data).__qualname__}" == "array.array"
    assert len(queue.data) == expected_length
    assert queue.full() is expected_full_status

# test_case_1
@pytest.mark.parametrize("invalid_max_size", [(-2944)])
def test_queue_initialization_with_negative_size(invalid_max_size):
    """
    This test verifies that initializing the Queue class with a negative max size raises an AssertionError.
    This test case covers the __init__ method of the Queue class.
    """
    # Setup: Nothing to setup as we are checking for an exception on initialization

    # Execution and Assertion: Check if an AssertionError is raised when trying to initialize a queue with a negative size
    with pytest.raises(AssertionError):
        module_0.Queue(invalid_max_size)

# test_case_2
@pytest.mark.parametrize("element_to_enqueue, max_size", [(-726, 2505)])
def test_enqueue_operation(element_to_enqueue, max_size):
    """
    This test verifies the enqueue operation of the Queue class.
    It checks the type of the queue object, the max size, head, tail, size, type and length of data before and after enqueuing an element.
    The test covers the __init__ and enqueue methods of the Queue class.
    """
    # Setup: Initialize a queue with max size
    queue = module_0.Queue(max_size)

    # Execution: Enqueue an element to the queue
    enqueue_status = queue.enqueue(element_to_enqueue)

    # Assertions: Check the type, max size, head, tail, size, type and length of data, and enqueue status of the queue after enqueue operation
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    assert queue.max == max_size
    assert queue.head == 0
    assert queue.tail == 1
    assert queue.size == 1
    assert f"{type(queue.data).__module__}.{type(queue.data).__qualname__}" == "array.array"
    assert len(queue.data) == max_size
    assert enqueue_status is True

# test_case_3
@pytest.mark.parametrize("max_size", [(2423)])
def test_dequeue_operation_on_empty_queue(max_size):
    """
    This test verifies the dequeue operation on an empty Queue.
    It checks the type of the queue object, the max size, head, tail, size, type and length of data before and after the dequeue operation.
    The test covers the __init__ and dequeue methods of the Queue class.
    """
    # Setup: Initialize a queue with max size
    queue = module_0.Queue(max_size)

    # Execution: Dequeue an element from the queue
    dequeued_element = queue.dequeue()

    # Assertions: Check the type, max size, head, tail, size, type and length of data, and dequeued element of the queue after dequeue operation
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    assert queue.max == max_size
    assert queue.head == 0
    assert queue.tail == 0
    assert queue.size == 0
    assert f"{type(queue.data).__module__}.{type(queue.data).__qualname__}" == "array.array"
    assert len(queue.data) == max_size
    assert dequeued_element is None

# test_case_4
@pytest.mark.parametrize("queue_size_1, queue_size_2, element_to_enqueue", [(1001, 649, 2010)])
def test_enqueue_and_dequeue_operations(queue_size_1, queue_size_2, element_to_enqueue):
    """
    This test verifies the enqueue and dequeue operations of the Queue class.
    It checks the type of the queue objects, the max size, head, tail, size, type and length of data, and full status before and after the enqueue and dequeue operations.
    The test covers the __init__, full, enqueue, and dequeue methods of the Queue class.
    """
    # Setup: Initialize three queues with different max sizes
    queue_1 = module_0.Queue(queue_size_1)
    queue_2 = module_0.Queue(queue_size_2)
    queue_3 = module_0.Queue(element_to_enqueue)

    # Execution: Enqueue an element to queue_2 and dequeue it, and dequeue an element from an empty queue (queue_3)
    enqueue_status = queue_2.enqueue(element_to_enqueue)
    dequeued_element = queue_2.dequeue()
    dequeued_element_from_empty_queue = queue_3.dequeue()

    # Assertions: Check the type, max size, head, tail, size, type and length of data, enqueue status, dequeued element, and full status of the queues after enqueue and dequeue operations
    assert f"{type(queue_1).__module__}.{type(queue_1).__qualname__}" == "queue_example.Queue"
    assert f"{type(queue_2).__module__}.{type(queue_2).__qualname__}" == "queue_example.Queue"
    assert f"{type(queue_3).__module__}.{type(queue_3).__qualname__}" == "queue_example.Queue"
    assert queue_1.max == queue_size_1
    assert queue_2.max == queue_size_2
    assert queue_3.max == element_to_enqueue
    assert queue_1.full() is False
    assert queue_2.full() is False
    assert queue_3.full() is False
    assert enqueue_status is True
    assert dequeued_element == element_to_enqueue
    assert dequeued_element_from_empty_queue is None
    assert queue_2.size == 0

# test_case_5
@pytest.mark.parametrize("queue_size, element_to_enqueue", [(1235, 4904)])
def test_enqueue_operation_and_empty_status(queue_size, element_to_enqueue):
    """
    This test verifies the enqueue operation and the empty status of the Queue class.
    It checks the type of the queue object, the max size, head, tail, size, type and length of data, and empty status before and after the enqueue operation.
    The test covers the __init__, empty, and enqueue methods of the Queue class.
    """
    # Setup: Initialize a queue with max size
    queue = module_0.Queue(queue_size)

    # Execution: Enqueue an element to the queue
    enqueue_status = queue.enqueue(element_to_enqueue)

    # Assertions: Check the type, max size, head, tail, size, type and length of data, enqueue status, and empty status of the queue after enqueue operation
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    assert queue.max == queue_size
    assert queue.head == 0
    assert queue.tail == 1
    assert queue.size == 1
    assert f"{type(queue.data).__module__}.{type(queue.data).__qualname__}" == "array.array"
    assert len(queue.data) == queue_size
    assert queue.empty() is False
    assert enqueue_status is True

# test_case_6
@pytest.mark.parametrize("queue_size, element_to_enqueue, enqueue_element_2", [(1187, 1441, 2245)])
def test_enqueue_dequeue_full_empty_operations(queue_size, element_to_enqueue, enqueue_element_2):
    """
    This test verifies the enqueue, dequeue, full, and empty operations of the Queue class.
    It checks the type of the queue object, the max size, head, tail, size, type and length of data,
    full and empty status before and after the enqueue and dequeue operations.
    The test covers the __init__, full, empty, enqueue, and dequeue methods of the Queue class.
    """
    # Setup: Initialize a queue with max size
    queue = module_0.Queue(queue_size)

    # Execution: Enqueue an element to the queue, dequeue it, and then enqueue another element
    enqueue_status_1 = queue.enqueue(element_to_enqueue)
    dequeued_element = queue.dequeue()
    enqueue_status_2 = queue.enqueue(enqueue_element_2)

    # Assertions: Check the type, max size, head, tail, size, type and length of data,
    # enqueue status, dequeued element, and full and empty status of the queue after enqueue and dequeue operations
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    assert queue.max == queue_size
    assert queue.head == 1
    assert queue.tail == 2
    assert queue.size == 1
    assert f"{type(queue.data).__module__}.{type(queue.data).__qualname__}" == "array.array"
    assert len(queue.data) == queue_size
    assert queue.empty() is False
    assert queue.full() is False
    assert enqueue_status_1 is True
    assert enqueue_status_2 is True
    assert dequeued_element == element_to_enqueue

# test_case_7
@pytest.mark.parametrize("queue_size_1, queue_size_2, element_to_enqueue_1, invalid_size, element_to_enqueue_2",
                         [(1187, 1080, 1187, -30, 1441)])
def test_enqueue_dequeue_operations_and_negative_initialization(queue_size_1, queue_size_2, element_to_enqueue_1, element_to_enqueue_2, invalid_size):
    """
    This test verifies the enqueue and dequeue operations of the Queue class and the initialization with a negative size.
    It checks the type of the queue object, the max size, head, tail, size, type and length of data,
    and full and empty status before and after the enqueue and dequeue operations, and also checks for an AssertionError when trying to initialize with a negative size.
    The test covers the __init__, full, enqueue, and dequeue methods of the Queue class.
    """
    # Setup: Initialize two queues with max sizes
    queue_1 = module_0.Queue(queue_size_1)
    queue_2 = module_0.Queue(queue_size_2)

    # Execution: Enqueue an element to queue_1 and dequeue it, then try to initialize a queue with a negative size
    enqueue_status_1 = queue_1.enqueue(element_to_enqueue_1)
    dequeued_element_1 = queue_1.dequeue()
    with pytest.raises(AssertionError):
        module_0.Queue(invalid_size)
    enqueue_status_2 = queue_2.enqueue(element_to_enqueue_2)
    dequeued_element_2 = queue_2.dequeue()

    # Assertions: Check the type, max size, head, tail, size, type and length of data,
    # enqueue status, dequeued element, and full and empty status of the queues after enqueue and dequeue operations
    assert f"{type(queue_1).__module__}.{type(queue_1).__qualname__}" == "queue_example.Queue"
    assert f"{type(queue_2).__module__}.{type(queue_2).__qualname__}" == "queue_example.Queue"
    assert queue_1.max == queue_size_1
    assert queue_2.max == queue_size_2
    assert queue_1.head == 1
    assert queue_2.head == 1
    assert queue_1.tail == 1
    assert queue_2.tail == 1
    assert queue_1.size == 0
    assert queue_2.size == 0
    assert f"{type(queue_1.data).__module__}.{type(queue_1.data).__qualname__}" == "array.array"
    assert f"{type(queue_2.data).__module__}.{type(queue_2.data).__qualname__}" == "array.array"
    assert len(queue_1.data) == queue_size_1
    assert len(queue_2.data) == queue_size_2
    assert queue_1.empty() is True
    assert queue_2.empty() is True
    assert queue_1.full() is False
    assert queue_2.full() is False
    assert enqueue_status_1 is True
    assert enqueue_status_2 is True
    assert dequeued_element_1 == element_to_enqueue_1
    assert dequeued_element_2 == element_to_enqueue_2
