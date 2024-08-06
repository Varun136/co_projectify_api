from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSkillsSerializer(serializers.Serializer):
    skills = serializers.ListField(required=True)

    def validate(self, data):
        for i in range(len(data.get("skills"))):
            skill = data.get("skills")[i]
            if not isinstance(skill, str):
                raise ValidationError(f"Invalid skill added: {skill}")
            data["skills"][i] = skill.title()
            
        return data