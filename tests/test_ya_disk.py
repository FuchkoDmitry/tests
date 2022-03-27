import pytest
from app.ya_disk import YaUploader


@pytest.fixture(scope='class')
def directories_list():
    directories = ['dir_1', 'dir_2', 'dir_3']
    yield directories
    del directories


class TestYaDisk:

    @classmethod
    def setup_class(self):
        self.ya_disk = YaUploader()

    @classmethod
    def teardown_class(self):
        del self.ya_disk

    def test_create_folder(self, directories_list):

        for directory in directories_list:
            status_code = self.ya_disk.create_folder(directory)
            assert status_code == 201

    def test_check_created_folder(self, directories_list):

        for directory in directories_list:
            result = self.ya_disk.check_created_folder(directory)
            assert result is True

    @pytest.mark.xfail(reason='folder not found')
    @pytest.mark.parametrize('dir_name', ['dir_4', 'dir_5'])
    def test_failed_check_created_folder(self, dir_name):
        result = self.ya_disk.check_created_folder(dir_name)
        assert result is True

    @pytest.mark.xfail(reason='folder was created earlier(error 409)')
    def test_failed_create_folder(self, directories_list):
        for directory in directories_list:
            status_code = self.ya_disk.create_folder(directory)
            assert status_code == 201
