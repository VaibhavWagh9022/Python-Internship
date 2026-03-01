import os
import re
import uuid
from flask import (
    render_template, redirect, url_for, flash,
    request, abort, current_app
)
from flask_login import login_required, current_user

from app import db
from app.posts import bp
from app.posts.forms import PostForm
from app.comments.forms import CommentForm
from app.models import Post, Category, Tag


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _slugify(text: str) -> str:
    """Turn a title into a URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text


def _save_image(file) -> str:
    """Save an uploaded image and return the filename."""
    ext      = file.filename.rsplit('.', 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"
    path     = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    return filename


def _populate_form_choices(form):
    """Fill the category dropdown with DB options."""
    categories       = Category.query.order_by(Category.name).all()
    form.category.choices = [(0, '— Select Category —')] + [
        (c.id, c.name) for c in categories
    ]


def _apply_tags(post: Post, tags_str: str):
    """Sync the post's tags from a comma-separated string."""
    tag_names = [t.strip().lower() for t in tags_str.split(',') if t.strip()]
    # Detach all current tags
    for t in post.tags.all():
        post.tags.remove(t)
    for name in tag_names:
        slug = _slugify(name)
        tag  = Tag.query.filter_by(slug=slug).first()
        if tag is None:
            tag = Tag(name=name, slug=slug)
            db.session.add(tag)
        post.tags.append(tag)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@bp.route('/')
def index():
    """List all published posts."""
    page  = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True)\
                      .order_by(Post.timestamp.desc())\
                      .paginate(page=page,
                                per_page=current_app.config['POSTS_PER_PAGE'],
                                error_out=False)
    return render_template('posts/index.html', title='All Posts', posts=posts)


@bp.route('/<slug>')
def show(slug):
    """Display a single post plus its comments."""
    post = Post.query.filter_by(slug=slug).first_or_404()
    if not post.published and (
        not current_user.is_authenticated or current_user != post.author
    ):
        abort(404)

    post.increment_views()
    db.session.commit()

    comments     = post.comments.filter_by(approved=True)\
                                .order_by(db.asc('timestamp')).all()
    comment_form = CommentForm()
    return render_template(
        'posts/show.html',
        title=post.title,
        post=post,
        comments=comments,
        comment_form=comment_form,
    )


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    _populate_form_choices(form)

    if form.validate_on_submit():
        slug = form.slug.data or _slugify(form.title.data)
        # Ensure slug is unique
        if Post.query.filter_by(slug=slug).first():
            slug = f"{slug}-{uuid.uuid4().hex[:6]}"

        post = Post(
            title     = form.title.data,
            slug      = slug,
            summary   = form.summary.data,
            content   = form.content.data,
            published = form.published.data,
            author    = current_user,
        )

        if form.category.data:
            post.category_id = form.category.data or None

        if form.image.data:
            post.image_url = _save_image(form.image.data)

        _apply_tags(post, form.tags.data or '')
        db.session.add(post)
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('posts.show', slug=post.slug))

    return render_template('posts/create.html', title='New Post', form=form)


@bp.route('/<slug>/edit', methods=['GET', 'POST'])
@login_required
def edit(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    if post.author != current_user and not current_user.is_admin:
        abort(403)

    form = PostForm(obj=post)
    _populate_form_choices(form)

    if form.validate_on_submit():
        post.title     = form.title.data
        post.slug      = form.slug.data
        post.summary   = form.summary.data
        post.content   = form.content.data
        post.published = form.published.data
        post.category_id = form.category.data or None

        if form.image.data:
            post.image_url = _save_image(form.image.data)

        _apply_tags(post, form.tags.data or '')
        db.session.commit()
        flash('Post updated!', 'success')
        return redirect(url_for('posts.show', slug=post.slug))
    elif request.method == 'GET':
        form.tags.data = ', '.join(t.name for t in post.tags.all())

    return render_template('posts/edit.html', title='Edit Post', form=form, post=post)


@bp.route('/<slug>/delete', methods=['POST'])
@login_required
def delete(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    if post.author != current_user and not current_user.is_admin:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.', 'info')
    return redirect(url_for('main.index'))
