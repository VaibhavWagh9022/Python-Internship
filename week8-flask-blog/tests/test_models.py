"""Unit tests for database models."""
import unittest
from app import create_app, db
from app.models import User, Post, Comment


class UserModelTestCase(unittest.TestCase):
    """Tests for the User model."""

    def setUp(self):
        self.app = create_app('testing')
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_ctx.pop()

    def _make_user(self, username='alice', email='alice@example.com', password='password123'):
        u = User(username=username, email=email)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        return u

    # ----------------------------------------------------------------
    def test_password_hashing(self):
        u = self._make_user()
        self.assertTrue(u.check_password('password123'))
        self.assertFalse(u.check_password('wrongpassword'))

    def test_password_is_hashed(self):
        u = self._make_user()
        self.assertNotEqual(u.password_hash, 'password123')

    def test_unique_username(self):
        self._make_user()
        u2 = User(username='alice', email='other@example.com')
        u2.set_password('pass')
        db.session.add(u2)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_repr(self):
        u = self._make_user()
        self.assertIn('alice', repr(u))


class PostModelTestCase(unittest.TestCase):
    """Tests for the Post model."""

    def setUp(self):
        self.app = create_app('testing')
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        db.create_all()

        self.user = User(username='bob', email='bob@example.com')
        self.user.set_password('secret')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_ctx.pop()

    def _make_post(self, title='Hello World', content='Content here.', slug='hello-world'):
        p = Post(title=title, content=content, slug=slug, author=self.user)
        db.session.add(p)
        db.session.commit()
        return p

    # ----------------------------------------------------------------
    def test_create_post(self):
        p = self._make_post()
        self.assertEqual(Post.query.count(), 1)
        self.assertEqual(p.author, self.user)

    def test_post_default_published(self):
        p = self._make_post()
        self.assertTrue(p.published)

    def test_post_views_increment(self):
        p = self._make_post()
        self.assertEqual(p.views, 0)
        p.increment_views()
        db.session.commit()
        self.assertEqual(p.views, 1)

    def test_cascade_delete_comments(self):
        p = self._make_post()
        c = Comment(content='Nice post!', author=self.user, post=p)
        db.session.add(c)
        db.session.commit()
        self.assertEqual(Comment.query.count(), 1)
        db.session.delete(p)
        db.session.commit()
        self.assertEqual(Comment.query.count(), 0)


class CommentModelTestCase(unittest.TestCase):
    """Tests for the Comment model."""

    def setUp(self):
        self.app = create_app('testing')
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        db.create_all()

        self.user = User(username='carol', email='carol@example.com')
        self.user.set_password('pass')
        db.session.add(self.user)
        db.session.commit()

        self.post = Post(title='Test', slug='test', content='Body.', author=self.user)
        db.session.add(self.post)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_ctx.pop()

    def test_create_comment(self):
        c = Comment(content='Great!', author=self.user, post=self.post)
        db.session.add(c)
        db.session.commit()
        self.assertEqual(Comment.query.count(), 1)
        self.assertTrue(c.approved)

    def test_comment_repr(self):
        c = Comment(content='Hi', author=self.user, post=self.post)
        db.session.add(c)
        db.session.commit()
        self.assertIn(str(c.id), repr(c))


if __name__ == '__main__':
    unittest.main()
