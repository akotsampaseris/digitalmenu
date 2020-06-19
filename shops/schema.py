import graphene
import django_filters
from graphene_django import DjangoObjectType, DjangoListField
from graphene_django.filter import DjangoFilterConnectionField

from .models import Shop

class ShopType(DjangoObjectType):
    class Meta:
        model = Shop
        fields = '__all__'
        filter_fields = ['name', 'slug', 'category', 'location']
        interfaces = (graphene.relay.Node, )


class Query:
    shop = graphene.relay.Node.Field(ShopType)
    all_shops = DjangoFilterConnectionField(ShopType)


class CreateShopMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        slug = graphene.String(required=True)

    shop = graphene.Field(ShopType)

    def mutate(self, info, name, slug):
        shop = Shop.objects.create(
            name=name,
            slug=slug,
            )

        return CreateShopMutation(shop=shop)


class UpdateShopMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        slug = graphene.String(required=True)

    shop = graphene.Field(ShopType)

    def mutate(self, info, name, slug):
        shop = Shop.objects.get(slug=slug)
        shop.name = name
        shop.save()

        return UpdateShopMutation(shop=shop)


class DeleteShopMutation(graphene.Mutation):
    class Arguments:
        slug = graphene.String()

    shop = graphene.Field(ShopType)

    def mutate(self, info, slug):
        shop = Shop.objects.get(slug=slug)
        shop.delete()

        return DeleteShopMutation(shop=shop)


class Mutation(graphene.ObjectType):
    create_shop = CreateShopMutation.Field()
    update_shop = UpdateShopMutation.Field()
    delete_shop = DeleteShopMutation.Field()
