import packages as pkg

def test_module0_versionpart_initialization():
    """Test initialization of VersionPart in module_0"""

    import module_0
    version_part_instance = module_0._VersionPart()
    assert type(version_part_instance).__name__ == "_VersionPart"

