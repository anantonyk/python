from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModel:

    def test_is_in_stock(self):
        product = mixer.blend('products.Product', quantity=1)
        assert product.is_in_stock == True

    def test_is_not_in_stock(self):
        product = mixer.blend('products.Product', quantity=0)
        assert product.is_in_stock == False