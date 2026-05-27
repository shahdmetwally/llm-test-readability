import pytest
import queue_example as queue_module
import array

def test_queue_initialization():
    max_size = 2505
    initial_value = -726
    queue = queue_module.Queue(max_size)
    
    # Check queue type
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    
    # Check queue properties
    assert queue.max_size == max_size
    assert queue.head == 0
    assert queue.tail == 0
    assert queue.size == 0
    
    # Check data type and length
    assert f"{type(queue.data).__module__}.{type(queue).__qualname__}" == "array.array"
    assert len(queue.data) == max_size
    
    # Enqueue an element
    is_enqueued = queue.enqueue(initial_value)
    assert is_enqueued is True
    assert queue.tail == 1
    assert queue.size == 1

def test_invalid_queue_size_input():
    invalid_size = -2944
    with pytest.raises(AssertionError):
        queue_module.Queue(invalid_size)

def test_queue_dequeue_on_empty_queue():
    max_size = 2423
    queue = queue_module.Queue(max_size)
    
    # Check dequeue on an empty queue
    dequeued_element = queue.dequeue()
    assert dequeued_element is None
    
    # Check if the queue is full (should be False)
    is_full = queue.full()
    assert is_full is False
    
    # Check that creating a queue with a size of 0 raises an AssertionError
    with pytest.raises(AssertionError):
        queue_module.Queue(0)

def test_queue_initialization_and_operations():
    # Setup
    max_size = 1001
    queue = queue_module.Queue(max_size)

    # Assert queue initialization
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    assert queue.max_size == max_size
    assert queue.head == 0
    assert queue.tail == 0
    assert queue.size == 0
    assert f"{type(queue.data).__module__}.{type(queue).__qualname__}" == "array.array"
    assert len(queue.data) == max_size

    # Test with different max sizes
    small_max_size = 649
    small_queue = queue_module.Queue(small_max_size)
    assert small_queue.head == 0
    assert small_queue.tail == 0
    assert small_queue.size == 0

    large_max_size = 3263
    large_queue = queue_module.Queue(large_max_size)
    assert large_queue.head == 0
    assert large_queue.tail == 0
    assert large_queue.size == 0

    # Test queue full condition
    is_full = large_queue.full()
    assert is_full is False

    # Enqueue and dequeue operations
    element = 2010
    enqueue_result = small_queue.enqueue(element)
    assert enqueue_result is True
    assert small_queue.tail == 1
    assert small_queue.size == 1

    dequeued_element = small_queue.dequeue()
    assert dequeued_element == element
    assert small_queue.head == 1
    assert small_queue.size == 0

    # Test full condition after enqueue and dequeue
    is_full = queue.full()
    assert is_full is False
    is_full = small_queue.full()
    assert is_full is False

    # Enqueue again
    enqueue_result = small_queue.enqueue(element)
    assert enqueue_result is True
    assert small_queue.tail == 2
    assert small_queue.size == 1

    # Dequeue from empty queue
    dequeued_element = large_queue.dequeue()
    assert dequeued_element is None

def test_queue_initialization_and_enqueue_deeper():
    # Create a queue with a maximum size of 1187
    max_size = 1187
    queue = queue_module.Queue(max_size)

    # Check the queue's type and attributes
    assert f"{type(queue).__module__}.{type(queue).__qualname__}" == "queue_example.Queue"
    assert queue.max_size == max_size
    assert queue.head == 0
    assert queue.tail == 0
    assert queue.size == 0
    assert f"{type(queue.data).__module__}.{type(queue).__qualname__}" == "array.array"
    assert len(queue.data) == max_size

    # Check if the queue is empty
    is_empty = queue.empty()
    assert is_empty is False

    # Enqueue an element
    element = max_size
    is_enqueued = queue.enqueue(element)
    assert is_enqueued is True
    assert queue.tail == 1
    assert queue.size == 1

    # Create another queue with a maximum size of 1
    queue2 = queue_module.Queue(True)
    assert f"{type(queue2).__module__}.{type(queue2).__qualname__}" == "queue_example.Queue"
    assert queue2.max_size is True
    assert queue2.head == 0
    assert queue2.tail == 0
    assert queue2.size == 0
    assert f"{type(queue2.data).__module__}.{type(queue2).__qualname__}" == "array.array"
    assert len(queue2.data) == 1

    # Check if the queue is full
    is_full = queue2.full()
    assert is_full is False

    # Enqueue an element
    element2 = 1441
    is_enqueued2 = queue2.enqueue(element2)
    assert is_enqueued2 is True
    assert queue2.size == 1

    # Check if the queue is full
    is_full2 = queue2.full()
    assert is_full2 is True

    # Create another queue with a maximum size of 1080
    queue3 = queue_module.Queue(1080)
    assert queue3.head == 0
    assert queue3.size == 0

    # Dequeue an element from queue2
    dequeued_element = queue2.dequeue()
    assert dequeued_element == 1441
    assert queue2.size == 0

    # Dequeue an element from queue
    dequeued_element2 = queue.dequeue()
    assert dequeued_element2 == max_size
    assert queue.head == 1
    assert queue.size == 0

    # Check if queue3 is full
    is_full3 = queue3.full()
    assert is_full3 is False

    # Enqueue an element into queue2
    is_enqueued3 = queue2.enqueue(False)
    assert is_enqueued3 is True
    assert queue2.size == 1

    # Try to create a queue with a negative size
    with pytest.raises(AssertionError):
        queue_module.Queue(-30)
