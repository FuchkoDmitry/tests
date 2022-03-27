import pytest
import builtins
from unittest import mock
from app.secretary import documents, directories, check_document_existance, \
    get_doc_owner_name, add_new_shelf, append_doc_to_shelf, delete_doc, \
    add_new_doc, remove_doc_from_shelf, get_doc_shelf, move_doc_to_shelf


def get_docs_numbers(directory_docs):
    doc_numbers = set()
    for document in directory_docs:
        doc_numbers.add(document['number'])
    return doc_numbers


@pytest.mark.parametrize('user_doc_number', get_docs_numbers(documents))
def test_check_document_existance(user_doc_number):
    assert check_document_existance(user_doc_number) is True


def test_get_doc_owner_name():
    with mock.patch.object(builtins, 'input', lambda _: "10006"):
        assert get_doc_owner_name() == "Аристарх Павлов"


@pytest.mark.xfail
def test_add_new_shelf(shelf_num='5'):
    assert add_new_shelf(shelf_num)[1] is False


def test_add_new_shelf_2(shelf_num='5'):
    add_new_shelf(shelf_num)
    assert shelf_num in directories


@pytest.mark.parametrize('doc_number, shelf_number', [('12345', '4'), ('3456', '1')])
def test_append_doc_to_shelf(doc_number, shelf_number):
    append_doc_to_shelf(doc_number, shelf_number)
    assert shelf_number in directories and doc_number in directories[shelf_number]


@mock.patch.object(builtins, 'input', lambda _: '10006')
def test_get_doc_shelf():
    dir_number = get_doc_shelf()
    assert dir_number in directories and '10006' in directories[dir_number]


@pytest.mark.parametrize('doc_number, shelf_number', [('2207 876234', '2'), ('11-2', '3')])
def test_move_doc_to_shelf(doc_number, shelf_number):
    with mock.patch.object(builtins, 'input', lambda _: doc_number):
        assert get_doc_shelf() in directories
    move_doc_to_shelf(doc_number, shelf_number)
    assert doc_number in directories[shelf_number]


@pytest.mark.parametrize('doc_type, number, owner_name, shelf_num',
                         [('insurance', '3456780', 'Jack', '5')])
def test_add_new_doc(doc_type, number, owner_name, shelf_num):
    assert add_new_doc(number, doc_type, owner_name, shelf_num) in directories \
           and number in directories[shelf_num]


@pytest.mark.parametrize('doc_number, shelf_number', [('2207 876234', '2'), ('11-2', '3')])
def test_remove_doc_from_shelf(doc_number, shelf_number):
    assert doc_number in directories[shelf_number]
    remove_doc_from_shelf(doc_number)
    assert doc_number not in directories[shelf_number]


@mock.patch.object(builtins, 'input', lambda _: '10006')
def test_delete_doc():
    assert delete_doc()[0] not in get_docs_numbers(documents)


def test_delete_doc_2():
    with mock.patch.object(builtins, 'input', lambda _: '11-3'):
        assert delete_doc() is None
