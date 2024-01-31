from rest_framework import serializers

from guias.models import Guia
from guias.serializers.GuiaChronogramSerializers import GuiaChronogramSerializerMain
from guias.serializers.GuiaCompetenciesSerializers import GuiaCompetenciesSerializerMain
from guias.serializers.GuiaResourcesSerializers import GuiaResourcesSerializerMain
from guias.serializers.GuiaResultsSerializers import GuiaResultsSerializerMain
from guias.serializers.GuiaSpecialtiesSerializers import GuiaSpecialtySerializerMain
from guias.serializers.UserSerializers import UserSerializerSmall


class GuiaSerializerMain(serializers.ModelSerializer):
    coordinator = UserSerializerSmall()
    teachers = UserSerializerSmall(many=True)
    identifiers = serializers.SerializerMethodField(method_name="get_identifiers")
    competencies = GuiaCompetenciesSerializerMain(many=True)
    hours = serializers.SerializerMethodField(method_name="get_hours")
    methodology = serializers.SerializerMethodField(method_name="get_methodology")
    evaluation = serializers.SerializerMethodField(method_name="get_evaluation")
    calification = serializers.SerializerMethodField(method_name="get_calification")
    results = GuiaResultsSerializerMain(many=True)
    resources = GuiaResourcesSerializerMain(many=True)
    chronogram = GuiaChronogramSerializerMain()

    def get_identifiers(self, obj):
        return {
            "type": obj.identifier_type,
            "character": obj.identifier_character,
            "specialty": GuiaSpecialtySerializerMain(obj.identifier_specialty).data,
            "subject": obj.identifier_subject,
            "course": obj.identifier_course,
            "semester": obj.identifier_semester,
            "credits": obj.identifier_credits,
            "hours_presence": obj.identifier_hours_presence,
            "department": obj.identifier_department,
            "prelation": obj.identifier_prelation,
            "language": obj.identifier_language
        }

    def get_hours(self, obj):
        return {
            "activities": obj.hours_activities,
            "probes": obj.hours_probes,
            "selfwork": obj.hours_selfwork,
            "preparation": obj.hours_preparatioin
        }

    def get_methodology(self, obj):
        return {
            "theory": obj.methodology_theory,
            "practical": obj.methodology_practical,
            "others": obj.methodology_others,
        }

    def get_evaluation(self, obj):
        return {
            "instruments": {
                "theory": obj.eval_instruments_theory,
                "practical": obj.eval_instruments_practical,
                "others": obj.eval_instruments_others,
            },
            "criteria": {
                "theory": obj.eval_criteria_theory,
                "practical": obj.eval_criteria_practical,
                "others": obj.eval_criteria_others,
            },
        }

    def get_calification(self, obj):
        return {
            "continual_evaluation": {
                "theory": obj.calification_continual_evaluation_theory,
                "practical": obj.calification_continual_evaluation_practical,
                "attitude": obj.calification_continual_evaluation_attitude,
            },
            "ordinary_evaluation": obj.calification_ordinary,
            "extraordinary_evaluation": obj.calification_extraordinary,
            "disabled_evaluation": {
                "theory": obj.calification_disabled_theory,
                "practical": obj.calification_disabled_practical,
                "attitude": obj.calification_disabled_attitude,
            }

        }

    class Meta:
        model = Guia
        fields = [
            "id", "title", "description", "identifiers", "coordinator", "teachers", "results", "competencies", "hours",
            "methodology", "evaluation", "calification", "chronogram", "resources"]
