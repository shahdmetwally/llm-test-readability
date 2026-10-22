# MANDATORY: Always include `import pytest` on its own line at the top.
import pytest
import codetiming_timer as module_0

import pytest
from unittest import mock
from mymodule import Module

class TestModule:
    @pytest.mark.asyncio
    async def test_setup_cfg_command_class(self):
        none_value = None
        with mock.patch.object(Module, 'build_setup_cfg_command_class', return_value=None):
            module = Module()
            result = await module.build_setup_cfg_command_class(none_value)
            assert result is None