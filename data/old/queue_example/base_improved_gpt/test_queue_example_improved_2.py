import pytest
import queue_example as module_0

# test_case_0
def test_queue_initialization_and_full_method():
    """Test for checking the initialization of Queue and the full() method.

    This test covers the initialization of the Queue class, including the setting of the max attribute,
    and checks the functionality of the full() method for a newly initialized Queue.

    It provides coverage for the following functions: __init__(), full().
    """
    # Setup: Initialize a Queue with a given size
    QUEUE_SIZE = 1256
    test_queue = module_0.Queue(QUEUE_SIZE)

    # Assertions for the initialization of the queue
    assert (
        f"{type(test_queue).__module__}.{type(test_queue).__qualname__}"
        == "queue_example.Queue"
    )
    assert test_queue.max == QUEUE_SIZE
    assert test_queue.head == 0
    assert test_queue.tail == 0
    assert test_queue.size == 0

    # Execution and assertion for the full() method
    is_queue_full = test_queue.full()
    assert is_queue_full is False

# test_case_1
def test_queue_negative_size_initialization():
    """Test for checking the initialization of Queue with a negative size.

    This test covers the initialization of the Queue class with a negative size,
    expecting an AssertionError to be raised.

    It provides coverage for the following functions: __init__().
    """
    # Setup: Define a negative queue size
    QUEUE_SIZE = -2944

    # Execution and assertion: Attempt to initialize the Queue and expect an AssertionError
    with pytest.raises(AssertionError):
        module_0.Queue(QUEUE_SIZE)

# test_case_2
def test_queue_enqueue_operation_and_negative_size_initialization():
    """Test for checking the enqueue operation and the initialization of Queue with a negative size.

    This test covers the enqueue operation of the Queue class and also attempts to initialize the Queue with a negative size,
    expecting an AssertionError to be raised.

    It provides coverage for the following functions: __init__(), enqueue().
    """
    # Setup: Initialize a Queue with a given size and define a value to enqueue
    QUEUE_SIZE = 2505
    ENQUEUE_VALUE = -726
    test_queue = module_0.Queue(QUEUE_SIZE)

    # Execution and assertion: Enqueue a value and check the state of the queue
    enqueue_result = test_queue.enqueue(ENQUEUE_VALUE)
    assert enqueue_result is True
    assert test_queue.tail == 1
    assert test_queue.size == 1

    # Execution and assertion: Attempt to initialize the Queue with a negative size and expect an AssertionError
    with pytest.raises(AssertionError):
        module_0.Queue(ENQUEUE_VALUE)

# test_case_3
def test_queue_dequeue_operation_full_method_and_invalid_initialization():
    """Test for checking the dequeue operation, full() method, and the initialization of Queue with an invalid size.

    This test covers the dequeue operation and full() method of the Queue class, and also attempts to initialize the Queue with an invalid size,
    expecting an AssertionError to be raised.

    It provides coverage for the following functions: __init__(), dequeue(), full().
    """
    # Setup: Initialize a Queue with a given size
    QUEUE_SIZE = 2423
    test_queue = module_0.Queue(QUEUE_SIZE)

    # Execution and assertion: Dequeue a value from an empty queue and check the returned value
    dequeued_value = test_queue.dequeue()
    assert dequeued_value is None

    # Execution and assertion: Check the full state of the queue
    is_queue_full = test_queue.full()
    assert is_queue_full is False

    # Execution and assertion: Attempt to initialize the Queue with an invalid size and expect an AssertionError
    with pytest.raises(AssertionError):
        module_0.Queue(is_queue_full)

# test_case_4
def test_queue_initialization_enqueue_dequeue_and_full_methods():
    """Test for checking the initialization of Queue, enqueue, dequeue operations, and the full() method.

    This test covers the initialization of the Queue class, the enqueue and dequeue operations, and checks the functionality of the full() method.

    It provides coverage for the following functions: __init__(), enqueue(), dequeue(), full().
    """
    # Setup: Initialize Queues with given sizes and define a value to enqueue
    QUEUE_SIZE_1 = 1001
    QUEUE_SIZE_2 = 649
    QUEUE_SIZE_3 = 3263
    ENQUEUE_VALUE = 2010
    test_queue_1 = module_0.Queue(QUEUE_SIZE_1)
    test_queue_2 = module_0.Queue(QUEUE_SIZE_2)
    test_queue_3 = module_0.Queue(QUEUE_SIZE_3)

    # Execution and assertion: Enqueue a value into test_queue_2, check the state of the queue, dequeue the value, and check the state again
    enqueue_result_1 = test_queue_2.enqueue(ENQUEUE_VALUE)
    assert enqueue_result_1 is True
    assert test_queue_2.tail == 1
    assert test_queue_2.size == 1

    dequeued_value = test_queue_2.dequeue()
    assert dequeued_value == ENQUEUE_VALUE
    assert test_queue_2.head == 1
    assert test_queue_2.size == 0

    # Execution and assertion: Check the full state of test_queue_1 and test_queue_2
    is_queue_1_full = test_queue_1.full()
    assert is_queue_1_full is False

    is_queue_2_full = test_queue_2.full()
    assert is_queue_2_full is False

    # Execution and assertion: Enqueue a value into test_queue_2 again and check the state of the queue
    enqueue_result_2 = test_queue_2.enqueue(ENQUEUE_VALUE)
    assert enqueue_result_2 is True
    assert test_queue_2.tail == 2
    assert test_queue_2.size == 1

    # Execution and assertion: Dequeue a value from an empty queue (test_queue_3) and check the returned value
    dequeued_value_from_empty_queue = test_queue_3.dequeue()
    assert dequeued_value_from_empty_queue is None

