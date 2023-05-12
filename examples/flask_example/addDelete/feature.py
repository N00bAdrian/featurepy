from aspectlib import Aspect, weave, Proceed, Return
from bs4 import BeautifulSoup
from flask import render_template_string

from .routes import delete

@Aspect
def addDeleteButton(filename, **kwargs):
    with open(f'messageBoard/templates/{filename}') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        card = soup.find("div", class_="card-body")
        del_button = soup.new_tag("a", attrs={
            "class": "btn btn-danger",
            "href": "/delete/{{msg.id}}"
        })
        del_button.string = "Delete"
        card.append(del_button)

        yield Return(render_template_string(soup.prettify(), **kwargs))

@Aspect
def addDeleteRoute():
    app = yield Proceed
    app.register_blueprint(delete.bp)

    yield Return(app)

class DeleteTemplate:
    def refine_get(self, original):
        def get(cls):
            with weave("flask.render_template", addDeleteButton):
                return original(cls)
            
        return get
    
class DeleteRoute:
    def refine_create_app(self, original):
        def create_app():
            app = original()
            app.register_blueprint(delete.bp)
            return app
        
        return create_app

def select(composer):
    # composer.compose_later(DeleteRoute(), 'messageBoard.app_factory')
    from messageBoard.routes.home import HomeView
    import messageBoard

    composer.compose(DeleteTemplate(), HomeView)
    composer.compose(DeleteRoute(), messageBoard)
    # weave('messageBoard.create_app', addDeleteRoute)