from flask import Blueprint, render_template, redirect
from .shipping_form import ShippingForm
from .models import Package, db

bp = Blueprint("root", __name__, url_prefix="/")

@bp.route("/")
def root_endpoint():
    packages = Package.query.all()
    Package.advance_all_locations()
    return render_template('package_status.html', packages=packages)


@bp.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')
    return render_template('shipping_request.html', form=form)