# test_case_5
def test_queue_initialization_enqueue_and_empty_method():
    """Test for checking the initialization of Queue, enqueue operation and the empty() method.

    This test covers the initialization of the Queue class, the enqueue operation, and checks the functionality of the empty() method.

    It provides coverage for the following functions: __init__(), enqueue(), empty().
    """
    # Setup: Initialize Queues with given sizes and define a value to enqueue
    QUEUE_SIZE_1 = 1235
    QUEUE_SIZE_2 = 3504
    ENQUEUE_VALUE = 4904
    test_queue_1 = module_0.Queue(QUEUE_SIZE_1)
    test_queue_2 = module_0.Queue(QUEUE_SIZE_2)

    # Execution and assertion: Check the empty state of test_queue_2, enqueue a value, and check the state again
    is_queue_2_empty_before = test_queue_2.empty()
    assert is_queue_2_empty_before is False

    enqueue_result = test_queue_2.enqueue(ENQUEUE_VALUE)
    assert enqueue_result is True
    assert test_queue_2.tail == 1
    assert test_queue_2.size == 1

    is_queue_2_empty_after = test_queue_2.empty()
    assert is_queue_2_empty_after is False

# test_case_6
def test_queue_initialization_enqueue_dequeue_full_empty_methods():
    """Test for checking the initialization of Queue, enqueue, dequeue operations, and the full and empty methods.

    This test covers the initialization of the Queue class, the enqueue and dequeue operations, and checks the functionality of the full and empty methods.

    It provides coverage for the following functions: __init__(), enqueue(), dequeue(), full(), empty().
    """
    # Setup: Initialize Queues with given sizes and define values to enqueue
    QUEUE_SIZE_1 = 1187
    QUEUE_SIZE_2 = True
    QUEUE_SIZE_3 = 1080
    QUEUE_SIZE_4 = True
    QUEUE_SIZE_5 = 2245
    QUEUE_SIZE_6 = 481
    ENQUEUE_VALUE_1 = 1187
    ENQUEUE_VALUE_2 = 1441
    ENQUEUE_VALUE_3 = False
    test_queue_1 = module_0.Queue(QUEUE_SIZE_1)
    test_queue_2 = module_0.Queue(QUEUE_SIZE_2)
    test_queue_3 = module_0.Queue(QUEUE_SIZE_3)
    test_queue_4 = module_0.Queue(QUEUE_SIZE_4)
    test_queue_5 = module_0.Queue(QUEUE_SIZE_5)
    test_queue_6 = module_0.Queue(QUEUE_SIZE_6)

    # Execution and assertion: Check the empty state of test_queue_1, enqueue a value, and check the state of the queue
    is_queue_1_empty = test_queue_1.empty()
    assert is_queue_1_empty is False

    enqueue_result_1 = test_queue_1.enqueue(ENQUEUE_VALUE_1)
    assert enqueue_result_1 is True
    assert test_queue_1.tail == 1
    assert test_queue_1.size == 1

    # Execution and assertion: Check the full state of test_queue_2, enqueue a value and check the state of the queue and its full state again
    is_queue_2_full_before_enqueue = test_queue_2.full()
    assert is_queue_2_full_before_enqueue is False

    enqueue_result_2 = test_queue_2.enqueue(ENQUEUE_VALUE_2)
    assert enqueue_result_2 is True
    assert test_queue_2.size == 1

    is_queue_2_full_after_enqueue = test_queue_2.full()
    assert is_queue_2_full_after_enqueue is True

    # Execution and assertion: Check the full state of test_queue_3, empty state of test_queue_4, and empty state of test_queue_5
    is_queue_3_full = test_queue_3.full()
    assert is_queue_3_full is False

    is_queue_4_empty = test_queue_4.empty()
    assert is_queue_4_empty is False

    is_queue_5_empty = test_queue_5.empty()
    assert is_queue_5_empty is False

    # Execution and assertion: Enqueue a value into test_queue_2, check the empty state of the queue
    enqueue_result_3 = test_queue_2.enqueue(is_queue_4_empty)
    assert enqueue_result_3 is True
    assert test_queue_2.size == 1

    is_queue_2_empty_after_enqueue = test_queue_2.empty()
    assert is_queue_2_empty_after_enqueue is True

    # Execution and assertion: Dequeue values from test_queue_3 and test_queue_4, check the state of the queues
    dequeue_result_1 = test_queue_3.dequeue()
    assert dequeue_result_1 is None

    dequeue_result_2 = test_queue_4.dequeue()
    assert dequeue_result_2 is None

    # Execution and assertion: Enqueue a value into test_queue_6 and check the state of the queue
    enqueue_result_4 = test_queue_6.enqueue(is_queue_2_full_after_enqueue)
    assert enqueue_result_4 is True
    assert test_queue_6.tail == 1
    assert test_queue_6.size == 1

    # Execution and assertion: Dequeue a value from test_queue_3 and check the state of the queue
    dequeue_result_3 = test_queue_3.dequeue()
    assert dequeue_result_3 is None

    # Execution and assertion: Check the empty state of test_queue_1 and full state of test_queue_3
    is_queue_1_empty = test_queue_1.empty()
    assert is_queue_1_empty is False

    is_queue_3_full = test_queue_3.full()
    assert is_queue_3_full is False

