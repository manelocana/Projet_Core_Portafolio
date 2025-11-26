from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__)


@pages_bp.route('/pages')
def pages():
    return render_template('pages.html', search_button=True)
