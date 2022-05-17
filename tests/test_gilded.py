import pytest

from logic.gilded_rose import GildedRose, Item

examples = (
    ("name", "input_sell_in", "input_quality", "expected_sell_in", "expected_quality"),
    [
        ("foo", 0, 0, -1, 0, "typical item"),
        ("foo", 2, 2, 1, 1, "typical item with 1 and 1"),
        ("Sulfuras, Hand of Ragnaros", 0, 0, 0, 0, "Sulfuras case"),
        ("Backstage passes to a TAFKAL80ETC concert", 5, 5, 4, 8, "Backstage case"),
    ]
)

@pytest.mark.parametrize(*examples)
def test_gilded(name, input_sell_in, input_quality, expected_sell_in, expected_quality):
    item = Item(name, input_sell_in, input_quality)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality

def test_foo():
    item = Item("foo", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == -1

def test_quality_2():
    item = Item("foo", 2, 2)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 1
    assert item.sell_in == 1

def test_sulfuras():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0
    assert item.sell_in == 0

def test_backstage():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 5)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 8
    assert item.sell_in == 4