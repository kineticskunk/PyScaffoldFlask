from flask_project import app , db

# Run Sever
if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)




# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))


# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = None
# db = SQLAlchemy(app)

# class Book(db.Model):
#     title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

#     def __repr__(self):
#         return "<Title: {}>".format(self.title)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.form:
#         book = Book(title=request.form.get("title"))
#         db.session.add(book)
#         db.session.commit()
#         # books = Book.query.all()
#     return render_template("home.html")

# @app.route("/update", methods=["POST"])
# def update():
#     newtitle = request.form.get("newtitle")
#     oldtitle = request.form.get("oldtitle")
#     book = Book.query.filter_by(title=oldtitle).first()
#     book.title = newtitle
#     db.session.commit()
    
#     if request.method == 'POST':
#          return redirect("/")
      
#     else:
#          return 'You Are using GET route'

    

# @app.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     book = Book.query.filter_by(title=title).first()
#     db.session.delete(book)
#     db.session.commit()
#     return redirect("/")
        
# if __name__ == "__main__":
#     app.run(debug=True)

# basedir = os.path.abspath(os.path.dirname(__file__))
# # Setting up SQL Database
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'db.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #Init Database
# db = SQLAlchemy(app)
# #Init ma
# ma = Marshmallow(app)
# # Product Class/Model

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name =db.Column(db.String(100), unique =True)
#     description = db.Column(db.String(200))
#     price =db.Column(db.Float)
#     qty = db.Column(db.Integer)

#     def __init__(self, name, description, price, qty):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.qty = qty
# #Product Schema
# class ProductSchema(ma.Schema):
#     class Meta:
#         fields =('id', 'name', 'description', 'price', 'qty')
# #Init schema
# pruduct_schema = ProductSchema(strict=True)  
# products_schema = ProductSchema(many=True, strict= True) 

# #Create a Product
# @app.route('/product', methods=['GET','POST'])
# def add_product():
#     name = request.json['name'] 
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     new_product = Product(name, description, price, qty)
#     db.session.add(new_product)
#     db.session.commit()

#     if request.method == 'POST':
#       return product_schema.jsonify(new_product)
#     else:
#          return 'You Are using GET route'

# #Getting All products

# @app.route('/product', methods=['GET'])
# def get_products():
#     all_products= Product.query.all()
#     result = products_schema.dump(all_products)
#     return jsonify(result.data)
         
# #Get Single product
# @app.route('/product/<id>', methods=['GET'])
# def get_product(id):
#     product= Product.query.get(id)
#     return product_schema.jsonify(product)

# #Update a Product 
      
# @app.route('/product/<id>', methods=['GET','POST'])
# def update_product():

#     product = Product.query.get(id) 
#     name = request.json['name'] 
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     product.name =name
#     product.description =description
#     product.price = price
#     product.qty= qty

#     db.session.commit()

#     if request.method == 'POST':
#       return product_schema.jsonify(product)
#     else:
#          return 'You Are using GET route'  

# #Delete a Product 
# @app.route('/product/<id>')
# def delete_product(id):
#     product= Product.query.get(id)
#     db.session.delete(product)
#     db.commit()
#     return products_schema.jsonify(product)               




