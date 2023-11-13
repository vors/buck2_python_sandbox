import lib
import sys
import torch
import pytest

def test_simple():
    assert lib.add_torch(1, 2) == torch.tensor(3)

# pytest.main([__file__])

