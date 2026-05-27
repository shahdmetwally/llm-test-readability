import pytest
import namedtupleutils as namedtupleutils
import collections as collections

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple handles a plain float value as input."""
    # Pass a raw float (non-collection type) to to_namedtuple
    float_value = -476.66
    namedtupleutils.to_namedtuple(float_value)

def test_to_namedtuple_with_tuple_and_set_inputs():
    """Test that to_namedtuple handles a tuple containing a float and a set, as well as a bare set."""

    # Define a sample float value used throughout the test
    sample_float = -67.0

    # Build a set from the sample float (duplicates collapse to one element)
    float_set = {sample_float, sample_float, sample_float, sample_float}

    # Build a tuple that contains both the float and the set
    tuple_with_set = (sample_float, float_set)

    # Convert the tuple (containing a float and a set) to a namedtuple
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_with_set)

    # Convert the bare set to a namedtuple
    namedtupleutils.to_namedtuple(float_set)

def test_to_namedtuple_converts_dict_and_handles_namedtuple_input():
    """Test that to_namedtuple converts a dict to a namedtuple, and that passing a namedtuple back in is also handled."""
    # Use a single string as both the key and value for the input dictionary
    field_name = "author"
    input_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dictionary to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(input_dict)

    # Pass the resulting namedtuple back into to_namedtuple to verify it handles namedtuple input
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_raises_on_bytes_input():
    """Test that to_namedtuple raises when given a bytes object as input."""
    # A raw bytes object is not a valid input for to_namedtuple
    invalid_bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"

    namedtupleutils.to_namedtuple(invalid_bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple as input."""
    # Provide an empty tuple as the input to convert
    empty_tuple = ()

    # Call to_namedtuple with the empty tuple
    result = namedtupleutils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_empty_ordered_dict_and_mixed_types():
    """Tests to_namedtuple with empty OrderedDicts, idempotent namedtuple inputs, and mixed tuples."""

    # Start with an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert empty OrderedDict to namedtuple, then apply idempotently
    namedtuple_from_empty_dict = namedtupleutils.to_namedtuple(empty_ordered_dict)
    namedtuple_idempotent = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict)

    # Repeat the same conversion pattern to verify consistent behaviour
    namedtuple_from_empty_dict_second = namedtupleutils.to_namedtuple(empty_ordered_dict)
    namedtuple_idempotent_second = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict_second)

    # A raw bytes object to be used in a mixed-type tuple
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert empty OrderedDict again independently
    namedtuple_from_empty_dict_third = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple containing a namedtuple and a bytes object
    mixed_tuple = (namedtuple_idempotent, raw_bytes)

    # Convert the mixed tuple to a namedtuple
    namedtuple_from_mixed_tuple = namedtupleutils.to_namedtuple(mixed_tuple)

    # One final conversion of the empty OrderedDict
    namedtuple_from_empty_dict_fourth = namedtupleutils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_converts_ordered_dict_with_special_char_key():
    """Test that to_namedtuple converts an OrderedDict with special-character keys, and that OrderedDict accepts None as a positional argument."""

    # A string containing special/control characters used as both key and value
    special_char_key = "wm=-g\ry#\x0b#:*"

    # Build a plain dict using the special-character string as key and value
    source_dict = {special_char_key: special_char_key, special_char_key: special_char_key}

    # Construct an OrderedDict from the source dict using keyword unpacking
    ordered_dict_input = collections.OrderedDict(**source_dict)

    # Convert the OrderedDict to a namedtuple; result is produced without error
    namedtuple_result = namedtupleutils.to_namedtuple(ordered_dict_input)

    # Verify that None can be passed as a positional argument to OrderedDict
    none_value = None
    args_with_none = [none_value]

    # Call OrderedDict with None as a positional arg; result is intentionally unused
    collections.OrderedDict(*args_with_none)

def test_to_namedtuple_with_nested_empty_list_and_none_input():
    """Test that to_namedtuple handles a nested empty list and a None input without raising."""

    # Build a list that contains one element: an empty list
    empty_list = []
    nested_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    result_from_nested_list = namedtupleutils.to_namedtuple(nested_list)

    # Also verify that None is accepted as input
    none_input = None
    namedtupleutils.to_namedtuple(none_input)

def test_to_namedtuple_with_varied_input_types():
    """Test that to_namedtuple handles dicts, tuples, namedtuples, and booleans as inputs without error."""

    # A long docstring string used as a dictionary key
    docstring_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Dict with repeated docstring key mapping to itself
    dict_with_docstring_keys = {docstring_key: docstring_key, docstring_key: docstring_key, docstring_key: docstring_key}

    # Convert a plain dict to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(dict_with_docstring_keys)

    false_value = False

    # Convert the same dict again to produce a second namedtuple
    namedtuple_from_dict_again = namedtupleutils.to_namedtuple(dict_with_docstring_keys)

    # Wrap the namedtuple in a tuple and convert that tuple
    tuple_containing_namedtuple = (namedtuple_from_dict_again,)
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_containing_namedtuple)

    # Build a dict using namedtuples and a bool as keys, then convert it
    dict_with_namedtuple_keys = {namedtuple_from_tuple: namedtuple_from_dict_again, false_value: namedtuple_from_dict_again}
    namedtuple_from_mixed_dict = namedtupleutils.to_namedtuple(dict_with_namedtuple_keys)

    # Convert an already-converted namedtuple (idempotency check)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    second_false_value = False

    # Convert the mixed-dict namedtuple a second time
    namedtuple_from_namedtuple_again = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a bare boolean value
    namedtupleutils.to_namedtuple(second_false_value)

def test_to_namedtuple_handles_chained_conversion_and_primitive_input():
    """Test that to_namedtuple handles chained re-conversion of nested structures and a plain integer."""

    # A string beginning with a form-feed control character
    form_feed_string = "\x0cMv"
    empty_tuple = ()

    # Dict with mixed key types; duplicate tuple key means last value wins
    nested_dict = {form_feed_string: empty_tuple, empty_tuple: form_feed_string, empty_tuple: empty_tuple}

    # Pair the string with the nested dict, then wrap in a list for conversion
    string_dict_pair = (form_feed_string, nested_dict)
    input_list = [string_dict_pair]

    # First conversion: convert the list of tuples to a namedtuple representation
    namedtuple_result = namedtupleutils.to_namedtuple(input_list)

    # Second conversion: re-convert the already-converted result (idempotency check)
    re_converted_result = namedtupleutils.to_namedtuple(namedtuple_result)

    # Third conversion: re-convert once more to confirm continued stability
    twice_re_converted_result = namedtupleutils.to_namedtuple(re_converted_result)

    # Verify that a plain integer input is accepted without raising an error
    integer_input = 2
    namedtupleutils.to_namedtuple(integer_input)

def test_to_namedtuple_with_bytes_key_and_value_dict():
    """Test that to_namedtuple handles a dict with identical bytes keys and values without error."""
    # A raw bytes object used as both the key and value in the dictionary
    bytes_key_and_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Dictionary where the same bytes object is repeated as key and value across all entries
    bytes_keyed_dict = {
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
    }

    # Verify that to_namedtuple can process a bytes-keyed dict without raising
    namedtupleutils.to_namedtuple(bytes_keyed_dict)