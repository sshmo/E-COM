import datetime

from django.test import TestCase
from .models import User, Product, Customer, Comment

# utcnow() wrong : https://stackoverflow.com/a/61049837
date = str(datetime.datetime.now(datetime.timezone.utc))


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='first', last_name='last')

    def test_first_name_content(self):
        user = User.objects.get(id=2)
        expected_object_name = f'{user.first_name}'
        self.assertEquals(expected_object_name, 'first')

    def test_last_name_content(self):
        user = User.objects.get(id=2)
        expected_object_name = f'{user.last_name}'
        self.assertEquals(expected_object_name, 'last')


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        Product.objects.create(title='Harry_Potter',
                               description='A good book',
                               price=1.03,
                               image='https://api.time.com/harry.jpg',
                               categury='book',
                               stock_number=4,
                               creation_time=date,
                               status=True,
                               )

        User.objects.create(first_name='first', last_name='last')
        user = User.objects.get(id=1)
        product = Product.objects.get(id=1)
        product.watchers.add(user)
        product.save()

    def test_product_title(self):
        product = Product.objects.get(id=1)
        expected_object_title = f'{product.title}'
        self.assertEquals(expected_object_title, 'Harry_Potter')

    def test_product_description(self):
        product = Product.objects.get(id=1)
        expected_object_description = f'{product.description}'
        self.assertEquals(expected_object_description, 'A good book')

    def test_product_creation_time(self):
        product = Product.objects.get(id=1)
        expected_object_creation_time = str(product.creation_time)
        self.assertEquals(expected_object_creation_time, date)


class CommentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        # Create a comment
        test_Comment = Comment.objects.create(
            commenter=testuser1,
            title='Blog title',
            comment='Body content...',
            comment_time=date)
        test_Comment.save()

    def test_comment_content(self):
        comment = Comment.objects.get(id=1)

        commenter = f'{comment.commenter}'
        body = f'{comment.comment}'
        comment_time= str(comment.comment_time)

        self.assertEqual(commenter, 'testuser1')
        self.assertEqual(body, 'Body content...')
        self.assertEqual(comment_time, date)
