from django.http import Http404
from rest_framework import status, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from substrapp.models import Problem
from substrapp.serializers import ProblemSerializer, LedgerProblemSerializer

"""List all problems saved on local storage or submit a new one"""


class ProblemViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        """
        Create a new Problem \n
            TODO add info about what has to be posted\n
        - Example with curl (on localhost): \n
            curl -u username:password -H "Content-Type: application/json"\
            -X POST\
            -d '{"name": "tough problem", "test_data":
            ["data_5c1d9cd1c2c1082dde0921b56d11030c81f62fbb51932758b58ac2569dd0b379",
            "data_5c1d9cd1c2c1082dde0921b56d11030c81f62fbb51932758b58ac2569dd0b389"],\
                "files": {"description.md": '#My tough problem',\
                'metrics.py': 'def AUC_score(y_true, y_pred):\n\treturn 1'}}'\
                http://127.0.0.1:8000/substrapp/problem/ \n
            Use double quotes for the json, simple quotes don't work.\n
        - Example with the python package requests (on localhost): \n
            requests.post('http://127.0.0.1:8000/runapp/rawdata/',\
                          auth=('username', 'password'),\
                          json={'name': 'tough problem', 'test_data': '??',\
                        'files': {'iris.csv': 'bla', 'specific.py': 'bli'}})\n
        ---
        response_serializer: ProblemSerializer
        """

        data = request.data
        serializer = self.get_serializer(data={'metrics': data['metrics'],
                                                       'description': data['description']})
        serializer.is_valid(raise_exception=True)

        # create on db
        instance = self.perform_create(serializer)

        # init ledger serializer
        ledger_serializer = LedgerProblemSerializer(data={'test_data': data.getlist('test_data'),
                                                          'name': data['name'],
                                                          'instance_pkhash': instance.pkhash})
        if not ledger_serializer.is_valid():
            # delete instance
            instance.delete()
            raise ValidationError(ledger_serializer.errors)

        # create on ledger
        ledger_serializer.create(ledger_serializer.validated_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        # TODO get problems from ledgers
        data = []

        return Response(data, status=status.HTTP_200_OK)

    def metrics(self, request, *args, **kwargs):
        instance = self.get_object()

        # TODO fetch problem from ledger
        # if requester has permission, return metrics

        serializer = self.get_serializer(instance)
        return Response(serializer.data['metrics'])

    def leaderboard(self, request, *args, **kwargs):

        # TODO fetch problem from ledger

        try:
            # try to get it from local db
            instance = self.get_object()
        except Http404:
            # TODO get instance from remote node
            # check hash
            # save problem in local db for later use
            pass
        else:
            pass

            # TODO query list of algos and models from ledger

            # sort algos given the best perfs of their models

            # return success, problem info, sorted algo + models

            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    def data(self, request, *args, **kwargs):
        instance = self.get_object()

        # TODO fetch list of data from ledger
        # query list of related algos and models from ledger

        # return success and model

        serializer = self.get_serializer(instance)
        return Response(serializer.data)