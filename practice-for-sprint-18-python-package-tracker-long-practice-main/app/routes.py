from flask import Blueprint, render_template
from .shipping_form import ShippingForm

bp = Blueprint("root", __name__, url_prefix="/")

@bp.route("/")
def index():
    return "Package Tracker"

@bp.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    # if form.validate_on_submit():
    #     shipped =
    return render_template('shipping_request.html', form=form)
