import pytest
from calculator import compute_calculation, prefix_calc, infix_calc


class TestCalculator:
    def test_compute_calculation(self):
        with pytest.raises(AssertionError):
            compute_calculation('test')
        with pytest.raises(AssertionError):
            compute_calculation('+ 3 2 hello')
        with pytest.raises(AssertionError):
            compute_calculation('world ( 3 + 2 )')

    def test_prefix_calc(self):
        assert prefix_calc('') is None
        assert prefix_calc('3') == 3
        assert prefix_calc(' + 1 2') == 3
        assert prefix_calc(' + 1 * 2 3') == 7
        assert prefix_calc(' + * 1 2 3') == 5
        assert prefix_calc(' - / 10 + 1 1 * 1 2') == 3
        assert prefix_calc(' - 0 3') == -3
        assert prefix_calc(' / 3 2') == 1.5

    def test_infix_calc(self):
        assert infix_calc('') is None
        with pytest.raises(AssertionError):
            infix_calc('( 3 + 2 ')
        with pytest.raises(AssertionError):
            infix_calc('(((3 + 2) / 5 )')

        assert infix_calc('( 1 + 2 )') == 3
        assert infix_calc('( 1 + ( 2 * 3 ) )') == 7
        assert infix_calc('( ( 1 * 2 ) + 3 )') == 5
        assert infix_calc('( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )') == -1.8

