from rest_framework import serializers

from .models import JackpotGames, SingleBet

class JackpotGamesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = JackpotGames

        fields = ('published_date', 'country', 'home_team', 'away_team', 'home_odds', 'draw_odds', 'away_odds', 'prediction')


class SingleBetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = SingleBet

        fields = ('published_date', 'country', 'home_team', 'home_score', 'away_score', 'away_team', 'prediction', 'status')
