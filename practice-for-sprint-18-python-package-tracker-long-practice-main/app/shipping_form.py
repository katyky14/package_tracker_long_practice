from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map


origin_cities = [city for city in map.keys()]
# destination_cities = [city for city in map.values()]
# destination_city = [city for city in destination_cities.values()]
def one_city(x):
  city = x.keys()
  values = set()
  for i in city:
    values.update(x[i])
  return list(values)




class ShippingForm(FlaskForm):
  sender_name = StringField('Sender Name', validators=[DataRequired()])
  recipient_name = StringField('Recipient Name', validators=[DataRequired()])
  origin = SelectField('Choose an origin', choices=origin_cities, validators=[DataRequired()])
  destination = SelectField('Choose a destination', choices=one_city(map), validators=[DataRequired()])
  express = BooleanField('Express Shipping')
  submit = SubmitField('Send package')
  cancel = SubmitField('Cancel')
