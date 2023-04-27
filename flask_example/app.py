# from messageBoard import create_app
import messageBoard
from featuremonkey import select_equation

select_equation('config.equation')
app = messageBoard.create_app()