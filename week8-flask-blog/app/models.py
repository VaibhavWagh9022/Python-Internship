from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# ---------------------------------------------------------------------------
# Association table: posts <-> tags (many-to-many)
# ---------------------------------------------------------------------------
post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id',  db.Integer, db.ForeignKey('tag.id'),  primary_key=True),
)


# ---------------------------------------------------------------------------
# User
# ---------------------------------------------------------------------------
class User(UserMixin, db.Model):
    """Registered user — can author posts and leave comments."""
    __tablename__ = 'user'

    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64),  unique=True, nullable=False, index=True)
    email         = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256))
    about_me      = db.Column(db.String(500))
    avatar_url    = db.Column(db.String(256), default='default_avatar.png')
    is_admin      = db.Column(db.Boolean, default=False)
    member_since  = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen     = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    posts    = db.relationship('Post',    backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    # ------------------------------------------------------------------
    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def ping(self) -> None:
        """Update last_seen timestamp."""
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def __repr__(self) -> str:
        return f'<User {self.username}>'


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))


# ---------------------------------------------------------------------------
# Category
# ---------------------------------------------------------------------------
class Category(db.Model):
    __tablename__ = 'category'

    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(64), unique=True, nullable=False)
    slug  = db.Column(db.String(64), unique=True, nullable=False)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self) -> str:
        return f'<Category {self.name}>'


# ---------------------------------------------------------------------------
# Tag
# ---------------------------------------------------------------------------
class Tag(db.Model):
    __tablename__ = 'tag'

    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    slug = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Tag {self.name}>'


# ---------------------------------------------------------------------------
# Post
# ---------------------------------------------------------------------------
class Post(db.Model):
    """Blog post authored by a User."""
    __tablename__ = 'post'

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(200), nullable=False)
    slug        = db.Column(db.String(200), unique=True, nullable=False, index=True)
    content     = db.Column(db.Text, nullable=False)
    summary     = db.Column(db.String(500))          # short excerpt
    image_url   = db.Column(db.String(256))          # optional cover image
    timestamp   = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published   = db.Column(db.Boolean, default=True)
    views       = db.Column(db.Integer, default=0)

    # Foreign keys
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    # Relationships
    comments = db.relationship(
        'Comment', backref='post', lazy='dynamic',
        cascade='all, delete-orphan'
    )
    tags = db.relationship('Tag', secondary=post_tags, backref='posts', lazy='dynamic')

    # ------------------------------------------------------------------
    def increment_views(self) -> None:
        self.views += 1
        db.session.add(self)

    def __repr__(self) -> str:
        return f'<Post {self.title!r}>'


# ---------------------------------------------------------------------------
# Comment
# ---------------------------------------------------------------------------
class Comment(db.Model):
    """Comment on a blog Post, written by a User."""
    __tablename__ = 'comment'

    id        = db.Column(db.Integer, primary_key=True)
    content   = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    approved  = db.Column(db.Boolean, default=True)   # set False for moderation

    # Foreign keys
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id   = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self) -> str:
        return f'<Comment {self.id} on Post {self.post_id}>'
