"""Tests for the Agent OS V1 starter preset."""

from __future__ import annotations

from pathlib import Path
from unittest import mock

from click.testing import CliRunner

from openjarvis.cli import cli


def test_agent_os_v1_is_accepted_preset_name(tmp_path: Path) -> None:
    """The CLI should recognize agent-os-v1 as a supported preset name."""
    config_dir = tmp_path / ".openjarvis"
    config_path = config_dir / "config.toml"

    with (
        mock.patch("openjarvis.cli.init_cmd.DEFAULT_CONFIG_DIR", config_dir),
        mock.patch("openjarvis.cli.init_cmd.DEFAULT_CONFIG_PATH", config_path),
    ):
        result = CliRunner().invoke(cli, ["init", "--preset", "agent-os-v1"])

    assert "Invalid value for '--preset'" not in result.output


def test_agent_os_v1_installs_expected_configuration(tmp_path: Path) -> None:
    """Installing the preset should write the coordinated Agent OS configuration."""
    config_dir = tmp_path / ".openjarvis"
    config_path = config_dir / "config.toml"

    with (
        mock.patch("openjarvis.cli.init_cmd.DEFAULT_CONFIG_DIR", config_dir),
        mock.patch("openjarvis.cli.init_cmd.DEFAULT_CONFIG_PATH", config_path),
    ):
        result = CliRunner().invoke(cli, ["init", "--preset", "agent-os-v1"])

    assert result.exit_code == 0
    content = config_path.read_text(encoding="utf-8")
    assert 'default_agent = "orchestrator"' in content
    assert "context_from_memory = true" in content
    assert "[tools.mcp]" in content
    assert "[traces]" in content
    assert 'host = "127.0.0.1"' in content
