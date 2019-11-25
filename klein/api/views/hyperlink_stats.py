import itertools
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models
from api.utils import decode_hyperlink_id


class HyperlinkStatsView(APIView):
    def get(self, request, slug):
        # Ignore any static file requests that make it to this point
        if '.' in slug:
            raise Http404('Short URL does not exist')

        # See if an alias exists
        hyperlink_aliases = models.HyperlinkAlias.objects.filter(
            alias=slug
        )
        if hyperlink_aliases.exists():
            hyperlink_history = models.HyperlinkView.objects.filter(
                hyperlink_alias=hyperlink_aliases.first()
            )
            created_on = hyperlink_aliases.first().created_on

        # See if it's a Hyperlink with a slug that was taken by an alias
        if slug[0] == '_':
            slug = slug[1:]

        # See if Hyperlink exists
        hyperlinks = models.Hyperlink.objects.filter(
            id=decode_hyperlink_id(slug)
        )
        if hyperlinks.exists():
            hyperlink_history = models.HyperlinkView.objects.filter(
                hyperlink=hyperlinks.first()
            )
            created_on = hyperlinks.first().created_on
        else:
            raise Http404('Short URL does not exist')

        ip_addresses = hyperlink_history.values_list('ip_address', flat=True).distinct()

        grouped_views = itertools.groupby(
            hyperlink_history.values('viewed_on'),
            lambda d: d.get('viewed_on').strftime('%Y-%m-%d')
        )
        hits_timeseries = [(day, len(list(this_day))) for day, this_day in grouped_views]

        return Response({
            'created_on': created_on,
            'total_hits': len(hyperlink_history),
            'total_users': len(ip_addresses),
            'hits_timeseries': hits_timeseries
        })
