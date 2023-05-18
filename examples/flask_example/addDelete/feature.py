from bs4 import BeautifulSoup
from tempfile import NamedTemporaryFile
from os import path

from .routes import delete

def add_delete_button(soup):
    card = soup.find("div", class_="card-body")
    del_button = soup.new_tag("a", attrs={
        "class": "btn btn-danger",
        "href": "/delete/{{msg.id}}"
    })
    del_button.string = "Delete"
    card.append(del_button)

    return soup

class DeleteTemplate:

    def refine_render(self, original):
        @staticmethod
        def render(filename, **kwargs):
            with open(f"messageBoard/templates/{filename}") as fp:
                soup = BeautifulSoup(fp, 'html.parser')
                soup = add_delete_button(soup)

                with NamedTemporaryFile(suffix=".html", dir="messageBoard/templates") as tfp:
                    tfp.write(str.encode(soup.prettify()))
                    tfp.seek(0)
                    return original(path.basename(tfp.name), **kwargs)
                
        return render
    
class DeleteRoute:
    def refine_create_app(self, original):
        def create_app():
            app = original()
            app.register_blueprint(delete.bp)
            return app
        
        return create_app

def select(composer):
    from messageBoard.routes.home import HomeView
    import messageBoard

    composer.compose(DeleteTemplate(), HomeView)
    composer.compose(DeleteRoute(), messageBoard)