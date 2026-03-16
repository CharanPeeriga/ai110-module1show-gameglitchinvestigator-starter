"""
conftest.py – runs before any test file is collected.

Mocks the `streamlit` module so that importing app.py (which has module-level
st.* calls) doesn't raise errors during the pytest collection phase.
"""
import sys
from unittest.mock import MagicMock

if "streamlit" not in sys.modules:
    mock_st = MagicMock()

    # selectbox must return a valid difficulty string or the dict lookup in app.py errors
    mock_st.sidebar.selectbox.return_value = "Normal"

    # columns(n) must be unpackable into n values
    def _columns(n, *args, **kwargs):
        return [MagicMock() for _ in range(n)]
    mock_st.columns.side_effect = _columns

    # session_state uses attribute access (st.session_state.secret) not dict access,
    # so it must be a MagicMock, not a plain dict.
    mock_st.session_state = MagicMock()

    sys.modules["streamlit"] = mock_st
