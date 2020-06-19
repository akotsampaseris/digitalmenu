import graphene

import shops.schema

class Query(shops.schema.Query,
            graphene.ObjectType):
    pass


class Mutation(shops.schema.Mutation,
               graphene.ObjectType):
    pass

schema = graphene.Schema(
            query=Query,
            mutation=Mutation,
            )
