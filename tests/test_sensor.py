"""Test NHL Sensor"""
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.nhl.const import DOMAIN
from tests.const import CONFIG_DATA


async def test_sensor(hass):

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="NHL",
        data=CONFIG_DATA,
    )

    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert "nhl" in hass.config.components
