from peewee import *
import datetime

db = SqliteDatabase('data.db')

class Fellah(Model):
    id=PrimaryKeyField()
    full_name=CharField()

    class Meta:
        database=db


class Mois(Model):
    id=PrimaryKeyField()
    label=TextField()
    designation=TextField()

    class Meta:
        database=db


class Aliment(Model):
    id = PrimaryKeyField()
    idmois = IntegerField()
    idfella = IntegerField()
    qunatite = IntegerField()
    date = DateTimeField(default=datetime.datetime.now)
    designation = TextField()

    class Meta:
        database = db


class Dette(Model):
    id=PrimaryKeyField()
    idfellah=IntegerField()
    prix=IntegerField()
    date=DateTimeField(default=datetime.datetime.now)
    idmois=IntegerField()
    designation=TextField()

    class Meta:
        database=db


class Creance(Model):
    id=PrimaryKeyField()
    idfellah=IntegerField()
    prix=IntegerField()
    q_lait_retenu=IntegerField ()
    prixu=IntegerField()
    idmois=IntegerField()
    total=IntegerField()
    designation=TextField()

    class Meta:
        database=db


class Facture(Model):
    id=PrimaryKeyField()
    idfellah=IntegerField()
    idmois=IntegerField()
    net=IntegerField()
    total_lait=IntegerField()
    total_aliment=IntegerField()
    total_dette=IntegerField()
    total_debit=IntegerField()
    total_gain=IntegerField()
    total_retenu=IntegerField()
    idcreance=IntegerField()
    prix=IntegerField()
    q_lait_retenu=IntegerField ()
    prixu=IntegerField()
    total=IntegerField()
    designation=TextField()
    date=DateTimeField(default=datetime.datetime.now)

    class Meta:
        database=db


class Virement(Model):
    id=PrimaryKeyField()
    idfellah=IntegerField()
    prix=IntegerField()
    date=DateTimeField(default=datetime.datetime.now)
    idmois=IntegerField()

    class Meta:
        database=db


class Lait(Model):
    id=PrimaryKeyField()
    idfellah=IntegerField()
    idmois=IntegerField()
    totale=IntegerField()
    prixu=IntegerField()
    date=DateTimeField(default=datetime.datetime.now)

    class Meta:
        database=db




class Lait_de_plus(Model):
    id = PrimaryKeyField()
    idfellah = IntegerField()
    idmois = IntegerField()
    date = DateTimeField(default=datetime.datetime.now)
    prixu = IntegerField()

    class Meta:
        database=db


class Debit(Model):
    id = PrimaryKeyField()
    idfellah = IntegerField()
    idmois = IntegerField()
    date = DateTimeField(default=datetime.datetime.now)
    prixu = IntegerField()
    somme=IntegerField()

    class Meta:
        database=db










def dbconnect():
    db.connect()

def create_database():

    if Fellah.table_exists():
        pass
    else:
        db.create_table(Fellah)

    if Mois.table_exists():
        pass
    else:
        db.create_table(Mois)

    if Aliment.table_exists():
        pass
    else:
        Aliment.create_table(Aliment)


    if Dette.table_exists():
        pass
    else:
        Dette.create_table(Dette)

    if Creance.table_exists():
        pass
    else:
        Creance.create_table(Creance)

    if Facture.table_exists():
        pass
    else:
        Facture.create_table(Facture)

    if Lait.table_exists():
        pass
    else:
        Lait.create_table(Lait)

    if Virement.table_exists():
        pass
    else:
        Virement.create_table(Virement)

    if Debit.table_exists():
        pass
    else:
        Debit.create_table(Debit)


    if Lait_de_plus.table_exists():
        pass
    else:
        Lait_de_plus.create_table(Lait_de_plus)



