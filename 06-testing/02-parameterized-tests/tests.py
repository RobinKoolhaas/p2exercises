import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize('string', [
    '',
    '()',
    '(())',
    '((()))',
    '()()()',
    '(())()'
])
def test_matching_parentheses(string):
    assert matching_parentheses(string) is True, f'{string} has matching parentheses'


@pytest.mark.parametrize('string', [
    '(',
    ')',
    ')(',
    '(()))(()'
])
def test_non_matching_parentheses(string):
    assert matching_parentheses(string) is False, f'{string} has non-matching parentheses'
