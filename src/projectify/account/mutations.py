
import graphql_jwt

import graphene

from projectify.graph.app_schema import(

		UserType,
		

	)


# The Json web token


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):

	user = graphene.Field(UserType)

	@classmethod
	def resolve(cls, root, info, **kwargs):

		return cls(user=info.context.user)