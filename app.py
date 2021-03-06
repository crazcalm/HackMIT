import flask, flask.views
import zip_code, theaters, movies_info


app = flask.Flask(__name__)

app.secret_key = "bacon"

class Page1(flask.views.MethodView):
    def get(self):
        return flask.render_template("index.html")
    
    def post(self):
        
        geo_x = flask.request.form["geo_x"]
        geo_y = flask.request.form["geo_y"]
        
        stack = [geo_x, geo_y]
        
        zip1 = zip_code.main(stack)
        theater_list = theaters.main(zip1)
        
        #print geo_x, "\n", geo_y
        
        return flask.render_template("testing.html", theater_list = theater_list)
    
class Page2(flask.views.MethodView):
    def get(self,stuff):
        
        stuff = str(stuff)
        if stuff.find("US") != -1:
            stuff = stuff.replace("-", "/")
            print stuff
            stuff = movies_info.main(stuff)
            return flask.render_template("testing2.html", stuff = stuff)
        
        else:
            return "404"
        #return stuff
    
app.add_url_rule("/<stuff>", view_func=Page2.as_view("index2"), methods=["GET"])
app.add_url_rule("/", view_func=Page1.as_view("index"), methods=["GET", "POST"])

app.debug = True
app.run()