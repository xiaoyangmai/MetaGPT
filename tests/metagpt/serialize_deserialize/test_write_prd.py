# -*- coding: utf-8 -*-
# @Date    : 11/22/2023 1:47 PM
# @Author  : stellahong (stellahong@fuzhi.ai)
# @Desc    :

import pytest

from metagpt.actions import WritePRD
from metagpt.schema import Message


@pytest.mark.asyncio
async def test_action_serdeser(new_filename):
    action = WritePRD()
    ser_action_dict = action.model_dump()
    assert "name" in ser_action_dict
    assert "llm" not in ser_action_dict  # not export

    new_action = WritePRD(**ser_action_dict)
    assert new_action.name == "WritePRD"
    action_output = await new_action.run(with_messages=Message(content="write a cli snake game"))
    assert len(action_output.content) > 0
