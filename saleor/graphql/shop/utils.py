from typing import Optional

from django_countries import countries

from ...shipping.models import ShippingZone


def get_countries_codes_list(in_shipping_zones: Optional[bool] = None):
    """Return set of countries codes."""
    all_countries_codes = {country[0] for country in countries}
    if in_shipping_zones is not None:
        covered_countries_codes = set()
        for zone in ShippingZone.objects.iterator():
            covered_countries_codes.update({country.code for country in zone.countries})

        if in_shipping_zones:
            return covered_countries_codes

        if not in_shipping_zones:
            return all_countries_codes - covered_countries_codes

    return all_countries_codes
