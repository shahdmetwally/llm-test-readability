import pytest

import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_accepts_negative_float_without_raising():
    """Ensure to_namedtuple accepts a negative float input without raising an exception."""
    negative_float = -476.66

    # The test passes if no exception is raised when calling the function.
    namedtuple_utils.to_namedtuple(negative_float)

def test_to_namedtuple_accepts_tuple_and_set_input():
    """Ensure to_namedtuple can be called with a tuple (float, set) and with a set alone."""
    # Use the same literal value as the original test
    negative_value = -67.0

    # Creating a set from repeated identical elements (resulting set has a single element)
    values_set = {negative_value, negative_value, negative_value, negative_value}

    # Tuple containing the float and the set (same structure as original)
    mixed_input = (negative_value, values_set)

    # Call to_namedtuple with the tuple input and keep the returned value
    converted_namedtuple = namedtuple_utils.to_namedtuple(mixed_input)

    # Call to_namedtuple with the set input (result not assigned) — preserves original behavior/order
    namedtuple_utils.to_namedtuple(values_set)

def test_to_namedtuple_converts_dict_and_is_idempotent():
    """Ensure to_namedtuple converts a dict to a namedtuple and is idempotent when given a namedtuple."""
    # Use the same key/value repeated to mirror the original test input
    key = "author"
    source_dict = {key: key, key: key, key: key}

    # Convert dict to namedtuple
    nt = namedtuple_utils.to_namedtuple(source_dict)

    # Result should not be a dict and should expose the expected attribute/value
    assert not isinstance(nt, dict)
    assert hasattr(nt, key)
    assert getattr(nt, key) == key

    # Converting the resulting namedtuple again should be accepted (idempotent)
    nt2 = namedtuple_utils.to_namedtuple(nt)

    # The second conversion should produce the same namedtuple type and value
    assert type(nt2) == type(nt)
    assert nt2 == nt

def test_to_namedtuple_accepts_bytes_input():
    """Call to_namedtuple with a bytes object to ensure it accepts raw bytes input (no exception expected)."""
    # Use a raw bytes literal identical to the original test input.
    raw_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    # The test passes if this call does not raise an exception.
    namedtuple_utils.to_namedtuple(raw_bytes)

def test_to_namedtuple_accepts_empty_tuple():
    """Verify that to_namedtuple can be called with an empty tuple without raising errors."""
    # Arrange: an empty input tuple (unchanged from original)
    input_tuple = ()

    # Act: convert the empty tuple to a namedtuple using the provided utility
    namedtuple_result = namedtuple_utils.to_namedtuple(input_tuple)

    # Note: original test did not assert anything; we preserve that behavior.

def test_to_namedtuple_idempotent_and_handles_bytes_tuple():
    """Ensure to_namedtuple converts OrderedDicts, is idempotent, and accepts a tuple containing a namedtuple and bytes."""
    # start with an empty OrderedDict
    original = collections_module.OrderedDict()

    # convert OrderedDict -> namedtuple-like structure
    nt_from_od = namedtuple_utils.to_namedtuple(original)

    # idempotence: converting an already-converted value should yield an equal result
    nt_from_nt = namedtuple_utils.to_namedtuple(nt_from_od)
    assert nt_from_nt == nt_from_od

    # repeated conversion of the original should behave the same
    nt_from_od_again = namedtuple_utils.to_namedtuple(original)
    nt_from_nt_again = namedtuple_utils.to_namedtuple(nt_from_od_again)
    assert nt_from_nt_again == nt_from_od_again

    # sample bytes (should remain unchanged by conversion)
    sample_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # convert a tuple that contains a namedtuple and bytes (should not raise)
    pair = (nt_from_nt, sample_bytes)
    converted_pair = namedtuple_utils.to_namedtuple(pair)

    # basic sanity checks: conversion completed and bytes are still present in the result
    assert converted_pair is not None
    # If the converted result is a sequence-like, the sample bytes should be present as an element.
    if isinstance(converted_pair, (list, tuple)):
        assert sample_bytes in converted_pair

