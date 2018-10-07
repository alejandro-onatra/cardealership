from rest_framework import serializers
from cardealership.cardealership.models import Car, MODEL_CHOICES, Rental


class CarSerializer(serializers.Serializer):

    id = serializers.IntegerField( read_only=True )
    brand = serializers.ChoiceField( choices=MODEL_CHOICES, required=True )
    year = serializers.DateField( required=True )
    model = serializers.CharField( max_length=60, required=True )

    def create(self, validated_data):
        """
        Create and return a new `Car` instance, given the validated data.
        """
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Car` instance, given the validated data.
        """
        instance.brand = validated_data.get('brand', instance.brand)
        instance.year = validated_data.get('year', instance.year)
        instance.model = validated_data.get('model', instance.model)
        instance.save()

        return instance


class RentalSerializer( serializers.ModelSerializer ):

    class Meta:

        model = Rental
        fields = ('id', 'start_date', 'end_date', 'cost', 'car')

        def create(self, validated_data):
            """
            Create and return a new `Rental` instance, given the validated data.
            """
            return Rental.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Rental` instance, given the validated data.
            """
            instance.start_date = validated_data.get('start_date', instance.start_date)
            instance.end_date = validated_data.get('end_date', instance.end_date)
            instance.cost = validated_data.get('cost', instance.cost)
            instance.car = validated_data.get('car', instance.car)

            instance.save()

            return instance


