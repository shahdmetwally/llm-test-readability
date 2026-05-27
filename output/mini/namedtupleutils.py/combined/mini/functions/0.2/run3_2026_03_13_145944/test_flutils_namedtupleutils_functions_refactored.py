import pytest

import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_accepts_float_input_no_exception():
    """Ensure to_namedtuple can be invoked with a float input (no exception expected)."""
    # Use the same literal input as the original test to preserve semantics.
    numeric_input = -476.66
    # Call the function under test; original test simply invoked the function without assertions.
    namedtuple_utils.to_namedtuple(numeric_input)

def test_to_namedtuple_handles_tuple_and_set_without_error():
    """Ensure to_namedtuple accepts a tuple containing a float and a set, and also accepts a set, without raising."""
    sample_float = -67.0
    duplicate_values_set = {sample_float, sample_float, sample_float, sample_float}
    input_tuple = (sample_float, duplicate_values_set)

    result_namedtuple = namedtuple_utils.to_namedtuple(input_tuple)
    namedtuple_utils.to_namedtuple(duplicate_values_set)

    assert isinstance(result_namedtuple, tuple)

def test_to_namedtuple_is_idempotent():
    """Convert a dict to a namedtuple and verify calling to_namedtuple again on the result is safe (idempotent)."""
    # Use the same literal key as the original test.
    key = "author"

    # Construct a dict using the key repeatedly (duplicate keys collapse, identical to original).
    input_dict = {key: key, key: key, key: key}

    # First conversion: dict -> namedtuple-like object.
    first_conversion = namedtuple_utils.to_namedtuple(input_dict)

    # Second conversion: call to_namedtuple on the previously converted object (should be safe / no-op).
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)

    # Ensure the second conversion is equivalent to the first (idempotent behavior).
    assert first_conversion == second_conversion

def test_to_namedtuple_accepts_bytes_input_no_exception():
    """Ensure to_namedtuple accepts a bytes input without raising an exception."""
    # Raw bytes input
    raw_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    # Call the function with bytes input; the test succeeds if no exception is raised.
    namedtuple_utils.to_namedtuple(raw_bytes)

def test_to_namedtuple_accepts_empty_tuple():
    """Ensure to_namedtuple can be called with an empty tuple (no exception raised)."""
    # Use an empty tuple as input (same literal as the original test).
    empty_tuple = ()
    # Call the function under test; we only ensure the call succeeds (original test had no assertions).
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_ordered_dict_and_various_inputs():
    """Ensure to_namedtuple accepts OrderedDict, namedtuples, and tuples containing a namedtuple and bytes."""
    # Start with an empty OrderedDict
    ordered_dict = collections_module.OrderedDict()

    # Convert OrderedDict to a namedtuple (multiple times to check repeated calls work)
    nt_from_ordered_dict_1 = namedtuple_utils.to_namedtuple(ordered_dict)
    nt_from_ordered_dict_2 = namedtuple_utils.to_namedtuple(ordered_dict)
    nt_from_ordered_dict_3 = namedtuple_utils.to_namedtuple(ordered_dict)
    nt_from_ordered_dict_4 = namedtuple_utils.to_namedtuple(ordered_dict)

    # Converting an already-converted namedtuple should be accepted (idempotence)
    nt_from_namedtuple = namedtuple_utils.to_namedtuple(nt_from_ordered_dict_1)
    nt_from_namedtuple_2 = namedtuple_utils.to_namedtuple(nt_from_ordered_dict_2)

    # A bytes literal — ensure it's accepted unchanged when paired with a namedtuple
    payload_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    pair_of_nt_and_bytes = (nt_from_namedtuple, payload_bytes)
    nt_from_pair = namedtuple_utils.to_namedtuple(pair_of_nt_and_bytes)

