import pytest
from api import PetFriends
from settings import valid_email, valid_password
from settings import invalid_email1, invalid_password1
from settings import invalid_email2, invalid_password2

pf = PetFriends
@pytest.fixture(autouse=True)
def test_get_api_key():
    """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, pytest.key = pf.get_api_key(valid_email, valid_password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in pytest.key

    yield

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert pytest.status == 200


@pytest.mark.parametrize("filter", ['', 'my_pets'], ids=['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(filter):
    """ Проверяем, что запрос всех питомцев возвращает не пустой список.
   Для этого сначала получаем api-ключ и сохраняем в переменную auth_key. Далее, используя этот ключ,
   запрашиваем список всех питомцев и проверяем, что список не пустой.
   Доступное значение параметра filter - 'my_pets' либо '' """

    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)

    assert len(result['pets']) > 0
