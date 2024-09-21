from flask import Flask
import graphene
from schemas import Query, Mutation
from flask_graphql import GraphQLView
from models import db
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:C0dingTemp012!@localhost/bakery_inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

# Set up the GraphQL schema
schema = graphene.Schema(query=Query, mutation=Mutation)

# Register the GraphQL endpoint and enable the GraphiQL UI
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    with app.app_context():
        # Create all database tables
        db.create_all()

    app.run(debug=True, port=8080)
