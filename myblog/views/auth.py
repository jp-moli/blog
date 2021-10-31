from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

auth = Blueprint('auth', __name__, url_prefix='/auth')

#Registrar un usuario
@auth.route('/register')
def register():
    return "Registar usuario"