# test_case_7
def test_queue_initialization_enqueue_dequeue_full_empty_methods_and_invalid_initialization():
    """Test for checking the initialization of Queue, enqueue, dequeue operations, full and empty methods, and invalid initialization.

    This test covers the initialization of the Queue class, the enqueue and dequeue operations, and checks the functionality of the full and empty methods. It also covers the case of trying to initialize a Queue with an invalid size.

    It provides coverage for the following functions: __init__(), enqueue(), dequeue(), full(), empty().
    """
    # Setup: Initialize Queues with given sizes and define values to enqueue
    QUEUE_SIZE_1 = 1187
    QUEUE_SIZE_2 = True
    QUEUE_SIZE_3 = 1080
    ENQUEUE_VALUE_1 = 1187
    ENQUEUE_VALUE_2 = 1441
    INVALID_QUEUE_SIZE = -30
    test_queue_1 = module_0.Queue(QUEUE_SIZE_1)
    test_queue_2 = module_0.Queue(QUEUE_SIZE_2)
    test_queue_3 = module_0.Queue(QUEUE_SIZE_3)

    # Execution and assertion: Check the empty state of test_queue_1
    is_queue_1_empty = test_queue_1.empty()
    assert is_queue_1_empty is False

    # Execution and assertion: Enqueue a value into test_queue_1, check the state of the queue
    enqueue_result_1 = test_queue_1.enqueue(ENQUEUE_VALUE_1)
    assert enqueue_result_1 is True
    assert test_queue_1.tail == 1
    assert test_queue_1.size == 1

    # Execution and assertion: Check the full state of test_queue_2, enqueue a value and check the state of the queue and its full state again
    is_queue_2_full_before_enqueue = test_queue_2.full()
    assert is_queue_2_full_before_enqueue is False

    enqueue_result_2 = test_queue_2.enqueue(ENQUEUE_VALUE_2)
    assert enqueue_result_2 is True
    assert test_queue_2.size == 1

    is_queue_2_full_after_enqueue = test_queue_2.full()
    assert is_queue_2_full_after_enqueue is True

    # Execution and assertion: Dequeue a value from test_queue_2 and test_queue_1, check the state of the queues
    dequeued_value_1 = test_queue_2.dequeue()
    assert dequeued_value_1 == ENQUEUE_VALUE_2
    assert test_queue_2.size == 0

    dequeued_value_2 = test_queue_1.dequeue()
    assert dequeued_value_2 == ENQUEUE_VALUE_1
    assert test_queue_1.head == 1
    assert test_queue_1.size == 0

    # Execution and assertion: Check the full state of test_queue_3
    is_queue_3_full = test_queue_3.full()
    assert is_queue_3_full is False

    # Execution and assertion: Enqueue a value into test_queue_2 again and check the state of the queue
    enqueue_result_3 = test_queue_2.enqueue(is_queue_1_empty)
    assert enqueue_result_3 is True
    assert test_queue_2.size == 1

    # Execution and assertion: Attempt to initialize the Queue with an invalid size and expect an AssertionError
    with pytest.raises(AssertionError):
        module_0.Queue(INVALID_QUEUE_SIZE)
