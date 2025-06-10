import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from prompts import load_prompt

def test_load_prompt_thought_seeds():
    text = load_prompt("thought_seeds")
    assert isinstance(text, str) and text.strip()

