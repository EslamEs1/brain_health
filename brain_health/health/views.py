from rest_framework import generics, mixins, viewsets
from rest_framework import permissions
from .tasks import send_email_task
from django.shortcuts import get_object_or_404
from brain_health.users.models import Therapist, Brain_Health_Score
from .serializers import (
    RelativeSerializer,
    MoodSerializer,
    SuggestionSerializer,
    AppointmentSerializer,
)
from brain_health.health.models import (
    Relative,
    Appointment,
    Suggestion,
    Message,
    Mood,
    SendMail,
)

class RelativeList(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):

    serializer_class = RelativeSerializer
    queryset = Relative.objects.all()
    permission_class = [permissions.IsAuthenticated]
    lookup_field = "pk"

    def get_queryset(self):
        return Relative.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class MoodListView(generics.ListAPIView):
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()
    permission_class = [permissions.IsAuthenticated]




class SuggestionByMoodView(generics.ListAPIView):
    serializer_class = SuggestionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        mood_name = self.request.query_params.get('mood', '').lower()
        mood = get_object_or_404(Mood, name__iexact=mood_name)

        suggestion = Suggestion.objects.filter(mood=mood).order_by('?').first()
        if not suggestion:
            return []

        user = self.request.user
        Brain_Health_Score.objects.create(user=user, rating=mood.score)

        message = Message.objects.filter(mood=mood).order_by('?').first()
        if message:
            suggestion_text = suggestion.suggestion_text
            message_text = message.message_text
            is_urgent = message.is_urgent
            relatives = user.relative.distinct("name", "email")
            for relative in relatives:
                message_body = f"Hey {relative.name}, {user.name} has been feeling {mood.name}.\n\n Here's a suggestion: {suggestion_text}\n\n{message_text}\n\nIs urgent: {is_urgent}\n\nThanks,"
                send_email_task.delay('Mood', message_body, ["brainhealth@gmail.com"])
                msg = f"{message_body} to {[relative.email]} from 'brainhealth@gmail.com'"
                SendMail.objects.create(message_text=msg)

        # if user.brain_health_score < 50:
        #     # User needs therapy, suggest therapists
        #     therapists = Therapist.objects.filter(is_available=True)
        #     for therapist in therapists:
        #         # Send an email to the user with the therapist details
        #         message_body = f"Hey {user.name}, we suggest that you meet with {therapist.name} for brain health therapy. You can contact them at {therapist.email} to schedule an appointment.\n\nThanks"
        #         send_email_task.delay('Brain Health Therapy', message_body, [user.email])


        return [suggestion]




