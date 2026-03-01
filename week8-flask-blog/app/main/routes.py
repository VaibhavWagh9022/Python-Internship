from flask import render_template, request, flash, redirect, url_for, current_app
from flask_login import current_user

from app import db
from app.main import bp
from app.main.forms import SearchForm, ContactForm
from app.models import Post, User, Category, Tag


@bp.route('/')
@bp.route('/index')
def index():
    """Home page — latest published posts."""
    page  = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True)\
                      .order_by(Post.timestamp.desc())\
                      .paginate(page=page,
                                per_page=current_app.config['POSTS_PER_PAGE'],
                                error_out=False)
    categories = Category.query.all()
    recent     = Post.query.filter_by(published=True)\
                           .order_by(Post.timestamp.desc()).limit(5).all()
    return render_template(
        'main/index.html',
        title='Home',
        posts=posts,
        categories=categories,
        recent=recent,
    )


@bp.route('/search')
def search():
    """Full-text search across post titles and content."""
    form = SearchForm(request.args, meta={'csrf': False})
    q    = request.args.get('q', '').strip()
    page = request.args.get('page', 1, type=int)

    if q:
        posts = Post.query.filter(
            Post.published == True,  # noqa: E712
            (Post.title.ilike(f'%{q}%')) | (Post.content.ilike(f'%{q}%'))
        ).order_by(Post.timestamp.desc())\
         .paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    else:
        posts = None

    return render_template('main/search.html', title='Search', q=q, posts=posts, form=form)


@bp.route('/about')
def about():
    return render_template('main/about.html', title='About')


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # In a real app you would send an email here via Flask-Mail
        flash('Thanks for reaching out! We\'ll get back to you soon.', 'success')
        return redirect(url_for('main.contact'))
    return render_template('main/contact.html', title='Contact', form=form)


@bp.route('/category/<slug>')
def category(slug):
    cat   = Category.query.filter_by(slug=slug).first_or_404()
    page  = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True, category=cat)\
                      .order_by(Post.timestamp.desc())\
                      .paginate(page=page,
                                per_page=current_app.config['POSTS_PER_PAGE'],
                                error_out=False)
    return render_template('main/category.html', title=cat.name, category=cat, posts=posts)


@bp.route('/tag/<slug>')
def tag(slug):
    tag_  = Tag.query.filter_by(slug=slug).first_or_404()
    page  = request.args.get('page', 1, type=int)
    posts = tag_.posts.filter_by(published=True)\
                      .order_by(Post.timestamp.desc())\
                      .paginate(page=page,
                                per_page=current_app.config['POSTS_PER_PAGE'],
                                error_out=False)
    return render_template('main/tag.html', title=f'#{tag_.name}', tag=tag_, posts=posts)


@bp.route('/rss')
def rss():
    """RSS / Atom feed of latest posts."""
    from feedgen.feed import FeedGenerator
    from flask import make_response

    fg = FeedGenerator()
    fg.id(request.url_root)
    fg.title('My Flask Blog')
    fg.link(href=request.url_root, rel='alternate')
    fg.description('Latest posts from My Flask Blog')

    posts = Post.query.filter_by(published=True)\
                      .order_by(Post.timestamp.desc()).limit(20).all()
    for post in posts:
        fe = fg.add_entry()
        fe.id(url_for('posts.show', slug=post.slug, _external=True))
        fe.title(post.title)
        fe.link(href=url_for('posts.show', slug=post.slug, _external=True))
        fe.description(post.summary or post.content[:300])
        fe.published(post.timestamp.replace(tzinfo=__import__('datetime').timezone.utc))

    rss_str  = fg.rss_str(pretty=True)
    response = make_response(rss_str)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response
