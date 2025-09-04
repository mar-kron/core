"""Hello state integration."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

DOMAIN = "hello_state"

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


def setup(hass: HomeAssistant, config) -> bool:
    """Set up the hello_state integration."""
    hass.states.set("hello_state.world", "Paulus")
    return True
