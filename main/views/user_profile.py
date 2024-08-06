from rest_framework.views import APIView
from main.models import Skill, Interest, UserSkill, UserInterest
from main.serializers import UserSkillsSerializer
from rest_framework.permissions import IsAuthenticated
from common.utils import make_response
from django.db import connection

class UserSkillsView(APIView):
    """Save and update user skills and Update database with new skills"""

    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user

        # Format and validate the skill data.
        serializer = UserSkillsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_skills = set(serializer.data.get("skills"))

        # Get existing skills in the db.
        skill_objs = list(Skill.objects.filter(name__in=user_skills).all())
        existing_skills = {skill.name for skill in skill_objs}

        # Get the additonal skills and add it to the db.
        new_skills = user_skills - existing_skills
        new_skill_objs = Skill.objects.bulk_create([Skill(name=skill) for skill in new_skills])

        # Assosciate skills to the user.
        skill_objs.extend(new_skill_objs)
        UserSkill.objects.bulk_create(
            UserSkill(user=user, skill=skill) for skill in skill_objs
        )
        return make_response({}, 200)
    
    def get(self, request):
        user = request.user
        skills = UserSkill.objects.filter(user=user).distinct("skill").values("skill__name").all()
        return make_response({}, 200)
        

