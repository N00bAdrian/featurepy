# from messageBoard import create_app
from fopy import select_equation

select_equation('config.equation')

# import messageBoard
# app = messageBoard.create_app()

from messageBoard import create_app
app = create_app()