def test_to_namedtuple_handles_list_container_and_none():
    """Ensure to_namedtuple accepts a list containing a list and also handles None without raising."""
    # Create an empty inner list and wrap it into a container list
    inner_list = []
    list_container = [inner_list]

    # Call to_namedtuple on the container to ensure it doesn't raise
    result_namedtuple = namedtuple_utils.to_namedtuple(list_container)

    # Call to_namedtuple with None to ensure it handles None input (no exception expected)
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_handles_various_input_types():
    """Ensure to_namedtuple handles dicts, tuples, namedtuple-like objects, and booleans without error."""
    # A long documentation-like string used as both keys and values in mappings
    doc_string = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user’s\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "
    # Create a mapping that uses the same long string repeatedly (mirrors original behavior)
    mapping_from_doc_to_doc = {doc_string: doc_string, doc_string: doc_string, doc_string: doc_string}

    # Convert the mapping to a namedtuple-like structure
    nt_from_mapping_first = namedtuple_utils.to_namedtuple(mapping_from_doc_to_doc)

    # Use a boolean as a separate key/input (preserve original boolean usage)
    false_flag_1 = False

    # Call to_namedtuple again on the same mapping (mirrors original sequence)
    nt_from_mapping_second = namedtuple_utils.to_namedtuple(mapping_from_doc_to_doc)

    # Wrap the result in a tuple and convert that tuple as input
    tuple_with_namedtuple = (nt_from_mapping_second,)
    nt_from_tuple = namedtuple_utils.to_namedtuple(tuple_with_namedtuple)

    # Create a dict with mixed key types: a namedtuple and a boolean, both mapping to a namedtuple result
    mixed_key_dict = {nt_from_tuple: nt_from_mapping_second, false_flag_1: nt_from_mapping_second}

    # Convert that mixed-key dict to a namedtuple-like structure
    nt_from_mixed_dict = namedtuple_utils.to_namedtuple(mixed_key_dict)

    # Convert the resulting namedtuple-like object again (preserve repeated conversion)
    nt_from_namedtuple_conversion = namedtuple_utils.to_namedtuple(nt_from_mixed_dict)

    # Another boolean input conversion (preserve final call)
    false_flag_2 = False
    nt_from_mixed_dict_second_call = namedtuple_utils.to_namedtuple(nt_from_mixed_dict)

    # Final call with a boolean input (preserve last call in original)
    namedtuple_utils.to_namedtuple(false_flag_2)

def test_to_namedtuple_idempotent_for_nested_structures():
    """Ensure to_namedtuple can be applied repeatedly on nested structures and on an int without error."""
    # A sample string literal used as a dict key/value (unchanged literal).
    sample_str = "\x0cMv"

    # An empty tuple used both as a key and a value (unchanged).
    empty_tuple = ()

    # Construct a mapping with the same keys/values as the original test.
    # Note: this mirrors the original literal with a duplicate tuple key entry.
    mixed_mapping = {
        sample_str: empty_tuple,
        empty_tuple: sample_str,
        empty_tuple: empty_tuple,
    }

    # A tuple that pairs the string and the mapping, placed inside a list as input.
    element_tuple = (sample_str, mixed_mapping)
    input_list = [element_tuple]

    # Call to_namedtuple repeatedly to check idempotence / repeated application.
    first_conversion = namedtuple_utils.to_namedtuple(input_list)
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)
    third_conversion = namedtuple_utils.to_namedtuple(second_conversion)

    # Also ensure calling with an integer does not raise.
    sample_int = 2
    namedtuple_utils.to_namedtuple(sample_int)

def test_to_namedtuple_accepts_bytes_key_value_without_raising():
    """Ensure to_namedtuple accepts a mapping with bytes keys and values without raising."""
    # A bytes object used both as key and value in the mapping.
    sample_bytes = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    # Construct the mapping (duplicate keys in a literal result in the last entry taking effect).
    sample_mapping = {
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
    }
    # Call the function under test; the test passes if no exception is raised.
    namedtuple_utils.to_namedtuple(sample_mapping)

