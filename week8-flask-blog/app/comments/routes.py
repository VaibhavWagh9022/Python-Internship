from flask import redirect, url_for, flash, request, abort
from flask_login import login_required, current_user

from app import db
from app.comments import bp
from app.comments.forms import CommentForm
from app.models import Comment, Post


@bp.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def create(post_id):
    """Add a new comment to a post."""
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            content  = form.content.data,
            author   = current_user,
            post     = post,
            approved = True,   # change to False for moderation queue
        )
        db.session.add(comment)
        db.session.commit()
        flash('Comment posted!', 'success')
    else:
        flash('Comment cannot be empty.', 'warning')
    return redirect(url_for('posts.show', slug=post.slug))


@bp.route('/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete(comment_id):
    """Delete a comment (owner or admin only)."""
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user and not current_user.is_admin:
        abort(403)
    post_slug = comment.post.slug
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted.', 'info')
    return redirect(url_for('posts.show', slug=post_slug))


@bp.route('/<int:comment_id>/approve', methods=['POST'])
@login_required
def approve(comment_id):
    """Approve a pending comment (admin only)."""
    if not current_user.is_admin:
        abort(403)
    comment = Comment.query.get_or_404(comment_id)
    comment.approved = True
    db.session.commit()
    flash('Comment approved.', 'success')
    return redirect(request.referrer or url_for('main.index'))
