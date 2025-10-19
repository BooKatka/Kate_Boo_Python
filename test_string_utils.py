import pytest
from string_utils import StringUtils


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, res_in', [
        ("привет", "Привет"),
        ("hello", "Hello"),
        ])
def test_positive_capitalize(string_in, res_in):
    string = StringUtils()
    res = string.capitalize(string_in)
    assert res == res_in
 
@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, res_in', [
       (" Hello", "Hello"),
       ("  hello", "hello"),
       (" привет", "привет"),
       (" привет!", "привет!")
       ])
def test_positive_trim(string_in, res_in):
    string = StringUtils()
    res = string.trim(string_in)
    assert res == res_in

@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
      ("123", "3", True),
      ("Hello", "T", False),
      ("Привет", "в", True)
      ])
def test_positive_contains(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.contains(string_in,symbol_in)
    assert res == res_in

@pytest.mark.negative_test
@pytest.mark.parametrize('string_in, res_in', [
    (None, None),
    ("", ""),
    (" ", " ")
    ])
def test_negative_trim(string_in, res_in):
    string = StringUtils()
    res = string.trim(string_in)
    assert res == res_in

@pytest.mark.negative_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
      (" ", "H", False),
      ("123", "H", False)
       ])

@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
    ("Привет", "ив", "Прет"),
    ("Balls", "s", "Ball"),
    ("20 августа 1983", "1983", "20 августа"),
    ("1920", "20", "19")
    ])
def test_positive_delete_symbol(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.delete_symbol(string_in, symbol_in)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
    ("Привет", " ", "Привет"),
    ("Ball", "s", "Ball")
    ])
def test_negative_delete_symbol(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.delete_symbol(string_in, symbol_in)
    assert res == res_in
def test_negative_contains(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.contains(string_in, symbol_in)

    assert res == res_in
