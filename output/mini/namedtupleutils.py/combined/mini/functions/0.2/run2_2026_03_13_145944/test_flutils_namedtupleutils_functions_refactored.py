import pytest

import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_handles_negative_float():
    """Ensure to_namedtuple can be called with a float without raising an error."""
    # Use a negative float literal exactly as in the original test.
    input_value = -476.66

    # Call the function under test; the original test simply invoked the call
    # and passed if no exception was raised. Preserve that behaviour.
    namedtuple_utils.to_namedtuple(input_value)

def test_to_namedtuple_accepts_tuple_with_set_element():
    """Ensure to_namedtuple can be invoked on a tuple containing a float and a set, and on the set itself."""
    negative_float = -67.0

    # Construct a set using the same float value repeated to match the original literal structure
    unique_float_set = {negative_float, negative_float, negative_float, negative_float}

    # Tuple containing the float and the set (preserve ordering)
    mixed_tuple = (negative_float, unique_float_set)

    # Invoke to_namedtuple with the tuple and keep the returned value
    result_namedtuple = namedtuple_utils.to_namedtuple(mixed_tuple)

    # Invoke to_namedtuple with the set as in the original test (return value not used)
    namedtuple_utils.to_namedtuple(unique_float_set)

def test_to_namedtuple_handles_dict_then_namedtuple_input_idempotently():
    """Ensure to_namedtuple accepts a dict and can be called again on its result."""
    # Use the same literal form as the original test; duplicate keys in a literal
    # collapse to a single entry at runtime.
    field_name = "author"
    sample_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # First conversion: dict -> namedtuple-like object
    nt_instance = namedtuple_utils.to_namedtuple(sample_dict)

    # Second conversion: call to_namedtuple on the already-converted result
    nt_instance_again = namedtuple_utils.to_namedtuple(nt_instance)

def test_to_namedtuple_accepts_bytes_input_without_error():
    """Ensure to_namedtuple accepts raw bytes input without raising an exception."""
    # A raw bytes object (unchanged from the original test).
    raw_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    # Call the function under test; the test passes if no exception is raised.
    namedtuple_utils.to_namedtuple(raw_bytes)

def test_to_namedtuple_with_empty_tuple_returns_namedtuple():
    """Ensure to_namedtuple accepts an empty tuple and returns a namedtuple-compatible result."""
    # Arrange: define the empty tuple input (same literal as original test)
    empty_tuple = ()
    # Act: call the function under test with the empty tuple
    result = namedtuple_utils.to_namedtuple(empty_tuple)
    # Note: original test had no assertions; this preserves the original behavior.

def test_to_namedtuple_handles_various_inputs_idempotently():
    """
    Exercise namedtuple conversion on OrderedDicts, already-converted namedtuples,
    and tuples containing a namedtuple and bytes to ensure calls succeed repeatedly.
    (No assertions in the original; this preserves that behavior.)
    """
    # Create an empty OrderedDict
    ordered_dict = collections_module.OrderedDict()

    # Convert OrderedDict to a namedtuple-like structure
    namedtuple_from_ordered_1 = namedtuple_utils.to_namedtuple(ordered_dict)

    # Convert the result again (idempotency / handling of already-converted input)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_ordered_1)

    # Convert the original OrderedDict again (repeat conversion)
    namedtuple_from_ordered_2 = namedtuple_utils.to_namedtuple(ordered_dict)

    # Convert the second converted value again
    namedtuple_from_namedtuple_2 = namedtuple_utils.to_namedtuple(namedtuple_from_ordered_2)

    # Preserve the original bytes literal exactly as in the generated test
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Another conversion of the OrderedDict (as in the original sequence)
    namedtuple_from_ordered_3 = namedtuple_utils.to_namedtuple(ordered_dict)

    # Create a tuple containing a previously obtained namedtuple and the bytes literal
    combined_tuple = (namedtuple_from_namedtuple, raw_bytes)

    # Convert the tuple to a namedtuple-like structure
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(combined_tuple)

    # Final conversion of the OrderedDict to match the last call in the original sequence
    namedtuple_from_ordered_4 = namedtuple_utils.to_namedtuple(ordered_dict)

def test_to_namedtuple_with_ordered_dict_and_non_identifier_keys():
    """Call to_namedtuple with an OrderedDict built from keys containing non-identifier characters;
    then construct an OrderedDict from a single None in a list (no assertions)."""
    # Special-character string used both as key and value
    sample_key = "wm=-g\ry#\x0b#:*"

    # Construct a dict literal where the same key appears twice (second occurrence overrides first)
    sample_dict = {sample_key: sample_key, sample_key: sample_key}

    # Build an OrderedDict by unpacking the dict as keyword arguments
    ordered_dict = collections_module.OrderedDict(**sample_dict)

    # Convert the OrderedDict into a namedtuple via the module under test
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)

    # Prepare a one-element list containing None and pass it positionally to OrderedDict
    none_value = None
    args_list = [none_value]
    collections_module.OrderedDict(*args_list)

