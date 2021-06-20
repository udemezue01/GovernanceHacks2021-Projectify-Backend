import graphene
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError

'''
App models

'''

from django.contrib.auth import get_user_model
User = get_user_model()


from project.models import (

		Contractor,
		Project,
		Review,

	)

from post.models import (


	Post,
	Comment,

	)

from userprofile.models import(

	Profile

	)



		# The User Model


class UserType(DjangoObjectType):

	class Meta:
		model = User


		# The Profile Model

class ProfileType(DjangoObjectType):

	class Meta:

		model = Profile

	avatar 	 		= graphene.String()
	cover_photo 	= graphene.String()


	def resolve_avatar(self, info):

		return info.context.build_absolute_uri(self.avatar.url)

	def resolve_cover_photo(self, info):

		return info.context.build_absolute_uri(self.cover_photo.url)


		# The contractor Model

class ContractorType(DjangoObjectType):

	class Meta:

		model = Contractor

		# The Project Model

class ProjectType(DjangoObjectType):

	class Meta:

		model  = Project

		# The Review Model

class ReviewType(DjangoObjectType):
	class Meta:

		model = Review


		# The Post Model

class PostType(DjangoObjectType):

	class Meta:

		model = Post

	photo   =  graphene.String()
	video 	=  graphene.String()


	def resolve_photo(self, info):
		return info.context.build_absolute_uri(self.photo)

	def resolve_video(self, info):
		return info.context.build_absolute_uri(self.video)

		# The Comment Model

class CommentType(DjangoObjectType):

	class Meta:

		model = Comment

	photo  		= graphene.String()

	def resolve_photo(self, info):

		return info.context.build_absolute_uri(self.photo)



class Query(object):

	# The User Detail

	me  			= 	graphene.Field(UserType)

	# The Profile Detail

	profile 		= 	graphene.Field(ProfileType)

	# The Project List and Detail Query

	projects 		=  graphene.List(ProjectType)
	project 		=  graphene.Field(ProjectType, id = graphene.Int())


	# The Contractor List and Detail Query

	contractors 	 =  graphene.List(ContractorType)
	contractor 		 =  graphene.Field(ContractorType, id = graphene.Int())


	# The Review List and Detail Query

	reviews			= 	graphene.List(ReviewType)
	review 			= 	graphene.Field(ReviewType, id = graphene.Int())


	# The Post List and Detail Query 

	posts 			= 	graphene.List(PostType)
	post 			= 	graphene.Field(PostType, id = graphene.Int())


	# The Comment List and Detail Query


	comments 		= 	graphene.List(CommentType)
	comment 		= 	graphene.Field(CommentType, id = graphene.Int())





	# The Authentication resolve Method




	# The User Detail Resolve Method


	def resolve_me(self, info, **kwargs):

		user 	=  info.context.user
		if user.is_anonymous:
			raise GraphQLError("You Must be authenticated to access this User")

		else:

			return user

	# The Profile Detail Resolve method

	def resolve_profile(self, info, **kwargs):

		user 	 = info.context.user

		if user.is_anonymous:

			raise GraphQLError('You must be authenticated to view this profile')

		else:

			return user.profile

	


	# The Contractor List and Detail Resolve  Method

	def resolve_contractors(self, info, **kwargs):

		user 		=  info.context.user

		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this guides")

		else:

			return Contractor.objects.all()


	def resolve_contractor(self, info, **kwargs):

		user 		= info.context.user
		id 			= kwargs.get('id')

		if user.is_anonymous:

			raise GraphQLError("you must be authenticated to view this guide")

		else:
			return Contractor.objects.get(pk = id)


	# The Project List and Detail Resolve  Method

	def resolve_projects(self, info, **kwargs):

		user 		=  info.context.user

		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this guides")

		else:

			return Project.objects.all()


	def resolve_project(self, info, **kwargs):

		user 		= info.context.user
		id 			= kwargs.get('id')

		if user.is_anonymous:

			raise GraphQLError("you must be authenticated to view this guide")

		else:
			return Project.objects.get(pk = id)


	# The Post List and Detail Resolve Method


	def resolve_posts(self, info, **kwargs):

		user 		=  info.context.user

		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this posts")

		else:
			return Post.objects.all()

	def resolve_post(self, info, **kwargs):

		user 		= info.context.user
		id 			= kwargs.get('id')


		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this post")

		else:
			
			return Post.objects.get(pk = id)

	# The Comments List and Detail Resolve Method


	def resolve_comments(self, info, **kwargs):

		user 		=   info.context.user
		
		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this comment")

		else:

			return Comment.objects.all()


	def resolve_comment(self, info, **kwargs):

		user 		=  info.context.user

		id 			= kwargs.get('id')

		if user.is_anonymous:

			raise GraphQLError ("you must be authenticated to view this comment")

		else:

			return Comment.objects.get(pk = id)














