# import graphene
# from graphene_sqlalchemy import SQLAlchemyObjectType
# from models import db, Product

# class ProductType(SQLAlchemyObjectType):
#     class Meta:
#         model = Product

# class Query(graphene.ObjectType):
#     all_products = graphene.List(ProductType)
#     product_by_id = graphene.Field(ProductType, id=graphene.Int(required=True))

#     def resolve_all_products(self, info):
#         return db.session.query(Product).all()

#     def resolve_product_by_id(self, info, id):
#         return db.session.get(Product, id)

# class CreateProduct(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#         price = graphene.Float(required=True)
#         quantity = graphene.Int(required=True)
#         category = graphene.String(required=True)

#     product = graphene.Field(ProductType)

#     def mutate(self, info, name, price, quantity, category):
#         new_product = Product(name=name, price=price, quantity=quantity, category=category)
#         db.session.add(new_product)
#         db.session.commit()
#         return CreateProduct(product=new_product)

# class UpdateProduct(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         name = graphene.String()
#         price = graphene.Float()
#         quantity = graphene.Int()
#         category = graphene.String()

#     product = graphene.Field(ProductType)

#     def mutate(self, info, id, name=None, price=None, quantity=None, category=None):
#         product = db.session.get(Product, id)
#         if product:
#             if name is not None:
#                 product.name = name
#             if price is not None:
#                 product.price = price
#             if quantity is not None:
#                 product.quantity = quantity
#             if category is not None:
#                 product.category = category
#             db.session.commit()
#             return UpdateProduct(product=product)
#         return UpdateProduct(product=None)  # Return None if product is not found

# class DeleteProduct(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)

#     success = graphene.Boolean()

#     def mutate(self, info, id):
#         product = db.session.get(Product, id)
#         if product:
#             db.session.delete(product)
#             db.session.commit()
#             return DeleteProduct(success=True)
#         return DeleteProduct(success=False)

# class Mutation(graphene.ObjectType):
#     create_product = CreateProduct.Field()
#     update_product = UpdateProduct.Field()
#     delete_product = DeleteProduct.Field()




import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import db, Product

class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = Product

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product_by_id = graphene.Field(ProductType, id=graphene.Int(required=True))

    def resolve_all_products(self, info):
        return db.session.query(Product).all()

    def resolve_product_by_id(self, info, id):
        return db.session.get(Product, id)

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        quantity = graphene.Int(required=True)
        category = graphene.String(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, price, quantity, category):
        new_product = Product(name=name, price=price, quantity=quantity, category=category)
        db.session.add(new_product)
        db.session.commit()
        return CreateProduct(product=new_product)

class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        price = graphene.Float()
        quantity = graphene.Int()
        category = graphene.String()

    product = graphene.Field(ProductType)

    def mutate(self, info, id, name=None, price=None, quantity=None, category=None):
        product = db.session.get(Product, id)
        if product:
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity
            if category is not None:
                product.category = category
            db.session.commit()
            return UpdateProduct(product=product)
        return UpdateProduct(product=None)  # Return None if product is not found

class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        product = db.session.get(Product, id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return DeleteProduct(success=True)
        return DeleteProduct(success=False)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()