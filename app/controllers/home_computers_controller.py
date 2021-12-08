from app.controllers.controller import ControllerBase
from flask import render_template

class HomeComputersController(ControllerBase):
    @staticmethod
    def get():
        return render_template('home_computers.html')