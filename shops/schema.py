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


class ShopInput(graphene.InputObjectType):
    slug = graphene.String(required=True)
    name = graphene.String(required=True)
    category = graphene.String()
    location = graphene.String()
    city = graphene.String()
    address_1 = graphene.String()
    address_2 = graphene.String()
    post_code = graphene.String()


class Query:
    shop = graphene.Field(ShopType, slug=graphene.String())
    all_shops = DjangoFilterConnectionField(ShopType)

    def resolve_shop(self, info, slug):
        return Shop.objects.get(slug=slug)


class CreateShopMutation(graphene.Mutation):
    class Arguments:
        shop_data = ShopInput(required=True)

    shop = graphene.Field(ShopType)

    def mutate(self, info, shop_data=None):
        shop = Shop.objects.create(
            slug=shop_data.slug,
            name=shop_data.name,
            category=shop_data.category,
            location=shop_data.location,
            city=shop_data.city,
            address_1=shop_data.address_1,
            address_2=shop_data.address_2,
            post_code=shop_data.post_code
            )

        return CreateShopMutation(shop=shop)


class UpdateShopMutation(graphene.Mutation):
    class Arguments:
        shop_data = ShopInput(required=True)

    shop = graphene.Field(ShopType)

    def mutate(self, info, shop_data):
        shop = Shop.objects.get(slug=shop_data.slug)
        shop.name = shop_data.name
        shop.category = shop_data.category
        shop.location = shop_data.location
        shop.city = shop_data.city
        shop.address_1 = shop_data.address_1
        shop.address_2 = shop_data.address_2
        shop.post_code = shop_data.post_code
        shop.save()

        return UpdateShopMutation(shop=shop)


class DeleteShopMutation(graphene.Mutation):
    class Arguments:
        slug = graphene.String(required=True)

    shop = graphene.Field(ShopType)

    def mutate(self, info, slug):
        shop = Shop.objects.get(slug=slug)
        shop.is_active = False
        #shop.slug = slug+'_deleted'
        shop.save()

        return DeleteShopMutation(shop=shop)


class UnDeleteShopMutation(graphene.Mutation):
    class Arguments:
        slug = graphene.String(required=True)

    shop = graphene.Field(ShopType)

    def mutate(self, info, slug):
        shop = Shop.objects.get(slug=slug)
        shop.is_active = True
        #shop.slug = slug.replace('_deleted', '')
        shop.save()

        return UnDeleteShopMutation(shop=shop)


class Mutation(graphene.ObjectType):
    create_shop = CreateShopMutation.Field()
    update_shop = UpdateShopMutation.Field()
    delete_shop = DeleteShopMutation.Field()
    undelete_shop = UnDeleteShopMutation.Field()
