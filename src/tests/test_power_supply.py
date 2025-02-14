import pytest
from src.models.power_supply import PowerSupply

@pytest.fixture
def sample_psu():
    """create a sample power supply object for testing"""
    return PowerSupply(
        manufacturer="SilverStone",
        name="SX750",
        sku=67890,
        price=139.99,
        size_standard="SFX",
        rated_wattage=750,
        certification_level="80+ Platinum",
        modular="Fully Modular",
        efficiency_rating_percentage=92.0,
        pcie_connectors=6,
        length=125
    )

# test getter methods
def test_get_size_standard(sample_psu):
    assert sample_psu.get_size_standard() == "SFX"

def test_get_rated_wattage(sample_psu):
    assert sample_psu.get_rated_wattage() == 750

def test_get_certification_level(sample_psu):
    assert sample_psu.get_certification_level() == "80+ Platinum"

def test_get_modular(sample_psu):
    assert sample_psu.get_modular() == "Fully Modular"

def test_get_efficiency_rating_percentage(sample_psu):
    assert sample_psu.get_efficiency_rating_percentage() == 92.0

def test_get_pcie_connectors(sample_psu):
    assert sample_psu.get_pcie_connectors() == 6

def test_get_length(sample_psu):
    assert sample_psu.get_length() == 125

# test setter methods
def test_set_size_standard(sample_psu):
    sample_psu.set_size_standard("ATX")
    assert sample_psu.get_size_standard() == "ATX"

def test_set_rated_wattage(sample_psu):
    sample_psu.set_rated_wattage(850)
    assert sample_psu.get_rated_wattage() == 850

def test_set_certification_level(sample_psu):
    sample_psu.set_certification_level("80+ Gold")
    assert sample_psu.get_certification_level() == "80+ Gold"

def test_set_modular(sample_psu):
    sample_psu.set_modular("Semi-Modular")
    assert sample_psu.get_modular() == "Semi-Modular"

def test_set_efficiency_rating_percentage(sample_psu):
    sample_psu.set_efficiency_rating_percentage(90.5)
    assert sample_psu.get_efficiency_rating_percentage() == 90.5

def test_set_pcie_connectors(sample_psu):
    sample_psu.set_pcie_connectors(4)
    assert sample_psu.get_pcie_connectors() == 4

def test_set_length(sample_psu):
    sample_psu.set_length(130)
    assert sample_psu.get_length() == 130

# test display_info method
def test_display_info(sample_psu):
    expected_output = (
        "SilverStone SX750 (SKU: 67890) - $139.99\n"
        "size standard: SFX\n"
        "wattage: 750W\n"
        "certification: 80+ Platinum\n"
        "modular: Fully Modular\n"
        "efficiency rating: 92.0%\n"
        "pcie connectors: 6\n"
        "length: 125mm"
    )
    assert sample_psu.display_info() == expected_output
