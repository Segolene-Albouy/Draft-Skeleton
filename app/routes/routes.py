from flask import render_template, request, flash, redirect
from flask_login import current_user, login_user, logout_user

from ..app import app, login
# from ..constantes import LIEUX_PAR_PAGE
# from ..modeles.donnees import Place
# from ..modeles.utilisateurs import User