def test_to_namedtuple_handles_ordereddict_with_complex_key():
    """Ensure to_namedtuple accepts an OrderedDict created from a dict with a complex string key,
    and exercise OrderedDict construction from a single None positional argument.
    """
    # Complex string used as both key and value.
    complex_key = "wm=-g\ry#\x0b#:*"

    # Construct a dict where the complex string is both key and value.
    sample_dict = {complex_key: complex_key, complex_key: complex_key}

    # Build an OrderedDict via kwargs unpacking from the sample dict.
    ordered_dict_from_kwargs = collections_module.OrderedDict(**sample_dict)

    # Convert the OrderedDict to a namedtuple using the utility under test.
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict_from_kwargs)

    # Exercise OrderedDict construction from a single None positional argument.
    single_item_args = [None]
    collections_module.OrderedDict(*single_item_args)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Call to_namedtuple on a nested empty list and on None to ensure calls succeed (no assertions expected)."""
    # Create an empty list (same as original `list_0 = []`)
    empty_list = []

    # Create a list that contains the empty list (same as original `list_1 = [list_0]`)
    nested_list = [empty_list]

    # Call to_namedtuple with the nested list and capture the result
    # (same call and ordering as original `var_0 = module_0.to_namedtuple(list_1)`)
    result_namedtuple = namedtuple_utils.to_namedtuple(nested_list)

    # Call to_namedtuple with None to ensure it accepts None without raising
    # (same as original `module_0.to_namedtuple(none_type_0)`)
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_handles_various_input_shapes():
    """Ensure to_namedtuple can be called with diverse input types/structures without error."""
    # A long sample string used as both keys and values in a dict to exercise edge cases.
    sample_docstring = (
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
    # A dict literal where the same string key is repeated (mirrors original test input).
    repeated_str_dict = {
        sample_docstring: sample_docstring,
        sample_docstring: sample_docstring,
        sample_docstring: sample_docstring,
    }

    # First conversion from dict -> namedtuple
    first_namedtuple = namedtuple_utils.to_namedtuple(repeated_str_dict)

    # A boolean value used later as a dictionary key.
    false_flag_0 = False

    # Second conversion (same input again to exercise idempotency/consistency)
    second_namedtuple = namedtuple_utils.to_namedtuple(repeated_str_dict)

    # Wrap the namedtuple in a single-element tuple and convert that tuple to a namedtuple.
    single_element_tuple = (second_namedtuple,)
    tuple_namedtuple = namedtuple_utils.to_namedtuple(single_element_tuple)

    # Construct a dict with non-string key(s): one key is the tuple_namedtuple, another is a boolean.
    mixed_key_dict = {tuple_namedtuple: second_namedtuple, false_flag_0: second_namedtuple}

    # Convert that dict to a namedtuple and perform nested conversions and repeats.
    mixed_namedtuple = namedtuple_utils.to_namedtuple(mixed_key_dict)
    nested_namedtuple = namedtuple_utils.to_namedtuple(mixed_namedtuple)
    false_flag_1 = False
    another_namedtuple = namedtuple_utils.to_namedtuple(mixed_namedtuple)

    # Final call with a boolean argument (ensures boolean inputs are handled without error).
    namedtuple_utils.to_namedtuple(false_flag_1)

def test_to_namedtuple_handles_nested_structures_and_is_reentrant():
    """Verify to_namedtuple handles a nested list/dict/tuple structure and is safe to call repeatedly."""
    # Construct the same nested inputs as the original test, with clearer variable names.
    key_str = "\x0cMv"
    empty_tuple = ()
    mixed_dict = {key_str: empty_tuple, empty_tuple: key_str, empty_tuple: empty_tuple}
    pair_tuple = (key_str, mixed_dict)
    nested_list = [pair_tuple]

    # First conversion: list -> namedtuple-like structure
    nt1 = namedtuple_utils.to_namedtuple(nested_list)
    # Re-convert the result to ensure the function tolerates being called on its own output
    nt2 = namedtuple_utils.to_namedtuple(nt1)
    nt3 = namedtuple_utils.to_namedtuple(nt2)

    # Also ensure calling with an integer input is accepted (as in the original test)
    number_input = 2
    namedtuple_utils.to_namedtuple(number_input)

def test_to_namedtuple_handles_bytes_key_value_mapping():
    """Ensure to_namedtuple accepts a mapping with bytes keys and values without raising an exception."""
    # bytes object used both as key and value (the mapping literal intentionally repeats the same pair)
    bytes_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    single_entry_dict = {
        bytes_value: bytes_value,
        bytes_value: bytes_value,
        bytes_value: bytes_value,
    }
    # Call the function under test; the test passes if no exception is raised.
    namedtuple_utils.to_namedtuple(single_entry_dict)

