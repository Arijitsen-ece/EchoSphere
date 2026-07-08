from unittest.mock import patch

from utils.theme import render_html_markup


def test_render_html_markup_passes_raw_html_to_component_renderer() -> None:
    with patch("utils.theme.components.html") as mock_html:
        render_html_markup('<h1 class="hero-title">EchoSphere</h1>', height=120)

    assert mock_html.called
    html_argument = mock_html.call_args.args[0]
    assert '<h1 class="hero-title">EchoSphere</h1>' in html_argument
    assert "<style>" in html_argument
