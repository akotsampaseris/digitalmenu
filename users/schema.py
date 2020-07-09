from django.contrib.auth import authenticate, login

import graphene
import django_filters
from graphene_django import DjangoObjectType, DjangoListField
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'
        filter_fields = ['email']
        interfaces = (graphene.relay.Node, )


class UserInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    first_name = graphene.String()
    last_name = graphene.String()


class Query:
    me = graphene.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)

    @login_required
    def resolve_me(self, info):
        user = info.context.user

        return user


class RegisterUserMutation(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, user_data=None):
        user = User.objects.create(
            email=user_data.email
        )
        user.set_password(user_data.password)
        user.save()

        return RegisterUserMutation(user=user)


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, user_data=None):
        user = User.objects.create(
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name
            )
        user.set_password(user_data.password)
        user.save()

        return CreateUserMutation(user=user)


class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, user_data):
        user = User.objects.get(email=user_data.email)
        user.first_name = user_data.first_name
        user.last_name  = user_data.last_name
        user.save()

        return UpdateUserMutation(user=user)


class DeleteUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, email):
        user = User.objects.get(email=email)
        user.is_active = False
        #shop.slug = slug+'_deleted'
        user.save()

        return DeleteUserMutation(user=user)


class UndeleteUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, email):
        user = User.objects.get(email=email)
        user.is_active = True
        #shop.slug = slug.replace('_deleted', '')
        user.save()

        return UndeleteUserMutation(user=user)


class Mutation(graphene.ObjectType):
    register_user = RegisterUserMutation.Field()
    create_user   = CreateUserMutation.Field()
    update_user   = UpdateUserMutation.Field()
    delete_user   = DeleteUserMutation.Field()
    undelete_user = UndeleteUserMutation.Field()
