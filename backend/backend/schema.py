import graphene
from graphene_django import DjangoObjectType
from storedata import models


class PersonType(DjangoObjectType):
    class Meta:
        model = models.Person
        fields = ('id', 'name', 'age')


class Query(graphene.ObjectType):
    all_names = graphene.List(PersonType)

    def resolve_all_names(root, info):
        return models.Person.objects.all()


schema = graphene.Schema(query=Query)