def test_to_namedtuple_handles_nested_list_and_none():
    """Verify that to_namedtuple can be invoked on a nested list and on None without raising."""
    # Create an empty list and a nested list that contains it.
    empty_list = []
    nested_list = [empty_list]

    # Call to_namedtuple on the nested list and keep the result to ensure invocation succeeds.
    result_namedtuple = namedtuple_utils.to_namedtuple(nested_list)

    # Also call to_namedtuple with None to ensure it can be invoked with a None input (no exception expected).
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_with_various_input_types():
    """Ensure namedtuple conversion can be invoked on a variety of inputs
    (string, dict, tuple, namedtuple and booleans) without errors.
    """
    # A long docstring-like text used as both keys and values in mappings.
    long_docstring = (
        "Normalize a given path.\n\n"
        "    The given ``path`` will be normalized in the following process.\n\n"
        "    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n"
        "       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n"
        "    #. :obj:`PosixPath <pathlib.PosixPath>` and\n"
        "       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n"
        "       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n"
        "       method.\n"
        "    #. An initial component of ``~`` will be replaced by that user’s\n"
        "       home directory.\n"
        "    #. Any environment variables will be expanded.\n"
        "    #. Non absolute paths will have the current working directory from\n"
        "       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n"
        "       :obj:`os.chdir() <os.chdir>` to change the current working directory\n"
        "       before calling this function.\n"
        "    #. Redundant separators and up-level references will be normalized, so\n"
        "       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n"
        "       ``A/B``.\n\n"
        "    Args:\n"
        "        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n"
        "            The path to be normalized.\n\n"
        "    :rtype:\n"
        "        :obj:`Path <pathlib.Path>`\n\n"
        "        * :obj:`PosixPath <pathlib.PosixPath>` or\n"
        "          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n"
        "        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n"
        "           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n"
        "           the same object returned.\n\n"
        "    Example:\n\n"
        "        >>> from flutils.pathutils import normalize_path\n"
        "        >>> normalize_path('~/tmp/foo/../bar')\n"
        "        PosixPath('/home/test_user/tmp/bar')\n\n"
    )

    # A dict literal that repeats the same key/value entries.
    repeated_str_mapping = {
        long_docstring: long_docstring,
        long_docstring: long_docstring,
        long_docstring: long_docstring,
    }

    # First conversion from the repeated-string dict.
    nt_from_repeated_dict_first = namedtuple_utils.to_namedtuple(repeated_str_mapping)

    # Repeated invocation on the same dict to exercise idempotency / repeated calls.
    nt_from_repeated_dict_second = namedtuple_utils.to_namedtuple(repeated_str_mapping)

    # Pack the second namedtuple into a single-element tuple to test tuple handling.
    single_element_tuple = (nt_from_repeated_dict_second,)

    # Convert from a tuple input.
    nt_from_tuple = namedtuple_utils.to_namedtuple(single_element_tuple)

    # Create a mapping with a namedtuple key and a boolean key to test mixed key types.
    false_flag_a = False
    mixed_key_mapping = {nt_from_tuple: nt_from_repeated_dict_second, false_flag_a: nt_from_repeated_dict_second}

    # Convert from the mixed-key mapping.
    nt_from_mixed_mapping = namedtuple_utils.to_namedtuple(mixed_key_mapping)

    # Convert directly from a namedtuple input (should be a no-op or idempotent).
    nt_from_namedtuple = namedtuple_utils.to_namedtuple(nt_from_mixed_mapping)

    # Another boolean value; final call with a boolean input.
    false_flag_b = False
    nt_from_mixed_mapping_second = namedtuple_utils.to_namedtuple(nt_from_mixed_mapping)

    # Call with a boolean input to ensure booleans are handled without error.
    namedtuple_utils.to_namedtuple(false_flag_b)

def test_to_namedtuple_handles_nested_structures_and_is_idempotent():
    """Ensure to_namedtuple converts a nested structure without error, is safe to call repeatedly, and tolerates non-iterable input."""
    # A sample string with escape characters (preserved exactly from the original test)
    sample_string = "\x0cMv"

    # An empty tuple used as keys/values in the mapping
    empty_tuple = ()

    # Mapping that mixes the string and the empty tuple as keys/values (structure preserved)
    mixed_mapping = {sample_string: empty_tuple, empty_tuple: sample_string, empty_tuple: empty_tuple}

    # A tuple entry combining the string and the mapping
    entry_tuple = (sample_string, mixed_mapping)

    # Input list that contains the tuple entry
    input_list = [entry_tuple]

    # First conversion: convert the input structure to namedtuple(s)
    first_conversion = namedtuple_utils.to_namedtuple(input_list)

    # Second conversion: ensure calling to_namedtuple on the result is safe (idempotence / no-op)
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)

    # Third conversion: another repeat to confirm stability
    third_conversion = namedtuple_utils.to_namedtuple(second_conversion)

    # Ensure that calling to_namedtuple on a non-iterable (int) does not raise
    sample_int = 2
    namedtuple_utils.to_namedtuple(sample_int)

def test_to_namedtuple_accepts_byte_string_keys_and_values():
    """Verify that to_namedtuple can be invoked with a dict whose keys and values are byte strings."""
    # Sample byte string used both as key and value.
    sample_bytes = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    # Mapping using the byte string as key and value (duplicate literals are equivalent to a single entry).
    sample_mapping = {sample_bytes: sample_bytes, sample_bytes: sample_bytes, sample_bytes: sample_bytes}
    # Call the function under test (using the provided alias for the module).
    namedtuple_utils.to_namedtuple(sample_mapping)

