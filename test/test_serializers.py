from django.test import TestCase
from b_api.serializer import *
from b_api.models import *
class TestPostSerializer(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Orgimchak odam uyga yol yoq qismi ilk bor sifatli tarzda bizda',
        content='Orgimchak odam uyga yol yoq nomli film dunyo boylab screenrecorder holatda tarqalib ketgan edi shu boisidan ham sifatli filmni hali beri hech kim tomosha qilmagan.', 
        updated_on="2021-12-22", created_on="2021-12-22", status=1)
    def test_data(self):
        data =PostListSerializer(self.post).data
        self.assertIsNotNone(data)
        assert data['id'] is not None
        assert data['title'] == 'Orgimchak odam uyga yol yoq qismi ilk bor sifatli tarzda bizda'
        self.assertEqual(data['status'], 1)
        assert data['content'] == 'Orgimchak odam uyga yol yoq nomli film dunyo boylab screenrecorder holatda tarqalib ketgan edi shu boisidan ham sifatli filmni hali beri hech kim tomosha qilmagan.'
        assert data['updated_on'] == "2021-12-22"
        assert data['created_on'] == "2021-12-22"