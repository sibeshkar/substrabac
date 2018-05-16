from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject

from .models import Problem, DataOpener, Data


class ProblemSerializer(serializers.ModelSerializer):
    test_data = serializers.ListField(child=serializers.CharField(
        min_length=69, max_length=69), min_length=1, max_length=None)
    name = serializers.CharField(min_length=1, max_length=60)

    class Meta:
        model = Problem
        fields = '__all__'

    def create(self, validated_data):
        return Problem.objects.create(description=validated_data["description"],
                                      metrics=validated_data["metrics"])

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = self._readable_fields

        for field in [x for x in fields if x.field_name not in ('test_data', 'name')]:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)

        # TODO take them from hyperledger

        return ret


    # def update(self, instance, validated_data):
