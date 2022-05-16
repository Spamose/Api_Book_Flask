from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from flask_cors import CORS, cross_origin
import datetime


app = Flask(__name__)


# Config BDD
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://postgres:Watibblackm17@localhost:5432/livre'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

db = SQLAlchemy(app)
CORS(app)


# Table livre


class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.BigInteger, nullable=False)
    titre = db.Column(db.String(50), nullable=False)
    auteur = db.Column(db.String(53), nullable=False)
    editeur = db.Column(db.String(53), nullable=False)
    dateSortie = db.Column(db.Date, nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)

    # METHODS

    def __repr__(self):
        return self.titre

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# Livre Schema


class LivreSchema(Schema):
    id = fields.Integer()
    isbn = fields.Integer()
    titre = fields.String()
    editeur = fields.String()
    auteur = fields.String()
    dateSortie = fields.DateTime()
    categorie_id = fields.Integer()


# Table categorie


class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    lib_categorie = db.Column(db.String(80), nullable=False)
    livres = db.relationship('Livre', backref='categories', lazy=True)

# ALL METHODS

    def __repr__(self):
        return self.lib_categorie

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# Categorie Schema


class CategorieSchema(Schema):
    id = fields.Integer()
    lib_categorie = fields.String()


####################################################################################################

@app.route('/livres', methods=['GET'])  # LISTE TOUS LES LIVRES
def get_all_livres():
    livres = Livre.get_all()
    serializer = LivreSchema(many=True)
    data = serializer.dump(livres)
    if livres is None:
        abort(404)
    else:
        return jsonify({"Nombres de livres": len(livres), "success": "True"}, data), 200


@app.route('/livres/<int:id>', methods=['GET'])  # LISTE DES LIVRES PAR ID
def get_id_livre(id):
    livres = Livre.get_by_id(id)
    serializer = LivreSchema()
    data = serializer.dump(livres)
    if livres is None:
        abort(404)
    return jsonify({"success": "True"}, data), 200


@app.route('/livres', methods=['POST'])  # AJOUTER LIVRES
def add_livre():
    data = request.get_json()

    try:
        new_livre = Livre(
            isbn=data.get('isbn'),
            titre=data.get('titre'),
            auteur=data.get('auteur'),
            editeur=data.get('editeur'),
            dateSortie=data.get('dateSortie'),
            categorie_id=data.get('categorie_id'))

        new_livre.save()
        serializer = LivreSchema()
        data = serializer.dump(new_livre)
        return jsonify({"success": "True", "message": "Ajout effectuer avec succes"}, data), 201

    except:
        abort(400)


@app.route('/livres/<int:id>', methods=['PUT'])  # MODIFIER LIVRES PAR ID
def update_livre(id):
    data = request.get_json()
    try:

        livre_to_update = Livre.get_by_id(id)
        if livre_to_update is None:
            abort(404)
        livre_to_update.isbn = data.get('isbn')
        livre_to_update.titre = data.get('titre')
        livre_to_update.auteur = data.get('auteur')
        livre_to_update.editeur = data.get('editeur')
        livre_to_update.dateSortie = data.get('dateSortie')
        livre_to_update.categorie_id = data.get('categorie_id')

        db.session.commit()
        serializer = LivreSchema()

        livre_data = serializer.dump(livre_to_update)
        return jsonify({"success": "True", "message": "Modification effectuer a succes"}, livre_data), 200

    except:
        abort(400)


# SUPPRESSION  LIVRES PAR ID
@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_livre(id):
    livre_to_delete = Livre.get_by_id(id)
    if livre_to_delete is None:
        abort(404)
    try:
        livre_to_delete.delete()
        return jsonify({"message": "Suppprimer avec succes"}), 204
    except:
        abort(400)


####################CATEGORIE#########################

@app.route('/categories', methods=['GET'])  # LISTE TOUTES LES CATGEGORIES
def get_all_categories():
    categories = Categorie.get_all()
    serializer = CategorieSchema(many=True)
    data = serializer.dump(categories)
    if categories is None:
        abort(404)
    else:
        return jsonify({"Nombres de categories": len(categories), "success": "True"}, data), 200


@app.route('/categories/<int:id>', methods=['GET'])  # LISTE CATEGORIES PAR ID
def get_id_categorie(id):
    categories = Categorie.get_by_id(id)
    serializer = CategorieSchema()
    data = serializer.dump(categories)
    if categories is None:
        abort(404)
    else:
        return jsonify({"success": "True"}, data), 200


@app.route('/categories', methods=['POST'])  # AJOUTER CATEGORIES
def add_cateorie():
    data = request.get_json()

    try:

        new_categorie = Categorie(
            lib_categorie=data.get('lib_categorie'))

        new_categorie.save()
        serializer = CategorieSchema()
        data = serializer.dump(new_categorie)
        return jsonify({"success": "True", "message": "Ajout effectuer avec succes"}, data), 201

    except:
        abort(400)


# MODIFIER CATEGORIES PAR ID
@app.route('/categories/<int:id>', methods=['PUT'])
def update_categorie(id):

        data = request.get_json()
    #try:

        categorie_to_update = Categorie.get_by_id(id)
        if categorie_to_update is None:
            abort(404)
        categorie_to_update.lib_categorie = data.get('lib_categorie')

        db.session.commit()
        serializer = CategorieSchema()

        categorie_data = serializer.dump(categorie_to_update)
        return jsonify({"success": "True", "message": "Modification effectuer a succes"}, categorie_data), 200

    #except:
        #abort(400)


# SUPPRESSION  LIVRES PAR ID
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_categorie(id):
    categorie_to_delete = Categorie.get_by_id(id)
    if categorie_to_delete is None:
        abort(404)
    try:
        categorie_to_delete.delete()
        return jsonify({"message": "Suppprimer avec succes"}), 204
    except:
        abort(400)


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad request'
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": 'Not found'
    }), 404


@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": 'Method Not allowed'
    }), 405


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": 'Unprocessable'
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": 'Internal server error',
    }), 500


# Run server
if __name__ == "__main__":
    app.run(debug=True)
